import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Wedding Invitation",
    page_icon="💍",
    layout="centered"
)

frame_path = Path(__file__).parent / "frame_cleanup.png"

if frame_path.exists():
    frame_data = base64.b64encode(frame_path.read_bytes()).decode()
    frame_url = f"data:image/png;base64,{frame_data}"
else:
    frame_url = ""


# ---------- CSS ----------
st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cormorant+Garamond:wght@400;500;600&family=Aref+Ruqaa+Ink&display=swap');


* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}


/* ---------- الخلفية العامة ---------- */

.stApp {{
    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(213, 164, 72, 0.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 88% 78%,
            rgba(176, 119, 37, 0.20),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #eadbc2,
            #f8efdf,
            #e5d2b0
        );
}}


header[data-testid="stHeader"] {{
    display: none !important;
}}


.block-container {{
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
    max-width: 500px !important;
    margin: 0 auto !important;
}}


div[data-testid="stVerticalBlock"] {{
    gap: 0 !important;
}}


/* ---------- البطاقة الرئيسية ---------- */

.invitation {{
    position: relative;
    overflow: hidden;

    width: min(480px, 100%);
    aspect-ratio: 2 / 3;

    margin: 0 auto;

    background-image: url("{frame_url}");
    background-size: 100% 100%;
    background-position: center;
    background-repeat: no-repeat;

    box-shadow:
        0 18px 50px rgba(82, 53, 17, 0.32);

    font-family: 'Amiri', serif;
}}

.invitation {{
    opacity: 0;

    animation:
        invitationReveal
        1.1s ease
        4.1s
        forwards;
}}

@keyframes invitationReveal {{

    0% {{
        opacity: 0;
        transform: scale(0.92);
    }}

    100% {{
        opacity: 1;
        transform: scale(1);
    }}
}}

/* ---------- الوهج الذهبي المتحرك ---------- */

.glow {{
    position: absolute;

    width: 190px;
    height: 190px;

    border-radius: 50%;

    background: rgba(255, 194, 77, 0.20);

    filter: blur(55px);

    pointer-events: none;

    z-index: 3;

    animation:
        warmGlow
        10s ease-in-out
        infinite alternate;
}}


.glow-left {{
    top: 7%;
    left: -105px;
}}


.glow-right {{
    top: 32%;
    right: -115px;

    animation-delay: 2.5s;
}}


.glow-bottom {{
    bottom: -105px;
    left: 30%;

    animation-delay: 5s;
}}


@keyframes warmGlow {{

    0% {{
        transform:
            translate(0, 0)
            scale(0.70);

        opacity: 0.18;
    }}

    50% {{
        transform:
            translate(25px, -18px)
            scale(1.08);

        opacity: 0.42;
    }}

    100% {{
        transform:
            translate(-18px, 20px)
            scale(1.35);

        opacity: 0.68;
    }}

}}


/* ---------- نقاط ذهبية براقة ---------- */

.light {{
    position: absolute;

    width: 3px;
    height: 3px;

    border-radius: 50%;

    background: #ffe6a1;

    box-shadow:
        0 0 5px #f6cf70,
        0 0 12px rgba(255, 210, 105, 0.95),
        0 0 22px rgba(218, 164, 52, 0.65);

    pointer-events: none;

    z-index: 6;

    animation:
        sparkle
        4.8s ease-in-out
        infinite;
}}


.light1 {{
    top: 15%;
    left: 17%;
}}


.light2 {{
    top: 20%;
    right: 17%;
    animation-delay: 1.0s;
}}


.light3 {{
    top: 30%;
    left: 12%;
    animation-delay: 2.2s;
}}


.light4 {{
    top: 39%;
    right: 12%;
    animation-delay: 0.7s;
}}


.light5 {{
    top: 49%;
    left: 15%;
    animation-delay: 2.8s;
}}


.light6 {{
    top: 56%;
    right: 14%;
    animation-delay: 1.4s;
}}


.light7 {{
    top: 67%;
    left: 12%;
    animation-delay: 3.0s;
}}


.light8 {{
    top: 76%;
    right: 13%;
    animation-delay: 2.0s;
}}


.light9 {{
    top: 27%;
    left: 27%;
    animation-delay: 3.6s;
}}


