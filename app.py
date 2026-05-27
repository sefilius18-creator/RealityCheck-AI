import streamlit as st
import google.generativeai as genai

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="RealityCheck AI",
    page_icon="🧠",
    layout="wide"
)

# =========================================
# GEMINI API
# =========================================

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "models/gemini-1.5-flash"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextArea textarea {
    background-color: #1C1F26;
    color: white;
    border-radius: 10px;
}

div[data-testid="stSidebar"] {
    background-color: #111827;
}

.result-box {
    background-color: #1C1F26;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #333;
    margin-top: 20px;
}

.metric-box {
    background-color: #1C1F26;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================

st.title("🧠 RealityCheck AI")

st.caption(
    "AI untuk mengecek apakah ide kamu realistis atau tidak"
)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("⚡ RealityCheck AI")

category = st.sidebar.selectbox(
    "Kategori Ide",
    [
        "Bisnis",
        "Trading",
        "Startup",
        "Content Creator",
        "Freelance",
        "Karir"
    ]
)

# =========================================
# INPUT
# =========================================

st.subheader("💡 Tulis Ide Kamu")

idea = st.text_area(
    "Masukkan ide atau rencana kamu",
    height=200,
    placeholder="Contoh: Saya mau buka coffee shop modal 10 juta..."
)

# =========================================
# BUTTON ANALYZE
# =========================================

if st.button("🚀 Analyze Reality"):

    if not idea.strip():

        st.warning("Masukkan ide terlebih dahulu")

    else:

        with st.spinner("AI sedang menganalisis ide..."):

            prompt = f"""
            Kamu adalah AI strategic advisor yang realistis,
            logis, dan brutal jujur.

            Analisis ide berikut:

            Ide:
            {idea}

            Kategori:
            {category}

            Berikan output dengan format berikut:

            Reality Score: [0-100]
            Risk Level: [LOW/MEDIUM/HIGH]

            Risiko Utama:
            - poin

            Blind Spots:
            - poin

            Survival Strategy:
            - poin

            Kesimpulan:
            - kesimpulan realistis

            Gunakan bahasa Indonesia.
            """

            response = model.generate_content(prompt)

            result = response.text

        # =========================================
        # PARSE SCORE
        # =========================================

        score = 50
        risk = "MEDIUM"
        color = "🟡"

        try:

            lines = result.split("\n")

            for line in lines:

                if "Reality Score" in line:

                    score_text = line.split(":")[1].strip()

                    score = int(
                        ''.join(filter(str.isdigit, score_text))
                    )

                if "Risk Level" in line:

                    risk = line.split(":")[1].strip().upper()

            if risk == "LOW":
                color = "🟢"

            elif risk == "MEDIUM":
                color = "🟡"

            else:
                color = "🔴"

        except:
            pass

        # =========================================
        # RESULT UI
        # =========================================

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Reality Score",
                f"{score}/100"
            )

        with col2:

            st.metric(
                "Risk Level",
                f"{color} {risk}"
            )

        st.markdown("---")

        st.subheader("🧠 AI Reality Analysis")

        st.markdown(
            f"""
            <div class="result-box">
            {result}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.caption("RealityCheck AI © 2026")
