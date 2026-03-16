#v2.3
import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace

# 1. 頁面基本配置
st.set_page_config(page_title="RightPick AI | Professional Suite", layout="wide")

# 2. 注入全局設計與 CSS
st.markdown("""
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    .glass-nav { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid #e2e8f0; margin-bottom: 1.5rem; }
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
