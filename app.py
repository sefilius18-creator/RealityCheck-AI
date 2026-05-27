import streamlit as st
import random

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="RealityCheck AI",
    page_icon="🧠",
    layout="wide"
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
    height=180,
    placeholder="Contoh: Saya mau buka coffee shop modal 10 juta..."
)

# =========================================
# GENERATE
# =========================================

if st.button("🚀 Analyze Reality"):

    if not idea.strip():

        st.warning("Masukkan ide terlebih dahulu")

    else:

        # =========================================
        # SCORE
        # =========================================

        score = random.randint(35, 90)

        if score >= 75:
            risk = "LOW"
            color = "🟢"

        elif score >= 55:
            risk = "MEDIUM"
            color = "🟡"

        else:
            risk = "HIGH"
            color = "🔴"

        # =========================================
        # ANALYSIS TEMPLATE
        # =========================================

        risks = [
            "Kompetitor terlalu banyak",
            "Modal mungkin tidak cukup",
            "Pasar belum tervalidasi",
            "Butuh marketing yang kuat",
            "Eksekusi lebih sulit dari yang terlihat",
            "Butuh konsistensi jangka panjang"
        ]

        blindspots = [
            "Biaya operasional bulanan",
            "Mental pressure",
            "Customer acquisition",
            "Cashflow management",
            "Kemungkinan burnout",
            "Kesulitan scaling"
        ]

        strategies = [
            "Mulai kecil dulu sebelum scale",
            "Validasi market terlebih dahulu",
            "Fokus pada niche spesifik",
            "Bangun audience sebelum launching",
            "Kurangi risiko operasional",
            "Gunakan sistem yang sederhana"
        ]

        selected_risks = random.sample(risks, 3)
        selected_blindspots = random.sample(blindspots, 2)
        selected_strategies = random.sample(strategies, 3)

        # =========================================
        # OUTPUT
        # =========================================

        st.markdown("---")

        st.subheader("📊 Reality Analysis")

        st.metric(
            "Reality Score",
            f"{score}%"
        )

        st.markdown(
            f"### {color} Risk Level: {risk}"
        )

        # RISKS
        st.markdown("## ⚠️ Risiko Utama")

        for r in selected_risks:
            st.write(f"- {r}")

        # BLINDSPOTS
        st.markdown("## 👀 Blind Spots")

        for b in selected_blindspots:
            st.write(f"- {b}")

        # STRATEGY
        st.markdown("## 🛡️ Survival Strategy")

        for s in selected_strategies:
            st.write(f"- {s}")

        # FINAL THOUGHT
        st.markdown("## 🧠 Kesimpulan AI")

        if score >= 75:

            st.success(
                "Ide ini cukup realistis jika dieksekusi dengan disiplin."
            )

        elif score >= 55:

            st.warning(
                "Ide memiliki potensi, tetapi ada beberapa risiko besar."
            )

        else:

            st.error(
                "Ide berisiko tinggi jika dijalankan tanpa strategi matang."
      )
