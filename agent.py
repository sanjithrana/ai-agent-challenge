import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

try:
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)
    print(" ChatGroq model initialized successfully.")
except Exception as e:
    print(f" Failed to initialize ChatGroq: {e}")
    llm = None


from typing import TypedDict

class AgentState(TypedDict):
    task: str
    plan: str
    code: str
    result: str


def plan_node(state: AgentState) -> dict:
    print("\n--- Planning ---")

    prompt = f"""
You are an expert Python developer.
Task: {state['task']}
Write a clear step-by-step plan to build a Python parser using PyMuPDF (fitz).
The function should be named `parse(pdf_path)` and return a pandas DataFrame.
    """

    if llm is None:
        print(" Offline fallback used.")
        return {
            "plan": """Step 1: Use fitz (PyMuPDF) to open the PDF.
Step 2: Extract text lines containing transaction details.
Step 3: Use regex to extract date, description, amount, and balance.
Step 4: Build a pandas DataFrame with columns ['Date','Description','Amount','Balance'].
Step 5: Return the DataFrame."""
        }

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        plan = response.content.strip()
        return {"plan": plan}
    except Exception as e:
        print(f" ChatGroq connection failed: {e}")
        return {
            "plan": "Offline fallback: extract text with PyMuPDF, parse lines, build pandas DataFrame, and return it."
        }


def code_node(state: AgentState) -> dict:
    print("\n---  Generating Code ---")

    plan = state["plan"]
    prompt = f"""
Based on this plan:

{plan}

Write complete, runnable Python code.
The function must be called `parse(pdf_path)` and return a pandas DataFrame.
    """

    if llm is None:
        print(" Offline fallback: generating basic PyMuPDF parser code.")
        code = """import fitz
import pandas as pd

def parse(pdf_path):
    doc = fitz.open(pdf_path)
    data = []
    for page in doc:
        text = page.get_text("text")
        lines = text.split("\\n")
        for line in lines:
            if any(char.isdigit() for char in line):
                data.append({"Line": line})
    return pd.DataFrame(data)
"""
        return {"code": code}

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        code = response.content.strip()
        return {"code": code}
    except Exception as e:
        print(f" Code generation failed: {e}")
        return {"code": "# Offline fallback: simple PyMuPDF parser skeleton"}



def test_node(state: AgentState) -> dict:
    print("\n---  Testing Code ---")
    code = state["code"]

    try:
        with open("my_sanmple_parser.py", "w", encoding="utf-8") as f:
            f.write(code)
        exec(code, globals())
        if "parse" in globals():
            result = " parse() function loaded successfully."
        else:
            result = " parse() not found in generated code."
    except Exception as e:
        result = f" Code execution error: {e}"

    return {"result": result}


My_workflow = StateGraph(AgentState)

My_workflow.add_node("plan_step", plan_node)
My_workflow.add_node("code_step", code_node)
My_workflow.add_node("test_step", test_node)

My_workflow.set_entry_point("plan_step")
My_workflow.add_edge("plan_step", "code_step")
My_workflow.add_edge("code_step", "test_step")
My_workflow.add_edge("test_step", END)

app = My_workflow.compile()


if __name__ == "__main__":
    task_input = input("Enter your target task (e.g: extract icici or sbi Bank PDF data): ")
    initial_state = {"task": task_input}

    print("\n\n Running Agent...")
    final_state = app.invoke(initial_state)

    print("\n----- FINAL OUTPUT -----")
    print("Plan:\n", final_state["plan"])
    print("\nCode:\n", final_state["code"])
    print("\nTest Result:\n", final_state["result"])
