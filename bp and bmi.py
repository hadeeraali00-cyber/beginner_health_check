import altair as alt
import pandas as pd
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

# beginner health check: blood pressure and BMI
# MY OWN HEALTH MINI PROJECT:for eduaction only
# run with: pip install streamlit then streamlit run python_beginner_health_check.py

import streamlit as st

st.title("beginner health check")
st.write("this is a learning project")

# 1. get inputs from users
weight=st.number_input("weight(kg)", min_value=30.0,max_value=250.0,value=70.0)
height_cm=st.number_input("height(cm)",min_value=100.0,max_value=220.0,value=170.0)
systolic=st.number_input("Top blood pressure number(systolic)",min_value=70,max_value=250,value=120)
diastolic=st.number_input("Bottom blood pressure(diastolic)",min_value=40,max_value=150,value=80)

# 2. get BMI weight(kg) divided by height(m) squared
height_m=height_cm/100
bmi=weight/ (height_m*height_m)

if  bmi < 18.5:
    bmi_group="underweight"
elif bmi < 25:
     bmi_group="normal weight"
elif bmi < 30.0:
     bmi_group="overweight"
else:
    bmi_group="obesity range"

# 3. sort blood pressure into groups (2020 ACC/AHA)
if systolic > 180 or diastolic > 120:
   bp_group="very high: seek immediate medical advice"
elif systolic >= 130-139 or diastolic >= 80-89:
    bp_group="stage 1 hypertension"
elif systolic >= 140 or diastolic >= 90:
    bp_group="stage 2 hypertension"
elif systolic >=120-130 or diastolic >=80-90:
    bp_group="elevated"
else:
    bp_group="normal"

# 3. show the results
st.subheader("your results")
st.write(f"bmi:{bmi:.1f} ({bmi_group})")
st.write(f"blood pressure:{systolic}/{diastolic} ({bp_group})")
st.caption("One reading is not enough. A doctor decides what your number means.")


    







