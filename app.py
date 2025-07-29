import streamlit as st
import random

st.set_page_config(page_title="Tarot del Asombro", page_icon="🔑", layout="wide")

# --- 1. DEFINICIÓN COMPLETA Y CORREGIDA DE LOS MAZOS ---

arcanos_mayores = [
    {"titulo": "La cicatriz como texto", "imagen": "cicatriz.png", "interpretacion": "Explora el error, el fallo o la ruptura como fuente de conocimiento.", "pregunta_clave": "¿Qué nos enseña lo que salió mal?"},
    {"titulo": "El exilio de la perspectiva", "imagen": "exilio.png", "interpretacion": "Obliga a tomar otro punto de vista. Cambia de rol, contexto o escala.", "pregunta_clave": "¿Cómo vería esto un otro radical?"},
    {"titulo": "El oráculo engañoso", "imagen": "oraculo.png", "interpretacion": "Identifica creencias asumidas, ideas falsas o simplificaciones.", "pregunta_clave": "¿Qué parece cierto pero no lo es del todo?"},
    {"titulo": "El nudo gordiano", "imagen": "nudo.png", "interpretacion": "Enfrenta una contradicción o dilema sin solución evidente. Habita la paradoja antes de resolver.", "pregunta_clave": "N/A"},
    {"titulo": "La encarnación del fantasma", "imagen": "fantasma.png", "interpretacion": "La traducción forzosa de una abstracción a un artefacto tangible.", "pregunta_clave": "Si no puedes construirlo, aún no lo has entendido."}
]

arcanos_de_tension = [
    {"pregunta": "¿Qué perderías si no pudieras pensar creativamente?", "traduccion_didactica": "Identifica la dependencia de un solo tipo de solución. Busca la función del pensamiento divergente.", "imagen": "tension_1.png"},
    {"pregunta": "¿Qué historia te estás contando que entorpece tu camino?", "traduccion_didactica": "Identifica una narrativa limitante o una interpretación automatizada del problema.", "imagen": "tension_2.png"},
    {"pregunta": "¿Cuándo sientes que la GEN IA o las redes sociales te manipulan?", "traduccion_didactica": "Reconoce la influencia externa o invisible en la toma de decisiones (datos, algoritmos, fuentes, autoridad).", "imagen": "tension_3.png"}
]

arcanos_ergodicos = [
    {"titulo": "ADICIÓN", "gesto": "Añade una capa. Inserta un nuevo elemento que cambie por completo el significado de la historia original.", "imagen": "adicion.png"},
    {"titulo": "OMISIÓN", "gesto": "Crea un vacío. Elimina el elemento más obvio o importante de la narrativa. ¿Qué nueva historia emerge del silencio y la ausencia?", "imagen": "omision.png"},
    {"titulo": "TRANSPOSICIÓN", "gesto": "Altera la secuencia. Cambia el orden de los eventos. Narra la historia desde el final hacia el principio.", "imagen": "transposicion.png"},
    {"titulo": "PERMUTACIÓN", "gesto": "Invierte la función. Toma un objeto y dale el significado de otro. Intercambia la función de dos elementos.", "imagen": "permutacion.png"}
]