.light10 {{
    top: 64%;
    right: 28%;
    animation-delay: 1.8s;
}}


.light11 {{
    top: 82%;
    left: 28%;
    animation-delay: 0.9s;
}}


.light12 {{
    top: 45%;
    right: 28%;
    animation-delay: 2.6s;
}}


@keyframes sparkle {{

    0%, 100% {{
        transform:
            translateY(0)
            scale(0.35);

        opacity: 0.10;
    }}

    35% {{
        opacity: 0.40;
    }}

    50% {{
        transform:
            translateY(-13px)
            scale(1.65);

        opacity: 1;
    }}

    75% {{
        opacity: 0.35;
    }}

}}


/* ---------- أضواء Bokeh ---------- */

.bokeh {{
    position: absolute;

    width: 11px;
    height: 11px;

    border-radius: 50%;

    background:
        rgba(255, 225, 157, 0.70);

    box-shadow:
        0 0 14px rgba(255, 221, 139, 0.85),
        0 0 30px rgba(220, 169, 63, 0.55);

    filter: blur(1px);

    pointer-events: none;

    z-index: 5;

    animation:
        bokehMove
        7s ease-in-out
        infinite;
}}


.bokeh1 {{
    top: 11%;
    left: 11%;
}}


.bokeh2 {{
    top: 24%;
    right: 9%;
    animation-delay: 1.8s;
}}


.bokeh3 {{
    bottom: 20%;
    left: 9%;
    animation-delay: 3.4s;
}}


.bokeh4 {{
    bottom: 13%;
    right: 10%;
    animation-delay: 0.9s;
}}


@keyframes bokehMove {{

    0%, 100% {{
        transform: scale(0.65);
        opacity: 0.18;
    }}

    50% {{
        transform: scale(1.45);
        opacity: 0.82;
    }}

}}

/* ---------- أضواء ذهبية عائمة في الخلفية ---------- */

.floating-light {{
    position: absolute;
    width: 5px;
    height: 5px;
    border-radius: 50%;

    background: #ffe7a3;

    box-shadow:
        0 0 6px #f6cf70,
        0 0 14px rgba(255, 210, 105, 0.95),
        0 0 28px rgba(218, 164, 52, 0.75);

    pointer-events: none;
    z-index: 7;
    opacity: 0;

    animation:
        floatLight
        8s ease-in-out
        infinite;
}}


.fl1 {{
    left: 18%;
    bottom: 18%;
    animation-delay: 0s;
}}

.fl2 {{
    left: 32%;
    bottom: 28%;
    animation-delay: 2s;
}}

.fl3 {{
    left: 48%;
    bottom: 12%;
    animation-delay: 4s;
}}

.fl4 {{
    left: 65%;
    bottom: 25%;
    animation-delay: 1s;
}}

.fl5 {{
    left: 78%;
    bottom: 15%;
    animation-delay: 5s;
}}

.fl6 {{
    left: 24%;
    bottom: 45%;
    animation-delay: 3s;
}}

.fl7 {{
    left: 73%;
    bottom: 42%;
    animation-delay: 6s;
}}

.fl8 {{
    left: 52%;
    bottom: 55%;
    animation-delay: 7s;
}}


@keyframes floatLight {{

    0% {{
        transform:
            translateY(30px)
            scale(0.3);

        opacity: 0;
    }}

    20% {{
        opacity: 0.75;
    }}

    50% {{
        transform:
            translateY(-80px)
            translateX(12px)
            scale(1.2);

        opacity: 1;
    }}

    75% {{
        opacity: 0.65;
    }}

    100% {{
        transform:
            translateY(-160px)
            translateX(-10px)
            scale(0.4);

        opacity: 0;
    }}

}}

/* ---------- جزيئات ذهبية عائمة ---------- */

.floating-particles {{
    position: absolute;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 4;
}}

.floating-particles span {{
    position: absolute;
    bottom: -15px;
    width: 4px;
    height: 4px;
    border-radius: 50%;

    background: #ffe6a1;

    box-shadow:
        0 0 6px #f6cf70,
        0 0 14px rgba(255, 210, 105, 0.95),
        0 0 25px rgba(218, 164, 52, 0.70);

    opacity: 0;

    animation:
        particleFloat
        9s ease-in-out
        infinite;
}}

