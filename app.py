import streamlit as st
import random

st.set_page_config(page_title="Tarot del Asombro", page_icon="🔑", layout="wide")

# --- 1. Definición de Mazos (Reorganizados según tu nuevo texto) ---

arcanos_mayores = [
    {"titulo": "La cicatriz como texto", "imagen": "cicatriz.png"},
    {"titulo": "El exilio de la perspectiva", "imagen": "exilio.png"},
    {"titulo": "El oráculo engañoso", "imagen": "oraculo.png"},
    {"titulo": "El nudo gordiano", "imagen": "nudo.png"}
]

arcanos_de_tension = [
    {"pregunta": "¿Qué perderías si no pudieras pensar creativamente?", "imagen": "tension_1.png"},
    {"pregunta": "¿Qué historia te estás contando que entorpece tu camino?", "imagen": "tension_2.png"},
    {"pregunta": "¿Cuándo sientes que la GEN IA o las redes sociales te manipulan?", "imagen": "tension_3.png"}
]

herramientas_del_creador = [
    {"titulo": "El pincel de la imaginación absoluta", "descripcion": "Arte analógico o digital", "imagen": "pincel.png"},
    {"titulo": "Lente de recuerdos infinitos", "descripcion": "Fotografía y documentación", "imagen": "lente.png"},
    {"titulo": "Espejo de rostros vivientes", "descripcion": "Creación de avatares", "imagen": "espejo.png"},
    {"titulo": "La lira sonora", "descripcion": "Sonorización, creación de canciones", "imagen": "lira.png"},
    {"titulo": "Pergamino de visiones dinámicas", "descripcion": "Mapas visuales, infografías, videos, etc.", "imagen": "pergamino.png"},
    {"titulo": "El libro de arena", "descripcion": "Investigación en buscadores o bibliotecas", "imagen": "libro_de_arena.png"},
    {"titulo": "La encarnación del fantasma", "descripcion": "Dar voz a lo ausente o silenciado.", "imagen": "fantasma.png"}
]

arcanos_ergodicos = [
    {"titulo": "ADICIÓN", "gesto": "Añade una capa. Inserta un nuevo elemento que cambie por completo el significado.", "imagen": "adicion.png"},
    {"titulo": "OMISIÓN", "gesto": "Crea un vacío. Elimina el elemento más obvio o importante.", "imagen": "omision.png"},
    {"titulo": "TRANSPOSICIÓN", "gesto": "Altera la secuencia. Narra la historia desde el final hacia el principio.", "imagen": "transposicion.png"},
    {"titulo": "PERMUTACIÓN", "gesto": "Invierte la función. Toma un objeto y dale el significado de otro.", "imagen": "permutacion.png"}
]

# --- 2. Interfaz Principal ---

st.title("Tarot del Asombro")
st.info(
    """
    Estás ante un dispositivo narrativo-pedagógico creado para activar la conciencia crítica, el pensamiento simbólico y la educación imaginativa. 
    Cada carta es una metáfora didáctica viva: no predice el futuro, sino que revela estructuras profundas del aprender, del crear y del narrarse a sí mismo.
    """
)

tab1, tab2, tab3 = st.tabs(["🔑 LA LLAVE DEL ASOMBRO", "🛠️ LAS HERRAMIENTAS DEL CREADOR", "⚗️ EL MANUAL DEL ALQUIMISTA"])

# --- PESTAÑA 1: LA LLAVE DEL ASOMBRO ---
with tab1:
    st.header("🔑 LA LLAVE DEL ASOMBRO")
    st.write("Función: Abrir. Desestabilizar. Invitar al conflicto creativo.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🜁 Arcanos Mayores")
        st.write("Acciones epistemológicas que simbolizan formas de estar y pensar el mundo.")
        if st.button("Sacar un Arcano Mayor"):
            carta = random.choice(arcanos_mayores)
            st.success(f"**Tu Arcano:** {carta['titulo']}")
            st.image(carta['imagen'])

    with col2:
        st.subheader("🜃 Arcanos de Tensión")
        st.write("Preguntas peligrosas diseñadas para abrir grietas en tus narrativas.")
        if st.button("Sacar un Arcano de Tensión"):
            carta = random.choice(arcanos_de_tension)
            st.warning(f"**Tu pregunta:** {carta['pregunta']}")
            st.image(carta['imagen'])

