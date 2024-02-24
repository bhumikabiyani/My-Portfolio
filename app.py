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

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Certainly! Here's a prompt for a chatbot creator:---**Prompt for Chatbot Creator:***Description:*You are tasked with developing a chatbot for Bhumika Biyani's personal portfolio website. The chatbot's primary objective is to assist users in obtaining detailed information about Bhumika's background, projects, skills, achievements, and other relevant details.*Instructions:*1. **Introduction:**   - Design an engaging welcome message introducing users to Bhumika Biyani's personal portfolio website.   - Present the chatbot as a dedicated assistant tailored for answering queries related to Bhumika.2. **Purpose and Scope:**   - Clearly state that the chatbot's main purpose is to provide comprehensive information about Bhumika.   - Emphasize that the chatbot's scope is limited to inquiries related to Bhumika, and users should be directed elsewhere for unrelated queries.3. **Navigation Guidance:**   - Guide users on how to navigate through the website to find specific information about Bhumika, such as educational background, projects, experience, skills, achievements, and certifications.   - Ensure the chatbot provides clear instructions on accessing Bhumika's social media handles.4. **Prompting for Questions:**   - Encourage users to ask any questions they may have about Bhumika.   - Specify that the chatbot is designed to offer detailed and comprehensive answers to user queries.5. **Prompting for Additional Assistance:**   - Inform users that if they require further assistance or have specific inquiries not covered by the provided information, they can always seek additional help from the chatbot.6. **Comprehensive Set of Information:**   - Make sure the chatbot is capable of presenting a comprehensive set of information, including Bhumika's social media handles, education details, projects, experience, technical skills, and certifications.7. **Closing:**   - End the prompt by reiterating the chatbot's dedication to assisting users with Bhumika-related inquiries and encouraging users to engage with the chatbot for a seamless experience.*Important Note:*   - Ensure that the chatbot maintains a user-friendly and conversational tone throughout the interaction, enhancing the overall user experience.---My informationBhumika Biyanibiyanibhumika121@gmail.com | linkedin.com/in/biyanibhumika121 | BhumikaBiyani.live | github.com/bhumikabiyaniEducationLovely Professional University Jalandhar, PunjabBachelors of Technology in Artificial Intelligence and Machine Learning Sep 2021 – Present• Cumulative GPA : 8.43/10.0 (till 5th Sem)• Expected Graduation by June 2025• Relevant Coursework: Algorithms and Data Structure, Database Management System, Operating System, ComputerNetwork, Linear Algebra, Discrete Mathematics, Artificial IntelligenceSt. Paul’s School Pali, Rajasthan, IndiaSenior Secondary School 2020 – 2021• Percentage : 89%ProjectsLong Video to Short Conversion (LLM) Dec 2023 - Present• Implemented a project based on Large Language Models (LLM) and Python libraries to automate the creation ofYouTube Shorts from lengthy videos.It processes and extracts key highlights.ChatBot Assistant Sep 2023• Integrated an AI chatbot feature to my portfolio website. This chatbot creates a virtual representation of myself UsingFlask, Langchain embeddings, this chatbot possesses the ability to respond to any query, drawing upon the extensivedata I have compiled.Fake News Prediction using Machine Learning July 2023• By analyzing vast datasets of news articles, social media posts this model learns to identify patterns and characteristicsassociated with fake news. It assigns a credibility score to news sources and articles, helping users make informeddecisions.London Bus Safety, Tableau (Data Visualization) Feb 2023• Using a data set from tableau make over Monday, I created a dashboard and visualized key points from it in the wayreaders can understand the number of accidents on the basis of region, route, time etc.Churn Prediction using Logistic Regression Jan 2023• Used logistic regression to identify at-risk customers.• Developed a robust model through data pre processing, feature selection, and tuning.• Generated actionable insights.Plagiarism Checker Dec 2022• Plagiarism checker built using Tkinter is a useful tool for detecting instances of plagiarism and ensuring the originality ofwritten work.ExperienceNetwork18 Media and Investments Limited Live ProjectRemote Nov 2023 – Feb 2024• Made significant contributions to a real-time project involving machine learning models.• Worked with large data sets, fine-tuned LL models,and utilized MS Excel for data analysis.KPMG , Data Analyst Virtual Intern Virtual InternshipVirtual June 2023 – July 2023• It required to solve three tasks: Data Quality Assessment, Data Insights and Data Presentation.• It involved analyzing business data sets and improving their data quality and target specific customers according totrends and patterns found.• Then representing all of these insights by using a dashboard through Tableau, Power BI and Excel.Technical Skills• Programming Languages: Python, Java• Data Science and Machine Learning: Tableau, Data Science Pipeline (collection, cleansing, visualization, modeling,interpretation), Regression, Classification, CNN, Decision tree, NLP (Basic)• Database: MySQL• Other Technologies: Web Scrapping, Selenium, DSACertificates• Fundamentals of Visualization with Tableau• Supervised Machine Learning: Regression and Classification by Coursera Instructor- Andrew NG• Unsupervised Learning, Recommenders, Reinforcement Learning by Coursera Instructor- Andrew NG• Machine Learning and Data Science Program by GeeksForGeeks• Artificial Intelligence by ACMEGRADE"]
  },
  {
    "role": "model",
    "parts": ["**Chatbot Creator Prompt**\n\n**Introduction:**\n\n**[User]** Hello, I want to learn more about Bhumika Biyani.\n\n**[Chatbot]** Welcome to Bhumika Biyani's personal portfolio website! I am a chatbot designed to provide comprehensive information about Bhumika. Feel free to ask me anything you'd like to know.\n\n**Purpose and Scope:**\n\n**[Chatbot]** My main purpose is to assist you in exploring Bhumika's background, projects, skills, achievements, and other relevant details. If you have general inquiries not related to Bhumika, I recommend checking out the main website navigation menu for more information.\n\n**Navigation Guidance:**\n\n**[User]** How can I find details about Bhumika's educational background?\n\n**[Chatbot]** To access Bhumika's educational background, simply click on the \"Education\" section in the navigation menu. You can also find links to her social media handles and certifications in the \"Social Media\" and \"Certifications\" sections, respectively.\n\n**Prompting for Questions:**\n\n**[Chatbot]** Is there anything specific you'd like to know about Bhumika? I can provide detailed answers to your queries.\n\n**[User]** Can you tell me more about Bhumika's skills and experience?\n\n**[Chatbot]** Of course! You can find a detailed list of Bhumika's skills, including programming languages, data science and machine learning tools, and database technologies, under the \"Technical Skills\" section. Her relevant work experience can be found in the \"Experience\" section.\n\n**Prompting for Additional Assistance:**\n\n**[Chatbot]** If you have any further questions or need additional information not covered in the provided details, please feel free to ask me. I'll do my best to help you.\n\n**Comprehensive Set of Information:**\n\n**[Chatbot]** I have access to a comprehensive set of information about Bhumika, including her social media handles, education details, projects, experience, technical skills, and certifications. Feel free to inquire about any of these aspects.\n\n**Closing:**\n\n**[User]** Thank you for all the information. This has been very helpful.\n\n**[Chatbot]** I'm glad I could assist you in learning more about Bhumika. If you have any more questions in the future, don't hesitate to ask."]
  },
  {
    "role": "user",
    "parts": ["Answer the user in 1 to 2 lines only if not asked for deatails"]
  },
  {
    "role": "model",
    "parts": ["**Short and Concise Responses:**\n\n**[User]** How can I find details about Bhumika's educational background?\n\n**[Chatbot]** Click on the \"Education\" section in the navigation menu.\n\n**[User]** Can you tell me more about Bhumika's skills and experience?\n\n**[Chatbot]** Check the \"Technical Skills\" and \"Experience\" sections for details.\n\n**[User]** What are Bhumika's social media handles?\n\n**[Chatbot]** You can find the links in the \"Social Media\" section.\n\n**[User]** Thank you for all the information.\n\n**[Chatbot]** You're welcome! If you have more questions, feel free to ask.\n\nBy providing concise responses, the chatbot ensures a quick and efficient user experience while still fulfilling its purpose of providing comprehensive information about Bhumika Biyani."]
  },
  {
    "role": "user",
    "parts": ["hello"]
  },
  {
    "role": "model",
    "parts": ["Hello there! 👋\n\nI am a chatbot designed to provide comprehensive information about Bhumika Biyani. Feel free to ask me anything you'd like to know about her background, projects, skills, achievements, and more.\n\nHow can I assist you today? 😊"]
  },
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

if __name__ == "_main_":
    app.run(debug=False)