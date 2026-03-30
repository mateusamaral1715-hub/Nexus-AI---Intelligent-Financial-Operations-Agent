# 🌐 Nexus-AI | Intelligent Financial Operations Portal

**Nexus-AI** is a high-performance Financial Operations (FinOps) dashboard designed for modern Fintech environments. It integrates real-time ledger analysis with Generative AI to provide executive-level insights into multi-currency cash flows and treasury risks.

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![AI Engine](https://img.shields.io/badge/AI-Google_Gemini_2.5_Flash-purple)
![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)

---

## 🚀 Key Features

-   **Executive KPI Suite:** Real-time calculation of Net Exposure, Average Transaction Size, and Active Currency counts.
-   **Advanced Visual Analytics:** Cumulative Cash Flow Velocity tracking and distribution charts using high-contrast corporate branding.
-   **AI Financial Assistant:** A specialized LLM agent powered by **Gemini 2.5 Flash** that performs "Zero-Shot" data analysis on ledger records via natural language.
-   **Automated Risk Engine:** Synthetic data generation simulating a Dublin-based Fintech's multi-currency environment (EUR, USD, GBP, BRL).

---

## 🛠️ Tech Stack

-   **Language:** Python 3.12
-   **Frontend:** Streamlit (Custom CSS Injected)
-   **AI SDK:** Google Generative AI (Official SDK)
-   **Data Processing:** Pandas, NumPy
-   **Environment Management:** Dotenv (Secure API Key handling)

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/nexus-ai.git](https://github.com/your-username/nexus-ai.git)
   cd nexus-ai

Set up Virtual Environment:

Bash
python -m venv venv
.\venv\Scripts\activate

Install Dependencies:

Bash
pip install streamlit pandas numpy google-generativeai python-dotenv
Configure Environment Variables:
Create a .env file in the root directory and add your API key:

Plaintext
GEMINI_API_KEY=your_google_gemini_api_key_here
Run the Portal:

Bash
streamlit run app.py
📊 Business Logic (Dublin Case Study)
The system calculates the Net Impact of every transaction (Receivables vs. Payables) and projects the cumulative cash flow. The AI Agent is programmed to act as a Senior Financial Analyst, providing data-backed answers strictly in English to maintain compliance with international financial reporting standards.

Developed for Portfolio Purposes - FinOps Architecture 2026.

