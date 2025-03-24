# -*- coding: utf-8 -*-
"""Detoxland: The self battle

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bLyXZeLcsd-APCkHZEpTzGBfTkSE7IWV
"""

# pip install streamlit
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

    html, body, [class*="st-"] {
        font-family: 'Kanit', sans-serif;
        text-align: center; /* จัดข้อความตรงกลาง */
    }

    h1, h2, h3 {
        font-family: 'Kanit', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CSS สำหรับตกแต่ง ---
st.markdown('''
    <style>
    body {
        background-color: #f4f4f4;
    }
    .big-title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .sub-title {
        font-size: 20px;
        color: #555;
        text-align: center;
    }
    .button-style {
        background-color: #4CAF50;
        color: white;
        padding: 15px 25px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
    </style>
''', unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="big-title">Detoxland: The Self Battle</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">ช่วยให้คุณโฟกัสและลดการใช้โซเชียลมีเดียอย่างมีสุขภาพจิตที่ดี</p>', unsafe_allow_html=True)

# --- Layout ของหน้า UI ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # เริ่มนับ Pomodoro ครั้งแรก
    if "pomodoro_count" not in st.session_state:
        st.session_state["pomodoro_count"] = 0

    # ปุ่มเริ่ม Pomodoro Timer
    if st.button("⏳ Start Pomodoro (25 min)", key="pomodoro"):
        st.session_state["end_time"] = time.time() + (25 * 60)
        st.session_state["pomodoro_count"] += 1
        st.success("✅ Pomodoro เริ่มแล้ว! ตั้งใจทำงานนะ ")

    # แสดงเวลาที่เหลือ
    if "end_time" in st.session_state:
        remaining_time = st.session_state["end_time"] - time.time()
        if remaining_time > 0:
            timer_placeholder = st.empty()  # สร้าง placeholder
            while remaining_time > 0:
                minutes = int(remaining_time // 60)
                seconds = int(remaining_time % 60)
                timer_placeholder.text(f"⏳ เวลาที่เหลือ: {minutes:02d}:{seconds:02d}")  # อัปเดต placeholder
                time.sleep(1)  # หน่วงเวลา 1 วินาที
                remaining_time = st.session_state["end_time"] - time.time()
            st.success(" Pomodoro เสร็จแล้ว! พักสักหน่อยนะ ️")
            quotes = [
                "ความสำเร็จมาจากก้าวเล็ก ๆ ในแต่ละวัน",
                "วันนี้อาจเป็นวันที่ดีที่สุดของคุณ",
                "อย่ากลัวที่จะเริ่มต้นใหม่",
                "ความสุขอยู่ในสิ่งเล็ก ๆ น้อย ๆ"
            ]
            st.write(random.choice(quotes))
        else:
            st.success(" Pomodoro เสร็จแล้ว! พักสักหน่อยนะ ️")
            quotes = [
                "ความสำเร็จมาจากก้าวเล็ก ๆ ในแต่ละวัน",
                "วันนี้อาจเป็นวันที่ดีที่สุดของคุณ",
                "อย่ากลัวที่จะเริ่มต้นใหม่",
                "ความสุขอยู่ในสิ่งเล็ก ๆ น้อย ๆ"
            ]
            st.write(random.choice(quotes))

    # ปุ่ม Reset Pomodoro
    if "end_time" in st.session_state and st.session_state["end_time"] == 0:  # เพิ่มเงื่อนไข
        if st.button("Reset Pomodoro"):
            st.session_state["end_time"] = 0  # รีเซ็ตเวลา
            st.info("Pomodoro ถูกรีเซ็ตแล้ว")

    # ระบบบันทึกอารมณ์ (Mental Health Tracker)
    st.subheader(" บันทึกอารมณ์ของคุณวันนี้")
    mood = st.selectbox("วันนี้คุณรู้สึกอย่างไร?", [" Happy", " Neutral", " Sad", " Anxious"])

    # คลังข้อความปลอบโยนสำหรับแต่ละอารมณ์
    mood_quotes = {
        " Happy": [
            " รอยยิ้มของคุณทำให้โลกสดใสขึ้นนะ!",
            " มีความสุขแบบนี้ต่อไปนะ วันนี้เป็นวันที่ดี!",
            " ขอให้ความสุขอยู่กับคุณเสมอ!"
        ],
        " Neutral": [
            " วันธรรมดาก็มีความหมายเสมอ",
            " บางครั้งแค่หายใจลึก ๆ ก็เพียงพอแล้ว",
            " ใช้เวลานี้เป็นโอกาสให้ตัวเองได้พักใจ"
        ],
        " Sad": [
            " ไม่เป็นไรนะ คุณไม่ได้อยู่คนเดียว",
            " อารมณ์เศร้าเป็นแค่ส่วนหนึ่งของชีวิต เดี๋ยวมันจะผ่านไป",
            "️ ฝนตกแล้ว เดี๋ยวก็มีสายรุ้งตามมา"
        ],
        " Anxious": [
            " ลองหายใจเข้าลึก ๆ แล้วค่อย ๆ ผ่อนคลายนะ",
            "☁️ ทุกความกังวลล้วนมีจุดสิ้นสุด เชื่อเถอะว่าคุณจะผ่านมันไปได้",
            " ลองนึกถึงทะเลที่เงียบสงบแล้วให้ความเครียดไหลออกไป"
        ]
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

    if st.button("ยังไม่ดีขึ้น"):
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
    responses = []
    for q in questions:
        responses.append(st.radio(q, ["ใช่", "ไม่ใช่"], index=1))

    if st.button(" วิเคราะห์ผล"):
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