herramientas_del_creador = [
    {"titulo": "El pincel de la imaginación absoluta", "aplicacion_didactica": "Representa con arte visual (collage, dibujo, maqueta, prototipo, mapa creativo).", "traduccion_ia": "🎨 DALL·E, Midjourney, Leonardo AI → generar ilustraciones, collages, concept art.", "imagen": "pincel.png"},
    {"titulo": "Lente de recuerdos infinitos", "aplicacion_didactica": "Usa fotos, documentación, archivo visual o narrativas del pasado.", "traduccion_ia": "🖼️ RunwayML (para remixar), Photoshop AI, o GPT con análisis de imagen.", "imagen": "lente.png"},
    {"titulo": "Espejo de rostros vivientes", "aplicacion_didactica": "Crea personajes o roles desde la perspectiva del otro.", "traduccion_ia": "🧑‍🎤 D-ID (avatares que hablan), HeyGen, o Character.AI para simular interacción.", "imagen": "espejo.png"},
    {"titulo": "La lira sonora", "aplicacion_didactica": "Traduce ideas a sonido: canción, podcast, atmósfera sonora.", "traduccion_ia": "🎵 Suno, Soundraw, ElevenLabs (voz para narrar un podcast generado).", "imagen": "lira.png"},
    {"titulo": "Pergamino de visiones dinámicas", "aplicacion_didactica": "Expresa con videos, visual thinking, teatro breve, infografías.", "traduccion_ia": "📽️ Gamma, Synthesia, RunwayML, o GPT + Canva para storyboard narrativo.", "imagen": "pergamino.png"},
    {"titulo": "El libro de arena", "aplicacion_didactica": "Investiga a fondo desde múltiples fuentes, contrasta saberes.", "traduccion_ia": "🔍 ChatGPT (modo investigador), Perplexity AI, Scite, Consensus.", "imagen": "libro_de_arena.png"},
    {"titulo": "La encarnación del fantasma", "aplicacion_didactica": "Da voz a lo ausente o silenciado; dramatiza lo invisible.", "traduccion_ia": "👻 D-ID (voz y rostro para personajes excluidos), Murf.AI, GPT con prompts simbólicos.", "imagen": "fantasma.png"}
]

# --- 2. Interfaz Principal ---

st.title("Tarot del Asombro")
st.info("Un dispositivo narrativo-pedagógico para activar la conciencia crítica, el pensamiento simbólico y la educación imaginativa.")

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
            st.write(f"_{carta['interpretacion']}_")
            st.caption(f"**Pregunta Clave:** {carta['pregunta_clave']}")
    with col2:
        st.subheader("🜃 Arcanos de Tensión")
        st.write("Preguntas peligrosas diseñadas para abrir grietas en tus narrativas.")
        if st.button("Sacar un Arcano de Tensión"):
            carta = random.choice(arcanos_de_tension)
            st.warning(f"**Tu pregunta:** {carta['pregunta']}")
            st.image(carta['imagen'], use_container_width=True)
            with st.expander("Ver Traducción Didáctica 📖"):
                st.write(carta['traduccion_didactica'])

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
            st.write(f"**Aplicación Didáctica:** {carta['aplicacion_didactica']}")
            st.info(f"**Sugerencia de IA:** {carta['traduccion_ia']}")
    with col4:
        st.subheader("⚗️ La Transmutación (Arcanos Ergódicos)")
        st.write("Los verbos de la creación y la deconstrucción para manipular la realidad narrativa.")
        if st.button("Elegir un Verbo del Alquimista"):
            carta = random.choice(arcanos_ergodicos)
            st.warning(f"**Tu Táctica:** {carta['titulo']}")
            st.image(carta['imagen'], use_container_width=True)
            st.caption(f"**Gesto:** {carta['gesto']}")

with tab3:
    st.header("⚗️ EL MANUAL DEL ALQUIMISTA")
    st.write("Función: Integrar. Diseñar. Reflexionar. Modelos que guían la práctica docente.")
    with st.expander("✨ SPARK: Un Ciclo Metodológico"):
        st.markdown("- **S**ituación provocadora\n- **P**rocesos emocionales\n- **A**ctivación creativa\n- **R**epresentación simbólica\n- **K**aleidoscopio de evaluación reflexiva")
    with st.expander("💡 Ritual de Uso Sugerido"):
        st.markdown("1.  **La Invocación:** Saca una carta de 'La Llave del Asombro'.\n2.  **La Reacción:** El grupo dialoga sobre el desafío.\n3.  **La Elección:** Elige una 'Herramienta del Creador' para prototipar una respuesta.\n4.  **La Creación:** Produce un artefacto narrativo (texto, imagen, video, etc.).\n5.  **La Reflexión:** Activa el ciclo SPARK para revisar el aprendizaje desde el asombro.")

# --- Módulo de Apoyo en la Barra Lateral ---
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write("Si te ha sido útil esta herramienta, considera apoyar su desarrollo futuro.")
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
