# Heath-Analyst

## Team Name
Vagabond Tinkers

---

## Problem Statement
Preventive healthcare relies on early identification of lifestyle-related health risks. However, lifestyle data such as physical activity, sleep patterns, diet habits, and stress indicators are often underutilized. Manual analysis is not scalable, creating the need for an intelligent, automated preventive health risk assessment system.

---

## Proposed Solution
This project presents an **Agentic AI-Based Preventive Health Risk Assessment System** built using **LangFlow** and **IBM Granite Model**. The system analyzes lifestyle data, identifies preventive health risks using guideline-based references, and provides assistive lifestyle improvement suggestions.

---

## System Architecture
The solution uses a multi-agent architecture consisting of:
- **Lifestyle Data Analysis Agent** – Processes and summarizes lifestyle data  
- **Preventive Risk Detection Agent** – Identifies risk patterns using RAG with preventive healthcare guidelines  
- **Health Advisory Assistant** – Provides assistive, non-diagnostic lifestyle recommendations  

---

## Technology Stack
- LangFlow  
- IBM Granite Model (ibm-granite-3-2-8b-instruct)  
- IBM Watsonx.ai  
- Retrieval-Augmented Generation (RAG)  
- Preventive healthcare and wellness guideline datasets  

---

## LangFlow Components Used
- Chat Input  
- Agent  
- IBM Watsonx AI (Granite Model)  
- Tavily Search API  
- Parser  
- Chat Output  

---

## Project Files
- `app.py` – Application entry point  
- `langflow_project.json` – Exported LangFlow workflow  
- `Project_Presentation.pptx` – Project presentation  
- `AI_Preventive_Health_Risk_Assessment.pdf` – Problem statement  

---

## How to Run the Project
1. Install LangFlow and required dependencies  
2. Load the exported LangFlow workflow (`langflow_project.json`)  
3. Run the application using:
   ```bash
   python app.py
