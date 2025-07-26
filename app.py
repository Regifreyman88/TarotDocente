import streamlit as st
import random

st.set_page_config(page_title="Tarot Docente", page_icon="🔮", layout="wide")

# --- 1. Definición de Mazos (con extensiones .png y .jpg corregidas) ---

arcanos_mayores = [
    {"titulo": "La cicatriz como texto", "imagen": "cicatriz.png"},
    {"titulo": "El exilio de la perspectiva", "imagen": "exilio.png"},
    {"titulo": "El oráculo engañoso", "imagen": "oraculo.png"},
    {"titulo": "El nudo gordiano", "imagen": "nudo.png"}
]

arcanos_de_tension = [
    {"pregunta": "¿Qué historia te estás contando que entorpece tu camino?", "traduccion_didactica": "Identifica una narrativa limitante...", "imagen": "tension_1.png"},
    {"pregunta": "¿Qué perderías si no pudieras pensar creativamente?", "traduccion_didactica": "Identifica la dependencia de un solo tipo de solución...", "imagen": "tension_2.png"},
    {"pregunta": "¿Cuándo sientes que la IA o las redes sociales te manipulan?", "traduccion_didactica": "Reconoce la influencia externa...", "imagen": "tension_3.png"}
]

arcanos_ergodicos = [
    {"titulo": "Adición", "imagen": "adicion.png"},
    {"titulo": "Omisión", "imagen": "omision.png"},
    {"titulo": "Transposición", "imagen": "transposicion.png"},
    {"titulo": "Permutación", "imagen": "permutacion.png"}
]

herramientas_del_creador = [
    {"titulo": "Pincel de la imaginación absoluta", "imagen": "pincel.png", "aplicacion_didactica": "Representa con arte visual...", "traduccion_ia": "🎨 DALL·E, Midjourney..."},
    {"titulo": "Lente de recuerdos infinitos", "imagen": "lente.png", "aplicacion_didactica": "Usa fotos, documentación...", "traduccion_ia": "🖼️ RunwayML, Photoshop AI..."},
    {"titulo": "Encarnación del fantasma", "imagen": "fantasma.png", "aplicacion_didactica": "Da voz a lo ausente...", "traduccion_ia": "👻 D-ID, Murf.AI..."}
]


# --- 2. Interfaz de la Aplicación con Pestañas ---

st.title("🔮 Tarot Docente")
st.write("Una herramienta para aplicar el pensamiento de diseño y la creatividad en el aula.")

tab1, tab2, tab3, tab4 = st.tabs(["✨ Arcanos Mayores", "💥 Arcanos de Tensión", "♻️ Arcanos Ergódicos", "🛠️ Herramientas del Creador"])

with tab1:
    st.header("✨ Arcanos Mayores")
    if st.button("Sacar un Arcano Mayor"):
        carta = random.choice(arcanos_mayores)
        st.subheader(carta["titulo"])
        st.image(carta["imagen"], use_container_width=True)
        # Aquí puedes añadir más detalles de la carta si quieres

with tab2:
    st.header("💥 Arcanos de Tensión")
    if st.button("Sacar un Arcano de Tensión"):
        carta = random.choice(arcanos_de_tension)
        st.subheader("Pregunta Peligrosa")
        st.image(carta["imagen"], use_container_width=True)
        st.warning(f"**{carta['pregunta']}**")
        with st.expander("Ver Traducción Didáctica 📖"):
            st.success(f"**Aplicación:** {carta['traduccion_didactica']}")

with tab3:
    st.header("♻️ Arcanos Ergódicos")
    if st.button("Sacar un Arcano Ergódico"):
        carta = random.choice(arcanos_ergodicos)
        st.subheader(carta["titulo"])
        st.image(carta["imagen"], use_container_width=True)
        # Aquí puedes añadir más detalles

with tab4:
    st.header("🛠️ Herramientas del Creador")
    if st.button("Sacar una Herramienta del Creador"):
        if herramientas_del_creador:
            carta = random.choice(herramientas_del_creador)
            st.subheader(carta["titulo"])
            st.image(carta["imagen"], use_container_width=True)
            with st.expander("Ver Aplicación Didáctica 📖"):
                st.success(f"**Aplicación Didáctica:** {carta['aplicacion_didactica']}")
                st.info(f"**Sugerencia de IA:** {carta['traduccion_ia']}")

# --- MÓDULO DE APOYO ---
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write(
    """
    ¿Te han gustado estas herramientas? 
    Tu apoyo me ayuda a seguir creando y mejorando más juegos educativos y creativos.
    
    ¡Gracias por tu generosidad!
    """
)
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
