#v2.1
import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace

# 1. 頁面配置
st.set_page_config(page_title="RightPick AI | Professional Suite", layout="wide")

# 2. 注入全局 CSS (讓 Streamlit 組件更像你的 HTML 設計)
st.markdown("""
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    .card { background: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1.5rem; }
    .rightpick-blue { background: #5ba4cf; }
    .glass-nav { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid #e2e8f0; margin-bottom: 2rem; }
</style>

<nav class="glass-nav px-8 py-4 flex justify-between items-center sticky top-0 z-50">
    <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rightpick-blue rounded-xl flex items-center justify-center text-white shadow-lg">
            <i class="fas fa-brain"></i>
        </div>
        <div>
            <h1 class="font-bold text-gray-900 leading-none" style="margin:0">RightPick <span class="text-blue-500">AI</span></h1>
            <span class="text-[10px] text-gray-400 font-bold tracking-widest uppercase">Occupation Suite v2.5</span>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# 3. 建立三欄佈局
col_left, col_mid, col_right = st.columns([1, 1.5, 1], gap="medium")

# --- 左欄：原本的測試卡片 ---
with col_left:
    # Interest Analysis
    st.markdown('''
        <div class="card">
            <div class="flex justify-between items-start mb-4">
                <h3 class="font-bold text-lg">Interest Analysis</h3>
                <span class="text-[10px] bg-blue-50 text-blue-600 px-2 py-1 rounded-full font-bold">JUPAS AI</span>
            </div>
            <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=400" class="rounded-xl mb-4 opacity-80">
            <a href="https://rightpickhk.com/career" style="text-decoration:none" target="_blank">
                <div class="text-center py-2.5 bg-gray-900 text-white rounded-xl font-bold text-[10px]">Find Interested Jobs</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # Personality Match
    st.markdown('''
        <div class="card">
            <div class="flex justify-between items-start mb-4">
                <h3 class="font-bold text-lg">Personality Match</h3>
                <span class="text-[10px] bg-purple-50 text-purple-600 px-2 py-1 rounded-full font-bold">18 TYPES</span>
            </div>
            <p class="text-[11px] text-gray-500 mb-4 italic">"How does your character fit the workplace culture?"</p>
            <a href="https://rightpickhk.com/personality" style="text-decoration:none" target="_blank">
                <div class="text-center py-2.5 bg-purple-600 text-white rounded-xl font-bold text-[10px]">Start Personality Test</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

# --- 中欄：核心 AI 功能 ---
with col_mid:
    st.markdown('<h3 class="font-bold text-xl mb-4 text-center">🎭 Multimodal Analyst</h3>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, use_container_width=True)
        
        if st.button("🚀 Start Professional Vibe Check", use_container_width=True):
            with st.spinner("AI analyzing your talent profile..."):
                try:
                    img_array = np.array(img)
                    results = DeepFace.analyze(img_array, actions=['emotion'], enforce_detection=False)
                    st.session_state['res'] = results[0]
                except Exception as e:
                    st.error("Could not detect face. Please use a clearer photo.")

    if 'res' in st.session_state:
        vibe = st.session_state['res']['dominant_emotion'].capitalize()
        st.markdown(f'''
            <div style="background: white; padding: 2rem; border-radius: 1.5rem; border: 2px solid #3b82f6; text-align: center;">
                <h4 class="text-blue-600 font-bold uppercase text-[10px] tracking-widest">Analysis Complete</h4>
                <div class="text-4xl font-black my-2">{vibe}</div>
                <p class="text-gray-500 text-sm">Your visual vibe suggests a strong match for <b>Strategic Leadership</b> roles.</p>
            </div>
        ''', unsafe_allow_html=True)

# --- 右欄：Salary & Scraper ---
with col_right:
    # Salary Insights
    st.markdown('''
        <div class="card">
            <div class="flex justify-between items-start mb-4">
                <h3 class="font-bold text-lg">Salary Insights</h3>
                <span class="text-[10px] bg-green-50 text-green-600 px-2 py-1 rounded-full font-bold">2026 HK</span>
            </div>
            <p class="text-[11px] text-gray-500 mb-4">Compare your pay with industry benchmarks.</p>
            <a href="https://rightpickhk.com/salary-compare" style="text-decoration:none" target="_blank">
                <div class="text-center py-2.5 bg-green-600 text-white rounded-xl font-bold text-[10px]">Analyze My Salary</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)

    # Skills Scraper (藍色大卡片)
    st.markdown('''
        <div style="background: #2563eb; color: white; padding: 1.5rem; border-radius: 1.5rem; box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);">
            <h2 class="font-bold italic text-sm">2026 Skills Scraper</h2>
            <div class="flex justify-between mt-4">
                <div><span class="block text-2xl font-black">82%</span><span class="text-[8px] uppercase">Bilingual</span></div>
                <div><span class="block text-2xl font-black">64%</span><span class="text-[8px] uppercase">AI Prompts</span></div>
            </div>
        </div>
    ''', unsafe_allow_html=True)
