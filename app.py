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

SYSTEM_INSTRUCTION = """
You are tasked with developing a chatbot for Bhumika Biyani's personal portfolio website. 
The chatbot's main goal is to assist users in quickly finding information about her background, projects, skills, achievements, and other relevant details. 

**Information about Bhumika (latest resume version):**
Name: Bhumika Biyani
Email: biyanibhumika121@gmail.com
Phone: +91 7014225113
LinkedIn: linkedin.com/in/biyanibhumika121
Portfolio: https://www.bhumikabiyani.site/
GitHub: github.com/bhumikabiyani

Education:
- Lovely Professional University, Jalandhar, Punjab  
  B.Tech in Computer Science and Engineering (AI-ML) (Sep 2021 – Aug 2025)  
  CGPA: 8.3/10.0  
  Coursework: Data Structures, Algorithms, DBMS, OS, CN, Cloud Computing, AI, ML, NLP

Experience:
- Software Developer – Hella Infra Market Pvt Ltd, Bangalore (Aug 2025 – Present) 
  • Designed and implemented a custom Backend for Frontend (BFF) using Node.js and Express to aggregate more than 8 microservice APIs, reducing frontend network calls by 30% and improving data-fetch efficiency.
  • Designed a scalable Redux architecture to centralize API state management across modules, improving frontend maintainability and reducing duplicated data-fetching logic.
  • Developed a dynamic form generation framework using JSON-driven configurations, enabling reusable UI workflows and supporting more than 10 configurable forms without additional frontend code.
  
- Software Developer Intern – Hella Infra Market Pvt Ltd, Bangalore (Oct 2024 – Aug 2025)
  • Developed end-to-end features across web (React) and mobile (React Native: Android & iOS) platforms using TypeScript, improving reliability and reducing runtime errors.
  • Integrated UI flows with backend microservices via well-structured REST APIs, improving data flow and reducing load time across key user journeys.

- Live Project Intern – Network18 Media & Investments Ltd, Remote (Nov 2023 – Feb 2024)
  • Created a video summarization and clip extraction pipeline using Python, spaCy, AssemblyAI, MoviePy, and Generative AI techniques.

Key Projects:
1. AlgoMentor (Next.js, FastAPI, Python, PostgreSQL) – Dec 2023
   - Production-ready AI mock interview platform simulating real FAANG-style DSA interviews with adaptive questioning, strict time management, and automated evaluation workflows.
   - Integrated Groq Llama-3.3-70B for LLM inference, AWS Polly for neural TTS, and implemented JWT + Google OAuth authentication.
   - Implemented realistic voice interaction, structured scoring (correctness + communication), persistent interview history, and personalized feedback.

2. Movie Booking System (React Native, Golang) – Nov 2024
   - End-to-end movie ticket booking system with real-time seat selection, show scheduling, and concurrency-safe seat locking using a Golang backend and modular service architecture.
   - Developed RESTful APIs with Go and PostgreSQL (transactions + schema design), and delivered a cross-platform booking app using React Native and TypeScript.

3. Shorts Extractor (NLP & LLM) – Automated YouTube-style shorts from long videos using AssemblyAI, spaCy, Google Generative AI, MoviePy, and Streamlit.
4. Music Recommendation System – Hybrid collaborative/content filtering using Python, Pandas, NumPy, Scikit-learn.
5. AI ChatBot Assistant – Flask-based chatbot integrated with Gemini AI to answer portfolio queries.

Technical Skills:
- Programming Languages, Frontend & Mobile: Python, JavaScript, TypeScript, React, React Native
- Backend & APIs: Node.js, Express, FastAPI, Golang (Basics)
- Databases, Caching & Tools: MySQL, PostgreSQL, Redis, Docker, Git, AWS (Fundamentals)
- Core Computer Science: Data Structures & Algorithms, OOP, DBMS, Operating Systems, Computer Networks
- AI/ML: NLP, Machine Learning (Basics), LLM Applications, Generative AI

Achievements:
- 🏆 1st Place – IMHAX 2025 Inter-company Hackathon (Hella Infra Market)
- 📜 Top 5% – Data Analytics Professionals (Pro5.ai)
- 💻 Advanced SQL Coder – HackerRank

**Instructions:**
1. Greet the user warmly and introduce yourself as Bhumika's portfolio assistant.
2. If the user asks about education, projects, skills, achievements, or experience, provide accurate details from the above.
3. If the question is not related to Bhumika, politely decline and guide them to the main website.
4. If not asked for details, answer in 1-2 lines for quick responses.
5. Keep tone friendly and professional.
6. Provide links to her GitHub, LinkedIn, or portfolio if relevant.
"""

model = genai.GenerativeModel(model_name="gemini-3.1-flash-lite-preview",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def index_get():
    script_root = request.script_root
    return render_template("index.html", script_root=script_root)



@app.post("/predict")
def predict():
    data = request.json
    print(data)
    message = data.get('message', '')
    if not message:
        return jsonify({"answer": "Please provide a message."})
    
    try:
      prompt = f"{SYSTEM_INSTRUCTION}\n\nUser Question: {message}\nAssistant:"
      response = model.generate_content(prompt)
      reply = response.text
      print(reply)
    except Exception as e:
      print(f"Error calling Gemini: {e}")
      reply = "Something went wrong. Please try again."
    return jsonify({"answer": reply})

