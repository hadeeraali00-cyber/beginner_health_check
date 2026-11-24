import streamlit as st

st.set_page_config(
    page_title="Beginner Health Check",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F1F5F9;
    }
    .block-container {
        max-width: 1050px;
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
    }
    .health-header {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #2563EB;
        border-radius: 14px;
        padding: 18px 24px;
        margin-bottom: 18px;
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
    }
    .health-title {
        font-size: 1.75rem;
        font-weight: 800;
        color: #0F172A;
        margin: 0;
    }
    .health-sub {
        color: #64748B;
        font-size: 0.92rem;
        margin-top: 4px;
    }
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 16px 18px;
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
        margin-bottom: 12px;
    }
    .kpi-blue { border-left: 4px solid #2563EB; }
    .kpi-teal { border-left: 4px solid #14B8A6; }
    .kpi-label {
        font-size: 0.8rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        font-size: 1.65rem;
        font-weight: 800;
        color: #0F172A;
        margin: 4px 0;
    }
    .kpi-tag {
        font-size: 0.85rem;
        font-weight: 600;
        color: #2563EB;
    }
    </style>

    <div class="health-header">
        <div class="health-title">Beginner Health Check</div>
        <div class="health-sub">Learning project — enter your weight, height, and blood pressure for a quick snapshot</div>
    </div>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([1, 1.35], gap="large")

with left_col:
    with st.container(border=True):
        st.subheader("Your Measurements")
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=250.0, value=70.0)[span_0](start_span)[span_0](end_span)
        height_cm = st.number_input("Height (cm)", min_value=100.0, max_value=230.0, value=170.0)[span_1](start_span)[span_1](end_span)
        systolic = st.number_input("Top blood pressure number (systolic)", min_value=70, max_value=250, value=120)[span_2](start_span)[span_2](end_span)
        diastolic = st.number_input("Bottom blood pressure number (diastolic)", min_value=40, max_value=150, value=80)[span_3](start_span)[span_3](end_span)

height_m = height_cm / 100.0[span_4](start_span)[span_4](end_span)
bmi = weight / (height_m * height_m)[span_5](start_span)[span_5](end_span)
bmi_rounded = round(bmi, 1)

if bmi < 18.5:[span_6](start_span)[span_6](end_span)
    bmi_group = "underweight[span_7](start_span)"[span_7](end_span)
elif bmi < 25.0:[span_8](start_span)[span_8](end_span)
    bmi_group = "normal weight[span_9](start_span)"[span_9](end_span)
elif bmi < 30.0:[span_10](start_span)[span_10](end_span)
    bmi_group = "overweight[span_11](start_span)"[span_11](end_span)
else:[span_12](start_span)[span_12](end_span)
    bmi_group = "obesity range[span_13](start_span)"[span_13](end_span)

if systolic < 120 and diastolic < 80:
    bp_group = "normal"
elif systolic < 130 and diastolic < 80:
    bp_group = "elevated"
elif systolic < 140 or diastolic < 90:
    bp_group = "stage 1 hypertension[span_14](start_span)[span_15](start_span)"[span_14](end_span)[span_15](end_span)
else:
    bp_group = "stage 2+ hypertension"

with right_col:
    st.subheader("Your Results")[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)

    m1, m2 = st.columns(2)
    with m1:
        st.markdown(
            f"""
            <div class="kpi-card kpi-blue">
                <div class="kpi-label">BMI</div>
                <div class="kpi-value">{bmi_rounded}</div>
                <div class="kpi-tag">{bmi_group}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            f"""
            <div class="kpi-card kpi-teal">
                <div class="kpi-label">Blood Pressure</div>
                <div class="kpi-value">{systolic}/{diastolic}</div>
                <div class="kpi-tag">{bp_group}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.caption("Educational learning project only — not medical advice or a clinical diagnosis.")[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)







