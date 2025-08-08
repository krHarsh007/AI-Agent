🧠 **The Lifelong Learning Co-Pilot**
A personalized, multi-agent system designed to guide individuals through a continuous journey of skill acquisition and career development. This project directly supports SDG 4.4 (Relevant skills for decent work) and SDG 4.3 (Equal access to technical/vocational and higher education) by democratizing access to tailored educational pathways.

🎯 Agent's Core Goal
To autonomously create, manage, and adapt a personalized lifelong learning path for a user, aligning their skills with current and future job market demands to ensure long-term employability.

🚀 Key Features & Agentic Tasks
The Lifelong Learning Co-Pilot performs a series of intelligent tasks to provide a comprehensive and dynamic learning plan:

Dynamic Skill Profiling: The agent initiates a conversation to understand the user's current skills, educational background, career goals, and learning preferences.

Skill Gap Analysis: It queries real-time labor market data and skill gap reports to identify the specific skills a user needs to bridge the gap between their current profile and their desired career trajectory.

Personalized Curriculum Generation: This core task involves autonomously searching and curating a variety of learning resources—from formal university courses and MOOCs to technical articles and hands-on projects—sequencing them into a logical, step-by-step learning plan.

Resource Aggregation: The agent connects to various educational platforms via APIs to fetch course details, syllabi, costs, and prerequisites.

Progress Tracking & Adaptation: The agent monitors user progress and dynamically adjusts the learning path. If a user struggles, it can suggest alternative resources. If the job market shifts, it can update the path with new, in-demand skills.

🤖 The Agentic Process (Powered by CrewAI)
This project leverages the CrewAI framework, where each agent has a specific expertise, to execute a seamless workflow.

🧑‍💼 Profiler Agent (Career Counselor): This agent's primary role is to interact with the user to build a comprehensive profile of their skills, goals, and preferences.

📈 Market Analyst Agent: This agent uses tools to analyze skill gap reports (e.g., from the National Skill Development Corporation) and real-time job market data to identify and validate high-demand skills.

👩‍🏫 Curriculum Designer Agent: Taking the user's profile and market analysis as input, this agent queries educational platforms (like Coursera, edX, and SWAYAM) to find relevant courses and resources. It then uses a recommender system algorithm to sequence these into a personalized learning path.

🧑‍💻 Manager Agent (Chief Strategist): The Manager Agent oversees the entire process, synthesizes the outputs from the other agents, and presents the final, actionable learning plan to the user.

🛠️ Tech Stack & Tools
Agent Framework: CrewAI , LangChain , LangGraph

Core LLM: Gemini Pro

Deployment: Render, GitHub

💻 Getting Started
To get a copy of this project up and running on your local machine for development and testing, follow these steps.

Prerequisites
Python 3.x

Pip

Installation
Clone the repository:

git clone https://github.com/krHarsh007/AI-Agent.git
cd AI-Agent

Install the required packages:

pip install -r requirements.txt

Configure your API keys for Gemini Pro and any educational platform APIs in a .env file.

Usage
Run the main script to start the agentic process:

python app.py

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
The CrewAI team for their excellent agentic framework.

Google for the powerful Gemini Pro LLM.

All open-source educational platforms and data sources that make this project possible.
