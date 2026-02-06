import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO

# Configuración de la página
st.set_page_config(page_title="SafeLab 2026", page_icon="🧪", layout="wide")

st.title("🛡️ Matriz Química con Identificación QR")
st.markdown("---")

# 1. CARGAR DATOS
try:
    df_s = pd.read_csv('Master_Sustancias_Final.csv')
    df_r = pd.read_csv('Reglas_Compatibilidad_Unificadas.csv')
except FileNotFoundError:
    st.error("⚠️ Error: No se encuentran los archivos. Ejecuta primero 'python generar_datos.py'")
    st.stop()

# 2. SELECTORES DE SUSTANCIAS
nombres = sorted(df_s['Nombre'].unique())
col_sel1, col_sel2 = st.columns(2)

with col_sel1:
    s1 = st.selectbox("Seleccione Sustancia A", nombres)
with col_sel2:
    s2 = st.selectbox("Seleccione Sustancia B", nombres)

# 3. LÓGICA DE COMPATIBILIDAD (CEREBRO)
# Buscamos en la tabla de reglas
res = df_r[
    ((df_r['Sustancia_A'] == s1) & (df_r['Sustancia_B'] == s2)) | 
    ((df_r['Sustancia_A'] == s2) & (df_r['Sustancia_B'] == s1))
]

veredicto = "Desconocido"
fuente = ""
detalle = ""

if s1 == s2:
    veredicto = "Mismo"
elif not res.empty:
    # Si la regla existe en el Excel
    estado = res.iloc[0]['Estado']
    fuente = res.iloc[0]['Origen']
    if estado == 'Incompatible':
        veredicto = "Incompatible"
    else:
        veredicto = "Compatible"
else:
    # RED DE SEGURIDAD (Si no está en el Excel, usamos lógica química)
    if "NITRICO" in s1 and ("POTASIO" in s2 or "HIDROXIDO" in s2):
        veredicto = "Incompatible"
        fuente = "Alerta de Seguridad Crítica"
        detalle = "Reacción violenta entre Ácido Fuerte y Base/Metal."
    elif "NITRICO" in s2 and ("POTASIO" in s1 or "HIDROXIDO" in s1):
        veredicto = "Incompatible"
        fuente = "Alerta de Seguridad Crítica"
        detalle = "Reacción violenta entre Ácido Fuerte y Base/Metal."
    else:
        veredicto = "SinDatos"

# 4. MOSTRAR RESULTADO (SEMÁFORO)
if veredicto == "Incompatible":
    st.error(f"### ❌ PROHIBIDO: INCOMPATIBLE\n**Fuente:** {fuente}\n\n{detalle}")
elif veredicto == "Compatible":
    st.success(f"### ✅ COMPATIBLE\n**Fuente:** {fuente}")
elif veredicto == "Mismo":
    st.info("ℹ️ Es la misma sustancia.")
else:
    st.warning("⚠️ Sin datos específicos en tablas. Consultar Ficha de Seguridad (FDS).")

st.markdown("---")

# 5. FICHAS TÉCNICAS CON CÓDIGO QR
c1, c2 = st.columns(2)

def mostrar_tarjeta(nombre, columna):
    # Buscar datos de la sustancia
    fila = df_s[df_s['Nombre'] == nombre]
    
    if not fila.empty:
        info = fila.iloc[0]
        with columna:
            st.subheader(nombre)
            # Mostrar Pictograma Grande
            st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{info['Pictograma']}</h1>", unsafe_allow_html=True)
            st.caption(f"Clase: {info['Clase']}")
            st.caption(f"CAS: {info['CAS']}")
            
            # --- GENERADOR DE QR ---
            # Crear el texto que leerá el celular
            texto_qr = f"QUIMICO: {nombre}\nCAS: {info['CAS']}\nCLASE: {info['Clase']}\nRIESGO: {info['Pictograma']}"
            
            # Crear imagen
            qr = qrcode.make(texto_qr)
            buffer = BytesIO()
            qr.save(buffer)
            
            # Mostrar imagen
            st.image(buffer, caption="Escanear para Identificar", width=150)
            # --- FIN QR ---

mostrar_tarjeta(s1, c1)
mostrar_tarjeta(s2, c2)