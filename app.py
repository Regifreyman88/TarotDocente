import streamlit as st
import random

# --- 1. Definición de los Mazos de Cartas ---
# ¡Asegúrate de que tus archivos de imagen tengan estos nombres exactos!

arcanos_mayores = [
    {
        "titulo": "I. LA CICATRIZ COMO TEXTO",
        "descripcion": "El acto de exhumar la narrativa no desde el pedestal del logro, sino desde la topografía de la fractura.",
        "aforismo": "Tu resiliencia no se mide por no haberte roto, sino por la forma en que la luz, ahora, entra a través de tus grietas.",
        "imagen": "cicatriz.png"
    },
    {
        "titulo": "II. EL EXILIO DE LA PERSPECTIVA",
        "descripcion": "El destierro voluntario de la propia mirada para ocupar, por un tiempo, el territorio del otro.",
        "aforismo": "Para entender la fuerza de tu argumento, primero debes aprender a destruirlo con las armas de tu enemigo.",
        "imagen": "exilio.png"
    },
    {
        "titulo": "III. EL ORÁCULO ENGAÑOSO",
        "descripcion": "Usar la IA no para obtener respuestas, sino para poner a prueba la fortaleza de las propias preguntas.",
        "aforismo": "Una pregunta débil busca una respuesta en la IA. Una pregunta fuerte busca una debilidad en la IA.",
        "imagen": "oraculo.png"
    },
    {
        "titulo": "IV. EL NUDO GORDIANO",
        "descripcion": "La capacidad de sostener ideas antagónicas en la mente, no para resolverlas, sino para habitar en la tensión fértil que generan.",
        "aforismo": "La creatividad no nace de resolver la contradicción, sino de hacerla habitable. Y después, fértil.",
        "imagen": "nudo.png"
    },
    {
        "titulo": "V. LA ENCARNACIÓN DEL FANTASMA",
        "descripcion": "La traducción forzosa de una abstracción a un artefacto tangible.",
        "aforismo": "Si no puedes construirlo, aún no lo has entendido. Nombrar es el eco, construir es la voz.",
        "imagen": "fantasma.png"
    }
]

arcanos_de_tension = [
    {
        "titulo": "PREGUNTA PELIGROSA",
        "pregunta": "¿Qué perderías si te vuelves verdaderamente creativo?",
        "imagen": "tension_1.png"
    },
    {
        "titulo": "PREGUNTA PELIGROSA",
        "pregunta": "¿Qué historia te estás contando que entorpece tu camino?",
        "imagen": "tension_2.png"
    },
    {
        "titulo": "PREGUNTA PELIGROSA",
        "pregunta": "¿Cuándo sientes que la IA generativa o las Redes Sociales te manipulan?",
        "imagen": "tension_3.png"
    },
    {
        "titulo": "PREGUNTA PELIGROSA",
        "pregunta": "Describe un acontecimiento de tu vida que, tras una sensación, te llevó a un descubrimiento que cambió el curso de los hechos.",
        "imagen": "tension_4.png"
    }
]

arcanos_ergodicos = [
    {
        "titulo": "ADICIÓN",
        "gesto": "Añade una capa. Inserta un nuevo elemento que cambie por completo el significado de la historia original.",
        "imagen": "adicion.png"
    },
    {
        "titulo": "OMISIÓN",
        "gesto": "Crea un vacío. Elimina el elemento más obvio o importante de la narrativa. ¿Qué nueva historia emerge del silencio?",
        "imagen": "omision.png"
    },
    {
        "titulo": "TRANSPOSICIÓN",
        "gesto": "Altera la secuencia. Narra la historia desde el final hacia el principio.",
        "imagen": "transposicion.png"
    },
    {
        "titulo": "PERMUTACIÓN",
        "gesto": "Invierte la función. Toma un objeto y dale el significado de otro.",
        "imagen": "permutacion.png"
    }
]