.floating-particles span:nth-child(1) {{
    left: 8%;
    animation-delay: 0s;
    animation-duration: 8s;
}}

.floating-particles span:nth-child(2) {{
    left: 17%;
    animation-delay: 2s;
    animation-duration: 10s;
}}

.floating-particles span:nth-child(3) {{
    left: 28%;
    animation-delay: 4s;
    animation-duration: 9s;
}}

.floating-particles span:nth-child(4) {{
    left: 39%;
    animation-delay: 1s;
    animation-duration: 11s;
}}

.floating-particles span:nth-child(5) {{
    left: 50%;
    animation-delay: 5s;
    animation-duration: 9s;
}}

.floating-particles span:nth-child(6) {{
    left: 61%;
    animation-delay: 3s;
    animation-duration: 10s;
}}

.floating-particles span:nth-child(7) {{
    left: 72%;
    animation-delay: 6s;
    animation-duration: 8s;
}}

.floating-particles span:nth-child(8) {{
    left: 83%;
    animation-delay: 1.5s;
    animation-duration: 10s;
}}

.floating-particles span:nth-child(9) {{
    left: 92%;
    animation-delay: 4.5s;
    animation-duration: 9s;
}}

.floating-particles span:nth-child(10) {{
    left: 23%;
    animation-delay: 7s;
    animation-duration: 11s;
}}

.floating-particles span:nth-child(11) {{
    left: 68%;
    animation-delay: 5.5s;
    animation-duration: 9s;
}}

.floating-particles span:nth-child(12) {{
    left: 45%;
    animation-delay: 8s;
    animation-duration: 10s;
}}

@keyframes particleFloat {{

    0% {{
        transform:
            translateY(20px)
            translateX(0)
            scale(0.3);

        opacity: 0;
    }}

    20% {{
        opacity: 0.65;
    }}

    50% {{
        transform:
            translateY(-260px)
            translateX(18px)
            scale(1.1);

        opacity: 0.9;
    }}

    75% {{
        opacity: 0.45;
    }}

    100% {{
        transform:
            translateY(-560px)
            translateX(-15px)
            scale(0.25);

        opacity: 0;
    }}
}}


/* ---------- شعاع ضوء ذهبي متحرك ---------- */

.light-ray {{
    position: absolute;

    top: -30%;
    left: -45%;

    width: 70%;
    height: 170%;

    background:
        linear-gradient(
            90deg,
            transparent 0%,
            rgba(255, 221, 145, 0.04) 35%,
            rgba(255, 220, 135, 0.18) 50%,
            rgba(255, 221, 145, 0.04) 65%,
            transparent 100%
        );

    transform: rotate(18deg);

    pointer-events: none;
    z-index: 4;

    animation:
        lightRayMove
        12s ease-in-out
        infinite;
}}

@keyframes lightRayMove {{

    0% {{
        transform:
            translateX(-45%)
            rotate(18deg);

        opacity: 0;
    }}

    20% {{
        opacity: 0.35;
    }}

    50% {{
        transform:
            translateX(70%)
            rotate(18deg);

        opacity: 0.55;
    }}

    80% {{
        opacity: 0.25;
    }}

    100% {{
        transform:
            translateX(150%)
            rotate(18deg);

        opacity: 0;
    }}
}}


/* ---------- وهج ناعم خلف الأسماء ---------- */

.name-glow {{
    position: absolute;

    top: 39%;
    left: 18%;
    right: 18%;

    height: 25%;

    background:
        radial-gradient(
            ellipse at center,
            rgba(225, 177, 69, 0.18),
            rgba(225, 177, 69, 0.07) 40%,
            transparent 72%
        );

    filter: blur(18px);

    pointer-events: none;
    z-index: 4;

    animation:
        nameGlowPulse
        6s ease-in-out
        infinite;
}}

@keyframes nameGlowPulse {{

    0%, 100% {{
        opacity: 0.35;
        transform: scale(0.92);
    }}

    50% {{
        opacity: 0.85;
        transform: scale(1.08);
    }}
}}


/* ---------- حاوية المحتوى ---------- */

