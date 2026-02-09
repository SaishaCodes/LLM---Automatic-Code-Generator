import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# Phase 1: Environment & LLM Setup
load_dotenv()

# Force environment to point to Groq even if a default call is made
os.environ["OPENAI_API_KEY"] = os.environ.get("GROQ_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

# Initialize the Native LLM
# Change from llama3-70b-8192 to one of these:
my_llm = LLM(
    model="groq/llama-3.3-70b-versatile", # Recommended: fastest and most capable
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0
)

# Phase 2: Agents (Passed my_llm explicitly)
analyst_agent = Agent(
    role='Legacy Code Analyst',
    goal='Create logic blueprints from Python 2 code.',
    backstory='Expert in reverse-engineering legacy systems.',
    llm=my_llm,
    verbose=True
)

architect_agent = Agent(
    role='Python 3.12 Specialist',
    goal='Rewrite logic into modern Python.',
    backstory='Expert in modern PEP standards and type hinting.',
    llm=my_llm,
    verbose=True
)

qa_agent = Agent(
    role='Software QA Engineer',
    goal='Generate pytest files for code validation.',
    backstory='Meticulous tester focused on edge cases.',
    llm=my_llm,
    verbose=True
)

# Phase 3: Tasks
# --- Phase 3: Load File and Define Tasks ---

# 1. Read the actual file content from your disk
with open('legacy.py', 'r') as f:
    legacy_content = f.read()

# 2. Pass that content into Task 1
task1 = Task(
    description=f"""
        Analyze the following legacy Python 2 code:
        ---
        {legacy_content}
        ---
        Create a logic blueprint and identify what needs to be modernized.
    """,
    expected_output="A structured markdown summary of the logic.",
    agent=analyst_agent
)

task2 = Task(
    description="Using the blueprint, rewrite the code into Python 3.12 with type hints and f-strings.",
    expected_output="Raw Python 3.12 code.",
    agent=architect_agent,
    context=[task1],
    output_file="modernized_code.py" # This will auto-save the result!
)

task3 = Task(
    description="Create a pytest suite for the refactored code.",
    expected_output="Raw pytest code.",
    agent=qa_agent,
    context=[task2],
    output_file="test_code.py" # This will auto-save the tests!
)
# Phase 4: Execution
project_crew = Crew(
    agents=[analyst_agent, architect_agent, qa_agent],
    tasks=[task1, task2, task3],
    verbose=True
)

print("### Ghostwriter AI Kicking Off ###")
print(project_crew.kickoff())