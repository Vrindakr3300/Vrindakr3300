<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00C9A7&height=200&section=header&text=Vrinda%20Kumar&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=38" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6C63FF&center=true&vCenter=true&width=800&lines=Hi%2C+I'm+Vrinda+Kumar+%F0%9F%91%8B;SDE+Intern+%40+InterGlobe+Technologies;Building+with+Python%2C+SQL%2C+and+REST+APIs;GenAI+%7C+Backend+Systems+%7C+Automation" alt="Typing SVG" />
</p>

<p align="center">
  <a href="mailto:vrindakr0504@gmail.com"><img src="https://img.shields.io/badge/EMAIL-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>

<p align="center">📍 Vellore, Tamil Nadu, India</p>

---

## 🧠 About Me

I'm a Computer Science undergraduate at **Vellore Institute of Technology**, currently working as an **SDE Intern at InterGlobe Technologies**, where I build a Python web application that aggregates hotel pricing data across travel platforms for centralized comparison and analysis, alongside backend services for automated reporting and financial workflows.

Previously, at **Dixon Technologies**, I built SQL-driven automation tools and REST APIs that cut manual effort by 95% and improved backend processing efficiency by ~70% in a manufacturing environment.

I enjoy working across backend systems, GenAI applications, and data-driven products — and I contribute to open source when I can.

---

## 💼 Experience

**SDE Intern — InterGlobe Technologies** · *May 2026 – Present* · Gurugram, India
- Developing a Python web app aggregating hotel pricing data from multiple travel platforms via API integrations for centralized comparison
- Building scalable backend services for data processing, Excel report generation, and automated email delivery
- Supporting the ITQ Finance team with financial data management and reporting workflows using Tally

**SDE Intern — Dixon Technologies** · *May 2025 – June 2025* · Noida, India
- Built SQL-driven automation tools and REST API solutions that reduced manual effort by 95%, saving 80+ hours/month
- Improved backend processing efficiency by ~70% through production data pipelines, process automation, and system integrations

---

## 🚀 Featured Projects

### 🗄️ SQL Co-Pilot
An agentic, schema-aware SQL assistant — ask questions in plain English and it retrieves relevant schema, decides what queries to run, executes them, and reports back, with a dedicated safety gate ensuring nothing mutates data without explicit human confirmation. Works across Postgres, MySQL, SQL Server, and SQLite through a single connection layer.

- **Agent loop**: hands the question + retrieved schema to Gemini, which can run queries, observe results/errors, and self-correct across iterations
- **RAG-based schema retrieval**: embeds each table locally (`sentence-transformers`) into a Chroma vector store so only relevant tables are sent to the model
- **Safety gate**: classifies every query as read-only or mutating; mutating queries are dry-run inside a rolled-back transaction and only committed after explicit human confirmation
- **Memory**: sliding-window chat context plus a persisted SQLite audit log of every query attempt

`Python` · `SQLAlchemy` · `Gemini` · `sentence-transformers` · `Chroma` · `sqlparse` · `Typer` · `Rich` · `SQLite`

```bash
git clone https://github.com/Vrindakr3300/sql-copilot.git
cd sql-copilot
poetry install
poetry run sql-copilot setup-demo
poetry run sql-copilot chat
```

---

### 🎙️ Multimodal GenAI Assistant (RAG-based)
Multimodal RAG platform integrating speech, image, and text inputs for context-aware information retrieval, with vector search pipelines built on chunking, embeddings, relevance ranking, and automated information extraction.

`Python` · `LLM APIs` · `Whisper` · `Gemini` · `Vector Search` · `REST APIs`

---

### 🏠 House Price Prediction — ML Backend System
XGBoost-based prediction system delivering real-time house price estimates through REST APIs, with backend workflows for data processing, model inference, validation, and cloud deployment.

`Python` · `XGBoost` · `Flask` · `REST APIs` · `Render`

---

### 💧 Hydration Essentials — Vision AI Backend Service
CNN-based image classification service achieving 92% validation accuracy on 1K+ samples, with REST APIs for real-time inference and monitoring for production deployment.

`Python` · `CNN` · `Flask` · `REST APIs`

---

## 📄 Research

**Predictive Modeling of Readmission Risk** — *ICAICS 2026*
Hospital readmission prediction model using Python, Pandas, NumPy, and XGBoost, with feature engineering and statistical analysis on EHR data, achieving ~70% recall in identifying high-risk patients.

---

## 🌱 Open Source

**ZamSync**
- Designed and implemented a CLI setup command (`zamsync setup --hub`) to automate distributed system initialization, consolidating multi-step deployment into a single workflow
- Integrated key generation, systemd service configuration, and deployment verification with safeguards against key overwrite, customizable bind support, and unit testing

---

## 🛠️ Tech Stack

**Languages**
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**Frameworks & Tools**
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

**CS Fundamentals & Practices**
`Data Structures & Algorithms` · `OOP` · `DBMS` · `Operating Systems` · `API Integration` · `Backend Development` · `Debugging` · `Agile Development` · `System Design` · `Data Analytics`

---

## 🏆 Certifications

| | Certification | Issuer | Date |
|---|---|---|---|
| ☁️ | Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate | Oracle | Sep 2025 |
| 🤖 | Artificial Intelligence using Google TensorFlow | — | Jun 2024 – Jul 2024 |

---

## 🎓 Education

**Vellore Institute of Technology**, Vellore, India
B.Tech in Computer Science — CGPA 7.73 (July 2022 – Present)

**Lotus Valley International School**, Noida, India
Class X & XII — 87% each (2020, 2022)

---

<p align="center">
  <a href="mailto:vrindakr0504@gmail.com">
    <img src="https://img.shields.io/badge/vrindakr0504%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
</p>

<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00C9A7,100:6C63FF&height=120&section=footer" />
</p>
