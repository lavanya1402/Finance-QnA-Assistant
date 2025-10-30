

```markdown
# 💹 Finance Q&A Assistant — Education, not Advice (2025)

A conversational AI application that helps users **learn financial concepts responsibly** using **Groq's high-speed LLM inference** and **Streamlit**.  
This assistant explains macroeconomics, investing basics, budgeting, portfolio risk, and fraud awareness — but **never provides financial advice**.

---

## 🚀 Overview

**Finance Q&A Assistant** is an interactive educational chatbot built on top of:
- **Groq LLM (Llama 3.3 70B Versatile)** — for ultra-fast, accurate financial explanations  
- **LangChain** — for message orchestration and context management  
- **Streamlit** — for a clean, modern chat-based user interface  

The goal is to make **finance literacy accessible**, transparent, and compliant with educational use.

---

## 🧠 Key Features

✅ Real-time Q&A on markets, investing, and personal finance  
✅ Mode-based context selection for specific topics  
✅ Ethical safeguards — no investment or tax recommendations  
✅ “Market Notes” panel to personalize context (CPI, Fed rates, earnings, etc.)  
✅ Context-aware conversation memory  
✅ Groq-powered speed for smooth educational interactions  

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
Educational Response Generation
(Filtered, Contextual, Safe)

````

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **LLM Backend** | Groq API (Llama-3.3-70B-Versatile) |
| **Framework** | LangChain ≥ 0.3 |
| **Environment** | Python 3.10 + virtual env |
| **Config** | `.env` for secure API key storage |

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
# or source .venv/bin/activate  (Mac/Linux)
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

## 🧮 Project Structure

```
Finance-QnA-Assistant/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── .env.example          # Example environment variables
└── README.md             # Project documentation
```

---

## 🗂️ Modes of Learning

| Mode                          | Description                                              |
| ----------------------------- | -------------------------------------------------------- |
| **Markets & Macro**           | Inflation, interest rates, yield curves, GDP, employment |
| **Investing 101**             | Stocks, bonds, ETFs, diversification, compounding        |
| **Risk & Portfolio Concepts** | Volatility, correlation, Sharpe ratio, drawdown          |
| **Personal Finance**          | Budgeting, debt, goals, emergency funds                  |
| **Fraud & Scam Watch (2025)** | Deepfake, phishing, “guaranteed return” scams            |
| **Crypto Basics**             | Blockchain, wallets, stablecoins, private-key safety     |

---

## 🧭 Example Prompts

* “How do interest rate changes affect bond prices?”
* “What is diversification and why does it matter?”
* “Explain the 50/30/20 budgeting rule.”
* “What are the most common scams in 2025?”
* “Describe the Sharpe ratio with a simple example.”
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

You can deploy this application easily on:

* **Streamlit Cloud** → zero-setup hosting
* **Docker + Groq API** → enterprise-grade reproducibility
* **Azure App Service / AWS Elastic Beanstalk** → scalable corporate hosting

---

## 🧭 Compliance & Ethics

* No recommendations, predictions, or investment guidance
* Educational use only
* All outputs filtered through LangChain prompt safety and contextual moderation

---

## 🧑‍💻 Author

**Lavanya Srivastava**
Built with ❤️ using Groq + LangChain + Streamlit
[LinkedIn Profile](https://www.linkedin.com/in/lavanya-srivastava/)

---

```
© 2025 Lavanya Srivastava. All rights reserved.
```

---


