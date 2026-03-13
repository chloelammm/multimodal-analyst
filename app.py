#v1 
import streamlit as st
from deepface import DeepFace
import cv2
from PIL import Image
import numpy as np

# 設置網頁標題
st.set_page_config(page_title="RightPick Multimodal Analyst", page_icon="🤖")

st.title("🤖 RightPick Multimodal Analyst")
st.markdown("透過 AI 分析你的面部氣場 (Career Vibe)")

# 上傳照片組件
uploaded_file = st.file_uploader("請上傳一張個人照片...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 顯示上傳的照片 (已將警告處改為 width='stretch')
    image = Image.open(uploaded_file)
    st.image(image, caption='已上傳照片', width='stretch')
    
    with st.spinner('AI 正在讀取你的 Vibe... 請稍候'):
        try:
            # 將 PIL 影像轉為 OpenCV 格式給 DeepFace 用
            img_array = np.array(image)
            
            # 1. 使用 DeepFace 分析
            results = DeepFace.analyze(img_path=img_array, 
                                     actions=['emotion', 'age', 'gender'])
            res = results[0]
            
            emotion = res['dominant_emotion']
            gender = res['dominant_gender']
            age = res['age']

            # 2. 顯示基礎數據分析
            st.divider()
            st.header("📊 AI Vibe Analysis Report")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("估計性別", gender)
            col2.metric("估計年齡", age)
            col3.metric("主導情緒", emotion.capitalize())

            # 3. 升級版：RightPick 18 型人格映射邏輯
            personality_type = ""
            vibe_description = ""
            career_path = ""

            # 根據情緒與年齡進行人格預判
            if emotion == 'happy':
                personality_type = "The Charismatic Connector (魅力連結者)"
                vibe_description = "擁有極強的親和力與正面能量，容易獲得客戶信任。"
                career_path = "Public Relations, Sales Manager, High-end Hospitality"
            elif emotion == 'neutral' and age >= 30:
                personality_type = "The Strategic Architect (戰略架構師)"
                vibe_description = "表情沉穩，展現出高度的邏輯思考與情緒控制能力。"
                career_path = "Operations Director, Senior Consultant, Risk Management"
            elif emotion == 'neutral' and age < 30:
                personality_type = "The Precision Specialist (精密專家)"
                vibe_description = "專注且理性，給人一種穩定、靠譜的技術專家印象。"
                career_path = "Backend Developer, Quality Assurance, Data Scientist"
            elif emotion == 'surprise':
                personality_type = "The Creative Disruptor (創意變革者)"
                vibe_description = "反應靈敏，富有想像力，具備打破常規的氣質。"
                career_path = "Advertising Creative, UI/UX Designer, Startup Founder"
            else:
                personality_type = "The Decisive Overseer (果斷監督者)"
                vibe_description = "威嚴且專注細節，適合需要高度紀律與合規性的環境。"
                career_path = "Legal Counsel, Auditor, Financial Controller"

            # 顯示 18 Personality Match 結果
            st.subheader(f"🎯 18 Personality Match: {personality_type}")
            st.info(f"**氣場解析：** {vibe_description}")
            st.success(f"**建議職業路徑：** {career_path}")
            
            # 增加互動感
            #st.balloons()

        except Exception as e:
            st.error(f"分析出錯：{e}")
            st.warning("請確保照片中有人臉且光線充足。")

else:
    st.info("請在上方上傳照片以開始 AI 分析。")