import streamlit as st
import streamlit.components.v1 as components
import time
import base64

# Configuración inicial
st.set_page_config(page_title="Love Wrapped 2026 💖", layout="centered")

# --- FUNCIONES DE CARGA (IMÁGENES Y AUDIO) ---
def get_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

# Carga de imágenes
img1, img2, img3, img4 = get_base64("foto1.jpeg"), get_base64("foto2.jpeg"), get_base64("foto3.jpeg"), get_base64("foto4.jpeg")

# Inicializar estado
if 'paso' not in st.session_state:
    st.session_state.paso = 'carga'

# --- LÓGICA DE MÚSICA ---
archivo_musica = "musica_romantica.mp3" if st.session_state.paso != 'final' else "musica_celebracion.mp3"
audio_b64 = get_base64(archivo_musica)

if audio_b64:
    audio_html = f"""
    <audio id="bg-music" autoplay loop>
        <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    </audio>
    <script>
        var audio = document.getElementById("bg-music");
        audio.volume = 0.5;
    </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #FFE4E1; }
    @keyframes fall { 0% { top: -10%; transform: rotate(0deg); } 100% { top: 110%; transform: rotate(360deg); } }
    .decoracion { position: fixed; top: -10%; z-index: 0; user-select: none; pointer-events: none; animation: fall linear infinite; opacity: 0.8; }
    .titulo { color: #800020; text-align: center; font-family: 'Georgia'; font-weight: bold; position: relative; z-index: 1; text-shadow: 2px 2px white; }
    
    .card-carta { 
        background: rgba(255, 255, 255, 0.9); padding: 40px; border-radius: 20px; border: 3px dashed #FF69B4; 
        color: #800020; text-align: center; position: relative; z-index: 1; font-size: 24px; line-height: 1.6;
        box-shadow: 0 10px 25px rgba(255, 105, 180, 0.2);
    }

    .card { background: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 15px; border: 2px dashed #FF69B4; color: #800020; text-align: center; position: relative; z-index: 1; }
    
    .stButton > button {
        border-radius: 20px !important; font-size: 16px !important; color: #800020 !important;
        border: 1px solid #FF69B4 !important; background-color: white !important; margin-top: 10px !important; width: 100%;
    }

    /* --- COLLAGE RESPONSIVE --- */
    .collage-wrapper { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        gap: 25px; 
        z-index: 1; 
        width: 100%;
    }

    .fila { 
        display: flex; 
        justify-content: center; 
        gap: 30px; 
        width: 100%;
        flex-wrap: wrap;
    }

    .foto-card { 
        background: white; 
        padding: 15px 15px 45px 15px; 
        box-shadow: 0 15px 30px rgba(0,0,0,0.2); 
        width: 90%;
        max-width: 320px;
        text-align: center; 
    }

    .foto-card img { 
        width: 100%; 
        height: auto; 
        aspect-ratio: 3/4;
        object-fit: cover; 
        border-radius: 8px;
    }

    .foto-card p { 
        margin-top: 15px; 
        font-family: 'Comic Sans MS', cursive; 
        font-size: 15px; 
        color: #444; 
        font-weight: bold; 
    }

    .f1 { transform: rotate(-4deg); } 
    .f2 { transform: rotate(4deg); } 
    .f3 { transform: rotate(-2deg); } 
    .f4 { transform: rotate(5deg); }

    /* Ajuste para celular */
    @media (max-width: 768px) {
        .fila {
            flex-direction: column;
            align-items: center;
            gap: 25px;
        }

        .foto-card {
            width: 85%;
            max-width: 340px;
        }
    }
    
    @keyframes heartbeat {
        0% { transform: scale(1); } 
        50% { transform: scale(1.1); } 
        100% { transform: scale(1); }
    }
    </style>

    <div class="decoracion" style="left:5%; font-size:35px; animation-duration:6s;">❤️</div>
    <div class="decoracion" style="left:50%; font-size:40px; animation-duration:14s;">🌹</div>
    <div class="decoracion" style="left:85%; font-size:32px; animation-duration:8s;">💖</div>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
def boton_continuar():
    if st.button("✨ Continuar", key=f"btn_{st.session_state.paso}"):
        orden = ['carga', 'stats', 'collage', 'latido', 'carta', 'pregunta']
        idx = orden.index(st.session_state.paso)
        st.session_state.paso = orden[idx + 1]
        st.rerun()

# --- PANTALLAS ---
if st.session_state.paso == 'carga':
    st.markdown("<h1 class='titulo'>❤️ love.wrapped 💖</h1>", unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(101):
        time.sleep(0.02)
        bar.progress(i)
    st.session_state.paso = 'stats'
    st.rerun()

elif st.session_state.paso == 'stats':
    st.markdown("<h2 class='titulo'>EL AÑO EN NÚMEROS ✨</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>💭 Días pensando en ti: <b>366 🌙</b></div><br>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🧪 Nivel de Química: <b>100% Explosivo! 🔥</b></div><br>", unsafe_allow_html=True)
    st.markdown("<div class='card'>✨ Mejor decisión: <b>Tú, siempre. 💍</b></div><br>", unsafe_allow_html=True)
    st.markdown("<div class='card'>❤️ Estado actual: <b>Enamorado 1000000000% 😍</b></div>", unsafe_allow_html=True)
    boton_continuar()

elif st.session_state.paso == 'collage':
    st.markdown("<h2 class='titulo'>NUESTROS MOMENTOS ✨</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="collage-wrapper">
        <div class="fila">
            <div class="foto-card f1"><img src="data:image/jpeg;base64,{img1}"><p>Aquel día en el río, donde el tiempo se detuvo contigo 🌊💖</p></div>
            <div class="foto-card f2"><img src="data:image/jpeg;base64,{img2}"><p>Amo esa risa tuya, incluso cuando intentas ocultarla 🥰✨</p></div>
        </div>
        <div class="fila">
            <div class="foto-card f3"><img src="data:image/jpeg;base64,{img3}"><p>Tus ojos... mi lugar favorito en el mundo entero 👀❤️</p></div>
            <div class="foto-card f4"><img src="data:image/jpeg;base64,{img4}"><p>Para siempre juntos... 🥰</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    boton_continuar()

elif st.session_state.paso == 'latido':
    st.markdown("<br><br><div style='text-align:center; font-size:100px; animation: heartbeat 1s infinite;'>❤️</div><h2 class='titulo'>Escucha mi corazón...</h2>", unsafe_allow_html=True)
    boton_continuar()

elif st.session_state.paso == 'carta':
    st.markdown("<h2 class='titulo'>Para ti... 💌</h2>", unsafe_allow_html=True)
    mensaje = """¿Para siempre?... ❤️<br><br>Sabes, siempre fui de esas personas que creen que todo, ¡¡¡TODO!!!, tiene un final y que las personas solo son etapas.<br><br>Pero tú eres quien me hace dudar, y no sé si esto sea eterno pero me enamoré, y solo puedo asegurarte que te amaré hasta que las galaxias colapsen.<br><br>Hasta que los mundos se acaben, hasta que la luna desaparezca, hasta que las estrellas ardan y el sol se apague.<br><br>Te amaré hasta que mi corazón deje de latir. Solo entonces, quizá, deje de amarte.<br><br>Y si no eres el amor de mi vida, diré que me equivoqué de vida, pero no de amor.<br><br>Te amo infinitamente."""
    st.markdown(f"<div class='card-carta' style='font-style: italic;'>{mensaje}</div>", unsafe_allow_html=True)
    boton_continuar()

elif st.session_state.paso == 'pregunta':
    st.markdown("<h1 class='titulo'>¿QUIERES SER MI SAN VALENTÍN? 💘</h1>", unsafe_allow_html=True)
    
    _, col1, col2, _ = st.columns([1, 2, 2, 1])

    with col1:
        if st.button("¡SÍ, ACEPTO! ❤️", key="final_si"):
            st.session_state.paso = 'final'
            st.rerun()
    
    with col2:
        components.html("""
        <div id="container" style="position: relative; width: 100%; height: 500px; overflow: visible;">
            <button id="noBtn" style="
                position: absolute; 
                padding: 10px 25px; 
                background: white; 
                color: #800020; 
                border: 1px solid #FF69B4; 
                border-radius: 20px; 
                font-size: 16px; 
                cursor: pointer; 
                left: 40%; 
                top: 0px;
                transition: 0.15s ease;
                z-index: 1000;
                white-space: nowrap;
                font-family: sans-serif;
            ">No... 💔</button>
        </div>
        <script>
            const btn = document.getElementById('noBtn');
            const container = document.getElementById('container');

            const mover = () => {
                const maxX = container.clientWidth - btn.clientWidth;
                const maxY = container.clientHeight - btn.clientHeight;

                let newX, newY;
                let intento = 0;

                do {
                    newX = Math.random() * maxX;
                    newY = Math.random() * maxY;
                    intento++;
                } 
                while (
                    Math.abs(newX - btn.offsetLeft) < 120 &&
                    Math.abs(newY - btn.offsetTop) < 120 &&
                    intento < 20
                );

                btn.style.left = newX + 'px';
                btn.style.top = newY + 'px';
            };

            btn.addEventListener('mouseover', mover);
            btn.addEventListener('click', (e) => { e.preventDefault(); mover(); });
        </script>
        """, height=500)

elif st.session_state.paso == 'final':
    st.balloons()
    st.markdown("<h1 class='titulo'>¡SABÍA QUE DIRÍAS QUE SÍ! 😍</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='card' style='font-size: 26px; border: 4px solid #FF69B4;'>
            🌸 <b>¡ERES LO MEJOR DE MI VIDA!</b> 🌸<br><br>
            Gracias por aceptar ser mi San Valentín.<br>
            <b>Te amo demasiado. ❤️</b><br><br>
            💍✨🌹
        </div>
    """, unsafe_allow_html=True)

