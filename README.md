**🧠 The Lifelong Learning Co-Pilot**

A personalized, multi-agent system that guides individuals through a continuous journey of skill acquisition and career development, supporting SDG 4.4 and 4.3.

**🚀Project Screenshot:**

<img width="1895" height="906" alt="Screenshot 2025-08-08 143942" src="https://github.com/user-attachments/assets/f5bc1069-a0a0-4588-b745-6c9af53180dd" />
<img width="1065" height="590" alt="Screenshot 2025-08-08 144221" src="https://github.com/user-attachments/assets/ba183ee1-b348-48eb-98c5-0234eb4d719d" />
<img width="1072" height="903" alt="Screenshot 2025-08-08 144244" src="https://github.com/user-attachments/assets/916ffe2d-e858-40f5-bcaf-f46c3185da67" />






**🎯 Agent's Core Goal**

To autonomously create, manage, and adapt a personalized lifelong learning path for a user, aligning their skills with current and future job market demands.


**🚀 Key Features**

Dynamic Skill Profiling: Creates a comprehensive profile of a user's current skills and career goals.

Skill Gap Analysis: Analyzes real-time labor market data to identify high-demand skills.

Personalized Curriculum: Curates and sequences diverse learning resources (courses, articles, projects) into a logical learning plan.

Resource Aggregation: Fetches course details, costs, and prerequisites from educational platforms via APIs.

Progress Tracking & Adaptation: Monitors progress and dynamically adjusts the learning path based on user performance or market shifts.


**🤖 The Agentic Process**

This project uses a hybrid framework of CrewAI, LangChain, and LangGraph to orchestrate a seamless workflow of specialized agents:

🧑‍💼 Profiler Agent: Creates a comprehensive user profile of skills and goals.

📈 Market Analyst Agent: Analyzes real-time job market data to identify high-demand skills.

👩‍🏫 Curriculum Designer Agent: Curates and sequences courses from platforms like Coursera, edX, and SWAYAM.

🧑‍💻 Manager Agent: Oversees the process and presents the final learning plan.


**🛠️ Tech Stack & Tools**

Agent Framework: CrewAI, LangChain, LangGraph

Core LLM: Gemini Pro

Deployment: Render, GitHub


**🌐 Deployment**

The Lifelong Learning Co-Pilot is deployed on Render with a continuous deployment pipeline. Changes pushed to the main branch are automatically built and deployed.

Live Demo
You can interact with the live version of the project here: https://lifelong-learning-ai-agent.onrender.com


**💻 Getting Started**

Prerequisites
Python 3.x

Pip

Installation
Clone the repository:

git clone https://github.com/krHarsh007/AI-Agent.git

cd AI-Agent


Install the required packages:

pip install -r requirements.txt


Configure your API keys in a .env file.

Usage
Run the main script to start the agentic process:

python app.py


**📄 License**

This project is licensed under the MIT License.


**🙏 Acknowledgements**

The CrewAI team

Google for the Gemini Pro LLM

Open-source educational platforms and data sources
