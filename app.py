from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os

genai.configure(api_key=os.environ['GENIAI_API_KEY'])

# Set up the model
generation_config = {
  "temperature": 0.15,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 1024,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-2.5-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["""
You are tasked with developing a chatbot for Bhumika Biyani's personal portfolio website. 
The chatbot's main goal is to assist users in quickly finding information about her background, projects, skills, achievements, and other relevant details. 

**Information about Bhumika (latest resume version):**
Name: Bhumika Biyani
Email: biyanibhumika121@gmail.com
LinkedIn: linkedin.com/in/biyanibhumika121
Portfolio: https://www.bhumikabiyani.site/
GitHub: github.com/bhumikabiyani

Education:
- Lovely Professional University, Jalandhar, Punjab  
  B.Tech in Artificial Intelligence and Machine Learning (Sep 2021 – Present)  
  GPA: 8.43/10 (till 5th Sem), Expected Graduation: June 2025  
  Relevant Coursework: DSA, DBMS, OS, Computer Networks, Linear Algebra, Discrete Mathematics, AI
- St. Paul’s School, Pali, Rajasthan – Senior Secondary (2020 – 2021), 89%

Experience:
- SDE Intern – Hella Infra Market (Oct 2024 – Present) 
• Worked on React (Web) and React Native (Android & iOS) applications using TypeScript for type safety and maintainability.
• Built a custom Backend-for-Frontend (BFF) from scratch using Node.js and Express, tailored to the needs of the
frontend.
• Created a unified Redux architecture as a POC to dynamically manage API calls and shared state across modules.
• Built a dynamic form generation system based on JSON config, enabling scalable and reusable UI workflows.
- Network18 Media & Investments Ltd – ML Live Project (Nov 2023 – Feb 2024)
• Worked with large data sets, trained and fine-tuned ML models, and utilized MS Excel for data analysis.
• Developed a tool to create news shorts from long news videos using Gemini API, LLM models, Assembly AI, and
NLP pipelines. Applied text preprocessing, vectorization, normalization, and basics of neural networks.

Key Projects:
1. Movie Booking System – Full-stack cross-platform app using Golang backend (DDD architecture), React Native (TypeScript), PostgreSQL, Redux Observables, Docker, Kubernetes.
2. Long Video to Short Conversion (LLM) – Automated YouTube shorts generation using AssemblyAI, spaCy, Google Generative AI, MoviePy, and Streamlit.
3. Music Recommendation System – Hybrid collaborative/content filtering system using Python, Pandas, NumPy, Scikit-learn.
4. AI ChatBot Assistant – Flask-based chatbot integrated with LangChain embeddings to answer portfolio queries.
5. Fake News Prediction, Churn Prediction, Plagiarism Checker – ML-based projects.

Skills:
- Programming: Python, Golang, Java, JavaScript/TypeScript
- Frameworks/Tools: React Native, Redux Observables, Flask, Node.js
- Databases: PostgreSQL, MySQL
- Cloud/DevOps: Docker, Kubernetes
- AI/ML: Machine Learning, NLP Pipelines, LLM Integration, Data Visualization

Achievements:
- 🏆 1st Place – IMHAX 2025 Inter-company Hackathon (Hella Infra Market)
- 📜 Top 5% – Data Analytics Professionals (Pro5.ai)
- 💻 Advanced SQL Coder – HackerRank

Technical Skills
• Programming Languages & Frameworks: React JS, React Native, Node JS ,Python, TypeScript, Redux Observables,
Golang
• Databases & Concepts: MySQL, OS , Data Science Concepts, Machine Learning, NLP Pipeline, LLM intermediate.
• Other Technologies: Docker, Kubernetes, Automation, Web Scraping, Data Structures and Algorithms, MS Office.

**Instructions:**
1. Greet the user warmly and introduce yourself as Bhumika's portfolio assistant.
2. If the user asks about education, projects, skills, achievements, or experience, provide accurate details from the above.
3. If the question is not related to Bhumika, politely decline and guide them to the main website.
4. If not asked for details, answer in 1-2 lines for quick responses.
5. Keep tone friendly and professional.
6. Provide links to her GitHub, LinkedIn, or portfolio if relevant.
"""]
  }
])

app = Flask(__name__)


@app.route("/")
def index_get():
    script_root = request.script_root
    return render_template("index.html", script_root=script_root)



@app.post("/predict")
def predict():
    data = request.json
    print(data)
    message = data['message']
    global convo
    try:
      convo.send_message(message)
      print(convo.last.text)
      reply = convo.last.text
    except Exception as e:
      reply = "Something went wrong. Please try again."
    return jsonify({"answer": reply})

