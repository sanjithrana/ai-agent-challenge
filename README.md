 #Karbon AI Agent Challenge

An autonomous **"Agent-as-Coder"** built with **LangGraph**, **Groq**, and **Python** that plans, writes, and tests custom **bank statement parsers** automatically.

---

## 🎯 Goal

This project implements an LLM-powered coding agent that can **generate a Python parser** for any bank statement PDF (e.g., ICICI, SBI, etc.).  
When run via CLI, the agent automatically:
1. Plans a parsing strategy   
2. Generates runnable Python code   
3. Tests the generated code   
4. Saves the final parser file  

---

##  Architecture Overview

The agent follows a simple LangGraph-based workflow:

```mermaid
graph TD
A[Input Task] --> B[Plan Node 📝]
B --> C[Code Node 💻]
C --> D[Test Node 🧪]
D --> E[End ✅]
Each node performs a distinct step:

plan_node → Writes a step-by-step approach to build a PDF parser.

code_node → Generates Python code implementing the plan.

test_node → Executes and validates the generated parser function.

⚙️ Setup & Run Instructions
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/sanjithrana/ai-agent-challenge.git
cd ai-agent-challenge
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv my_env
my_env\Scripts\activate       # Windows
# or
source my_env/bin/activate    # macOS/Linux
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Add your Groq API key
Create a .env file in your project root:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
5️⃣ Run the agent
bash
Copy code
python agent.py --target icici
💡 Example:
Input → “extract icici Bank PDF data”
Output → custom_parser/icici_parser.py containing a parse(pdf_path) function that returns a pandas DataFrame.

📁 Project Structure
bash
Copy code
ai-agent-challenge/
│
├── agent.py                  # Main AI agent code (LangGraph workflow)
├── data/                     # Folder for sample PDFs & CSVs
├── custom_parser/            # Auto-generated parsers
├── requirements.txt          # Dependencies list
├── .env                      # API keys (excluded from Git)
├── .gitignore                # Ignored files and folders
└── README.md                 # Documentation (this file)
🧠 Example Flow
sql
Copy code
Enter your target task (e.g: extract icici or sbi Bank PDF data): icici
Running Agent...

--- Planning ---
✅ Generated parsing plan

--- Generating Code ---
✅ Parser code created

--- Testing Code ---
✅ parse() function loaded successfully
Output:

📝 Plan printed in console

💻 Parser file written to my_sample_parser.py

✅ Test confirmation message

📊 Evaluation Criteria (as per challenge)
Weight	Dimension
35%	Agent autonomy (self-debug loops)
25%	Code quality (typing, clarity, documentation)
20%	Architecture (LangGraph flow design)
20%	Demo ≤ 60s showing agent → parser → pytest green

🧰 Dependencies
LangChain / LangGraph

Groq API

FastAPI (optional integration)

pandas, fitz (PyMuPDF), dotenv

Install manually if missing:

bash
Copy code
pip install langchain langgraph groq python-dotenv pandas pymupdf
🧑‍💻 Author
Sanjith Rana
GitHub: @sanjithrana

🪪 License
This project is licensed under the MIT License.

🏁 Summary
“An autonomous AI agent that plans, codes, tests, and delivers working parsers for bank statements — end-to-end, with no manual intervention.”

yaml
Copy code

---

Would you like me to add a **“Demo Commands” section** that shows how to automatically test the generated parser against a sample CSV (to meet Task T4 in the challenge)?






