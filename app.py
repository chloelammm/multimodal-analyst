#v2.2
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
    /* 隱藏 Streamlit 預設的上邊距 */
    .block-container { padding-top: 0rem; }
</style>

<nav class="glass-nav px-8 py-4 flex justify-between items-center sticky top-0 z-50">
    <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rightpick-blue rounded-xl flex items-center justify-center text-white shadow-lg">
            <i class="fas fa-brain"></i>
        </div>
        <div>
            <h1 class="font-bold text-gray-900 leading-none" style="margin:0">RightPick <span class="text-blue-500">AI</span></h1>
            <span class="text-[10px] text-gray-400 font-bold tracking-widest uppercase">Professional Suite v2.5</span>
        </div>
    </div>
    <div class="hidden lg:flex space-x-6 text-sm font-semibold text-gray-500">
        <span>Market Trends</span><span>GBA Portal</span><span>Resume Lab</span>
    </div>
</nav>
""", unsafe_allow_html=True)

# 3. 頁面佈局：左側 1/3 (三個卡片) | 右側 2/3 (主功能)
col_left, col_right = st.columns([1, 2.2], gap="large")

with col_left:
    # --- 1. Interest Analysis ---
    st.markdown('''
        <div class="card-base">
            <div class="flex justify-between items-start mb-3">
                <h3 class="font-bold text-lg">Interest Analysis</h3>
                <span class="text-[10px] bg-blue-50 text-blue-600 px-2 py-1 rounded-full font-bold">JUPAS AI</span>
            </div>
            <div style="background: #f1f5f9; height: 80px; border-radius: 1rem; margin-bottom: 1rem; display: flex; align-items: center; justify-center; overflow: hidden;">
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400" style="width:100%; object-fit: cover; opacity: 0.6;">
            </div>
            <a href="https://rightpickhk.com/career" target="_blank" style="text-decoration:none">
                <div class="text-center py-2 bg-gray-900 text-white rounded-xl font-bold text-[10px]">Find Interested Jobs</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # --- 2. Personality Match ---
    st.markdown('''
        <div class="card-base">
            <div class="flex justify-between items-start mb-3">
                <h3 class="font-bold text-lg">Personality Match</h3>
                <span class="text-[10px] bg-purple-50 text-purple-600 px-2 py-1 rounded-full font-bold">18 TYPES</span>
            </div>
            <div class="flex space-x-2 mb-3">
                <div class="w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center text-[8px] font-bold text-purple-600 shadow-sm">ENTP</div>
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-[8px] font-bold text-blue-600 shadow-sm">ISTJ</div>
            </div>
            <a href="https://rightpickhk.com/personality" target="_blank" style="text-decoration:none">
                <div class="text-center py-2 bg-purple-600 text-white rounded-xl font-bold text-[10px]">Start Personality Test</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # --- 3. Salary Insights ---
    st.markdown('''
        <div class="card-base">
            <div class="flex justify-between items-start mb-3">
                <h3 class="font-bold text-lg">Salary Insights</h3>
                <span class="text-[10px] bg-green-50 text-green-600 px-2 py-1 rounded-full font-bold">HK / GBA</span>
            </div>
            <p class="text-[10px] text-gray-500 mb-3">Compare your pay with 2026 industry benchmarks.</p>
            <a href="https://rightpickhk.com/salary-compare" target="_blank" style="text-decoration:none">
                <div class="text-center py-2 bg-green-600 text-white rounded-xl font-bold text-[10px]">Analyze My Salary</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

with col_right:
    # --- 上方：Skills Scraper (保持藍色亮點) ---
    st.markdown('''
        <div style="background: #2563eb; color: white; padding: 1.5rem; border-radius: 1.5rem; margin-bottom: 1.5rem; position: relative; overflow: hidden;">
            <div class="flex justify-between items-center">
                <div>
                    <h2 class="text-lg font-bold italic">2026 Skills Scraper</h2>
                    <p class="text-blue-100 text-[10px]">Live summary of Job Finding websites (HK/GBA)</p>
                </div>
                <div class="flex space-x-6">
                    <div class="text-center"><span class="block text-2xl font-black">82%</span><span class="text-[8px] text-blue-200">LANGUAGES</span></div>
                    <div class="text-center"><span class="block text-2xl font-black">64%</span><span class="text-[8px] text-blue-200">AI TOOLS</span></div>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    # --- 下方：AI Multimodal Analyst (這部分取代了 AI Resume Lab) ---
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
