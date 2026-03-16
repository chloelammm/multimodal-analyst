import streamlit as st
import pandas as pd
from deepface import DeepFace
from PIL import Image
import numpy as np

# --- 1. 頁面基本設定 ---
st.set_page_config(page_title="RightPick AI | Professional Suite", layout="wide")

# --- 2. 注入你的專業 HTML/CSS ---
# 我們將你的 HTML 拆解，用 st.markdown 注入
professional_ui = """
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; }
    .rightpick-blue { background: #5ba4cf; }
    .rightpick-orange { background: #ff6b35; }
    .glass-nav { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid #e2e8f0; }
</style>

<nav class="glass-nav px-8 py-4 flex justify-between items-center sticky top-0 z-50 mb-6">
    <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rightpick-blue rounded-xl flex items-center justify-center text-white shadow-lg">
            <i class="fas fa-brain"></i>
        </div>
        <div>
            <h1 class="font-bold text-gray-900 leading-none" style="margin:0">RightPick <span class="text-blue-500">AI</span></h1>
            <span class="text-[10px] text-gray-400 font-bold tracking-widest uppercase">Occupation Suite v2.5</span>
        </div>
    </div>
    <div class="hidden lg:flex space-x-6 text-sm font-semibold text-gray-500">
        <span>Market Trends</span><span>GBA Portal</span><span>Resume Lab</span>
    </div>
</nav>
"""
st.markdown(professional_ui, unsafe_allow_html=True)

# --- 3. 佈局設計 ---
col_left, col_right = st.columns([1, 2], gap="large")

with col_left:
    # 這裡放原本 HTML 的左側卡片設計
    st.markdown('''
        <div style="background: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #f1f5f9; margin-bottom: 1.5rem;">
            <h3 style="font-weight: bold; font-size: 1.125rem; margin-bottom: 1rem;">Multimodal Analyst</h3>
            <p style="font-size: 0.75rem; color: #64748b; margin-bottom: 1rem;">Upload a photo to analyze your professional vibe and match it with career roles.</p>
        </div>
    ''', unsafe_allow_html=True)
    
    # --- Streamlit 原生功能組件 ---
    uploaded_file = st.file_uploader("選擇照片 (JPG/PNG)", type=['jpg', 'jpeg', 'png'])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Ready for Analysis", use_container_width=True)
        
        if st.button("🚀 Start AI Analysis", use_container_width=True):
            with st.spinner("AI is decoding your vibe..."):
                try:
                    # 原本的 DeepFace 邏輯
                    img_array = np.array(img)
                    results = DeepFace.analyze(img_array, actions=['emotion', 'age', 'gender'], enforce_detection=False)
                    
                    # 存入 Session State 顯示在右邊
                    st.session_state['analysis_done'] = True
                    st.session_state['results'] = results[0]
                except Exception as e:
                    st.error(f"Analysis failed: {e}")

with col_right:
    # 這裡放右側的 2026 Skills Scraper 和 分析結果
    st.markdown("""
        <div style="background: #2563eb; color: white; padding: 2rem; border-radius: 1.5rem; margin-bottom: 2rem;">
            <h2 style="font-weight: bold; font-style: italic; font-size: 1.25rem;">2026 Skills Scraper</h2>
            <div style="display: flex; gap: 2rem; margin-top: 1rem;">
                <div><span style="display: block; font-size: 2rem; font-weight: 900;">82%</span><span style="font-size: 0.6rem; opacity: 0.8;">MANDARIN/ENG</span></div>
                <div><span style="display: block; font-size: 2rem; font-weight: 900;">64%</span><span style="font-size: 0.6rem; opacity: 0.8;">AI PROMPTING</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if 'analysis_done' in st.session_state:
        res = st.session_state['results']
        emotion = res['dominant_emotion'].capitalize()
        
        # 將 AI 數據填入你的 HTML 模板中
        st.markdown(f"""
            <div style="background: white; padding: 2rem; border-radius: 1.5rem; border: 1px solid #bfdbfe; box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.1);">
                <h3 style="font-weight: bold; font-size: 1.25rem; margin-bottom: 1.5rem;">AI Talent Analysis</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                    <div>
                        <h4 style="font-size: 0.7rem; color: #94a3b8; font-weight: 900; text-transform: uppercase;">Professional Vibe</h4>
                        <div style="margin-top: 0.5rem; padding: 0.5rem 1rem; background: #eff6ff; color: #1d4ed8; font-weight: bold; border-radius: 9999px; display: inline-block;">
                            {emotion} & Confident
                        </div>
                    </div>
                    <div>
                        <h4 style="font-size: 0.7rem; color: #94a3b8; font-weight: 900; text-transform: uppercase;">Best Match</h4>
                        <p style="font-weight: bold;">Business Analyst (Fintech)</p>
                        <span style="color: #3b82f6; font-size: 0.75rem; font-weight: bold;">98% Compatibility</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Waiting for your input on the left panel...")
