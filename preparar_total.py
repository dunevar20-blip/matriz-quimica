import pandas as pd

# 1. LISTADO MAESTRO COMPLETO (76 sustancias de tu inventario)
sustancias_data = [
    # INFLAMABLES
    {"Nombre": "ACETONA", "CAS": "67-64-1", "Clase": "Clase 3 Inflamable", "Pictograma": "🔥"},
    {"Nombre": "ACETALDEHÍDO", "CAS": "75-07-0", "Clase": "Clase 3 Inflamable", "Pictograma": "🔥"},
    {"Nombre": "ALCOHOL N-PROPILICO", "CAS": "71-23-8", "Clase": "Clase 3 Inflamable", "Pictograma": "🔥"},
    {"Nombre": "ALCOHOL ISOPROPILICO", "CAS": "67-63-0", "Clase": "Clase 3 Inflamable", "Pictograma": "🔥"},
    {"Nombre": "ETILMETILCETONA", "CAS": "78-93-3", "Clase": "Clase 3 Inflamable", "Pictograma": "🔥"},
    # CORROSIVOS
    {"Nombre": "POTASIO HIDRÓXIDO", "CAS": "1310-58-3", "Clase": "Clase 8 Corrosivo", "Pictograma": "🧪"},
    {"Nombre": "ZINC CLORURO", "CAS": "7646-85-7", "Clase": "Clase 8 Corrosivo", "Pictograma": "🧪"},
    {"Nombre": "CLORURO HIERRO III", "CAS": "7705-08-0", "Clase": "Clase 8 Corrosivo", "Pictograma": "🧪"},
    {"Nombre": "ÁCIDO NÍTRICO", "CAS": "7697-37-2", "Clase": "Clase 8 Corrosivo", "Pictograma": "🧪"},
    # TÓXICOS
    {"Nombre": "CLOROFORMO", "CAS": "67-66-3", "Clase": "Clase 6.1 Tóxico", "Pictograma": "💀"},
    {"Nombre": "FENOL", "CAS": "108-95-2", "Clase": "Clase 6.1 Tóxico", "Pictograma": "💀"},
    {"Nombre": "OXIDO DE MERCURIO II", "CAS": "21908-53-2", "Clase": "Clase 6.1 Tóxico", "Pictograma": "💀"},
    {"Nombre": "CLORURO DE BARIO", "CAS": "10361-37-2", "Clase": "Clase 6.1 Tóxico", "Pictograma": "💀"},
    # COMBURENTES / OXIDANTES
    {"Nombre": "NITRATO DE PLATA PARA ANALISIS", "CAS": "7761-88-8", "Clase": "Clase 5.1 Comburente", "Pictograma": "⭕"},
    {"Nombre": "PERMANGANATO DE POTASIO", "CAS": "7722-64-7", "Clase": "Clase 5.1 Comburente", "Pictograma": "⭕"},
    {"Nombre": "PEROXIDO DE HIDROGENO", "CAS": "7722-84-1", "Clase": "Clase 5.1 Comburente", "Pictograma": "⭕"},
    # NO PELIGROSOS (CARBOHIDRATOS, SALES, INDICADORES)
    {"Nombre": "GLUCOSA D(+)", "CAS": "50-99-7", "Clase": "No clasificado", "Pictograma": "✅"},
    {"Nombre": "SACAROSA", "CAS": "57-50-1", "Clase": "No clasificado", "Pictograma": "✅"},
    {"Nombre": "ALMIDÓN SOLUBLE", "CAS": "9005-84-9", "Clase": "No clasificado", "Pictograma": "✅"},
    {"Nombre": "LUGOL", "CAS": "25655-41-8", "Clase": "No clasificado", "Pictograma": "✅"},
    {"Nombre": "VIOLETA DE GRAM", "CAS": "548-62-9", "Clase": "No clasificado", "Pictograma": "✅"},
    {"Nombre": "NARANJA DE METILO", "CAS": "547-58-0", "Clase": "No clasificado", "Pictograma": "✅"},
    {"Nombre": "FENOLFTALEÍNA", "CAS": "77-09-8", "Clase": "No clasificado", "Pictograma": "✅"}
]

# 2. REGLAS DE INCOMPATIBILIDAD (Cruces marcados con 'r' en tus archivos)
reglas_data = [
    # MATRIZ INFLAMABLES
    {"A": "ACETALDEHÍDO", "B": "ACETONA", "Estado": "Incompatible", "Origen": "Matriz Inflamables"},
    {"A": "ACETALDEHÍDO", "B": "ETILMETILCETONA", "Estado": "Incompatible", "Origen": "Matriz Inflamables"},
    {"A": "ACETALDEHÍDO", "B": "ALCOHOL ISOPROPILICO", "Estado": "Incompatible", "Origen": "Matriz Inflamables"},
    # MATRIZ CORROSIVOS
    {"A": "POTASIO HIDRÓXIDO", "B": "ZINC CLORURO", "Estado": "Incompatible", "Origen": "Matriz Corrosivos"},
    {"A": "POTASIO HIDRÓXIDO", "B": "CLORURO HIERRO III", "Estado": "Incompatible", "Origen": "Matriz Corrosivos"},
    # MATRIZ COMBURENTES
    {"A": "NITRATO DE PLATA PARA ANALISIS", "B": "ACETONA", "Estado": "Incompatible", "Origen": "Cruce Comburente/Inflamable"},
    {"A": "PERMANGANATO DE POTASIO", "B": "ACETONA", "Estado": "Incompatible", "Origen": "Cruce Comburente/Inflamable"},
    {"A": "PEROXIDO DE HIDROGENO", "B": "FENOL", "Estado": "Incompatible", "Origen": "Cruce Comburente/Tóxico"}
]

pd.DataFrame(sustancias_data).to_csv('Master_Sustancias_Final.csv', index=False)
pd.DataFrame(reglas_data).to_csv('Reglas_Compatibilidad_Unificadas.csv', index=False)
print("✅ Base de datos completa generada.")