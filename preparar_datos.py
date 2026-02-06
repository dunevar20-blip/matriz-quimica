import pandas as pd

# 1. Crear el Maestro de Sustancias (Listado con Pictogramas)
sustancias_data = {
    'Nombre': ['ACETONA', 'ACETALDEHÍDO', 'ALCOHOL ISOPROPILICO', 'POTASIO HIDRÓXIDO', 'ÁCIDO NÍTRICO', 'NITRATO DE PLATA', 'FENOL', 'CLOROFORMO'],
    'CAS': ['67-64-1', '75-07-0', '67-63-0', '1310-58-3', '7697-37-2', '7761-88-8', '108-95-2', '67-66-3'],
    'Clase': ['Clase 3 Inflamable', 'Clase 3 Inflamable', 'Clase 3 Inflamable', 'Clase 8 Corrosivo', 'Clase 8 Corrosivo', 'Clase 5.1 Comburente', 'Clase 6.1 Tóxico', 'Clase 6.1 Tóxico'],
    'Pictograma': ['🔥 (Inflamable)', '🔥 (Inflamable)', '🔥 (Inflamable)', '🧪 (Corrosivo)', '🧪 (Corrosivo)', '⭕ (Oxidante)', '💀 (Tóxico)', '💀 (Tóxico)'],
    'Incompatibilidades': ['Evitar oxidantes fuertes y ácidos.', 'Incompatible con alcoholes y cetonas.', 'Evitar ácidos fuertes.', 'Reacciona con ácidos y metales.', 'Reacción violenta con inflamables.', 'Evitar materiales combustibles.', 'Evitar oxidantes.', 'Evitar metales alcalinos.']
}

# 2. Crear las Reglas de Compatibilidad (Cruces de tus matrices)
reglas_data = [
    {'Sustancia_A': 'ACETONA', 'Sustancia_B': 'ACETALDEHÍDO', 'Estado': 'Incompatible', 'Origen': 'Matriz Inflamables'},
    {'Sustancia_A': 'ACETONA', 'Sustancia_B': 'ALCOHOL ISOPROPILICO', 'Estado': 'Compatible', 'Origen': 'Matriz Inflamables'},
    {'Sustancia_A': 'NITRATO DE PLATA', 'Sustancia_B': 'ACETONA', 'Estado': 'Incompatible', 'Origen': 'Matriz Comburentes'},
    {'Sustancia_A': 'POTASIO HIDRÓXIDO', 'Sustancia_B': 'ÁCIDO NÍTRICO', 'Estado': 'Incompatible', 'Origen': 'Matriz Corrosivos'},
    {'Sustancia_A': 'FENOL', 'Sustancia_B': 'CLOROFORMO', 'Estado': 'Compatible', 'Origen': 'Matriz Tóxicos'}
]

# Guardar archivos
pd.DataFrame(sustancias_data).to_csv('Master_Sustancias_Final.csv', index=False)
pd.DataFrame(reglas_data).to_csv('Reglas_Compatibilidad_Unificadas.csv', index=False)

print("✅ Archivos 'Master_Sustancias_Final.csv' y 'Reglas_Compatibilidad_Unificadas.csv' creados con éxito.")