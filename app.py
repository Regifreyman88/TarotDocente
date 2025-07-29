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
    {"titulo": "PER