caja_de_herramientas = [
    {
        "titulo": "EL MICRÓFONO AMPLIFICADOR",
        "descripcion": "Para debates, pódcasts y la argumentación talentosa.",
        "imagen": "microfono.png"
    },
    {
        "titulo": "LA LIRA SONORA",
        "descripcion": "Armoniza melodías y sentimientos, convirtiendo cualquier tema en una sinfonía viva.",
        "imagen": "lira.png"
    },
    {
        "titulo": "EL ESPEJO DE ROSTROS",
        "descripcion": "Revela rostros y emociones únicas, prestando un rostro humano a lo virtual.",
        "imagen": "espejo.png"
    },
    {
        "titulo": "PINCEL DE LA IMAGINACIÓN",
        "descripcion": "Con un simple trazo, colores y formas infinitas cobran vida.",
        "imagen": "pincel.png"
    },
    {
        "titulo": "PERGAMINO DE VISIONES DINÁMICAS",
        "descripcion": "Herramientas de visualización que no son diagramas estáticos, sino narrativas que guían.",
        "imagen": "pergamino.png"
    },
    {
        "titulo": "EL LIBRO DE ARENA",
        "descripcion": "Palabras eternas que fluyen como granos de memoria. Investigación profunda.",
        "imagen": "libro_de_arena.png"
    },
    {
        "titulo": "EL LENTE DE LOS RECUERDOS",
        "descripcion": "Este lente no solo observa recuerdos, sino que los guarda como un tesoro: reflexión y documentación.",
        "imagen": "lente.png"
    },
    {
        "titulo": "ARTE TERAPIA",
        "descripcion": "En el reino de este pincel, los colores transforman no sólo el lienzo, sino también el espíritu.",
        "imagen": "arteterapia.png"
    },
    {
        "titulo": "EDUCACIÓN IMAGINATIVA",
        "descripcion": "Uso de la imaginación: Somática, Mítica, Romántica, Filosófica e Irónica.",
        "imagen": "imaginativa.png"
    }
]

# --- 2. Diseño de la Interfaz con Streamlit ---

st.set_page_config(page_title="Tarot Docente", layout="wide")

# Título de la aplicación
st.title("🔮 Tarot Docente: diseña tu clase")
st.write("Haz clic en un mazo para sacar una carta y encontrar inspiración.")

# Crear columnas para los botones
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Sacar Arcano Mayor"):
        carta_seleccionada = random.choice(arcanos_mayores)
        st.session_state.carta_actual = carta_seleccionada

with col2:
    if st.button("Sacar Arcano de Tensión"):
        carta_seleccionada = random.choice(arcanos_de_tension)
        st.session_state.carta_actual = carta_seleccionada

with col3:
    if st.button("Sacar Arcano Ergódico"):
        carta_seleccionada = random.choice(arcanos_ergodicos)
        st.session_state.carta_actual = carta_seleccionada
        
with col4:
    if st.button("Sacar Herramienta"):
        carta_seleccionada = random.choice(caja_de_herramientas)
        st.session_state.carta_actual = carta_seleccionada

# --- 3. Mostrar la Carta Seleccionada ---

# Usamos st.session_state para "recordar" la última carta sacada
if 'carta_actual' in st.session_state:
    carta = st.session_state.carta_actual
    
    st.markdown("---") # Una línea divisoria
    
    # Contenedor para la carta con un borde
    with st.container(border=True):
        # Mostrar la imagen si existe
        if "imagen" in carta:
            try:
                # Streamlit buscará el archivo con este nombre en tu Space
                st.image(carta["imagen"], use_column_width=True)
            except Exception as e:
                st.error(f"Error al cargar la imagen '{carta['imagen']}'. Asegúrate de que el archivo esté subido al Space.")
        
        # Mostrar el texto de la carta
        if "titulo" in carta:
            st.subheader(carta["titulo"])
        if "descripcion" in carta:
            st.write(f"_{carta['descripcion']}_")
        if "aforismo" in carta:
            st.write(f"**❝ {carta['aforismo']} ❞**")
        if "pregunta" in carta:
            st.write(f"**{carta['pregunta']}**")
        if "gesto" in carta:
            st.write(carta["gesto"])
