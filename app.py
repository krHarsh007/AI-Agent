import os
import getpass
import time
import json
from flask import Flask, render_template, request, redirect, url_for, session, Response
# from dotenv import load_dotenv  <- This line is no longer needed
from functools import lru_cache
# This import is not used in this version, but is harmless
from langgraph.graph import StateGraph, END 
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Dict, Optional
import markdown2

# load_dotenv()  <- This line is no longer needed

app = Flask(__name__)
app.secret_key = os.urandom(24)

# --- AgentState class and the three agent node functions ---
class AgentState(TypedDict):
    user_profile: Dict[str, str]
    market_analysis: Optional[str]
    learning_plan: Optional[str]
    final_output: Optional[str]

# Agent node functions
def market_analyst_node(state: AgentState) -> AgentState:
    print("--- 📈 Running Market Analyst Agent ---")
    profile = state['user_profile']
    prompt = (
        f"You are a Market Analyst AI. Your task is to identify the top 5-7 most in-demand skills for the role of a '{profile['career_goal']}'. "
        f"The user's current skills are '{profile['current_skills']}'. "
        "Analyze real-time labor market data from sources like LinkedIn and skill databases. "
        "Identify key skills to bridge the gap. Respond only with a comma-separated list of crucial skills."
    )
    # ---
    # --- THIS IS THE FIX ---
    # Switched to the stable 'gemini-pro' model to resolve the 404 error
    llm = ChatGoogleGenerativeAI(model='gemini-flash-latest', temperature=0.5)
    # ---
    # ---
    response = llm.invoke(prompt)
    state['market_analysis'] = response.content.strip()
    return state


def curriculum_designer_node(state: AgentState) -> AgentState:
    print("--- 📚 Running Curriculum Designer Agent ---")
    profile = state['user_profile']
    analysis = state['market_analysis']
    prompt = (
        "You are an expert Curriculum Designer AI. Create a personalized, step-by-step learning plan. "
        f"User Profile:\n- Goal: {profile['career_goal']}\n- Current Skills: {profile['current_skills']}\n- Preferred Style: {profile['learning_style']}\n"
        f"Skills to Acquire: {analysis}\n\n"
        "Instructions:\n"
        "1. Create a logical, sequenced learning path with 3-4 major steps (e.g., Step 1: Foundational Knowledge).\n"
        "2. For each step, suggest a mix of learning resources from platforms like Coursera, edX, YouTube, and technical blogs.\n"
        "3. Include at least one course, one practical project idea, and one article/documentation link per step.\n"
        "4. Tailor the resource types to the user's learning style.\n"
        "5. Present the output in clear, structured Markdown."
    )
    # ---
    # --- THIS IS THE FIX ---
    llm = ChatGoogleGenerativeAI(model='gemini-flash-latest', temperature=0.5)
    # ---
    # ---
    response = llm.invoke(prompt)
    state['learning_plan'] = response.content.strip()
    return state


def manager_node(state: AgentState) -> AgentState:
    print("--- 🎯 Running Chief Strategist Agent ---")
    plan = state['learning_plan']
    profile = state['user_profile']
    prompt = (
        "You are the Chief Strategist of a personalized coaching service. Format the following learning plan into a final, user-friendly output. "
        f"The user's goal is to become a {profile['career_goal']}.\n"
        "Start with a motivational summary, present the plan clearly, and end with an encouraging closing statement."
        "\n\n--- Raw Learning Plan ---\n"
        f"{plan}"
    )
    # ---
    # --- THIS IS THE FIX ---
    llm = ChatGoogleGenerativeAI(model='gemini-flash-latest', temperature=0.5)
    # ---
    # ---
    response = llm.invoke(prompt)
    state['final_output'] = response.content.strip()
    return state
# --- WORKFLOW FUNCTION ---
@lru_cache(maxsize=128)
def run_agentic_workflow(user_profile_json):
    user_profile = json.loads(user_profile_json)
    initial_state = {"user_profile": user_profile}
    
    try:
        # Step 1: Market Analyst
        yield "data: Step 1/3: Analyzing market trends for your career goal...\n\n"
        market_analysis_state = market_analyst_node(initial_state)
        time.sleep(1)

        # Step 2: Curriculum Designer
        yield "data: Step 2/3: Curating a personalized, step-by-step learning plan...\n\n"
        curriculum_designer_state = curriculum_designer_node(market_analysis_state)
        time.sleep(1)

        # Step 3: Manager
        yield "data: Step 3/3: Formatting the final plan and adding a professional touch...\n\n"
        manager_state = manager_node(curriculum_designer_state)

        # Final step: convert to HTML and yield the final result
        final_output = manager_state.get('final_output', 'Sorry, an error occurred.')
        html_output = markdown2.markdown(final_output)
        
        yield f"result: {json.dumps(html_output)}\n\n"

    except Exception as e:
        print(f"[ERROR] An exception occurred during workflow: {e}")
        error_message = f"<h2>An Error Occurred</h2><p>Sorry, we couldn't generate your plan. The following error occurred: {e}</p>"
        yield f"result: {json.dumps(error_message)}\n\n"

# --- FLASK ROUTES ---

@app.route('/')
def home():
    """Displays the initial empty form."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Handles the form submission and returns the streaming response."""
    user_profile = {
        "current_skills": request.form.get('current_skills'),
        "career_goal": request.form.get('career_goal'),
        "learning_style": request.form.get('learning_style')
    }
    user_profile_json = json.dumps(user_profile, sort_keys=True)
    return Response(run_agentic_workflow(user_profile_json), mimetype='text/event-stream')

if __name__ == '__main__':
    # Setting host='0.0.0.0' makes it accessible on your network
    app.run(host='0.0.0.0',debug=True)

