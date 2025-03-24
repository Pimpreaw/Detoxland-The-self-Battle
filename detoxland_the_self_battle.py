# -*- coding: utf-8 -*-
"""Detoxland: The self battle"""

import streamlit as st
import time
import random

# --- ตั้งค่า UI ---
st.set_page_config(page_title="Detoxland: The Self Battle", page_icon="", layout="wide")

# --- แทรกฟอนต์ Kanit และจัดข้อความตรงกลาง ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;700&display=swap');
    html, body, [class*="st-"], p, span, div, h1, h2, h3, h4, h5, h6 { /* เพิ่ม selector อื่นๆ */
        font-family: 'Kanit', sans-serif !important; /* เพิ่ม !important เพื่อให้มีผล */
        text-align: center !important; /* เพิ่ม !important เพื่อให้มีผล */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CSS สำหรับตกแต่ง ---
st.markdown('''
    <style>
    body {
        background-color: #a9b665; /* สีเบจเขียวเข้มแบบธรรมชาติ */
        /* background-image: url('YOUR_PASTEL_BACKGROUND_IMAGE_URL.png'); /* ลบหรือแทนที่ URL ภาพพื้นหลัง PNG */
        background-size: cover;
        background-position: center;
    }
    .big-title {
        font-size: 250px;
        font-weight: bold;
        color: #8fbc8f; /* สีเขียวอ่อน */
    }
    .sub-title {
        font-size: 20px;
        color: #556b2f; /* สีเขียวเข้ม */
    }
    .button-style {
        background-color: #8fbc8f; /* สีเขียวอ่อน */
        color: white;
        padding: 15px 25px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        display: block; /* จัดปุ่มให้อยู่ตรงกลางด้วย */
        margin-left: auto;
        margin-right: auto;
    }
    .st-emotion-cache- {} /* แก้ปัญหาการจัดกึ่งกลางของบาง elements ใน Streamlit */
    </style>
''', unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="big-title">Detoxland: The Self Battle</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">ช่วยให้คุณโฟกัสและลดการใช้โซเชียลมีเดียอย่างมีสุขภาพจิตที่ดี</p>', unsafe_allow_html=True)
st.markdown('<img src="YOUR_GIF_IMAGE_URL.gif" width="200" style="display: block; margin-left: auto; margin-right: auto;">', unsafe_allow_html=True) # เพิ่ม GIF

# --- Layout ของหน้า UI ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # --- Pomodoro Timer ---
    with st.container():
        st.subheader("Pomodoro Timer")

        if "end_time" not in st.session_state:
            st.session_state["end_time"] = 0
        if "pomodoro_running" not in st.session_state:
            st.session_state["pomodoro_running"] = False

        def start_pomodoro():
            st.session_state["end_time"] = time.time() + (25 * 60)
            st.session_state["pomodoro_running"] = True

        def reset_pomodoro():
            st.session_state["end_time"] = 0
            st.session_state["pomodoro_running"] = False

        if st.button("Start Pomodoro (25 min)", key="start_pomodoro", type="primary", use_container_width=True, className="button-style", on_click=start_pomodoro):
            pass # การกระทำจะอยู่ในฟังก์ชัน start_pomodoro

        if st.button("Reset Pomodoro", key="reset_pomodoro", use_container_width=True, className="button-style", on_click=reset_pomodoro):
            pass # การกระทำจะอยู่ในฟังก์ชัน reset_pomodoro

        timer_placeholder = st.empty()  # สร้าง placeholder สำหรับแสดงเวลา

        if st.session_state["pomodoro_running"]:
            if st.session_state["end_time"] > time.time():
                remaining_time = st.session_state["end_time"] - time.time()
                minutes = int(remaining_time // 60)
                seconds = int(remaining_time % 60)
                timer_placeholder.markdown(f"⏳ เวลาที่เหลือ: **{minutes:02d}:{seconds:02d}**")
                time.sleep(1) # หน่วงเวลา 1 วินาที
                st.rerun() # สั่งให้ Streamlit รันใหม่เพื่ออัปเดตเวลา
            else:
                st.success(" Pomodoro เสร็จแล้ว! พักสักหน่อยนะ ️")
                st.session_state["pomodoro_running"] = False
                st.session_state["end_time"] = 0
                timer_placeholder.empty() # ลบ placeholder เมื่อ Pomodoro เสร็จสิ้น
        elif st.session_state["end_time"] > time.time() and not st.session_state["pomodoro_running"]:
            # กรณีที่ end_time ถูกตั้งไว้แล้ว แต่ pomodoro_running เป็น False (เช่น หลังรีเซ็ต)
            remaining_time = st.session_state["end_time"] - time.time()
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            timer_placeholder.markdown(f"⏳ เวลาที่เหลือ: **{minutes:02d}:{seconds:02d}**")
			
    # ระบบบันทึกอารมณ์ (Mental Health Tracker)
    st.subheader(" บันทึกอารมณ์ของคุณวันนี้")
    mood = st.selectbox("วันนี้คุณรู้สึกอย่างไร?", [" Happy", " Neutral", " Sad", " Anxious"])

    # คลังข้อความปลอบโยนสำหรับแต่ละอารมณ์
    mood_quotes = {
        " Happy": [" รอยยิ้มของคุณทำให้โลกสดใสขึ้นนะ!", " มีความสุขแบบนี้ต่อไปนะ วันนี้เป็นวันที่ดี!", " ขอให้ความสุขอยู่กับคุณเสมอ!"],
        " Neutral": [" วันธรรมดาก็มีความหมายเสมอ", " บางครั้งแค่หายใจลึก ๆ ก็เพียงพอแล้ว", " ใช้เวลานี้เป็นโอกาสให้ตัวเองได้พักใจ"],
        " Sad": [" ไม่เป็นไรนะ คุณไม่ได้อยู่คนเดียว", " อารมณ์เศร้าเป็นแค่ส่วนหนึ่งของชีวิต เดี๋ยวมันจะผ่านไป", "️ ฝนตกแล้ว เดี๋ยวก็มีสายรุ้งตามมา"],
        " Anxious": [" ลองหายใจเข้าลึก ๆ แล้วค่อย ๆ ผ่อนคลายนะ", "☁️ ทุกความกังวลล้วนมีจุดสิ้นสุด เชื่อเถอะว่าคุณจะผ่านมันไปได้", " ลองนึกถึงทะเลที่เงียบสงบแล้วให้ความเครียดไหลออกไป"]
    }

    # สีปุ่มและข้อความตามอารมณ์
    mood_styles = {
        " Happy": {"color": "#FFD700", "text": "✨ วันนี้สดใส! มาลุยกันเถอะ!"},
        " Neutral": {"color": "#A9A9A9", "text": "⏳ ค่อย ๆ ไป ไม่ต้องรีบ"},
        " Sad": {"color": "#4682B4", "text": " พักสักหน่อยแล้วค่อยเริ่มใหม่"},
        " Anxious": {"color": "#FF6347", "text": " ลองสูดหายใจลึก ๆ ก่อนเริ่มงาน"}
    }

    # ปรับแต่งปุ่มบันทึกอารมณ์ด้วย HTML/CSS
    if st.markdown(f"""
        <style>
        .stButton>button {{
            background-color: {mood_styles.get(mood, {}).get('color', 'lightgray')};
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }}
        </style>
        <button>{mood_styles.get(mood, {}).get('text', 'บันทึกอารมณ์')}</button>
    """, unsafe_allow_html=True):
        comforting_message = random.choice(mood_quotes.get(mood, [""]))
        st.write(f"✅ บันทึกอารมณ์สำเร็จ! \n\n {comforting_message}")

    # ฟีเจอร์จัดการอาการแพนิค
    st.subheader(" จัดการอาการแพนิค")
    panic_option = st.selectbox("เลือกอาการแพนิค:",
                                 ["ฉันรู้สึกเครียด", "ฉันหายใจไม่ออก / หัวใจเต้นแรง",
                                  "ฉันรู้สึกเหมือนกำลังจะเป็นลม", "ฉันรู้สึกเหมือนหลุดออกจากโลกความจริง"])

    if panic_option == "ฉันหายใจไม่ออก / หัวใจเต้นแรง":
        st.write("ลองใช้เทคนิค 4-7-8: หายใจเข้า 4 วินาที กลั้นหายใจ 7 วินาที และหายใจออก 8 วินาที")
    elif panic_option == "ฉันรู้สึกเหมือนกำลังจะเป็นลม":
        st.write("หาที่นั่ง, ดื่มน้ำ, วางมือบนพื้นเพื่อสร้างความมั่นคง")
    elif panic_option == "ฉันรู้สึกเหมือนหลุดออกจากโลกความจริง":
        st.write("ใช้ 5-4-3-2-1 technique: บอก 5 สิ่งที่เห็น, 4 สิ่งที่สัมผัส, 3 สิ่งที่ได้ยิน, 2 กลิ่นที่ได้กลิ่น, และ 1 สิ่งที่ได้ลิ้มรส")

    if st.button("ยังไม่ดีขึ้น", key="panic_button", use_container_width=True, className="button-style"):
        st.write("หากอาการยังไม่ดีขึ้น โปรดติดต่อสายด่วนสุขภาพจิต 1323 หรือปรึกษาแพทย์และผู้เชี่ยวชาญด้านสุขภาพจิตในโรงพยาบาล")

    # แบบสอบถามวัดระดับอาการติดโซเชียล
    st.subheader(" แบบสอบถาม: คุณติดโซเชียลแค่ไหน?")
    questions = [
        "1. คุณใช้โซเชียลมีเดียเป็นสิ่งแรกหลังตื่นนอนหรือไม่?",
        "2. คุณรู้สึกว่าต้องเช็คโซเชียลตลอดเวลาไหม?",
        "3. คุณใช้โซเชียลจนกระทบเวลานอนหรือไม่?",
        "4. คุณรู้สึกกังวลเมื่อไม่ได้ใช้โซเชียลมีเดียหรือไม่?",
        "5. คุณเคยพยายามลดการใช้โซเชียลแต่ทำไม่ได้หรือไม่?",
        "6. คุณใช้โซเชียลขณะกินข้าวหรือไม่?",
        "7. คุณรู้สึกว่าต้องเช็คโซเชียลแม้ว่าจะไม่มีการแจ้งเตือนหรือไม่?",
        "8. คุณเคยรู้สึกผิดหรือเสียใจหลังจากใช้โซเชียลมากเกินไปหรือไม่?",
        "9. คุณเคยหลีกเลี่ยงการพบปะคนจริง ๆ เพื่ออยู่กับโซเชียลหรือไม่?"
    ]
    responses =
    for i, q in enumerate(questions):
        responses.append(st.radio(q, ["ใช่", "ไม่ใช่"], index=1, key=f"question_{i}"))

    if st.button(" วิเคราะห์ผล", key="analyze_button", use_container_width=True, className="button-style"):
        score = responses.count("ใช่")
        if score <= 1:
            st.success("คุณมีวินัยในการใช้โซเชียลได้ดีมาก! ลองแชร์เคล็ดลับให้เพื่อน ๆ บ้างนะ")
            st.write("การมีวินัยในการใช้โซเชียลมีเดียเป็นสิ่งสำคัญที่ช่วยให้คุณรักษาสมดุลในชีวิตได้ดี คุณสามารถนำเคล็ดลับและประสบการณ์ของคุณไปแบ่งปันให้กับผู้อื่น เพื่อเป็นกำลังใจและแรงบันดาลใจในการใช้โซเชียลมีเดียอย่างมีสติ")

        elif score <= 3:
            st.warning("คุณอาจใช้โซเชียลมากกว่าที่ควร ลองตั้งเวลาพักหรือลอง Digital Detox")
            st.write("การใช้โซเชียลมีเดียมากเกินไปอาจส่งผลกระทบต่อสุขภาพกายและสุขภาพจิตของคุณ ลองกำหนดเวลาพักจากโซเชียลมีเดีย หรือลองทำกิจกรรม Digital Detox เพื่อลดการใช้โซเชียลมีเดียและหันมาใส่ใจกับกิจกรรมอื่น ๆ ในชีวิตประจำวัน")

        elif score == 4:
            st.warning("คุณอาจพึ่งพาโซเชียลมีเดียมากไป ลองจำกัดเวลาการใช้และหาเวลาทำกิจกรรมออฟไลน์บ้าง")
            st.write("การพึ่งพาโซเชียลมีเดียมากเกินไปอาจทำให้คุณละเลยกิจกรรมอื่น ๆ ที่สำคัญในชีวิต ลองกำหนดเวลาการใช้โซเชียลมีเดียในแต่ละวัน และหาเวลาทำกิจกรรมออฟไลน์ที่คุณชื่นชอบ เช่น อ่านหนังสือ ออกกำลังกาย หรือพบปะเพื่อนฝูง")

        else:
            st.error("คุณอาจมีภาวะติดโซเชียล ควรลองปรึกษาผู้เชี่ยวชาญหรือหาแอปช่วยควบคุมการใช้งาน")
            st.write("การติดโซเชียลมีเดียเป็นภาวะที่ส่งผลกระทบต่อชีวิตประจำวันของคุณอย่างมาก การปรึกษาผู้เชี่ยวชาญหรือหาแอปช่วยควบคุมการใช้งานเป็นทางเลือกที่ดีในการจัดการปัญหานี้ คุณสามารถเริ่มต้นจากการพูดคุยกับเพื่อนสนิท คนในครอบครัว หรือผู้เชี่ยวชาญด้านสุขภาพจิต เพื่อขอคำแนะนำและรับการสนับสนุน นอกจากนี้ ยังมีแอปพลิเคชันและเครื่องมือออนไลน์มากมายที่ช่วยให้คุณติดตามและจำกัดเวลาการใช้โซเชียลมีเดียได้ หากคุณรู้สึกว่าการติดโซเชียลมีเดียส่งผลกระทบต่อสุขภาพจิตของคุณอย่างรุนแรง การปรึกษาแพทย์หรือผู้เชี่ยวชาญด้านสุขภาพจิตเป็นสิ่งสำคัญ เพื่อให้ได้รับการวินิจฉัยและการรักษาที่เหมาะสม")

st.write("---")  # เส้นคั่น
st.markdown("<p style='text-align: center;'> Detoxland ช่วยให้คุณลดความเครียดและโฟกัสกับชีวิตมากขึ้น</p>", unsafe_allow_html=True)
