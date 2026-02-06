import pandas as pd
import glob
import unicodedata
import re

print("🔄 Iniciando procesamiento inteligente...")

# 1. FUNCIÓN DE LIMPIEZA (Para que los nombres siempre coincidan)
def limpiar(texto):
    if pd.isna(texto): return ""
    texto = str(texto).upper()
    texto = "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    texto = re.sub(r'[^A-Z0-9]', ' ', texto) # Solo letras y numeros
    return " ".join(texto.split())

# 2. CARGAR INVENTARIO DESDE TU EXCEL
try:
    # Busca el archivo que empieza con "MATRIZ" y contiene "Listado"
    archivo_lista = glob.glob("*Listado*.csv")[0]
    df_lista = pd.read_csv(archivo_lista, skiprows=2)
    
    # Extraer columnas clave
    df_lista = df_lista.iloc[:, [0, 1, 4, 6]] # Nombre, CAS, Clase, Incompat
    df_lista.columns = ['Nombre', 'CAS', 'Clase', 'Incompat']
    
    # Limpiar nombres
    df_lista['Nombre_Limpio'] = df_lista['Nombre'].apply(limpiar)
    df_lista['Nombre'] = df_lista['Nombre'].str.strip().str.upper()
    
    print(f"✅ Se cargaron {len(df_lista)} sustancias del Excel.")
    
except Exception as e:
    print(f"⚠️ No se encontró el Excel (Error: {e}). Usando modo respaldo.")
    df_lista = pd.DataFrame(columns=['Nombre', 'CAS', 'Clase', 'Incompat', 'Nombre_Limpio'])

# 3. AGREGAR SUSTANCIAS FALTANTES (Como el Ácido Nítrico)
faltantes = [
    {"Nombre": "ACIDO NITRICO", "CAS": "7697-37-2", "Clase": "Clase 8 Corrosivo", "Incompat": "Bases, Inflamables, Reductores"},
    {"Nombre": "POTASIO HIDROXIDO", "CAS": "1310-58-3", "Clase": "Clase 8 Corrosivo (Base)", "Incompat": "Acidos, Metales"},
]

for f in faltantes:
    f['Nombre_Limpio'] = limpiar(f['Nombre'])
    if f['Nombre_Limpio'] not in df_lista['Nombre_Limpio'].values:
        df_lista = pd.concat([df_lista, pd.DataFrame([f])], ignore_index=True)

# Asignar Pictogramas
def get_pic(clase):
    c = str(clase).upper()
    if 'INFLAMABLE' in c: return '🔥'
    if 'CORROSIVO' in c: return '🧪'
    if 'TOXICO' in c: return '💀'
    if 'COMBURENTE' in c or 'OXIDANTE' in c: return '⭕'
    return '✅'

df_lista['Pictograma'] = df_lista['Clase'].apply(get_pic)

# 4. GENERAR REGLAS DE TUS MATRICES + REGLAS LÓGICAS
reglas = []

# A) Reglas extraídas de tus archivos CSV de matrices
for archivo in glob.glob("*Matriz*.csv"):
    try:
        df_m = pd.read_csv(archivo, skiprows=1)
        # Buscar columna de incompatibilidad
        col_inc = [c for c in df_m.columns if "INCOMPAT" in str(c).upper()]
        if not col_inc: continue
        idx = df_m.columns.get_loc(col_inc[0])
        
        headers = df_m.columns[idx+1:]
        
        for i, row in df_m.iterrows():
            # Buscar nombre en las primeras columnas
            nombre_a = ""
            for k in range(1, 4):
                val = str(row.iloc[k])
                if len(val) > 3 and not val.replace('.','').isdigit():
                    nombre_a = val
                    break
            
            if not nombre_a: continue
            a_limpio = limpiar(nombre_a)
            
            for h in headers:
                b_limpio = limpiar(h)
                val = str(row[h]).lower().strip()
                if 'r' in val:
                    reglas.append({"A": a_limpio, "B": b_limpio, "Estado": "Incompatible", "Origen": "Tu Matriz Excel"})
    except:
        continue

# B) REGLAS MANUALES DE SEGURIDAD (Para cubrir lo que falta en el Excel)
reglas_extra = [
    # ACIDO NITRICO vs POTASIO (Hidróxido, Carbonato, etc)
    {"A": "ACIDO NITRICO", "B": "POTASIO HIDROXIDO", "E": "Incompatible", "O": "Regla Ácido-Base"},
    {"A": "ACIDO NITRICO", "B": "POTASIO Y SODIO TARTRATO", "E": "Incompatible", "O": "Regla Oxidante-Reductor"},
    {"A": "ACIDO NITRICO", "B": "ACETONA", "E": "Incompatible", "O": "Regla Oxidante-Inflamable"},
    {"A": "ACIDO NITRICO", "B": "ALCOHOL ISOPROPILICO", "E": "Incompatible", "O": "Regla Oxidante-Inflamable"},
    
    # ACETALDEHIDO (Tu conclusión dice que es incompatible con todo)
    {"A": "ACETALDEHIDO", "B": "ACETONA", "E": "Incompatible", "O": "Matriz Inflamables"},
    {"A": "ACETALDEHIDO", "B": "ALCOHOL", "E": "Incompatible", "O": "Matriz Inflamables"}, # Regla genérica
]

for r in reglas_extra:
    reglas.append({"A": limpiar(r['A']), "B": limpiar(r['B']), "Estado": r['E'], "Origen": r['O']})

# Guardar
df_reglas = pd.DataFrame(reglas)
df_lista.to_csv('Master_Sustancias_Final.csv', index=False)
df_reglas.to_csv('Reglas_Compatibilidad_Unificadas.csv', index=False)

print(f"✅ ¡LISTO! Base de datos generada con {len(df_lista)} sustancias y {len(df_reglas)} reglas.")