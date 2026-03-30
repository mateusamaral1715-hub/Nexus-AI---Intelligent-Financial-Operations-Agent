import streamlit as st
import pandas as pd
import numpy as np
import os
import google.generativeai as genai
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

# ==========================================
# UI CONFIGURATION & CSS INJECTION (Dublin Standard)
# ==========================================
st.set_page_config(page_title="Nexus-AI | Intelligent Financial Operations", layout="wide", page_icon="🌐")

# Inject Custom CSS for Branding
st.markdown("""
    <style>
        /* Color Palette & Global Styles */
        :root {
            --primary-blue: #0A2540; /* Trust */
            --ai-purple: #635BFF;   /* Innovation */
            --success-green: #00D924;
            --danger-red: #FF4B4B;
            --bg-white: #FFFFFF;
        }

        /* Customize Main Background */
        .stApp {
            background-color: #F6F9FC;
        }

        /* Top Header Area */
        .main-header {
            font-size: 36px;
            font-weight: 800;
            color: var(--primary-blue);
            margin-bottom: 5px;
        }
        .sub-header {
            font-size: 18px;
            color: #425466;
            margin-bottom: 30px;
        }

        /* KPI Card Styling */
        .metric-card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border-left: 5px solid #E6EBF1;
        }
        .metric-card.positive {
            border-left: 5px solid var(--success-green);
        }
        .metric-card.negative {
            border-left: 5px solid var(--danger-red);
        }
        .metric-label {
            font-size: 14px;
            color: #697386;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .metric-value {
            font-size: 28px;
            font-weight: 700;
            color: var(--primary-blue);
        }

        /* AI Chat Customization */
        .stChatInputContainer {
            border-top: 1px solid #E6EBF1;
        }
        div[data-testid="stChatMessage"] {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title Section (Custom HTML/CSS)
st.markdown("""
    <div class="main-header">🌐 Nexus-AI Portal</div>
    <div class="sub-header">Intelligent Ledger Analysis & Financial Operations Agent</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# PHASE 1: DATA ENGINE (FinTech Case Study)
# ==========================================
@st.cache_data
def generate_ledger_data(records=200): # Increased records for better portfolio view
    """Generates synthetic multi-currency transactions."""
    np.random.seed(42)
    data = {
        'Date': [(datetime.today() - timedelta(days=np.random.randint(0, 90))).strftime('%Y-%m-%d') for _ in range(records)],
        'Amount': np.random.uniform(5000, 150000, records).round(2),
        'Currency': np.random.choice(['EUR', 'USD', 'GBP', 'BRL'], records),
        'Type': np.random.choice(['Receivable', 'Payable'], records),
        'Status': np.random.choice(['Settled', 'Pending'], records)
    }
    df = pd.DataFrame(data)
    df['Net_Impact'] = df.apply(lambda x: x['Amount'] if x['Type'] == 'Receivable' else -x['Amount'], axis=1)
    return df

df_ledger = generate_ledger_data()

# ==========================================
# PHASE 2: EXECUTIVE DASHBOARD (KPI Cards + Charts)
# ==========================================
st.subheader("📊 Global Treasury Overview")

# Calculate Key KPIs (Assuming EUR as Base for display purposes)
# In a real app, we would use real-time FX conversion rates.
total_receivables = df_ledger[df_ledger['Type'] == 'Receivable']['Amount'].sum()
total_payables = df_ledger[df_ledger['Type'] == 'Payable']['Amount'].sum()
net_position = total_receivables - total_payables
avg_txn_size = df_ledger['Amount'].mean()

# Display KPIs using Custom CSS Cards
col1, col2, col3, col4 = st.columns(4)

# KPI 1: Total Volume
col1.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Volume (Raw Sum)</div>
        <div class="metric-value">{ (total_receivables + total_payables) / 1000000:.1f}M</div>
    </div>
""", unsafe_allow_html=True)

# KPI 2: Avg Transaction Size
col2.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Average Transaction</div>
        <div class="metric-value">{avg_txn_size/1000:.1f}k</div>
    </div>
""", unsafe_allow_html=True)

# KPI 3: Net Position
net_css_class = "positive" if net_position >= 0 else "negative"
col3.markdown(f"""
    <div class="metric-card {net_css_class}">
        <div class="metric-label">Net Position (Receivables - Payables)</div>
        <div class="metric-value">{net_position / 1000000:.1f}M</div>
    </div>
""", unsafe_allow_html=True)

# KPI 4: Active Currencies
col4.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Active Currencies</div>
        <div class="metric-value">{len(df_ledger['Currency'].unique())}</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts Section
col_a, col_b = st.columns([1, 2]) # Adjusted ratio for better chart balance

with col_a:
    st.write("**Transaction Distribution by Currency**")
    # Custom color bar chart
    st.bar_chart(df_ledger['Currency'].value_counts())

with col_b:
    st.write("**Cumulative Cash Flow Velocity (Net Impact Time Series)**")
    chart_df = df_ledger.copy()
    chart_df['Date'] = pd.to_datetime(chart_df['Date'])
    # Sort and calculate cumulative sum for better velocity view
    chart_df = chart_df.sort_values(by='Date')
    chart_df['Cumulative_Cashflow'] = chart_df['Net_Impact'].cumsum()
    # Deep blue chart color
    st.line_chart(chart_df.set_index('Date')['Cumulative_Cashflow'], color="#0A2540")

st.markdown("---")

# ==========================================
# PHASE 3: AI ANALYTICS (Auto-Detection Engine)
# ==========================================
st.subheader("🤖 FinOps Intelligent Assistant (Gemini 2.5 Flash)")
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    
    # Auto-select the best available Flash model
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    target_model = next((m for m in available_models if 'flash' in m), available_models[0])
    model = genai.GenerativeModel(target_model)
    
    # Display engine status with professional styling
    st.markdown(f"<span style='color: #697386;'>Operational Engine: {target_model.replace('models/', '')}</span>", unsafe_allow_html=True)

    user_input = st.chat_input("Ask about cash flow summaries, currency risks, or specific totals...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.spinner("Nexus-AI is analyzing the global ledger..."):
            try:
                csv_data = df_ledger.to_csv(index=False)
                
                prompt = f"""
                You are a Senior Financial Analyst at a Dublin-based Fintech. 
                Analyze the following synthetic transaction data (CSV format) for trends, risks, and totals:
                
                {csv_data}
                
                User Question: {user_input}
                
                Instructions:
                1. Provide a professional, concise, data-backed answer.
                2. Calculate specific totals if requested.
                3. Use the data provided only.
                4. Always respond strictly in English as per company policy.
                """
                
                response = model.generate_content(prompt)
                
                with st.chat_message("assistant", avatar="🌐"):
                    st.write(response.text)
                    
            except Exception as e:
                st.error(f"Nexus-AI Engine Operational Error: {e}")
else:
    st.warning("Configuration Missing: Please add GEMINI_API_KEY to your .env file.")

# ==========================================
# PROFESSIONAL FOOTER (Dublin Standard)
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #697386; font-size: 14px;'>
        Nexus-AI Ledger Agent - Internal FinOps Tool. Powered by Google Gemini.
    </div>
""", unsafe_allow_html=True)