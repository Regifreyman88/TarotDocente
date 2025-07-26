import streamlit as st
import random

st.set_page_config(page_title="Tarot Docente", page_icon="🔮", layout="wide")

# --- 1. Definición de TODOS los Mazos con Información Didáctica ---

arcanos_mayores = [
    {
        "titulo": "La cicatriz como texto", "imagen": "cicatriz.png",
        "interpretacion": "Explora el error, el fallo o la ruptura como fuente de conocimiento.",
        "pregunta_clave": "¿Qué nos enseña lo que salió mal?",
        "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.",
        "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."
    },
    {
        "titulo": "El exilio de la perspectiva", "imagen": "exilio.png",
        "interpretacion": "Obliga a tomar otro punto de vista. Cambia de rol, contexto o escala.",
        "pregunta_clave": "¿Cómo vería esto un otro radical?",
        "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.",
        "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."
    },
    {
        "titulo": "El oráculo engañoso", "imagen": "oraculo.png",
        "interpretacion": "Identifica creencias asumidas, ideas falsas o simplificaciones.",
        "pregunta_clave": "¿Qué parece cierto pero no lo es del todo?",
        "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.",
        "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."
    },
    {
        "titulo": "El nudo gordiano", "imagen": "nudo.png",
        "interpretacion": "Enfrenta una contradicción o dilema sin solución evidente. Habita la paradoja antes de resolver.",
        "pregunta_clave": "N/A",
        "funcion_simbolica": "Desestabiliza. Invita a mirar desde otro ángulo.",
        "aplicacion_transversal": "Cambia el marco. Observa lo que dabas por hecho."
    }
]

arcanos_de_tension = [
    {
        "pregunta": "¿Qué historia te estás contando que entorpece tu camino?",
        "traduccion_didactica": "Identifica una narrativa limitante o una interpretación automatizada del problema.",
        "imagen": "tension_1.png",
        "funcion_simbolica": "Provoca una pregunta difícil.",
        "aplicacion_transversal": "Detecta el conflicto o sesgo oculto."
    },
    {
        "pregunta": "¿Qué perderías si no pudieras pensar creativamente?",
        "traduccion_didactica": "Identifica la dependencia de un solo tipo de solución. Busca la función del pensamiento divergente.",
        "imagen": "tension_2.png",
        "funcion_simbolica": "Provoca una pregunta difícil.",
        "aplicacion_transversal": "Detecta el conflicto o sesgo oculto."
    },
    {
        "pregunta": "¿Cuándo sientes que la IA o las redes sociales te manipulan?",
        "traduccion_didactica": "Reconoce la influencia externa o invisible en la toma de decisiones (datos, algoritmos, fuentes, autoridad).",
        "imagen": "tension_3.png",
        "funcion_simbolica": "Provoca una pregunta difícil.",
        "aplicacion_transversal": "Detecta el conflicto o sesgo oculto."
    }
]

arcanos_ergodicos = [
    {
        "titulo": "Adición", "imagen": "adicion.png",
        "aplicacion_generica": "Agrega un elemento disruptivo (dato nuevo, variable, personaje, condición límite).",
        "funcion_simbolica": "Interviene. Transforma.",
        "aplicacion_transversal": "Modifica un proceso, estructura o producto para ver qué revela el cambio."
    },
    {
        "titulo": "Omisión", "imagen": "omision.png",
        "aplicacion_generica": "Elimina una pieza clave y analiza cómo cambia el sistema, discurso o fenómeno.",
        "funcion_simbolica": "Interviene. Transforma.",
        "aplicacion_transversal": "Modifica un proceso, estructura o producto para ver qué revela el cambio."
    },
    {
        "titulo": "Transposición", "imagen": "transposicion.png",
        "aplicacion_generica": "Reorganiza los pasos, eventos, etapas o argumentos. Cambia el orden y observa los efectos.",
        "funcion_simbolica": "Interviene. Transforma.",
        "aplicacion_transversal": "Modifica un proceso, estructura o producto para ver qué revela el cambio."
    },
    {
        "titulo": "Permutación", "imagen": "permutacion.png",
        "aplicacion_generica": "Intercambia funciones, roles o significados entre dos elementos del sistema.",
        "funcion_simbolica": "Interviene. Transforma.",
        "aplicacion_transversal": "Modifica un proceso, estructura o producto para ver qué revela el cambio."
    }
]

herramientas_del_creador = [
    {
        "titulo": "Pincel de la imaginación absoluta", "imagen": "pincel.png",
        "aplicacion_didactica": "Representa con arte visual (collage, dibujo, maqueta, prototipo, mapa creativo).",
        "traduccion_ia": "🎨 DALL·E, Midjourney, Leonardo AI → generar ilustraciones, collages, concept art."
    },
    {
        "titulo": "Lente de recuerdos infinitos", "imagen": "lente.png",
        "aplicacion_didactica": "Usa fotos, documentación, archivo visual o narrativas del pasado.",
        "traduccion_ia": "🖼️ RunwayML (para remixar), Photoshop AI, o GPT + imagen como asistente de análisis narrativo de fotos."
    },
    {
        "titulo": "Encarnación del fantasma", "imagen": "fantasma.png",
        "aplicacion_didactica": "Da voz a lo ausente o silenciado; dramatiza lo invisible.",
        "traduccion_ia": "👻 D-ID (voz y rostro para personajes excluidos), Murf.AI, GPT con prompts simbólicos."
    }
]


# --- 2. Interfaz de la Aplicación con Pestañas ---

st.title("🔮 Tarot Docente")
st.write("Una herramienta para aplicar el pensamiento de diseño y la creatividad en el aula.")

tab1, tab2, tab3, tab4 = st.tabs(["✨ Arcanos Mayores", "💥
