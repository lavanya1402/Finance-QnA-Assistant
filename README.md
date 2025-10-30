```markdown
# 💹 Finance Q&A Assistant — Education, not Advice (2025)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange)

🌐 **Live Demo:** [https://finance-qna-assistant.streamlit.app](https://finance-qna-assistant.streamlit.app)

A conversational AI application that helps users **learn financial concepts responsibly** using **Groq’s high-speed LLM inference** and **Streamlit’s interactive UI**.  
The assistant explains macroeconomics, investing basics, budgeting, portfolio risk, and fraud awareness — but **never provides financial, investment, or tax advice**.

---

## 🚀 Overview

**Finance Q&A Assistant** is an interactive educational chatbot built on top of:

- **Groq LLM (Llama 3.3 70B Versatile)** — ultra-fast, high-quality financial explanations  
- **LangChain** — message orchestration and context management  
- **Streamlit** — clean, chat-style educational interface  

The goal is to make **financial literacy accessible**, transparent, and safe through guided education.

---

## 🧠 Key Features

✅ Real-time Q&A on markets, investing, and personal finance  
✅ Mode-based context selection for focused learning  
✅ Ethical safeguards — no investment or prediction responses  
✅ “Market Notes” panel for user-provided financial context (CPI, Fed, earnings, etc.)  
✅ Context-aware conversation memory  
✅ Groq-powered low-latency responses  
✅ Deployable instantly on Streamlit Cloud  

---

## 🧩 Architecture

```

User Input (Streamlit Chat)
│
▼
LangChain Message Pipeline
(System + Human + AI Messages)
│
▼
Groq API (Llama-3.3-70B-Versatile)
│
▼
Educational Response Generation (filtered, safe, and contextual)

````

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **LLM Backend** | Groq API (Llama-3.3-70B-Versatile) |
| **Framework** | LangChain ≥ 0.3 |
| **Environment** | Python 3.10 + virtual environment |
| **Config** | `.env` for secure API key handling |

---

## 🧾 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/lavanya1402/Finance-QnA-Assistant.git
cd Finance-QnA-Assistant
````

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # on Windows
# or source .venv/bin/activate  # on Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Groq API key

Create a `.env` file:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🗂️ Learning Modes

| Mode                          | Description                                                |
| ----------------------------- | ---------------------------------------------------------- |
| **Markets & Macro**           | Inflation, interest rates, GDP, employment, yield curves   |
| **Investing 101**             | Stocks, bonds, ETFs, diversification, compounding          |
| **Risk & Portfolio Concepts** | Volatility, correlation, Sharpe ratio, drawdown            |
| **Personal Finance**          | Budgeting, debt, emergency funds, financial goals          |
| **Fraud & Scam Watch (2025)** | Deepfake scams, phishing, fake “guaranteed return” schemes |
| **Crypto Basics**             | Blockchain, wallets, stablecoins, private key safety       |

---

## 💬 Example Prompts

* “How do interest rate changes affect bond prices?”
* “What is diversification and why does it matter?”
* “Explain the 50/30/20 budgeting rule.”
* “What are the most common investment scams in 2025?”
* “Describe the Sharpe ratio in simple terms.”
* “How do stablecoins maintain their value?”

---

## 🧰 Requirements

```
streamlit
python-dotenv
langchain>=0.3.0
langchain-core>=0.3.0
langchain-groq>=0.1.4
tiktoken
```

---

## 🌐 Deployment

The app is optimized for:

* **Streamlit Cloud** – zero setup, live in seconds
* **Docker + Groq API** – enterprise-grade portability
* **Azure / AWS App Service** – scalable hosting for teams

---

## 🧭 Compliance & Ethics

* Educational content only — **no financial, tax, or investment advice**
* Uses system prompts to enforce responsible, factual, and safe answers
* Respects Groq & LangChain model safety standards

---

## 👩‍💻 Author

**Lavanya Srivastava**
💡 AI Developer | Generative AI & Agentic Systems Educator
📧 [lavanaya.srivastava@gmail.com](mailto:lavanaya.srivastava@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/lavanya-srivastava/)

---

© 2025 Lavanya Srivastava. All rights reserved.

```

---


