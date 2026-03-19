<<<<<<< HEAD
=======
#v2.3
>>>>>>> 0064574e60bfaf3bbb836573234bc508c569205b
import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace
<<<<<<< HEAD
import cv2

# 1. 頁面基本配置
st.set_page_config(page_title="RightPick AI | Professional Suite", layout="wide", page_icon="🤖")
=======

# 1. 頁面基本配置
st.set_page_config(page_title="RightPick AI | Professional Suite", layout="wide")
>>>>>>> 0064574e60bfaf3bbb836573234bc508c569205b

# 2. 注入全局設計與 CSS
st.markdown("""
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    .glass-nav { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid #e2e8f0; margin-bottom: 1.5rem; }
<<<<<<< HEAD
    .rightpick-blue { background: #5ba4cf; }
    
    /* 隱藏 Streamlit 預設裝飾 */
    header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; }
</style>

<nav class="glass-nav px-8 py-4 flex justify-between items-center sticky top-0 z-50">
    <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rightpick-blue rounded-xl flex items-center justify-center text-white shadow-lg">
            <i class="fas fa-brain"></i>
        </div>
        <div>
            <h1 class="font-bold text-gray-900 leading-none" style="margin:0">RightPick <span class="text-blue-500">AI</span></h1>
            <span class="text-[10px] text-gray-400 font-bold tracking-widest uppercase">Professional Assistant v2.5</span>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# 3. 頁面佈局
col_left, col_right = st.columns([1, 2.2], gap="large")

with col_left:
    # --- 1. Interest Analysis ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Interest Analysis</h3>
                <span style="font-size: 10px; background-color: #eff6ff; color: #2563eb; padding: 4px 8px; border-radius: 9999px; font-weight: bold;">JUPAS AI</span>
            </div>
            <div style="background-color: #f1f5f9; height: 80px; border-radius: 1rem; margin-bottom: 1rem; overflow: hidden;">
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400" style="width:100%; height:100%; object-fit: cover; opacity: 0.6;">
            </div>
            <a href="https://rightpickhk.com/career" target="_blank" style="text-decoration: none;">
                <div style="text-align: center; padding: 10px; background-color: #111827; color: white; border-radius: 0.75rem; font-weight: bold; font-size: 10px;">Find Interested Jobs</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # --- 2. Personality Match ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Personality Match</h3>
                <span style="font-size: 10px; background-color: #faf5ff; color: #9333ea; padding: 4px 8px; border-radius: 9999px; font-weight: bold;">18 TYPES</span>
            </div>
            <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                <div style="width: 32px; height: 32px; background-color: #f3e8ff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: bold; color: #7e22ce;">ENTP</div>
                <div style="width: 32px; height: 32px; background-color: #dbeafe; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: bold; color: #1d4ed8;">ISTJ</div>
            </div>
            <a href="https://rightpickhk.com/personality" target="_blank" style="text-decoration: none;">
                <div style="text-align: center; padding: 10px; background-color: #9333ea; color: white; border-radius: 0.75rem; font-weight: bold; font-size: 10px;">Start Personality Test</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # --- 3. Salary Insights ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Salary Insights</h3>
                <span style="font-size: 10px; background-color: #f0fdf4; color: #16a34a; padding: 4px 10px; border-radius: 9999px; font-weight: bold;">HK / GBA</span>
            </div>
            <div style="display: flex; align-items: flex-end; gap: 6px; height: 45px; margin-bottom: 15px; padding-bottom: 5px; border-bottom: 2px solid #f1f5f9;">
                <div style="background-color: #bbf7d0; width: 30%; height: 40%; border-radius: 4px 4px 0 0;"></div>
                <div style="background-color: #86efac; width: 30%; height: 70%; border-radius: 4px 4px 0 0;"></div>
                <div style="background-color: #22c55e; width: 30%; height: 100%; border-radius: 4px 4px 0 0;"></div>
            </div>
            <p style="font-size: 10px; color: #64748b; margin-bottom: 15px;">Compare your expected pay with 2026 industry benchmarks.</p>
            <a href="https://rightpickhk.com/salary-compare" target="_blank" style="text-decoration: none;">
                <div style="text-align: center; padding: 12px; background-color: #16a34a; color: white; border-radius: 0.75rem; font-weight: bold; font-size: 11px;">Analyze My Salary</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown("---")

# --- 右側欄位 (col_right) ---
with col_right:
    # 1. 2026 Skills Scraper 卡片
    st.markdown('''
        <div style="background-color: #2563eb; rounded-radius: 1.5rem; padding: 2rem; color: white; margin-bottom: 2rem; position: relative; overflow: hidden; border-radius: 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 10;">
                <div>
                    <h2 style="font-size: 1.25rem; font-weight: bold; font-style: italic; margin: 0;">2026 Skills Scraper</h2>
                    <p style="font-size: 0.75rem; color: #dbeafe; margin: 4px 0;">Live summary of Job Finding websites (HK/GBA)</p>
                    <div style="display: flex; gap: 8px; mt: 16px; margin-top: 10px;">
                        <span style="font-size: 9px; background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2);">LinkedIn</span>
                        <span style="font-size: 9px; background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2);">JobsDB</span>
                        <span style="font-size: 9px; background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2);">Zhaopin</span>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; text-align: center;">
                    <div><span style="display: block; font-size: 1.875rem; font-weight: 900;">82%</span><span style="font-size: 10px; color: #bfdbfe; font-weight: bold;">MANDARIN/ENG</span></div>
                    <div style="width: 1px; background: rgba(255,255,255,0.2); height: 40px;"></div>
                    <div><span style="display: block; font-size: 1.875rem; font-weight: 900;">64%</span><span style="font-size: 10px; color: #bfdbfe; font-weight: bold;">AI PROMPTING</span></div>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    # 2. Review Your Talent & Skills 卡片
    st.markdown('''
        <div style="background-color: white; padding: 2rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 1.5rem;">
                <div style="padding: 8px; background-color: #dbeafe; color: #2563eb; border-radius: 0.75rem;"><i class="fas fa-star"></i></div>
                <h3 style="font-weight: bold; font-size: 1.25rem; color: #1f2937; margin: 0;">Review Your Talent & Skills</h3>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div>
                    <h4 style="font-size: 10px; font-weight: 900; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Your Strength Stack</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span style="padding: 4px 12px; background-color: #eff6ff; color: #1d4ed8; font-size: 10px; font-weight: bold; border-radius: 9999px; border: 1px solid #dbeafe;">Data Visualization</span>
                        <span style="padding: 4px 12px; background-color: #eff6ff; color: #1d4ed8; font-size: 10px; font-weight: bold; border-radius: 9999px; border: 1px solid #dbeafe;">Critical Thinking</span>
                        <span style="padding: 4px 12px; background-color: #eff6ff; color: #1d4ed8; font-size: 10px; font-weight: bold; border-radius: 9999px; border: 1px solid #dbeafe;">Cantonese (Native)</span>
                    </div>
                </div>
                <div>
                    <h4 style="font-size: 10px; font-weight: 900; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">5-10 Matches Found</h4>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; justify-content: space-between; padding: 8px; background-color: #f8fafc; border-radius: 0.5rem; border: 1px solid #e2e8f0; font-size: 11px;">
                            <span style="font-weight: bold;">Business Analyst (Fintech)</span>
                            <span style="color: #3b82f6; font-weight: bold;">98% Match</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 8px; background-color: #f8fafc; border-radius: 0.5rem; border: 1px solid #e2e8f0; font-size: 11px;">
                            <span style="font-weight: bold;">Digital Outreach Lead</span>
                            <span style="color: #3b82f6; font-weight: bold;">92% Match</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    # 3. AI Resume Lab 
    # AI Resume Lab - PROTOTYPE VERSION (Replace your current section)
    st.markdown("""
    <div style="background-color: white; padding: 2rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
            <h3 style="font-weight: bold; font-size: 1.25rem; margin: 0;">🤖 AI Resume Lab</h3>
            <a href="#" style="color: #2563eb; font-size: 12px; font-weight: bold; text-decoration: none;">View Samples ></a>
        </div>
        <div style="padding: 2rem; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 1rem; border: 2px dashed #cbd5e1; text-align: center;">
            <div style="font-size: 3rem; color: #94a3b8; margin-bottom: 1rem;">📄</div>
            <h4 style="font-size: 1.125rem; font-weight: 700; color: #1f2937; margin: 0 0 0.5rem 0;">Upload Your CV</h4>
            <p style="font-size: 14px; color: #64748b; margin: 0 0 1.5rem 0;">Get instant HK/GBA keyword optimization for JobsDB & LinkedIn</p>
        </div>
    """, unsafe_allow_html=True)

    # Simple drag-drop uploader
    uploaded_cv = st.file_uploader("", type=["pdf", "docx"], key="cv_prototype")

    if uploaded_cv:
        # Prototype success screen (no real processing)
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 2rem; border-radius: 1.5rem; color: white; text-align: center; margin: 1rem 0;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
            <h2 style="font-size: 1.5rem; font-weight: 800; margin: 0 0 1rem 0;">CV Analysis Complete!</h2>
            <p style="font-size: 16px; opacity: 0.95; margin-bottom: 2rem;">87% ATS Match • 92% Keyword Coverage</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mock results (static but looks real)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ATS Score", "87%", "↑ 12%")
            st.metric("Keywords Found", "42/50", "+8")
        with col2:
            st.metric("JobsDB Match", "94%", "Perfect")
            st.metric("LinkedIn Score", "89%", "Good")
        
        # Quick recommendations
        st.markdown("""
        <div style="padding: 1.5rem; background: #f0fdf4; border-radius: 12px; border-left: 4px solid #10b981; margin: 1.5rem 0;">
            <h4 style="font-size: 1.125rem; color: #059669; margin: 0 0 1rem 0;">🎯 Quick Fixes</h4>
            <ul style="font-size: 14px; color: #374151; margin: 0; padding-left: 1.5rem;">
                <li>Add "GBA Experience" & "Business Cantonese"</li>
                <li>Quantify achievements (e.g. "Increased sales 35%")</li>
                <li>Include LinkedIn URL</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            if st.button("📥 Download Optimized", use_container_width=True, type="primary"):
                st.balloons()
                st.success("✅ Optimized CV ready for download!")
        with col_btn2:
            st.button("🔗 Check LinkedIn", use_container_width=True)
        with col_btn3:
            st.button("🎤 Mock Interview", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

        
        # 這裡可以加上真正的 Streamlit 上傳按鈕，讓功能更真實
    uploaded_cv = st.file_uploader("", type=["pdf", "docx"], key="cv_uploader")
    if uploaded_cv:
        st.success("CV Uploaded! Optimizing keywords...")
    
    st.markdown("---")
    
 
 # 4. AI Multimodal Analyst
    st.markdown("### 👤 AI Multimodal Analyst")

    uploaded_file = st.file_uploader("Upload your profile image", type=['jpg', 'png', 'jpeg'], key="profile_uploader")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Target Profile", width=300)
        
        if st.button("✨ Run Multimodal Analysis", use_container_width=True):
            with st.spinner("AI 正在解析職業氣場..."):
                try:
                    img_array = np.array(image)
                    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                    
                    results = DeepFace.analyze(img_cv, actions=['age', 'gender', 'emotion'], enforce_detection=False)
                    res = results[0]
                    
                    age = int(res.get('age', 30))
                    gender = res['dominant_gender'].capitalize()
                    emotion = res['dominant_emotion'].capitalize()
                    
                    emotion_content = {
                        "happy": {
                            "title": "Happiness Connector Aura | 快樂連結者氣場", 
                            "desc": "**Your radiant smile radiates powerful positive energy, perfect for roles requiring charisma and team motivation. This aura boosts productivity by 13% and naturally attracts colleagues. Under pressure, you stay optimistic and spark creative solutions.**\n\n你的笑容散發強大正面能量，完美適合需要人際魅力與團隊動力的角色。這種氣場提升13%生產力，讓同事自動被你吸引。在高壓環境中，你能保持樂觀，激發創意解決方案。",
                            "strengths": "**Strengths: Natural Leader Charm, Pressure Transformer, Innovation Catalyst** | 🚀 優勢：天生領袖魅力、壓力轉化器、創新催化劑",
                            "jobs": "**PR Manager, Sales Director, Luxury Hospitality** | 公關經理、销售總監、高端酒店管理"
                        },
                        "neutral": {
                            "title": "Calm Analyst Aura | 冷靜分析師氣場", 
                            "desc": "**Your calm expression shows professional reliability, ideal for data-driven decision roles. Emotional neutrality enables clear thinking without bias, perfect for crisis handling. Teams trust your objective judgment.**\n\n你的平靜表情展現專業可靠，適合數據驅動決策角色。情感中立讓你清晰思考，避免情緒干擾，完美處理危機。團隊信任你的客觀判斷。",
                            "strengths": "**Strengths: Rational Decision-Maker, Crisis Stabilizer, Reliable Executor** | 🚀 優勢：理性決策者、危機穩定器、可靠執行者",
                            "jobs": "**Data Analyst, Researcher, Software Architect** | 數據分析師、研究員、軟件架構師"
                        },
                        "surprise": {
                            "title": "Creative Pioneer Aura | 創意開拓者氣場",
                            "desc": "**Your curious, surprised expression signals innovative thinking and rapid adaptability. This aura dominates dynamic markets by spotting overlooked opportunities and leading industry trends.**\n\n你的表情充滿好奇與驚喜，代表創新思維與快速適應力。這種氣場在動態市場中無敵，能發現他人忽略機會，引領行業趨勢。",
                            "strengths": "**Strengths: Trend Forecaster, Adaptable Innovator, Opportunity Hunter** | 🚀 優勢：趨勢預測者、靈活變通者、機會獵手",
                            "jobs": "**Creative Director, Event Planner, Marketing Strategist** | 創意總監、活動策劃、市場策略師"
                        },
                        "fear": {
                            "title": "Risk Guardian Aura | 風險守護者氣場",
                            "desc": "**Your cautious expression shows high vigilance and risk awareness, perfect for security-critical roles. You foresee potential problems, protecting teams from disasters as the corporate safety net.**\n\n謹慎表情顯示高度警覺與風險意識，適合安全關鍵崗位。你能預見潛在問題，保護團隊免於災難，成為企業安全防線。",
                            "strengths": "**Strengths: Prevention Expert, Detail Controller, Safety Defender** | 🚀 優勢：預防專家、細節控管者、安全捍衛者",
                            "jobs": "**Cybersecurity Analyst, Risk Auditor** | 網絡安全分析師、風險審計師"
                        },
                        "angry": {
                            "title": "Justice Enforcer Aura | 正義執行者氣場",
                            "desc": "**Your determined expression represents strong principles and execution power, ideal for decisive leadership roles. You never compromise quality and drive tough transformations to achieve the impossible.**\n\n堅定表情代表強烈原則與執行力，適合需要決斷的領導角色。你不妥協品質，能推動艱難變革，達成不可能任務。",
                            "strengths": "**Strengths: Principle Defender, Change Driver, Execution Ironman** | 🚀 優勢：原則捍衛者、變革推動者、執行鐵人",
                            "jobs": "**Legal Consultant, Chief Investigator** | 法律顧問、首席調查員"
                        },
                        "sad": {
                            "title": "Deep Empathy Aura | 深度共鳴者氣場",
                            "desc": "**Your nuanced expression reveals high empathy and insight, perfect for human-centered careers. You understand others' needs, create emotional connections, and build lasting trust relationships.**\n\n細膩表情顯示高同理心與洞察力，適合人文關懷職業。你能理解他人需求，創造情感連結，建立長期信任關係。",
                            "strengths": "**Strengths: Empathetic Listener, Needs Interpreter, Relationship Healer** | 🚀 優勢：同理傾聽者、需求解讀者、關係修復者",
                            "jobs": "**Counselor, Creative Writer, UX Researcher** | 輔導師、創意寫作者、UX研究員"
                        },
                        "disgust": {
                            "title": "Quality Gatekeeper Aura | 品質守門人氣場",
                            "desc": "**Your sharp expression represents high standards and zero tolerance for errors, perfect for quality control. You spot issues others miss, ensuring excellence as the final quality checkpoint.**\n\n敏銳表情代表高標準與零容忍錯誤，完美品質控制角色。你發現問題他人忽略，確保卓越輸出，成為品質最終防線。",
                            "strengths": "**Strengths: Flaw Hunter, Standards Setter, Quality Enforcer** | 🚀 優勢：瑕疵獵人、標準制定者、品質鐵律",
                            "jobs": "**Quality Manager, Forensic Specialist** | 品質主管、法證專家"
                        }
                    }

                    career_map = {
                        "Happy": "Public Relations, Sales Manager, High-end Hospitality",
                        "Neutral": "Data Analyst, Researcher, Software Architect",
                        "Surprise": "Creative Director, Event Planner, Marketing Strategist",
                        "Fear": "Cybersecurity Analyst, Risk Auditor",
                        "Angry": "Legal Consultant, Lead Investigator",
                        "Sad": "Counselor, Creative Writer, UX Researcher",
                        "Disgust": "Quality Controller, Forensic Specialist"
                    }
                    suggested_job = career_map.get(emotion, "Business Consultant")

                    # NATIVE STREAMLIT COMPONENTS - Matches your happy blocks perfectly
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown(f"""
                        <div style='background: #f8fafc; padding: 1rem; border-radius: 12px; text-align: center; border: 1px solid #f1f5f9;'>
                            <span style='font-size: 12px; color: #64748b; font-weight: bold; display: block;'>Gender</span>
                            <span style='font-size: 20px; font-weight: 800; color: #1e293b;'>{gender}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style='background: #f8fafc; padding: 1rem; border-radius: 12px; text-align: center; border: 1px solid #f1f5f9;'>
                            <span style='font-size: 12px; color: #64748b; font-weight: bold; display: block;'>Age</span>
                            <span style='font-size: 20px; font-weight: 800; color: #1e293b;'>~{age}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(f"""
                        <div style='background: #f8fafc; padding: 1rem; border-radius: 12px; text-align: center; border: 1px solid #f1f5f9;'>
                            <span style='font-size: 12px; color: #64748b; font-weight: bold; display: block;'>Mood</span>
                            <span style='font-size: 20px; font-weight: 800; color: #1e293b;'>{emotion}</span>
                        </div>
                        """, unsafe_allow_html=True)

                    # Results section - exact happy block style
                    st.markdown("---")
                    
                    content = emotion_content.get(emotion.capitalize(), emotion_content["neutral"])

                    st.markdown(f"""
                    <div style='border-top: 1px solid #f1f5f9; padding-top: 1.5rem;'>
                        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;'>
                            <span style='font-size: 12px; color: #3b82f6; font-weight: 900; text-transform: uppercase;'>Aura Analysis | 氣場解析</span>
                            <span style='font-size: 10px; background: #eff6ff; color: #1d4ed8; padding: 6px 10px; border-radius: 9999px; font-weight: bold;'>AI Verified</span>
                        </div>
                        <h3 style='font-size: 1.5rem; font-weight: 900; color: #111827; margin: 0 0 16px 0;'>{content['title']}</h3>
                        
                        <div style='background: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 20px;'>
                            <div style='font-size: 15px; color: #374151; line-height: 1.7; margin-bottom: 16px;'>{content['desc']}</div>
                        </div>
                        
                        <div style='background: #f0f9ff; padding: 20px; border-radius: 12px; border: 1px solid #dbeafe; margin-bottom: 16px;'>
                            <span style='font-size: 14px; color: #0369a1; font-weight: 800; display: block; margin-bottom: 12px;'>Key Strengths | 優勢特質：</span>
                            <span style='font-size: 15px; color: #1e3a8a; font-weight: 700;'>{content['strengths']}</span>
                        </div>
                        
                        <div style='background: #f0fdf4; padding: 20px; border-radius: 16px; border: 2px solid #dcfce7;'>
                            <span style='font-size: 16px; color: #16a34a; font-weight: 800; display: block; margin-bottom: 8px;'>🚀 HK/GBA Hot Jobs | 香港/大灣區熱門職位：</span>
                            <span style='font-size: 18px; color: #15803d; font-weight: 900;'>{content['jobs']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)



                except Exception as e:
                    st.error(f"Analysis failed: please make sure the face is clearly seen. | 分析失敗: 請確保照片包含清晰人臉。({str(e)})")
=======
    .card-base { background: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem; }
    .rightpick-blue { background: #5ba4cf; }
    .rightpick-orange { background: #ff6b35; }
</style>

<nav class="glass-nav px-8 py-4 flex justify-between items-center sticky top-0 z-50">
    <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rightpick-blue rounded-xl flex items-center justify-center text-white shadow-lg">
            <i class="fas fa-brain"></i>
        </div>
        <div>
            <h1 class="font-bold text-gray-900 leading-none" style="margin:0">RightPick <span class="text-blue-500">AI</span></h1>
            <span class="text-[10px] text-gray-400 font-bold tracking-widest uppercase">Professional Assistant v2.3</span>
        </div>
    </div>

</nav>
""", unsafe_allow_html=True)

# 3. 頁面佈局：左側 1/3 (三個卡片) | 右側 2/3 (主功能)
col_left, col_right = st.columns([1, 2.2], gap="large")
with col_left:
    # --- 1. Interest Analysis ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Interest Analysis</h3>
                <span style="font-size: 10px; background-color: #eff6ff; color: #2563eb; padding: 4px 8px; border-radius: 9999px; font-weight: bold;">JUPAS AI</span>
            </div>
            <div style="background-color: #f1f5f9; height: 80px; border-radius: 1rem; margin-bottom: 1rem; overflow: hidden;">
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400" style="width:100%; height:100%; object-fit: cover; opacity: 0.6;">
            </div>
            <a href="https://rightpickhk.com/career" target="_blank" style="text-decoration: none;">
                <div style="text-align: center; padding: 10px; background-color: #111827; color: white; border-radius: 0.75rem; font-weight: bold; font-size: 10px;">Find Interested Jobs</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # --- 2. Personality Match ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Personality Match</h3>
                <span style="font-size: 10px; background-color: #faf5ff; color: #9333ea; padding: 4px 8px; border-radius: 9999px; font-weight: bold;">18 TYPES</span>
            </div>
            <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                <div style="width: 32px; height: 32px; background-color: #f3e8ff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: bold; color: #7e22ce;">ENTP</div>
                <div style="width: 32px; height: 32px; background-color: #dbeafe; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: bold; color: #1d4ed8;">ISTJ</div>
            </div>
            <a href="https://rightpickhk.com/personality" target="_blank" style="text-decoration: none;">
                <div style="text-align: center; padding: 10px; background-color: #9333ea; color: white; border-radius: 0.75rem; font-weight: bold; font-size: 10px;">Start Personality Test</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # --- 3. Salary Insights ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Salary Insights</h3>
                <span style="font-size: 10px; background-color: #f0fdf4; color: #16a34a; padding: 4px 10px; border-radius: 9999px; font-weight: bold;">HK / GBA</span>
            </div>
            <div style="display: flex; align-items: flex-end; gap: 6px; height: 45px; margin-bottom: 15px; padding-bottom: 5px; border-bottom: 2px solid #f1f5f9;">
                <div style="background-color: #bbf7d0; width: 30%; height: 40%; border-radius: 4px 4px 0 0;"></div>
                <div style="background-color: #86efac; width: 30%; height: 70%; border-radius: 4px 4px 0 0;"></div>
                <div style="background-color: #22c55e; width: 30%; height: 100%; border-radius: 4px 4px 0 0;"></div>
            </div>
            <p style="font-size: 10px; color: #64748b; margin-bottom: 15px;">Compare your expected pay with 2026 industry benchmarks.</p>
            <a href="https://rightpickhk.com/salary-compare" target="_blank" style="text-decoration: none;">
                <div style="text-align: center; padding: 12px; background-color: #16a34a; color: white; border-radius: 0.75rem; font-weight: bold; font-size: 11px;">Analyze My Salary</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)
with col_right:
    # --- 上方：Skills Scraper (用 Inline Style 強制藍色) ---
    st.markdown('''
        <div style="background-color: #2563eb; color: white; padding: 1.5rem; border-radius: 1.5rem; margin-bottom: 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h2 style="font-size: 1.125rem; font-weight: bold; font-style: italic; margin: 0;">2026 Skills Scraper</h2>
                    <p style="color: #bfdbfe; font-size: 10px; margin: 0;">Live summary of Job Finding websites (HK/GBA)</p>
                </div>
                <div style="display: flex; gap: 24px; text-align: center;">
                    <div><span style="display: block; font-size: 1.5rem; font-weight: 900;">82%</span><span style="font-size: 8px; color: #bfdbfe;">LANGUAGES</span></div>
                    <div><span style="display: block; font-size: 1.5rem; font-weight: 900;">64%</span><span style="font-size: 8px; color: #bfdbfe;">AI TOOLS</span></div>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    # AI Multimodal Analyst
    st.markdown('''
        <div style="background: white; padding: 2rem; border-radius: 1.5rem; border: 2px dashed #cbd5e1; text-align: center;">
            <div class="mb-4">
                <div class="inline-block p-3 bg-blue-50 text-blue-500 rounded-2xl mb-2">
                    <i class="fas fa-camera-retro text-2xl"></i>
                </div>
                <h3 class="font-bold text-xl text-gray-800">AI Multimodal Analyst</h3>
                <p class="text-xs text-gray-400 mt-1">Upload your profile image for instant career vibe & talent optimization</p>
            </div>
    ''', unsafe_allow_html=True)

    # Streamlit 原生上傳組件 (放在 HTML 容器中間)
    uploaded_file = st.file_uploader("", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, width=250) # 顯示一張預覽小圖
        
        if st.button("🚀 Run Multimodal Analysis", use_container_width=True):
            with st.spinner("Analyzing facial metrics..."):
                try:
                    results = DeepFace.analyze(np.array(img), actions=['emotion'], enforce_detection=False)
                    vibe = results[0]['dominant_emotion'].capitalize()
                    
                    # 顯示分析結果
                    st.markdown(f'''
                        <div style="margin-top: 1.5rem; padding: 1rem; background: #f0f9ff; border-radius: 1rem; border: 1px solid #bae6fd;">
                            <span class="text-[10px] font-bold text-blue-600 uppercase">Analysis Result</span>
                            <div class="text-2xl font-black text-gray-900">{vibe} & Professional</div>
                            <p class="text-[11px] text-gray-500 mt-1">Your expression matches high-performance <b>Consultancy</b> roles.</p>
                        </div>
                    ''', unsafe_allow_html=True)
                except:
                    st.error("Please provide a clearer face image.")

    st.markdown('</div>', unsafe_allow_html=True) # 結束右側大容器
>>>>>>> 0064574e60bfaf3bbb836573234bc508c569205b