.content {{
    position: absolute;

    inset: 0;

    z-index: 10;

    width: 100%;
    height: 100%;

    text-align: center;

    pointer-events: none;
}}


/* ==================================================
   دعوة زفاف
   ================================================== */

.arabic-title {{
    position: absolute;

    top: 15.5%;

    left: 5%;
    right: 5%;

    font-family:
        'Aref Ruqaa Ink',
        'Amiri',
        serif;

    font-size:
        clamp(
            39px,
            10.5vw,
            58px
        );

    font-weight: bold;

    line-height: 1.15;

    background:
        linear-gradient(
            to bottom,
            #a96f16,
            #e3b94f,
            #9b6212,
            #dcae3d,
            #925b0f
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;

    filter:
        drop-shadow(
            0 2px 4px
            rgba(92, 53, 11, 0.4)
        );

    z-index: 12;

    animation:
        titleAppear
        1.5s ease
        both;
}}


/* ==================================================
   النص الترحيبي
   ================================================== */

.message {{
    position: absolute;

    top: 29.5%;

    left: 6%;
    right: 6%;

    font-family:
        'Amiri',
        serif;

    font-size:
        clamp(
            15px,
            4.4vw,
            21px
        );

    font-weight: 700;

    line-height: 1.75;

    background:
        linear-gradient(
            to bottom,
            #80520f,
            #b8791e,
            #8b5a12
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;

    filter:
        drop-shadow(
            0 1px 1px
            rgba(255, 240, 200, 0.6)
        );

    z-index: 12;

    animation:
        fadeUp
        1.4s ease
        0.35s
        both;
}}


/* ==================================================
   الخط فوق الأسماء
   ================================================== */

.name-decoration {{
    position: absolute;

    left: 15%;
    right: 15%;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent 0%,
            rgba(130, 82, 20, 0.18) 12%,
            rgba(157, 103, 29, 0.90) 42%,
            rgba(207, 158, 65, 0.95) 50%,
            rgba(157, 103, 29, 0.90) 58%,
            rgba(130, 82, 20, 0.18) 88%,
            transparent 100%
        );

    z-index: 12;
}}


/* الخط العلوي */
.name-decoration.top {{
    top: 40.5%;
}}


/* الخط السفلي */
.name-decoration.bottom {{
    top: 62.5%;
}}


/* الماسة في وسط الخط */

.name-decoration::before {{
    content: "";

    position: absolute;

    top: 50%;
    left: 50%;

    width: 8px;
    height: 8px;

    background: #a56c1b;

    transform:
        translate(-50%, -50%)
        rotate(45deg);

    box-shadow:
        0 0 6px
        rgba(218, 170, 65, 0.55);
}}


/* ==================================================
   أسماء العروسين
   ================================================== */

.names {{
    position: absolute;

    left: 0;
    right: 0;

    font-family:
        'Aref Ruqaa Ink',
        'Amiri',
        serif;

    font-size:
        clamp(
            28px,
            8.2vw,
            43px
        );

    font-weight: bold;

    line-height: 1.15;

    background:
        linear-gradient(
            to bottom,
            #9a6010,
            #e0b44c,
            #9b6212
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;

    filter:
        drop-shadow(
            0 2px 5px
            rgba(91, 53, 9, 0.45)
        );

    z-index: 12;

    animation:
        nameAppear
        1.4s ease
        0.9s
        both;
}}


/* اسم العريس */

.groom {{
    top: 42.5%;
}}


/* اسم العروس */

.bride {{
    top: 54.0%;
}}


/* ==================================================
   علامة &
   ================================================== */

.ampersand {{
    position: absolute;

    top: 48.3%;

    left: 0;
    right: 0;

    font-family:
        'Cormorant Garamond',
        serif;

    font-size:
        clamp(
            29px,
            8vw,
            39px
        );

    line-height: 1;

    background:
        linear-gradient(
            to bottom,
            #8f5910,
            #d5a53c,
            #8f5910
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;

    filter:
        drop-shadow(
            0 2px 4px
            rgba(94, 55, 10, 0.35)
        );

    z-index: 12;
}}


/* زخرفة صغيرة على جانبي & */

.ampersand::before,
.ampersand::after {{
    content: "";

    position: absolute;

    top: 50%;

    width: 48px;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(157, 103, 29, 0.78)
        );
}}


.ampersand::before {{
    right:
        calc(50% + 31px);
}}


.ampersand::after {{
    left:
        calc(50% + 31px);

    transform: scaleX(-1);
}}


/* ==================================================
   اليوم / الساعة / مكان الحفل
   ================================================== */

.details-container {{
    position: absolute;

    top: 66.5%;

    left: 13%;
    right: 13%;

    z-index: 12;

    display: flex;

    justify-content:
        space-around;

    align-items: center;

    font-family:
        'Amiri',
        serif;

    font-size:
        clamp(
            12px,
            3.5vw,
            16px
        );

    animation:
        fadeUp
        1.4s ease
        1.15s
        both;

    text-align: center;
}}


/* كل قسم */

.detail-item {{
    flex: 0 1 auto;
    width: 31%;

    min-width: 0;

    padding:
        0 5px;

    border-right:
        1px solid
        rgba(154, 99, 25, 0.48);
}}


.detail-item:last-child {{
    border-right: none;
}}


/* عنوان: اليوم / الساعة / مكان الحفل */

.detail-label {{
    display: block;

    font-size: 0.85em;

    font-weight: 400;

    margin-bottom: 5px;

    white-space: nowrap;

    background:
        linear-gradient(
            to bottom,
            #80520f,
            #bd8122
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;
}}


/* القيمة */

.detail-value {{
    display: block;

    font-size: 1em;

    font-weight: 700;

    line-height: 1.55;

    background:
        linear-gradient(
            to bottom,
            #80520f,
            #c28a27,
            #80520f
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;

    filter:
        drop-shadow(
            0 1px 2px
            rgba(255, 224, 151, 0.6)
        );
}}


/* ==================================================
   الحركات
   ================================================== */

@keyframes fadeUp {{

    from {{
        opacity: 0;

        transform:
            translateY(13px);
    }}

    to {{
        opacity: 1;

        transform:
            translateY(0);
    }}

}}


@keyframes titleAppear {{

    from {{
        opacity: 0;

        transform:
            translateY(-14px)
            scale(0.93);
    }}

    to {{
        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }}

}}

@keyframes invitationReveal {{

    0% {{
        opacity: 0;
        transform: scale(0.92);
    }}

    100% {{
        opacity: 1;
        transform: scale(1);
    }}
}}

@keyframes nameAppear {{

    from {{
        opacity: 0;

        transform:
            scale(0.88);
    }}

    to {{
        opacity: 1;

        transform:
            scale(1);
    }}

}}


/* ==================================================
   الهاتف
   ================================================== */

@media (max-width: 600px) {{

    .block-container {{
        padding-left: 0.25rem !important;
        padding-right: 0.25rem !important;
    }}


    .invitation {{
        width: 100%;
        max-width: 480px;
    }}


    .arabic-title {{
        top: 15.5%;

        font-size: 45px;
    }}


    .message {{
        top: 29.5%;

        font-size: 18px;
    }}


    .name-decoration.top {{
        top: 40.5%;
    }}


    .groom {{
        top: 42.5%;
    }}


    .ampersand {{
        top: 48.3%;
    }}


    .bride {{
        top: 54.0%;
    }}


    .name-decoration.bottom {{
        top: 62.5%;
    }}


    .details-container {{
        top: 66.5%;

        left: 8%;
        right: 8%;

        font-size: 12px;
    }}


    .detail-item {{
        padding:
            0 4px;
    }}


    .detail-label {{
        margin-bottom: 4px;
    }}

}}


/* ==================================================
   افتتاحية الظرف الفاخر
   ================================================== */

.envelope-intro {{
    position: fixed;
    inset: 0;

    width: 100vw;
    height: 100vh;

    z-index: 9999;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        radial-gradient(
            circle at center,
            #fffaf0 0%,
            #f5ead7 48%,
            #e7d5b5 100%
        );

    overflow: hidden;

    pointer-events: none;

    animation:
        introFadeOut
        0.8s ease
        4.2s
        forwards;
}}


/* ---------- الظرف ---------- */

.envelope {{
    position: relative;

    width: min(390px, 82vw);
    aspect-ratio: 1.48 / 1;

    perspective: 1200px;

    filter:
        drop-shadow(
            0 22px 35px
            rgba(91, 58, 20, 0.28)
        );

    animation:
        envelopeEntrance
        1.1s ease
        both;
}}


/* ---------- جسم الظرف ---------- */

.envelope-body {{
    position: absolute;

    inset: 0;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #fff9eb 0%,
            #f7ead2 42%,
            #ead4a9 100%
        );

    border:
        2px solid
        #c89b4d;

    border-radius: 9px;

    box-shadow:
        inset 0 0 0 5px
        rgba(255,255,255,0.35),

        inset 0 0 35px
        rgba(167,117,38,0.16);
}}


/* إطار داخلي ذهبي */

.envelope-body::before {{
    content: "";

    position: absolute;

    inset: 12px;

    border:
        1px solid
        rgba(175,126,46,0.55);

    border-radius: 5px;
}}


/* لمعان داخلي */

.envelope-body::after {{
    content: "";

    position: absolute;

    inset: 0;

    background:
        radial-gradient(
            ellipse at 30% 25%,
            rgba(255,255,255,0.50),
            transparent 38%
        );

    pointer-events: none;
}}


/* ---------- الجهة اليسرى من الظرف ---------- */

.envelope-left {{
    position: absolute;

    left: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-top:
        125px solid transparent;

    border-left:
        194px solid #e7d1a4;

    z-index: 3;
}}


/* ---------- الجهة اليمنى ---------- */

.envelope-right {{
    position: absolute;

    right: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-top:
        125px solid transparent;

    border-right:
        194px solid #e7d1a4;

    z-index: 3;
}}


/* ---------- الغطاء العلوي ---------- */

.envelope-flap {{
    position: absolute;

    top: 0;
    left: 0;

    width: 0;
    height: 0;

    border-left:
        195px solid transparent;

    border-right:
        195px solid transparent;

    border-top:
        132px solid #d4ae69;

    transform-origin: top center;

    z-index: 8;

    filter:
        drop-shadow(
            0 4px 5px
            rgba(87,54,13,0.22)
        );

    animation:
        flapOpen
        1.35s
        cubic-bezier(.45,0,.15,1)
        1.75s
        forwards;
}}


/* ---------- خط ذهبي على الغطاء ---------- */

.envelope-flap::after {{
    content: "";

    position: absolute;

    top: -124px;
    left: -145px;

    width: 290px;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,236,172,0.75),
            transparent
        );

    transform: rotate(0deg);
}}


/* ==================================================
   ختم أحمر فاخر
   ================================================== */

.envelope-seal {{
    position: absolute;

    left: 50%;
    top: 50%;

    width: 70px;
    height: 70px;

    transform:
        translate(-50%, -50%);

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #c94a43,
            #9e2728 55%,
            #711719 100%
        );

    border:
        3px solid
        #d9b35c;

    box-shadow:
        0 0 0 3px
        rgba(255,230,157,0.75),

        0 5px 15px
        rgba(90,24,20,0.40),

        0 0 25px
        rgba(159,38,35,0.35);

    z-index: 15;

    animation:
        sealOpen
        0.75s
        cubic-bezier(.4,0,.2,1)
        1.55s
        forwards;
}}


