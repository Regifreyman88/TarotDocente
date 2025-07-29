import streamlit as st
import random

st.set_page_config(page_title="Tarot Docente", page_icon="🔮", layout="wide")

# --- 1. Definición de Mazos (Nombres de imagen verificados con tu GitHub) ---

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
    {"titulo": "Lente de recuerdos infinitos", "imagen": "lente.png", "aplicacion_didactica": "Usa fotos, documentación, archivo visual o narrativas del pasado.", "traduccion_ia": "🖼️ RunwayML (para remixar), Photoshop AI, o GPT + imagen como asistente de análisis narrativo de fotos."},
    {"titulo": "Espejo de rostros vivientes", "imagen": "espejo.png", "aplicacion_didactica": "Crea personajes o roles desde la perspectiva del otro.", "traduccion_ia": "🧑‍🎤 D-ID (avatares que hablan), HeyGen, o Character.AI para simular interacción."},
    {"titulo": "Lira sonora", "imagen": "lira.png", "aplicacion_didactica": "Traduce ideas a sonido: canción, podcast, atmósfera sonora.", "traduccion_ia": "🎵 Suno, Soundraw, ElevenLabs (voz para narrar un podcast generado)."},
    {"titulo": "Pergamino de visiones dinámicas", "imagen": "pergamino.png", "aplicacion_didactica": "Expresa con videos, visual thinking, teatro breve, infografías.", "traduccion_ia": "📽️ Gamma, Synthesia, RunwayML, o GPT + Canva para storyboard narrativo."},
    {"titulo": "Libro de arena", "imagen": "libro_de_arena.png", "aplicacion_didactica": "Investiga a fondo desde múltiples fuentes, contrasta saberes.", "traduccion_ia": "🔍 ChatGPT (modo investigador), Perplexity AI, Scite, Consensus para papers."}
]

# --- 2. Interfaz de la Aplicación con Pestañas ---

st.title("🔮 Tarot Docente")
st.write("Una herramienta para aplicar el pensamiento de diseño y la creatividad en el aula.")

tab1, tab2, tab3, tab4 = st.tabs(["✨ Arcanos Mayores", "💥 Arcanos de Tensión", "♻️ Arcanos Ergódicos", "🛠️ Herramientas del Creador"])

with tab1:
    st.header("✨ Arcanos Mayores")
    st.info("Función: Desestabilizar y cambiar el marco de referencia. Elige un concepto para explorarlo a fondo.")
    
    titulos = [carta["titulo"] for carta in arcanos_mayores]
    opcion_seleccionada = st.selectbox("Selecciona un Arcano Mayor:", titulos)
    
    carta = next((c for c in arcanos_mayores if c["titulo"] == opcion_seleccionada), None)
    
    if carta:
        st.subheader(carta["titulo"])
        st.image(carta["imagen"], use_container_width=True)
        st.write(f"_{carta['interpretacion']}_")
        with st.expander("Ver Aplicación Didáctica 📖"):
            st.success(f"**Aplicación Transversal:** {carta['aplicacion_transversal']}")
            st.write(f"**Pregunta Clave:** {carta['pregunta_clave']}")

with tab2:
    st.header("💥 Arcanos de Tensión")
    st.info("Función: Provocar una pregunta difícil y detectar conflictos ocultos.")
    
    if st.button("Sacar un Arcano de Tensión"):
        carta = random.choice(arcanos_de_tension)
        st.subheader("Pregunta Peligrosa")
        st.image(carta["imagen"], use_container_width=True)
        st.warning(f"**{carta['pregunta']}**")
        with st.expander("Ver Traducción Didáctica 📖"):
            st.success(f"**Aplicación:** {carta['traduccion_didactica']}")

with tab3:
    st.header("♻️ Arcanos Ergódicos")
    st.info("Función: Intervenir y transformar un proceso para revelar algo nuevo.")

    if st.button("Sacar un Arcano Ergódico"):
        carta = random.choice(arcanos_ergodicos)
        st.subheader(carta["titulo"])
        st.image(carta["imagen"], use_container_width=True)
        with st.expander("Ver Aplicación Didáctica 📖"):
            st.success(f"**Aplicación Genérica:** {carta['aplicacion_generica']}")

with tab4:
    st.header("🛠️ Herramientas del Creador")
    st.info("Función: Elegir el lenguaje para expresar y materializar ideas.")

    if st.button("Sacar una Herramienta del Creador"):
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
