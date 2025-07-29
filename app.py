import streamlit as st
import random

st.set_page_config(page_title="Tarot Docente", page_icon="🔮", layout="wide")

# --- 1. Definición de TODOS los Mazos con Información Didáctica ---

arcanos_mayores = [
    {"titulo": "La cicatriz como texto", "imagen": "cicatriz.png", "interpretacion": "Explora el error, el fallo o la ruptura como fuente de conocimiento.", "pregunta_clave": "¿Qué nos enseña lo que salió mal?", "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.", "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."},
    {"titulo": "El exilio de la perspectiva", "imagen": "exilio.png", "interpretacion": "Obliga a tomar otro punto de vista. Cambia de rol, contexto o escala.", "pregunta_clave": "¿Cómo vería esto un otro radical?", "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.", "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."},
    {"titulo": "El oráculo engañoso", "imagen": "oraculo.png", "interpretacion": "Identifica creencias asumidas, ideas falsas o simplificaciones.", "pregunta_clave": "¿Qué parece cierto pero no lo es del todo?", "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.", "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."},
    {"titulo": "El nudo gordiano", "imagen": "nudo.png", "interpretacion": "Enfrenta una contradicción o dilema sin solución evidente. Habita la paradoja antes de resolver.", "pregunta_clave": "N/A", "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.", "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."},
    {"titulo": "Encarnación del fantasma", "imagen": "fantasma.png", "interpretacion": "Da voz a lo ausente o silenciado; dramatiza lo invisible.", "pregunta_clave": "N/A", "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.", "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."}
]

arcanos_de_tension = [
    {"pregunta": "¿Qué historia te estás contando que entorpece tu camino?", "traduccion_didactica": "Identifica una narrativa limitante o una interpretación automatizada del problema.", "imagen": "tension_1.png", "funcion_simbolica": "Provoca una pregunta difícil.", "aplicacion_transversal": "Detecta el conflicto o sesgo oculto."},
    {"pregunta": "¿Qué perderías si no pudieras pensar creativamente?", "traduccion_didactica": "Identifica la dependencia de un solo tipo de solución. Busca la función del pensamiento divergente.", "imagen": "tension_2.png", "funcion_simbolica": "Provoca una pregunta difícil.", "aplicacion_transversal": "Detecta el conflicto o sesgo oculto."},
    {"pregunta": "¿Cuándo sientes que la IA o las redes sociales te manipulan?", "traduccion_didactica": "Reconoce la influencia externa o invisible en la toma de decisiones (datos, algoritmos, fuentes, autoridad).", "imagen": "tension_3.png", "funcion_simbolica": "Provoca una pregunta difícil.", "aplicacion_transversal": "Detecta el conflicto o sesgo oculto."}
]

arcanos_ergodicos = [
    {"titulo": "Adición", "imagen": "adicion.png", "aplicacion_generica": "Agrega un elemento disruptivo (dato nuevo, variable, personaje, condición límite).", "funcion_simbolica": "Interviene. Transforma.", "aplicacion_transversal": "Modifica un proceso, estructura o producto para ver qué revela el cambio."},
    {"titulo": "Omisión", "imagen": "omision.png", "aplicacion_generica": "Elimina una pieza clave y analiza cómo cambia el sistema, discurso o fenómeno.", "funcion_simbolica": "Interviene. Transforma.", "aplicacion_transversal": "Modifica un proceso..."},
    {"titulo": "Permutación", "imagen": "permutacion.png", "aplicacion_generica": "Intercambia funciones, roles o significados entre dos elementos del sistema.", "funcion_simbolica": "Interviene. Transforma.", "aplicacion_transversal": "Modifica un proceso..."},
    {"titulo": "Transposición", "imagen": "transposicion.png", "aplicacion_generica": "Reorganiza los pasos, eventos, etapas o argumentos. Cambia el orden y observa los efectos.", "funcion_simbolica": "Interviene. Transforma.", "aplicacion_transversal": "Modifica un proceso..."}
]

herramientas_del_creador = [
    {"titulo": "Pincel de la imaginación absoluta", "imagen": "pincel.png", "aplicacion_didactica": "Representa con arte visual (collage, dibujo, maqueta, prototipo, mapa creativo).", "traduccion_ia": "🎨 DALL·E, Midjourney, Leonardo AI → generar ilustraciones, collages, concept art."},
    {"titulo": "Lente de recuerdos infinitos", "imagen": "lente.png", "aplicacion_didactica": "Usa fotos, documentación, archivo visual o narrativas del pasado.", "traduccion_ia": "🖼️ RunwayML (para remixar), Photoshop AI, o GPT con análisis de imagen."},
    {"titulo": "Espejo de rostros vivientes", "imagen": "espejo.png", "aplicacion_didactica": "Crea personajes o roles desde la perspectiva del otro.", "traduccion_ia": "🧑‍🎤 D-ID (avatares que hablan), HeyGen, o Character.AI para simular interacción."},
    {"titulo": "Lira sonora", "imagen": "lira.png", "aplicacion_didactica": "Traduce ideas a sonido: canción, podcast, atmósfera sonora.", "traduccion_ia": "🎵 Suno, Soundraw, ElevenLabs (voz para narrar un podcast generado)."},
    {"titulo": "Pergamino de visiones dinámicas", "imagen": "pergamino.png", "aplicacion_didactica": "Expresa con videos, visual thinking, teatro breve, infografías.", "traduccion_ia": "📽️ Gamma, Synthesia, RunwayML, o GPT + Canva para storyboard narrativo."},
    {"titulo": "Libro de arena", "imagen": "libro_de_arena.png", "aplicacion_didactica": "Investiga a fondo desde múltiples fuentes, contrasta saberes.", "traduccion_ia": "🔍 ChatGPT (modo investigador), Perplexity AI, Scite, Consensus."}
]