/* الرمز داخل الختم */

.envelope-seal::before {{
    content: "◆";

    position: absolute;

    inset: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    color: #f6df9b;

    font-size: 23px;

    text-shadow:
        0 1px 2px
        rgba(67,20,15,0.45);
}}


/* لمعان الختم */

.envelope-seal::after {{
    content: "";

    position: absolute;

    top: 10px;
    left: 14px;

    width: 18px;
    height: 9px;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.25);

    transform: rotate(-25deg);

    filter: blur(1px);
}}


/* ==================================================
   حركات الظرف
   ================================================== */

@keyframes envelopeEntrance {{

    0% {{
        opacity: 0;

        transform:
            translateY(35px)
            scale(0.88);
    }}

    100% {{
        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }}

}}


/* فتح الغطاء */

@keyframes flapOpen {{

    0% {{
        transform:
            rotateX(0deg);
    }}

    100% {{
        transform:
            rotateX(-180deg);
    }}

}}


/* اختفاء الختم */

@keyframes sealOpen {{

    0% {{
        opacity: 1;

        transform:
            translate(-50%, -50%)
            scale(1)
            rotate(0deg);
    }}

    70% {{
        opacity: 1;

        transform:
            translate(-50%, -50%)
            scale(1.08)
            rotate(4deg);
    }}

    100% {{
        opacity: 0;

        transform:
            translate(-50%, -50%)
            scale(0.25)
            rotate(12deg);
    }}

}}


    /* تبدأ بالخروج من فتحة الظرف */

    25% {{
        opacity: 1;

        transform:
            translate(-50%, -12%)
            scale(0.70);
    }}


    /* نصف البطاقة تقريباً أصبح خارج الظرف */

    42% {{
        opacity: 1;

        transform:
            translate(-50%, -42%)
            scale(0.74);
    }}


    /* البطاقة تخرج بالكامل من الظرف */

    58% {{
        opacity: 1;

        transform:
            translate(-50%, -72%)
            scale(0.80);
    }}


    /* تبدأ بالتقدم للأمام والتكبير */

    72% {{
        opacity: 1;

        transform:
            translate(-50%, -92%)
            scale(1.00);

        z-index: 12;
    }}


    /* تكبر أكثر وتتحرك نحو مركز الشاشة */

    86% {{
        opacity: 1;

        transform:
            translate(-50%, -104%)
            scale(1.45);

        z-index: 20;
    }}


    /* الحجم النهائي تقريباً */

    100% {{
        opacity: 1;

        transform:
            translate(-50%, -108%)
            scale(2.05);

        z-index: 30;
    }}

}}