# --- PESTAÑA 2: LAS HERRAMIENTAS DEL CREADOR ---
with tab2:
    st.header("🛠️ LAS HERRAMIENTAS DEL CREADOR")
    st.write("Función: Elegir. Prototipar. Dar forma a la respuesta.")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("El Taller")
        st.write("Técnicas narrativas y visuales para responder a los dilemas planteados.")
        if st.button("Elegir una Herramienta"):
            carta = random.choice(herramientas_del_creador)
            st.success(f"**Tu Herramienta:** {carta['titulo']}")
            st.image(carta['imagen'])
            st.caption(carta['descripcion'])

    with col4:
        st.subheader("⚗️ La Transmutación (Arcanos Ergódicos)")
        st.write("Los verbos de la creación y la deconstrucción para manipular la realidad narrativa.")
        if st.button("Elegir un Verbo del Alquimista"):
            carta = random.choice(arcanos_ergodicos)
            st.warning(f"**Tu Táctica:** {carta['titulo']}")
            st.image(carta['imagen'])
            st.caption(carta['gesto'])

# --- PESTAÑA 3: EL MANUAL DEL ALQUIMISTA ---
with tab3:
    st.header("⚗️ EL MANUAL DEL ALQUIMISTA")
    st.write("Función: Integrar. Diseñar. Reflexionar. Aquí no hay cartas para sacar, sino modelos que guían la práctica docente.")
    
    with st.expander("✨ SPARK: Un Ciclo Metodológico"):
        st.markdown(
            """
            - **S**ituación provocadora
            - **P**rocesos emocionales
            - **A**ctivación creativa
            - **R**epresentación simbólica
            - **K**aleidoscopio de evaluación reflexiva
            """
        )

    with st.expander("🎓 Otros Conceptos Pedagógicos"):
        st.markdown(
            """
            - **Pensamiento crítico:** Análisis, argumentación y reflexión.
            - **Educación imaginativa:** Situar la actividad en una de las Imaginaciones (somática, mítica, romántica, filosófica o irónica).
            - **Flipped classroom:** El conocimiento se pone del revés, y el aprendiz intercambia el papel con el maestro.
            - **Tapiz de conexión ubicua:** Uso de redes sociales, digitales o análogas.
            - **Arte terapia:** Arte como expresión emocional y autoconocimiento.
            """
        )
        
    with st.expander("🌀 La Espiral del Polímata"):
        st.write("Representa la integración de diversos lenguajes de conocimiento en una creación única, facilitando conexiones transdisciplinares. Se utiliza en contextos donde se cruzan arte y ciencia o se combinan diferentes lenguajes expresivos.")
        
    with st.expander("💡 Ritual de Uso Sugerido"):
        st.markdown(
            """
            1.  **La Invocación:** El docente saca un Arcano de "La Llave del Asombro" (ej. "EL NUDO GORDIANO").
            2.  **La Reacción:** El grupo dialoga sobre el desafío.
            3.  **La Elección:** El equipo elige una "Herramienta del Creador" para ejecutar una táctica. (Ej: "Decidimos usar la OMISIÓN con el Pincel de la Imaginación").
            4.  **La Creación:** Producen su artefacto (texto, collage, video, etc.).
            5.  **La Reflexión:** Comparten su creación y aprendizaje.
            """
        )

# --- Módulo de Apoyo en la Barra Lateral ---
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write("Si te ha sido útil esta herramienta, considera apoyar su desarrollo futuro.")
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
