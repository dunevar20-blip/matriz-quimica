import pandas as pd

print("🚀 Generando Base de Datos Química Correcta...")

# 1. INVENTARIO (Nombres de columna ESTÁNDAR)
sustancias = [
    {"Nombre": "ACETONA", "CAS": "67-64-1", "Clase": "INFLAMABLE", "Pictograma": "🔥"},
    {"Nombre": "ACETALDEHIDO", "CAS": "75-07-0", "Clase": "INFLAMABLE", "Pictograma": "🔥"},
    {"Nombre": "ALCOHOL ISOPROPILICO", "CAS": "67-63-0", "Clase": "INFLAMABLE", "Pictograma": "🔥"},
    {"Nombre": "ALCOHOL N PROPILICO", "CAS": "71-23-8", "Clase": "INFLAMABLE", "Pictograma": "🔥"},
    {"Nombre": "ETILMETILCETONA", "CAS": "78-93-3", "Clase": "INFLAMABLE", "Pictograma": "🔥"},
    {"Nombre": "1 BUTANOL", "CAS": "71-36-3", "Clase": "INFLAMABLE", "Pictograma": "🔥"},
    {"Nombre": "ACIDO NITRICO", "CAS": "7697-37-2", "Clase": "CORROSIVO", "Pictograma": "🧪"},
    {"Nombre": "POTASIO HIDROXIDO", "CAS": "1310-58-3", "Clase": "CORROSIVO", "Pictograma": "🧪"},
    {"Nombre": "ZINC CLORURO", "CAS": "7646-85-7", "Clase": "CORROSIVO", "Pictograma": "🧪"},
    {"Nombre": "CLORURO HIERRO III", "CAS": "7705-08-0", "Clase": "CORROSIVO", "Pictograma": "🧪"},
    {"Nombre": "FENOL", "CAS": "108-95-2", "Clase": "TOXICO", "Pictograma": "💀"},
    {"Nombre": "CLOROFORMO", "CAS": "67-66-3", "Clase": "TOXICO", "Pictograma": "💀"},
    {"Nombre": "CLORURO DE BARIO", "CAS": "10361-37-2", "Clase": "TOXICO", "Pictograma": "💀"},
    {"Nombre": "OXIDO DE MERCURIO II", "CAS": "21908-53-2", "Clase": "TOXICO", "Pictograma": "💀"},
    {"Nombre": "NITRATO DE PLATA", "CAS": "7761-88-8", "Clase": "COMBURENTE", "Pictograma": "⭕"},
    {"Nombre": "PERMANGANATO DE POTASIO", "CAS": "7722-64-7", "Clase": "COMBURENTE", "Pictograma": "⭕"},
    {"Nombre": "PEROXIDO DE HIDROGENO", "CAS": "7722-84-1", "Clase": "COMBURENTE", "Pictograma": "⭕"},
    {"Nombre": "BICROMATO DE POTASIO", "CAS": "7778-50-9", "Clase": "COMBURENTE", "Pictograma": "⭕"},
    {"Nombre": "ACIDO BORICO", "CAS": "10043-35-3", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "ACIDO CITRICO", "CAS": "77-92-9", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "LUGOL", "CAS": "25655-41-8", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "VIOLETA DE GRAM", "CAS": "548-62-9", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "GLUCOSA", "CAS": "50-99-7", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "SACAROSA", "CAS": "57-50-1", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "ALMIDON", "CAS": "9005-84-9", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "CLORURO DE SODIO", "CAS": "7647-14-5", "Clase": "NO PELIGROSO", "Pictograma": "✅"},
    {"Nombre": "BICARBONATO DE SODIO", "CAS": "144-55-8", "Clase": "NO PELIGROSO", "Pictograma": "✅"}
]

# 2. REGLAS (Usando 'Sustancia_A', 'Estado', 'Origen')
reglas = [
    {"Sustancia_A": "ACIDO NITRICO", "Sustancia_B": "POTASIO HIDROXIDO", "Estado": "Incompatible", "Origen": "Regla Ácido-Base"},
    {"Sustancia_A": "ACETALDEHIDO", "Sustancia_B": "ACETONA", "Estado": "Incompatible", "Origen": "Matriz Inflamables"},
    {"Sustancia_A": "ACETALDEHIDO", "Sustancia_B": "ALCOHOL ISOPROPILICO", "Estado": "Incompatible", "Origen": "Matriz Inflamables"},
    {"Sustancia_A": "ACETALDEHIDO", "Sustancia_B": "ALCOHOL N PROPILICO", "Estado": "Incompatible", "Origen": "Matriz Inflamables"},
    {"Sustancia_A": "POTASIO HIDROXIDO", "Sustancia_B": "ZINC CLORURO", "Estado": "Incompatible", "Origen": "Matriz Corrosivos"},
    {"Sustancia_A": "POTASIO HIDROXIDO", "Sustancia_B": "CLORURO HIERRO III", "Estado": "Incompatible", "Origen": "Matriz Corrosivos"},
    {"Sustancia_A": "POTASIO HIDROXIDO", "Sustancia_B": "YODO RESUBLIMADO", "Estado": "Incompatible", "Origen": "Matriz Corrosivos"},
    {"Sustancia_A": "NITRATO DE PLATA", "Sustancia_B": "ACETONA", "Estado": "Incompatible", "Origen": "Matriz Comburentes"},
    {"Sustancia_A": "PERMANGANATO DE POTASIO", "Sustancia_B": "ACETONA", "Estado": "Incompatible", "Origen": "Matriz Comburentes"},
    {"Sustancia_A": "PERMANGANATO DE POTASIO", "Sustancia_B": "FENOL", "Estado": "Incompatible", "Origen": "Matriz Comburentes"},
    {"Sustancia_A": "PEROXIDO DE HIDROGENO", "Sustancia_B": "PERMANGANATO DE POTASIO", "Estado": "Incompatible", "Origen": "Matriz Comburentes"},
    {"Sustancia_A": "ACIDO NITRICO", "Sustancia_B": "ACETONA", "Estado": "Incompatible", "Origen": "Regla Oxidante Fuerte"},
    {"Sustancia_A": "ACIDO NITRICO", "Sustancia_B": "ALCOHOL ISOPROPILICO", "Estado": "Incompatible", "Origen": "Regla Oxidante Fuerte"},
    {"Sustancia_A": "ACIDO NITRICO", "Sustancia_B": "FENOL", "Estado": "Incompatible", "Origen": "Regla de Nitración Violenta"}
]

# Guardar los archivos CSV
df_s = pd.DataFrame(sustancias)
df_r = pd.DataFrame(reglas)

df_s.to_csv('Master_Sustancias_Final.csv', index=False)
df_r.to_csv('Reglas_Compatibilidad_Unificadas.csv', index=False)

print(f"✅ ¡ÉXITO! Se repararon los archivos: {len(sustancias)} sustancias y {len(reglas)} reglas.")