
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Round-Up & Rise: Student Micro-Investing Demo")

# --- User Inputs ---
st.sidebar.header("Student Profile")
age = st.sidebar.slider("Age", 18, 30, 21)
monthly_income = st.sidebar.number_input("Monthly Income (€)", min_value=100, value=800)
entertainment = st.sidebar.number_input("Monthly Entertainment Spend (€)", min_value=0, value=50)
payment_method = st.sidebar.selectbox("Preferred Payment Method", ["Credit/Debit Card", "Mobile Payment App", "Cash"])

# --- Risk Score Function ---
def assign_risk_score(age, income, entertainment, method):
    score = 0
    score += 3 if income > 1200 else 2 if income > 700 else 1
    score += 3 if age <= 20 else 2 if age <= 23 else 1
    score += 3 if entertainment > 100 else 2 if entertainment > 50 else 1
    score += 3 if method == "Mobile Payment App" else 2 if method == "Credit/Debit Card" else 1
    return score

# --- Map Risk Score to Risk Profile ---
score = assign_risk_score(age, monthly_income, entertainment, payment_method)

if score <= 6:
    risk_profile = "Low"
    expected_return = 0.06
elif score <= 9:
    risk_profile = "Medium"
    expected_return = 0.12
else:
    risk_profile = "High"
    expected_return = 0.16

st.subheader(f"🧠 Your Risk Profile: {risk_profile}")
st.caption(f"Risk Score: {score} | Expected Annual Return: {expected_return*100:.0f}%")

# --- Estimate Monthly Round-Ups ---
avg_txn = entertainment / 10 if entertainment > 0 else 5
estimated_txns = (avg_txn if avg_txn > 0 else 10)
monthly_roundups = estimated_txns * 0.30
st.markdown(f"💰 Estimated Monthly Investment from Spare Change: **€{monthly_roundups:.2f}**")

# --- Simulate Portfolio Growth ---
months = 24
balance = []
current = 0
for i in range(months):
    current = (current + monthly_roundups) * (1 + expected_return / 12)
    balance.append(current)

# --- Plot Growth ---
st.subheader("📈 Projected Portfolio Growth")
fig, ax = plt.subplots()
ax.plot(range(1, months+1), balance)
ax.set_xlabel("Month")
ax.set_ylabel("Portfolio Value (€)")
ax.set_title("24-Month Growth Projection")
st.pyplot(fig)