# --- 2. Interfaz Principal ---

st.title("Tarot del Asombro")
st.info(
    """
    Estás ante un dispositivo narrativo-pedagógico creado para activar la conciencia crítica, el pensamiento simbólico y la educación imaginativa. 
    Cada carta es una metáfora didáctica viva: no predice el futuro, sino que revela estructuras profundas del aprender, del crear y del narrarse a sí mismo.
    """
)

tab1, tab2, tab3 = st.tabs(["🔑 LA LLAVE DEL ASOMBRO (El Oráculo)", "🛠️ LAS HERRAMIENTAS DEL CREADOR (El Taller)", "⚗️ EL MANUAL DEL ALQUIMISTA (La Metodología)"])

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
            st.image(carta['imagen'], use_container_width=True)
    with col2:
        st.subheader("🜃 Arcanos de Tensión")
        st.write("Preguntas peligrosas diseñadas para abrir grietas en tus narrativas.")
        if st.button("Sacar un Arcano de Tensión"):
            carta = random.choice(arcanos_de_tension)
            st.warning(f"**Tu pregunta:** {carta['pregunta']}")
            st.image(carta['imagen'], use_container_width=True)

with tab2:
    st.header("🛠️ LAS HERRAMIENTAS DEL CREADOR")
    st.write("Función: Elegir. Prototipar. Dar forma a la respuesta.")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("El Taller de Creación")
        st.write("Técnicas y lenguajes para dar forma a tu respuesta narrativa, visual o simbólica.")
        if st.button("Elegir una Herramienta"):
            carta = random.choice(herramientas_del_creador)
            st.success(f"**Tu Herramienta:** {carta['titulo']}")
            st.image(carta['imagen'], use_container_width=True)
    with col4:
        st.subheader("⚗️ La Transmutación (Arcanos Ergódicos)")
        st.write("Los verbos de la creación y la deconstrucción para manipular la realidad narrativa.")
        if st.button("Elegir un Verbo del Alquimista"):
            carta = random.choice(arcanos_ergodicos)
            st.warning(f"**Tu Táctica:** {carta['titulo']}")
            st.image(carta['imagen'], use_container_width=True)
            st.caption(carta['gesto'])

with tab3:
    st.header("⚗️ EL MANUAL DEL ALQUIMISTA")
    st.write("Función: Integrar. Diseñar. Reflexionar. Modelos que guían la práctica docente.")
    
    with st.expander("✨ SPARK: Un Ciclo Metodológico"):
        st.markdown("- **S**ituación provocadora\n- **P**rocesos emocionales\n- **A**ctivación creativa\n- **R**epresentación simbólica\n- **K**aleidoscopio de evaluación reflexiva")
    
    # --- SECCIÓN ACTUALIZADA Y MEJORADA ---
    with st.expander("🧠 Educación Imaginativa"):
        st.markdown(
            """
            Es una forma única de enseñanza que aprovecha la vida emocional e imaginativa de los estudiantes. 
            Se enfoca en "herramientas cognitivas" que estimulan la imaginación en todas las áreas temáticas.
            
            El docente puede diseñar una actividad para estimular uno de los siguientes **tipos de imaginación:**
            
            - **Somática:** Comprensión a través del cuerpo y los sentidos.
            - **Mítica:** Comprensión a través de historias, metáforas y opuestos binarios.
            - **Romántica:** Comprensión a través de la fascinación por los límites de la realidad y lo extraordinario.
            - **Filosófica:** Comprensión a través de la búsqueda de patrones y teorías generales.
            - **Irónica:** Comprensión a través de la conciencia de las limitaciones del lenguaje y las teorías.
            """
        )
        
    with st.expander("💡 Ritual de Uso Sugerido"):
        st.markdown("1.  **La Invocación:** Saca una carta de 'La Llave del Asombro'.\n2.  **La Reacción:** El grupo dialoga sobre el desafío.\n3.  **La Elección:** Elige una 'Herramienta del Creador'.\n4.  **La Creación:** Produce un artefacto narrativo (texto, imagen, video, etc.).\n5.  **La Reflexión:** Activa el ciclo SPARK para revisar el aprendizaje desde el asombro.")

# --- Módulo de Apoyo en la Barra Lateral ---
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write("Si te ha sido útil esta herramienta, considera apoyar su desarrollo futuro.")
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
