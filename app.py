import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace
import cv2
import pdfplumber
import plotly.graph_objects as go

#version 2.7 - with Poll + skill cards

# 1. 頁面基本配置
st.set_page_config(page_title="RightPick AI | Professional Suite", layout="wide", page_icon="🤖")


# 2. 注入全局設計與 CSS
st.markdown("""
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    .glass-nav { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid #e2e8f0; margin-bottom: 1.5rem; }
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
            <span class="text-[10px] text-gray-400 font-bold tracking-widest uppercase">Professional Assistant v2.6</span>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)


# 3. 頁面佈局
# col_left, col_right = st.columns([1, 2.2], gap="large")
col_left, col_mid, col_right = st.columns([0.8, 1.5, 1], gap="medium")

with col_left:
#3 tests
    # --- 1. Interest Analysis ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 0.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Interest Analysis</h3>
                <span style="font-size: 10px; background-color: #eff6ff; color: #2563eb; padding: 4px 8px; border-radius: 9999px; font-weight: bold;">JUPAS AI</span>
            </div>
            <div style="background-color: #f1f5f9; height: 60px; border-radius: 1rem; margin-bottom: 1rem; overflow: hidden;">
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400" style="width:100%; height:100%; object-fit: cover; opacity: 0.6;">
            </div>
        </div>
    ''', unsafe_allow_html=True)

    with st.popover("Start Career Quiz | 開始職業測評", use_container_width=True):
        st.subheader("Quick Diagnostic | 快速診斷")
        
        # 問題 1
        q1 = st.radio(
            "1. Which do you prefer working with? | 你更喜歡處理什麼？",
            [
                "Data & Logic | 數據與邏輯", 
                "Creative Design | 創意設計", 
                "People & Social | 人際溝通", 
                "Hands-on Technical | 實務操作"
            ]
        )
        
        # 問題 2
        q2 = st.selectbox(
            "2. Ideal work environment? | 理想工作環境？",
            [
                "Corporate / Office | 大型企業/辦公室", 
                "Startup / Flexible | 初創公司/靈活空間", 
                "Studio / Outdoor | 工作室/戶外", 
                "Remote / Digital | 遠端工作/數位化"
            ]
        )
        
        # 問題 3
        q3 = st.select_slider(
            "3. What do you value most? | 你最看重什麼？",
            options=["Stability | 穩定", "Salary | 薪酬", "Impact | 影響力", "Innovation | 創新"]
        )
        
        if st.button("Generate My Analysis | 生成我的分析"):
            # 診斷邏輯
            result_title = ""
            result_desc = ""
            
            if "Data" in q1 or "Innovation" in q3:
                result_title = "Data Science / FinTech"
                result_desc = "You have a strong analytical mindset. | 你具備強大的邏輯分析能力。"
            elif "Creative" in q1:
                result_title = "Digital Media / UIUX"
                result_desc = "Your strength lies in visual storytelling. | 你的優勢在於視覺敘事。"
            elif "People" in q1:
                result_title = "Management / Marketing"
                result_desc = "You are a natural communicator. | 你是天生的溝通者。"
            else:
                result_title = "Engineering / IT Ops"
                result_desc = "You excel at solving practical problems. | 你擅長解決實際問題。"
                
            st.markdown(f"""
            <div style="background: #f0fdf4; padding: 15px; border-radius: 12px; border: 1px solid #bbf7d0; margin-top: 15px;">
                <p style="color: #166534; font-size: 12px; font-weight: bold; margin-bottom: 5px;">RESULT | 分析結果：</p>
                <h4 style="margin:0; color: #15803d; font-size: 1.1rem;">{result_title}</h4>
                <p style="font-size: 13px; color: #166534; margin-top: 5px;">{result_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.caption("Powered by RightPick")
            st.markdown("[Test for a Full Interest Analysis Report →](https://rightpickhk.com/career)")

    # --- 2. Personality Match ---
    import plotly.graph_objects as go

# --- 2. Personality Match (Advanced Weighted & Bilingual) ---
    st.markdown('''
    <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 0.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
            <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">RightPick Talent Matrix | 人才矩陣</h3>
            <span style="font-size: 10px; background-color: #f0fdf4; color: #16a34a; padding: 4px 10px; border-radius: 9999px; font-weight: bold;">v4.2 PRO</span>
        </div>
        <p style="font-size: 11px; color: #64748b; margin: 0;">Scientific trait analysis for the 2026 GBA market. | 針對 2026 大灣區市場的科學特質分析。</p>
    </div>
    ''', unsafe_allow_html=True)

    with st.popover("🚀 Launch Professional Assessment | 啟動專業深度測評", use_container_width=True):
        st.markdown("#### Workplace Behavioral Audit | 職場行為審計")
        st.write("Rate from **1 (Strongly Disagree | 極不同意)** to **5 (Strongly Agree | 極同意)**")

        questions = [
            # E vs I
            ("I feel energized after a day of back-to-back client meetings. | 經過一整天密集的客戶會議後，我感到充滿活力。", "E"),
            ("I prefer brainstorming in a group rather than solving problems alone. | 我傾向團隊腦力激盪，多於獨自解決問題。", "E"),
            ("I am usually the first to speak up in cross-functional workshops. | 在跨部門工作坊中，我通常是第一個發言的人。", "E"),
            ("I find large networking events in Central/GBA exciting. | 我覺得在中環或大灣區的大型交流活動非常有趣。", "E"),
            # S vs N
            ("I focus more on immediate practical facts than future theories. | 我更關注目前的實際事實，而非未來的理論。", "S"),
            ("I prefer following a proven standard operating procedure (SOP). | 我傾向遵循已被證實有效的標準作業程序 (SOP)。", "S"),
            ("I value realistic experience over abstract innovation. | 比起抽象的創新，我更看重務實的經驗。", "S"),
            ("I am more comfortable with data I can see and verify. | 處理看得見且能驗證的數據讓我感到更踏實。", "S"),
            # T vs F
            ("I make decisions based on logical analysis rather than feelings. | 我根據邏輯分析做決定，而非個人感覺。", "T"),
            ("I believe being direct is more important than protecting feelings. | 我認為直接指出問題比顧及對方感受更重要。", "T"),
            ("I prioritize project efficiency over team social harmony. | 我優先考慮項目效率，多於團隊的社交和諧。", "T"),
            ("I rely on objective metrics to settle workplace disagreements. | 我依賴客觀指標來解決職場上的分歧。", "T"),
            # J vs P
            ("I feel more comfortable with a strictly planned weekly schedule. | 我對嚴格規劃的每週時程表感到更自在。", "J"),
            ("I prefer finishing tasks well before the deadline to avoid stress. | 我喜歡在死線前早早完成任務以避免壓力。", "J"),
            ("I like to have my digital work environment highly organized. | 我喜歡將數位工作環境整理得井井有條。", "J"),
            ("I feel uneasy when a project's requirements change last minute. | 當項目需求在最後一刻改變時，我會感到不安。", "J"),
        ]

        scores = []
        for i, (q_text, trait) in enumerate(questions):
            val = st.select_slider(f"**Q{i+1}.** {q_text}", options=[1, 2, 3, 4, 5], value=3, key=f"adv_q_{i}")
            scores.append((val, trait))
            if (i + 1) % 4 == 0: st.divider()

        if st.button("Generate Report | 生成報告", use_container_width=True):
            e_val = sum(s[0] for s in scores[0:4])
            s_val = sum(s[0] for s in scores[4:8])
            t_val = sum(s[0] for s in scores[8:12])
            j_val = sum(s[0] for s in scores[12:16])

            # Dimension selection
            mcode = f"{'E' if e_val >= 12 else 'I'}{'S' if s_val >= 12 else 'N'}{'T' if t_val >= 12 else 'F'}{'J' if j_val >= 12 else 'P'}"

            # Logic for Radar Chart Percentages (Min 4pts = 0%, Max 20pts = 100%)
            # This shows how much you lean into the E, S, T, and J traits.
            #radar_values = [(v - 4) / 16 * 100 for v in [e_val, s_val, t_val, j_val]]
            categories = ['Extraversion', 'Sensing', 'Thinking', 'Judging']

            profiles = {
                "INTJ": {"title": "The Architect | 戰略建築師", "path": "AI Strategy & Deep Tech", "match": 98},
                "INTP": {"title": "The Logician | 邏輯學家", "path": "Data Science & Research", "match": 96},
                "ENTJ": {"title": "The Commander | 指揮官", "path": "Tech Ventures & Management", "match": 97},
                "ENTP": {"title": "The Debater | 辯論家", "path": "Product Innovation & Growth", "match": 95},
                "INFJ": {"title": "The Advocate | 提倡者", "path": "UX Strategy & ESG Consulting", "match": 94},
                "INFP": {"title": "The Mediator | 調解者", "path": "Creative Design & Content", "match": 92},
                "ENFJ": {"title": "The Protagonist | 主人翁", "path": "Talent Dev & Public Relations", "match": 93},
                "ENFP": {"title": "The Campaigner | 競選者", "path": "Digital Marketing & Creative Lead", "match": 95},
                "ISTJ": {"title": "The Logistician | 物流師", "path": "FinTech Compliance & IT Audit", "match": 94},
                "ISFJ": {"title": "The Defender | 守衛者", "path": "Customer Success & HR Ops", "match": 91},
                "ESTJ": {"title": "The Executive | 總經理", "path": "Operations & Project Management", "match": 96},
                "ESFJ": {"title": "The Consul | 執政官", "path": "Sales Director & Event Strategy", "match": 92},
                "ISTP": {"title": "The Virtuoso | 鑑賞家", "path": "Systems Engineering & Forensics", "match": 93},
                "ISFP": {"title": "The Adventurer | 探險家", "path": "Creative Arts & Branding", "match": 90},
                "ESTP": {"title": "The Entrepreneur | 企業家", "path": "Fintech Trading & Sales Lead", "match": 94},
                "ESFP": {"title": "The Entertainer | 表演者", "path": "Media & Hospitality Management", "match": 91}
            }
            res = profiles.get(mcode, {"title": "Industry Specialist", "path": "General Management", "match": 85})

        # # --- Display Radar Chart ---
        #  # --- Premium Radar Chart Styling ---
        #     fig = go.Figure()

        #     # User's Result Trace
        #     fig.add_trace(go.Scatterpolar(
        #         r=radar_values + [radar_values[0]],
        #         theta=categories + [categories[0]],
        #         fill='toself',
        #         fillcolor='rgba(37, 99, 235, 0.2)',  # Soft blue fill
        #         line=dict(color='#2563eb', width=3),  # Bold electric blue border
        #         marker=dict(color='#1e40af', size=8),
        #         name='Your Profile'
        #     ))

        #     # Optional: Add a "Baseline" or "Average" for comparison (The "Advanced" touch)
        #     fig.add_trace(go.Scatterpolar(
        #         r=[50, 50, 50, 50, 50],
        #         theta=categories + [categories[0]],
        #         fill='none',
        #         line=dict(color='rgba(148, 163, 184, 0.5)', width=1, dash='dot'),
        #         name='Industry Avg'
        #     ))

        #     fig.update_layout(
        #         polar=dict(
        #             bgcolor="rgba(0,0,0,0)", # Transparent background
        #             radialaxis=dict(
        #                 visible=True,
        #                 range=[0, 100],
        #                 showline=False,
        #                 gridcolor="#e2e8f0",
        #                 tickfont=dict(size=10, color="#94a3b8")
        #             ),
        #             angularaxis=dict(
        #                 tickfont=dict(size=12, color="#1e293b", weight="bold"),
        #                 gridcolor="#e2e8f0",
        #                 rotation=90, # Starts from the top
        #                 direction="clockwise"
        #             )
        #         ),
        #         showlegend=False,
        #         height=400,
        #         margin=dict(l=50, r=50, t=30, b=30),
        #         paper_bgcolor='rgba(0,0,0,0)',
        #         plot_bgcolor='rgba(0,0,0,0)',
        #     )

        #     st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

            # --- Result Card ---
            st.markdown(f"""
            <div style="background: #f8fafc; padding: 25px; border-radius: 1.5rem; border: 2px solid #e2e8f0; margin-top: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="background: #0f172a; color: white; padding: 5px 15px; border-radius: 99px; font-size: 12px; font-weight: bold;">{mcode}</span>
                    <span style="color: #64748b; font-size: 11px; font-weight: bold;">COMPETENCY MATCH: {res['match']}%</span>
                </div>
                <h2 style="margin: 15px 0 5px 0; color: #1e293b; font-size: 1.5rem;">{res['title']}</h2>
                <p style="font-size: 13px; color: #475569; border-bottom: 1px solid #e2e8f0; padding-bottom: 15px;">
                    Optimized Career Path: <b>{res['path']}</b>
                </p>
                <div style="margin-top: 15px;">
                    <p style="font-size: 12px; color: #1e293b;"><strong>AI Insight | AI 洞察:</strong></p>
                    <p style="font-size: 12px; color: #64748b; line-height: 1.6;">
                        Your profile indicates high adaptability in <b>cross-border collaboration</b> within the GBA ecosystem. 
                        Your decision-making style is perfectly suited for high-stakes 2026 tech environments.
                        <br><br>
                        你的特質顯示你在大灣區生態圈的<b>跨境協作</b>中具備極高適應力。你的決策風格非常適合 2026 年高壓的科技產業環境。
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("[Get Full 20-Page Personality Analysis →](https://rightpickhk.com/personality)")

# --- 3. Salary Insights (Interactive Benchmark Tool) ---
    st.markdown('''
        <div style="background-color: white; padding: 1.5rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 0.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <h3 style="font-weight: bold; font-size: 1.125rem; margin: 0; color: #111827;">Salary Insights</h3>
                <span style="font-size: 10px; background-color: #f0fdf4; color: #16a34a; padding: 4px 10px; border-radius: 9999px; font-weight: bold;">HK / GBA 2026</span>
            </div>
            <div style="display: flex; align-items: flex-end; gap: 6px; height: 45px; margin-bottom: 10px; padding-bottom: 5px; border-bottom: 2px solid #f1f5f9;">
                <div style="background-color: #bbf7d0; width: 30%; height: 40%; border-radius: 4px 4px 0 0;"></div>
                <div style="background-color: #86efac; width: 30%; height: 70%; border-radius: 4px 4px 0 0;"></div>
                <div style="background-color: #22c55e; width: 30%; height: 100%; border-radius: 4px 4px 0 0;"></div>
            </div>
            <p style="font-size: 10px; color: #64748b; margin-bottom: 5px;">Compare your expected pay with 2026 industry benchmarks.</p>
        </div>
    ''', unsafe_allow_html=True)

    with st.popover("Analyze My Salary | 薪資分析", use_container_width=True):
        st.write("### Market Benchmark (2026) | 市場基準")
        
        # 職位列表
        roles_options = [
            "Data Science / AI | 數據科學",
            "Software Engineering | 軟體工程",
            "Banking & Finance | 銀行與金融",
            "UX/UI Design | 介面設計",
            "Digital Marketing | 數位行銷"
        ]
        
        job_role = st.selectbox("Select Job Role | 選擇職位類別", roles_options)
        
        expected_pay = st.slider(
            "Monthly Expected Salary (HKD) | 預期月薪",
            min_value=15000,
            max_value=100000, # 擴大範圍以應對資深職位
            value=28000,
            step=1000
        )
        
        if st.button("Compare with Market | 與市場對比", use_container_width=True):
            # 更加擬真的 2026 市場預測數據 (中位數)
            market_data = {
                "Data Science / AI": 38500,
                "Software Engineering": 34000,
                "Banking & Finance": 32000,
                "UX/UI Design": 29500,
                "Digital Marketing": 25500
            }
            
            # 獲取基準薪資
            avg_pay = market_data.get(job_role, 30000)
            diff_pct = ((expected_pay - avg_pay) / avg_pay) * 100
            
            # 顯示基準
            st.write(f"**Market Median (2026):** HKD {avg_pay:,}")
            
            # 邏輯判斷
            if diff_pct > 20:
                st.success(f"**Premium Range:** Your expectation is {abs(diff_pct):.1f}% above average. Target top-tier firms.")
            elif diff_pct >= -10 and diff_pct <= 20:
                st.info(f"**Market Fit:** Your expectation is within the healthy market range ({diff_pct:+.1f}%).")
            else:
                st.warning(f"**Below Market:** Your expectation is {abs(diff_pct):.1f}% below average. Consider negotiating higher.")

            # 動態建議區塊 (根據職位)
            top_quartile = int(avg_pay * 1.35) # 前 25% 的高薪水平
            
            st.markdown(f"""
            <div style="background-color: #f8fafc; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; margin-top: 15px;">
                <p style="font-size: 13px; color: #334155; margin: 0;">
                    <strong>💡 Market Tip for {job_role.split(' | ')[0]}:</strong><br>
                    High-demand skills like <b>Cloud Architecture</b> or <b>Generative AI</b> can push GBA packages beyond <b>HKD {top_quartile:,}</b> in 2026.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            st.markdown("[View Full 2026 Salary Guide →](https://rightpickhk.com/salary-compare)")

    st.markdown("---")


# # --- 右側欄位 (col_right) --- skills scraper + skills review
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


#     # 2. Review Your Talent & Skills 卡片
# --- 1. 強化版技能池 (Categorized Skills Pool) ---
# 將技能分類，讓用戶在選擇時更有組織感
    SKILLS_MARKET = {
        "Technical / Hard Skills": [
            "Python (Data Science)", "Machine Learning", "Generative AI Prompting", 
            "SQL / NoSQL", "Cloud Computing (AWS/Azure)", "React / Next.js", 
            "Mobile Dev (Flutter/Dart)", "Cybersecurity", "Financial Modeling", "SEO/SEM"
        ],
        "Tools & Software": [
            "Figma / Adobe XD", "Tableau / Power BI", "Git / GitHub", 
            "Docker / Kubernetes", "Google Analytics 4", "Salesforce CRM"
        ],
        "Soft Skills & Languages": [
            "Critical Thinking", "Project Management", "Cantonese (Native)", 
            "English (Business)", "Mandarin (Professional)", "UX Writing", "Public Speaking"
        ]
    }

    # 攤平成為一個單一列表供 multiselect 使用
    ALL_SKILLS_FLAT = [skill for sublist in SKILLS_MARKET.values() for skill in sublist]

    # --- 2. 強化版職業資料庫 (Enhanced Job DB) ---
    # 包含 2026 年高薪及高需求職位
    JOB_DATABASE = {
        "AI Solution Architect": {
            "skills": ["Generative AI Prompting", "Python (Data Science)", "Cloud Computing (AWS/Azure)", "Critical Thinking"],
            "desc": "Designing AI-driven workflows for enterprises."
        },
        "Fintech Business Analyst": {
            "skills": ["Financial Modeling", "SQL / NoSQL", "Tableau / Power BI", "English (Business)"],
            "desc": "Bridging the gap between finance and technology."
        },
        "Full-Stack Developer (GBA Focus)": {
            "skills": ["React / Next.js", "Python (Data Science)", "Git / GitHub", "Cantonese (Native)"],
            "desc": "Building cross-border digital platforms."
        },
        "UX/UI Product Designer": {
            "skills": ["Figma / Adobe XD", "UX Writing", "Critical Thinking", "User Research"],
            "desc": "Creating human-centric AI interfaces."
        },
        "Digital Growth Strategist": {
            "skills": ["SEO/SEM", "Google Analytics 4", "Public Speaking", "Mandarin (Professional)"],
            "desc": "Driving user acquisition in the GBA market."
        },
        "Cybersecurity Consultant": {
            "skills": ["Cybersecurity", "Cloud Computing (AWS/Azure)", "Docker / Kubernetes", "Critical Thinking"],
            "desc": "Protecting enterprise data integrity."
        }
    }

    # --- 3. UI 渲染 ---

    st.markdown('''
        <div style="margin-bottom: 1.5rem;">
            <h3 style="font-weight: bold; font-size: 1.25rem; color: #1f2937; margin: 0;">Review Your Talent & Skills</h3>
            <p style="font-size: 0.875rem; color: #64748b;">Update your stack to see 2026 career compatibility.</p>
        </div>
    ''', unsafe_allow_html=True)

    col_input, col_display = st.columns([1.1, 1])

    with col_input:
        st.markdown('<p style="font-size: 11px; font-weight: 900; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.8rem;">Select Your Professional Stack</p>', unsafe_allow_html=True)
        
        # 分類展示 (選填：這裡使用 multiselect 即可，或是可以分三個 multiselect)
        user_skills = st.multiselect(
            "Search skills (e.g., Python, Figma, Cantonese)",
            options=ALL_SKILLS_FLAT,
            default=["Python (Data Science)", "Critical Thinking", "Cantonese (Native)"],
            label_visibility="collapsed"
        )

    with col_display:
        st.markdown('<p style="font-size: 11px; font-weight: 900; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.8rem;">Matching Career Paths</p>', unsafe_allow_html=True)
        
        if not user_skills:
            st.warning("Please add skills to view matches.")
        else:
            # 計算匹配度
            results = []
            for job_title, data in JOB_DATABASE.items():
                required = data["skills"]
                # 計算交集
                match_count = len(set(user_skills).intersection(set(required)))
                score = int((match_count / len(required)) * 100)
                
                if score > 0:
                    results.append({"title": job_title, "score": score, "desc": data["desc"]})
            
            # 排序：分數最高排前面
            results = sorted(results, key=lambda x: x["score"], reverse=True)

            for item in results:
                # 根據分數決定顏色
                score_color = "#16a34a" if item["score"] >= 75 else "#2563eb" if item["score"] >= 40 else "#94a3b8"
                
                st.markdown(f'''
                    <div style="background-color: white; padding: 12px; border-radius: 1rem; border: 1px solid #e2e8f0; margin-bottom: 10px; transition: 0.3s;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div style="width: 75%;">
                                <div style="font-size: 13px; font-weight: bold; color: #1e293b;">{item["title"]}</div>
                                <div style="font-size: 10px; color: #64748b; margin-top: 2px;">{item["desc"]}</div>
                            </div>
                            <div style="font-size: 14px; font-weight: 800; color: {score_color};">
                                {item["score"]}%
                            </div>
                        </div>
                        <div style="width: 100%; background-color: #f1f5f9; height: 4px; border-radius: 2px; margin-top: 8px;">
                            <div style="background-color: {score_color}; width: {item["score"]}%; height: 100%; border-radius: 2px;"></div>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)

    st.caption("✨ Matches updated in real-time based on RightPick's 2026 Skills Matrix.")

with col_mid:
    # 3. AI Resume Lab
    # --- 定義職位類別關鍵字與建議課程數據庫 ---
    # 這裡可以根據 RightPick 的定位，加入更多 HK/GBA 相關的關鍵字
    # --- 經過驗證的職位類別與 LinkedIn Learning 連結數據庫 ---
    JOB_DATABASE = {
        "Data Science / AI": {
            "keywords": ["python", "machine learning", "pandas", "sql", "pytorch", "tensorflow", "data visualization", "scikit-learn"],
            "courses": [
                {"skill": "Machine Learning Foundations", "url": "https://www.linkedin.com/learning/search?keywords=Machine+Learning+Foundations&upsellOrderOrigin=default_guest_learning&trk=homepage-learning_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "Data Science Principles", "url": "https://www.linkedin.com/learning/search?keywords=Data+Science+Principles&upsellOrderOrigin=default_guest_learning&trk=learning-serp_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "Generative AI for Professionals", "url": "https://www.linkedin.com/learning/search?keywords=Generative+AI+for+Professionals&upsellOrderOrigin=default_guest_learning&trk=learning-serp_learning-search-bar_search-submit", "platform": "LinkedIn Learning"}
            ]
        },
        "Digital Marketing": {
            "keywords": ["seo", "sem", "google analytics", "content strategy", "social media", "copywriting", "crm", "ads"],
            "courses": [
                {"skill": "Online Marketing Foundations", "url": "https://www.linkedin.com/learning/search?keywords=Online+Marketing+Foundations&upsellOrderOrigin=default_guest_learning&trk=learning-serp_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "Google Analytics 4 (GA4)", "url": "https://www.linkedin.com/learning/search?keywords=Google+Analytics+4+%28GA4%29&upsellOrderOrigin=default_guest_learning&trk=learning-serp_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "SEO Foundations", "url": "https://www.linkedin.com/learning/topics/seo", "platform": "LinkedIn Learning"}
            ]
        },
        "Software Engineering": {
            "keywords": ["react", "node.js", "javascript", "git", "docker", "aws", "api", "restful", "typescript", "cloud"],
            "courses": [
                {"skill": "Full-Stack Web Development", "url": "https://www.linkedin.com/learning/topics/full-stack-web-development", "platform": "LinkedIn Learning"},
                {"skill": "Cloud Computing", "url": "https://www.linkedin.com/learning/search?keywords=Cloud+Computing&upsellOrderOrigin=default_guest_learning&trk=learning-serp_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "DevOps Foundations", "url": "https://www.linkedin.com/learning/topics/devops", "platform": "LinkedIn Learning"}
            ]
        },
        "Finance & Fintech": {
            "keywords": ["wealth management", "risk analysis", "investment", "cfa", "compliance", "excel", "banking", "blockchain"],
            "courses": [
                {"skill": "Financial Analysis Foundations", "url": "https://www.linkedin.com/learning/search?keywords=Financial+Analysis+Foundations&upsellOrderOrigin=default_guest_learning&trk=learning-page-not-found_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "FinTech Foundations", "url": "https://www.linkedin.com/learning/search?keywords=FinTech+Foundations&upsellOrderOrigin=default_guest_learning&trk=learning-serp_learning-search-bar_search-submit", "platform": "LinkedIn Learning"},
                {"skill": "Corporate Finance", "url": "https://www.linkedin.com/learning/topics/corporate-finance", "platform": "LinkedIn Learning"}
            ]
        },
        "UX/UI Design": {
            "keywords": ["figma", "sketch", "adobe xd", "wireframing", "prototyping", "user research", "usability testing"],
            "courses": [
                {"skill": "User Experience (UX) Design", "url": "https://www.linkedin.com/learning/topics/user-experience", "platform": "LinkedIn Learning"},
                {"skill": "Figma for UX Design", "url": "https://www.linkedin.com/learning/search?keywords=Figma+for+UX+Design&upsellOrderOrigin=default_guest_learning&trk=learning-page-not-found_learning-search-bar_search-submit", "platform": "LinkedIn Learning"}
            ]
        }    
    }

    st.markdown("""
        <div style="background-color: white; padding: 2rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                <h3 style="font-weight: bold; font-size: 1.25rem; margin: 0;">🤖 AI Resume Lab & Course Finder</h3>
            </div>
    """, unsafe_allow_html=True)

    # 1. 職位類別選擇
    category = st.selectbox(
        "Step 1: Select Target Job Category | 選擇目標職位類別",
        options=list(JOB_DATABASE.keys()),
        index=0
    )

    # 2. 上傳檔案
    uploaded_cv = st.file_uploader("Step 2: Upload Your CV (PDF)", type=["pdf"], key="cv_analyzer_v3")

    if uploaded_cv:
        with st.spinner("Analyzing CV content..."):
            # 讀取 PDF 內容
            try:
                with pdfplumber.open(uploaded_cv) as pdf:
                    cv_text = "".join([page.extract_text().lower() for page in pdf.pages if page.extract_text()])
                
                # 關鍵字比對邏輯
                target_data = JOB_DATABASE[category]
                found_keywords = [k for k in target_data["keywords"] if k in cv_text]
                missing_keywords = [k for k in target_data["keywords"] if k not in cv_text]
                
                match_rate = int((len(found_keywords) / len(target_data["keywords"])) * 100)

                # 顯示分析結果
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); padding: 1.5rem; border-radius: 1rem; color: white; margin: 1rem 0;">
                    <h4 style="margin:0; font-size: 14px; opacity: 0.8;">{category} Keyword Match Rate</h4>
                    <div style="font-size: 2.5rem; font-weight: 800;">{match_rate}%</div>
                </div>
                """, unsafe_allow_html=True)

                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.markdown("#### ✅ Found Skills")
                    for k in found_keywords:
                        st.markdown(f"<span style='color: #16a34a; font-size: 13px;'>● {k.upper()}</span>", unsafe_allow_html=True)
                
                with res_col2:
                    st.markdown("#### 🔍 Missing Skills")
                    for k in missing_keywords:
                        st.markdown(f"<span style='color: #dc2626; font-size: 13px;'>● {k.upper()}</span>", unsafe_allow_html=True)

                # 3. 課程推薦區塊
                st.markdown("---")
                st.markdown("#### 📚 Recommended Courses to Enrich Your Experience")
                st.info(f"To improve your profile for **{category}**, consider these courses:")
                
                for course in target_data["courses"]:
                    # 邏輯：如果課程對應的技能是用戶缺少的，則顯示推薦（或全部顯示作為參考）
                    st.markdown(f"""
                    <div style="padding: 1rem; background: #f8fafc; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <div style="font-weight: bold; color: #1e293b; font-size: 14px;">{course['skill']}</div>
                            <div style="font-size: 12px; color: #64748b;">{course['platform']}</div>
                        </div>
                        <a href="{course['url']}" target="_blank" style="text-decoration: none; background: #2563eb; color: white; padding: 6px 14px; border-radius: 6px; font-size: 12px; font-weight: bold;">View Course</a>
                    </div>
                    """, unsafe_allow_html=True)
            
            except Exception as e:
                st.error(f"Error processing PDF: {e}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    
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
                            "desc": "Your radiant smile radiates powerful positive energy, perfect for roles requiring charisma and team motivation. This aura boosts productivity by 13% and naturally attracts colleagues. Under pressure, you stay optimistic and spark creative solutions.\n\n你的笑容散發強大正面能量，完美適合需要人際魅力與團隊動力的角色。這種氣場提升13%生產力，讓同事自動被你吸引。在高壓環境中，你能保持樂觀，激發創意解決方案。",
                            "strengths": "**Strengths: Natural Leader Charm, Pressure Transformer, Innovation Catalyst** | 🚀 優勢：天生領袖魅力、壓力轉化器、創新催化劑",
                            "jobs": "**PR Manager, Sales Director, Luxury Hospitality** | 公關經理、销售總監、高端酒店管理"
                        },
                        "neutral": {
                            "title": "Calm Analyst Aura | 冷靜分析師氣場",
                            "desc": "Your calm expression shows professional reliability, ideal for data-driven decision roles. Emotional neutrality enables clear thinking without bias, perfect for crisis handling. Teams trust your objective judgment.\n\n你的平靜表情展現專業可靠，適合數據驅動決策角色。情感中立讓你清晰思考，避免情緒干擾，完美處理危機。團隊信任你的客觀判斷。",
                            "strengths": "**Strengths: Rational Decision-Maker, Crisis Stabilizer, Reliable Executor** | 🚀 優勢：理性決策者、危機穩定器、可靠執行者",
                            "jobs": "**Data Analyst, Researcher, Software Architect** | 數據分析師、研究員、軟件架構師"
                        },
                        "surprise": {
                            "title": "Creative Pioneer Aura | 創意開拓者氣場",
                            "desc": "Your curious, surprised expression signals innovative thinking and rapid adaptability. This aura dominates dynamic markets by spotting overlooked opportunities and leading industry trends.\n\n你的表情充滿好奇與驚喜，代表創新思維與快速適應力。這種氣場在動態市場中無敵，能發現他人忽略機會，引領行業趨勢。",
                            "strengths": "**Strengths: Trend Forecaster, Adaptable Innovator, Opportunity Hunter** | 🚀 優勢：趨勢預測者、靈活變通者、機會獵手",
                            "jobs": "**Creative Director, Event Planner, Marketing Strategist** | 創意總監、活動策劃、市場策略師"
                        },
                        "fear": {
                            "title": "Risk Guardian Aura | 風險守護者氣場",
                            "desc": "Your cautious expression shows high vigilance and risk awareness, perfect for security-critical roles. You foresee potential problems, protecting teams from disasters as the corporate safety net.\n\n謹慎表情顯示高度警覺與風險意識，適合安全關鍵崗位。你能預見潛在問題，保護團隊免於災難，成為企業安全防線。",
                            "strengths": "**Strengths: Prevention Expert, Detail Controller, Safety Defender** | 🚀 優勢：預防專家、細節控管者、安全捍衛者",
                            "jobs": "**Cybersecurity Analyst, Risk Auditor** | 網絡安全分析師、風險審計師"
                        },
                        "angry": {
                            "title": "Justice Enforcer Aura | 正義執行者氣場",
                            "desc": "Your determined expression represents strong principles and execution power, ideal for decisive leadership roles. You never compromise quality and drive tough transformations to achieve the impossible.\n\n堅定表情代表強烈原則與執行力，適合需要決斷的領導角色。你不妥協品質，能推動艱難變革，達成不可能任務。",
                            "strengths": "**Strengths: Principle Defender, Change Driver, Execution Ironman** | 🚀 優勢：原則捍衛者、變革推動者、執行鐵人",
                            "jobs": "**Legal Consultant, Chief Investigator** | 法律顧問、首席調查員"
                        },
                        "sad": {
                            "title": "Deep Empathy Aura | 深度共鳴者氣場",
                            "desc": "Your nuanced expression reveals high empathy and insight, perfect for human-centered careers. You understand others' needs, create emotional connections, and build lasting trust relationships.\n\n細膩表情顯示高同理心與洞察力，適合人文關懷職業。你能理解他人需求，創造情感連結，建立長期信任關係。",
                            "strengths": "**Strengths: Empathetic Listener, Needs Interpreter, Relationship Healer** | 🚀 優勢：同理傾聽者、需求解讀者、關係修復者",
                            "jobs": "**Counselor, Creative Writer, UX Researcher** | 輔導師、創意寫作者、UX研究員"
                        },
                        "disgust": {
                            "title": "Quality Gatekeeper Aura | 品質守門人氣場",
                            "desc": "Your sharp expression represents high standards and zero tolerance for errors, perfect for quality control. You spot issues others miss, ensuring excellence as the final quality checkpoint.\n\n敏銳表情代表高標準與零容忍錯誤，完美品質控制角色。你發現問題他人忽略，確保卓越輸出，成為品質最終防線。",
                            "strengths": "**Strengths: Flaw Hunter, Standards Setter, Quality Enforcer** | 🚀 優勢：瑕疵獵人、標準制定者、品質鐵律",
                            "jobs": "**Quality Manager, Forensic Specialist** | 品質主管、法證專家"
                        }
                    }


                    career_map = {
                        "happy": "Public Relations, Sales Manager, High-end Hospitality",
                        "neutral": "Data Analyst, Researcher, Software Architect",
                        "surprise": "Creative Director, Event Planner, Marketing Strategist",
                        "fear": "Cybersecurity Analyst, Risk Auditor",
                        "angry": "Legal Consultant, Lead Investigator",
                        "sad": "Counselor, Creative Writer, UX Researcher",
                        "disgust": "Quality Controller, Forensic Specialist"
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