/* لمعان الظرف */

@keyframes envelopeShine {{

    0% {{
        left: -80%;
        opacity: 0;
    }}

    25% {{
        opacity: 1;
    }}

    100% {{
        left: 145%;
        opacity: 0;
    }}

}}


/* اختفاء طبقة الافتتاحية */

@keyframes introFadeOut {{

    0% {{
        opacity: 1;
        visibility: visible;
    }}

    78% {{
        opacity: 1;
    }}

    100% {{
        opacity: 0;
        visibility: hidden;
    }}

}}

</style>
""",
    unsafe_allow_html=True
)

# ---------- HTML ----------
st.markdown("""<div class="envelope-intro"><div class="envelope"><div class="envelope-body"></div><div class="envelope-left"></div><div class="envelope-right"></div><div class="envelope-flap"></div><div class="envelope-seal"></div><div class="envelope-shine"></div></div></div>""", unsafe_allow_html=True)
st.markdown("""<div class="invitation"><div class="glow glow-left"></div><div class="glow glow-right"></div><div class="glow glow-bottom"></div><div class="floating-light fl1"></div><div class="floating-light fl2"></div><div class="floating-light fl3"></div><div class="floating-light fl4"></div><div class="floating-light fl5"></div><div class="floating-light fl6"></div><div class="floating-light fl7"></div><div class="floating-light fl8"></div><div class="light light1"></div><div class="light light2"></div><div class="light light3"></div><div class="light light4"></div><div class="light light5"></div><div class="light light6"></div><div class="light light7"></div><div class="light light8"></div><div class="light light9"></div><div class="light light10"></div><div class="light light11"></div><div class="light light12"></div><div class="bokeh bokeh1"></div><div class="bokeh bokeh2"></div><div class="bokeh bokeh3"></div><div class="bokeh bokeh4"></div><div class="floating-particles"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div><div class="light-ray"></div><div class="name-glow"></div><div class="content"><div class="arabic-title">دعوة زفاف</div><div class="message">بكل حب وسرور<br>نتشرف بدعوتكم لمشاركتنا فرحتنا</div><div class="name-decoration top"></div><div class="names groom"> ملاك الحسن</div><div class="ampersand">&</div><div class="names bride">محمد  </div><div class="name-decoration bottom"></div><div class="details-container"><div class="detail-item"><span class="detail-label">اليوم</span><span class="detail-value">2028/01/07</span></div><div class="detail-item"><span class="detail-label">الساعة</span><span class="detail-value">17:00 pm</span></div><div class="detail-item"><span class="detail-label">مكان الحفل</span><span class="detail-value"> بن موسى</span></div></div></div></div>""", unsafe_allow_html=True)