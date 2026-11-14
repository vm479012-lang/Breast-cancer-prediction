
import os
import joblib
import pandas as pd
import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="OncoDetect AI",
    page_icon="🎗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CUSTOM CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --background: #07110f;
    --surface: #0d1c18;
    --surface2: #11251f;
    --border: #244538;
    --green: #00d6a0;
    --green2: #00a982;
    --white: #f1faf6;
    --muted: #91aaa1;
}

/* Main page */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: var(--background);
    color: var(--white);
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

.block-container {
    max-width: 1500px;
    padding: 1.5rem 2rem 2rem;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #091713;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
}

[data-testid="stSidebar"] * {
    color: var(--white);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: var(--muted);
}

/* Hero */

.hero {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(
            ellipse at 85% 10%,
            rgba(0,214,160,.22),
            transparent 40%
        ),
        linear-gradient(120deg, #0b1b17, #103b30);

    border: 1px solid #245b48;
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 24px;
    box-shadow: 0 12px 35px rgba(0,0,0,.20);
}

.hero-tag {
    display: inline-block;
    background: rgba(0,214,160,.10);
    border: 1px solid rgba(0,214,160,.35);
    color: #00e4a8;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.2px;
}

.hero h1 {
    color: white;
    font-size: clamp(28px, 4vw, 43px);
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 17px 0 10px;
}

.hero p {
    color: #b4d1c5;
    font-size: 14px;
    line-height: 1.8;
    margin: 4px 0;
}

.hero-bottom {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.hero-pill {
    color: #b6ead5;
    background: rgba(0,0,0,.20);
    border: 1px solid rgba(139,226,190,.22);
    padding: 8px 13px;
    border-radius: 8px;
    font-size: 11px;
}

/* Sidebar custom HTML */

.brand {
    font-size: 23px;
    font-weight: 800;
    color: white;
    letter-spacing: -1px;
}

.brand span {
    color: var(--green);
}

.brand-caption {
    font-size: 9px;
    color: var(--green);
    letter-spacing: 2px;
    font-weight: 700;
    margin-top: 8px;
}

.side-heading {
    color: white;
    font-size: 13px;
    font-weight: 700;
    margin: 20px 0 12px;
}

.side-link {
    background: #10241d;
    border: 1px solid #1a382d;
    border-radius: 9px;
    padding: 12px;
    margin: 9px 0;
    color: #d8ebe2;
    font-size: 12px;
}

.side-link.active {
    background: #12382b;
    border-color: #087f5c;
    color: #00e0a5;
}

.side-note {
    background: #10221c;
    border: 1px solid #1d3b32;
    border-radius: 12px;
    padding: 15px;
    color: #b6cfc3;
    font-size: 11px;
    line-height: 1.9;
}

/* Section headings */

.section-heading {
    color: #f4fff9;
    font-size: 20px;
    font-weight: 700;
    margin: 20px 0 5px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 16px;
}

/* Overview cards */

.stat-card {
    background: linear-gradient(145deg, #11251f, #0b1915);
    border: 1px solid #214438;
    border-radius: 15px;
    padding: 20px;
    min-height: 140px;
    box-shadow: 0 7px 20px rgba(0,0,0,.13);
    transition: .2s ease;
}

.stat-card:hover {
    border-color: #00a982;
    transform: translateY(-2px);
}

.stat-icon {
    font-size: 21px;
    margin-bottom: 13px;
}

.stat-label {
    color: #94afa3;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
}

.stat-value {
    color: #00dfaa;
    font-size: 21px;
    font-weight: 800;
    margin-top: 7px;
}

.stat-description {
    color: #819d90;
    font-size: 10px;
    margin-top: 6px;
}

/* Measurement expanders */

[data-testid="stExpander"] {
    background: #0d1c18 !important;
    border: 1px solid #244538 !important;
    border-radius: 13px !important;
    margin-bottom: 13px;
    overflow: hidden;
}

[data-testid="stExpander"] details {
    background: #0d1c18 !important;
}

[data-testid="stExpander"] details > summary {
    background: #11251f !important;
    color: #f1faf6 !important;
    border-radius: 12px !important;
    padding: 13px !important;
}

[data-testid="stExpander"] details > summary:hover {
    background: #17372b !important;
}

[data-testid="stExpander"] details > summary p {
    color: #e7f4f3 !important;
    font-weight: 700 !important;
}

[data-testid="stExpander"] details[open] > summary {
    background: #11251f !important;
    color: #00d6a0 !important;
}

/* Measurement labels */

[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    color: #c4ddd1 !important;
    font-size: 11px !important;
}

/* Number inputs */

[data-testid="stNumberInput"] input {
    background: #10231d !important;
    color: white !important;
    border: 1px solid #315548 !important;
    border-radius: 8px !important;
}

[data-testid="stNumberInput"] button {
    background: #17372b !important;
    color: #00e0a5 !important;
    border-color: #315548 !important;
}

/* Analyze button */

.stFormSubmitButton > button {
    background: linear-gradient(100deg, #00b98b, #00d6a0) !important;
    color: #04130d !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 800 !important;
    min-height: 49px;
    box-shadow: 0 5px 18px rgba(0,214,160,.15);
}

.stFormSubmitButton > button:hover {
    background: #32efb6 !important;
    color: #04130d !important;
    box-shadow: 0 0 20px rgba(0,214,160,.25);
}

/* Prediction banner */

.result-banner {
    border-radius: 14px;
    padding: 20px;
    font-size: 19px;
    font-weight: 800;
    margin: 12px 0 18px;
}

.benign {
    background: #0d3024;
    border: 1px solid #147c57;
    color: #38e6ad;
}

.malignant {
    background: #321a1a;
    border: 1px solid #a64747;
    color: #ff8989;
}

/* Probability cards */

.probability-card {
    background: linear-gradient(145deg, #11251f, #0c1915);
    border: 1px solid #214438;
    border-radius: 15px;
    padding: 24px;
    text-align: center;
    min-height: 125px;
}

.probability-label {
    color: #9ab5a8;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .5px;
}

.probability-value {
    color: #00e0a5;
    font-size: 34px;
    font-weight: 800;
    margin-top: 9px;
}

.probability-value.red {
    color: #ff8585;
}

/* Disclaimer */

.disclaimer {
    background: #292315;
    border: 1px solid #66552b;
    border-radius: 11px;
    padding: 16px;
    color: #e8d59b;
    font-size: 11px;
    line-height: 1.8;
    margin-top: 18px;
}

/* Footer */

.footer {
    border-top: 1px solid #1d382e;
    margin-top: 30px;
    padding: 22px 0 5px;
    text-align: center;
    color: #78958a;
    font-size: 11px;
    line-height: 1.8;
}

/* Charts */

[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"] {
    background: #0d1c18;
    border: 1px solid #244538;
    border-radius: 13px;
    padding: 12px;
}

/* Alerts */

.stAlert {
    border-radius: 10px;
}

/* Responsive */

@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 23px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .stat-card {
        padding: 14px;
        min-height: 120px;
    }

    .stat-value {
        font-size: 17px;
    }

    .probability-value {
        font-size: 27px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD TRAINED MODEL
# =========================================================

MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "models",
        "best_breast_cancer_model.joblib"
    )
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    bundle = load_model()
    model = bundle["model"]
    feature_names = bundle["feature_names"]

except Exception as error:
    st.error(f"Unable to load trained model: {error}")
    st.stop()


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    st.html("""
    <div class="brand">🎗️ OncoDetect <span>AI</span></div>
    <div class="brand-caption">
        INTELLIGENT HEALTHCARE ANALYTICS
    </div>
    """)

    st.markdown("---")

    st.html("""
    <div class="side-heading">PLATFORM</div>

    <div class="side-link active">
        ⌂ &nbsp; Prediction Dashboard
    </div>

    <div class="side-link">
        ◈ &nbsp; Logistic Regression Model
    </div>

    <div class="side-link">
        ▦ &nbsp; 30 Diagnostic Features
    </div>
    """)

    st.markdown("---")

    st.html("""
    <div class="side-heading">HOW IT WORKS</div>

    <div class="side-note">
        <b>01</b> &nbsp; Enter measurement values<br><br>
        <b>02</b> &nbsp; Analyze with the ML model<br><br>
        <b>03</b> &nbsp; View prediction results<br><br>
        <b>04</b> &nbsp; Review the disclaimer
    </div>
    """)

    st.markdown("---")

    st.caption("PROJECT INFORMATION")
    st.markdown("**CODE-A-NOVA**")
    st.caption("ML Developer Internship")
    st.caption("Wisconsin Diagnostic Dataset")


# =========================================================
# 5. HERO SECTION
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-tag">
        ● &nbsp; AI-POWERED HEALTHCARE ANALYTICS
    </div>

    <h1>Smarter Analysis.<br>Better Insights.</h1>

    <p>
        Welcome to OncoDetect AI — a machine learning
        demonstration for breast cancer classification.
    </p>

    <p>
        Explore diagnostic measurements and model predictions
        using the Wisconsin Diagnostic Breast Cancer dataset.
    </p>

    <div class="hero-bottom">
        <span class="hero-pill">✦ Machine Learning</span>
        <span class="hero-pill">◈ 30 Features</span>
        <span class="hero-pill">✓ Model Evaluation</span>
    </div>

</div>
""")


# =========================================================
# 6. OVERVIEW
# =========================================================

st.markdown("### Platform Overview")
st.caption("Your model and analysis at a glance.")

stat_columns = st.columns(3, gap="small")

stats = [
    (
        "🧠",
        "MACHINE LEARNING MODEL",
        "Logistic Regression",
        "Hyperparameter-tuned pipeline"
    ),
    (
        "◈",
        "INPUT FEATURES",
        "30 Measurements",
        "Diagnostic characteristics"
    ),
    (
        "📈",
        "MODEL TEST ACCURACY",
        "97.37%",
        "Held-out test dataset"
    )
]

for column, (icon, label, value, description) in zip(
    stat_columns, stats
):

    with column:

        st.html(f"""
        <div class="stat-card">

            <div class="stat-icon">{icon}</div>

            <div class="stat-label">{label}</div>

            <div class="stat-value">{value}</div>

            <div class="stat-description">{description}</div>

        </div>
        """)


# =========================================================
# 7. FEATURE GROUPING
# =========================================================

groups = {
    "Mean Measurements": [
        f for f in feature_names
        if f.startswith("mean ")
    ],

    "Standard Error Measurements": [
        f for f in feature_names
        if f.endswith("error")
    ],

    "Worst Measurements": [
        f for f in feature_names
        if f.startswith("worst ")
    ]
}

assigned_features = {
    feature
    for group in groups.values()
    for feature in group
}

remaining_features = [
    f for f in feature_names
    if f not in assigned_features
]

if remaining_features:
    groups["Other Measurements"] = remaining_features


# =========================================================
# 8. INPUT SECTION
# =========================================================

st.markdown("### Diagnostic Analysis")

st.caption(
    "Enter all 30 diagnostic measurements in their respective categories."
)

values = {}

with st.form("prediction_form"):

    for group_name, features in groups.items():

        with st.expander(
            f"▦  {group_name}  ·  {len(features)} features",
            expanded=True
        ):

            columns = st.columns(3, gap="medium")

            for index, feature in enumerate(features):

                with columns[index % 3]:

                    values[feature] = st.number_input(
                        feature,
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f",
                        key=f"measurement_{feature}"
                    )

    st.markdown("---")

    submitted = st.form_submit_button(
        "✦  ANALYZE MEASUREMENTS",
        use_container_width=True
    )


# =========================================================
# 9. PREDICTION ENGINE
# =========================================================

if submitted:

    invalid_features = [
        feature
        for feature in feature_names
        if values[feature] <= 0
    ]

    if invalid_features:

        st.warning(
            f"Please enter positive values for all 30 features. "
            f"{len(invalid_features)} feature(s) still need values."
        )

    else:

        # Prepare model input in the original feature order

        input_df = pd.DataFrame(
            [[values[name] for name in feature_names]],
            columns=feature_names
        )

        # Predict

        prediction = model.predict(input_df)[0]

        probabilities = model.predict_proba(input_df)[0]

        class_probabilities = dict(
            zip(model.classes_, probabilities)
        )

        malignant_probability = (
            class_probabilities[1] * 100
        )

        benign_probability = (
            class_probabilities[0] * 100
        )

        # =================================================
        # RESULT HEADER
        # =================================================

        st.markdown("---")
        st.markdown("### Prediction Analysis Results")

        st.caption(
            "Output generated by your trained Logistic Regression model."
        )

        # =================================================
        # PREDICTION BANNER
        # =================================================

        if prediction == 1:

            st.html("""
            <div class="result-banner malignant">
                ⚠ &nbsp; Model Prediction: Malignant
            </div>
            """)

        else:

            st.html("""
            <div class="result-banner benign">
                ✓ &nbsp; Model Prediction: Benign
            </div>
            """)

        # =================================================
        # PROBABILITY CARDS
        # =================================================

        probability_columns = st.columns(2, gap="medium")

        with probability_columns[0]:

            st.html(f"""
            <div class="probability-card">

                <div class="probability-label">
                    MALIGNANT PROBABILITY
                </div>

                <div class="probability-value red">
                    {malignant_probability:.2f}%
                </div>

            </div>
            """)

        with probability_columns[1]:

            st.html(f"""
            <div class="probability-card">

                <div class="probability-label">
                    BENIGN PROBABILITY
                </div>

                <div class="probability-value">
                    {benign_probability:.2f}%
                </div>

            </div>
            """)

        # =================================================
        # PROBABILITY CHART
        # =================================================

        st.markdown("### Probability Distribution")

        chart_df = pd.DataFrame(
            {
                "Class": ["Malignant", "Benign"],
                "Probability (%)": [
                    malignant_probability,
                    benign_probability
                ]
            }
        ).set_index("Class")

        st.bar_chart(
            chart_df,
            horizontal=True
        )

        # =================================================
        # DISCLAIMER
        # =================================================

        st.html("""
        <div class="disclaimer">

            <b>⚕ Medical Disclaimer</b><br>

            This application is an educational machine learning
            demonstration, not a medical diagnostic tool.

            Its predictions and probabilities are not clinically
            validated and must not be used for medical decisions.

            Always consult a qualified healthcare professional.

        </div>
        """)


# =========================================================
# 10. FOOTER
# =========================================================

st.html("""
<div class="footer">

    <b>🎗️ OncoDetect AI</b><br>

    Intelligent Healthcare Analytics<br>

    Built with Python · Pandas · Scikit-learn · Streamlit<br>

    CODE-A-NOVA | ML Developer Internship

</div>
""")
