from flask import Flask, render_template, request
import google.generativeai as genai

from reports.pdf_generator import generate_pdf

app = Flask(__name__)

# --------------------------------
# Gemini Configuration
# --------------------------------

genai.configure(
    api_key="AQ.Ab8RN6JAD_bkCcLtLz9AHxOqetQnoq7wwGxt7mN44wrSNHujTw"
)

model = genai.GenerativeModel(
    "gemini-flash-latest"
)

# --------------------------------
# AI Reasoning Function
# --------------------------------

def get_ai_reasoning(question):

    prompt = f"""
You are an Explainable AI system.

Analyze the user's question and return:

Facts:
- Fact 1
- Fact 2

Reasoning:
1. Step 1
2. Step 2

Conclusion:
Final Answer

User Question:
{question}
"""

    response = model.generate_content(prompt)

    text = response.text

    facts = []
    trace = []
    conclusions = []

    current_section = ""

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("Facts"):
            current_section = "facts"
            continue

        if line.startswith("Reasoning"):
            current_section = "reasoning"
            continue

        if line.startswith("Conclusion"):
            current_section = "conclusion"
            continue

        if not line:
            continue

        if current_section == "facts":
            facts.append(line)

        elif current_section == "reasoning":
            trace.append(line)

        elif current_section == "conclusion":
            conclusions.append(line)

    return facts, conclusions, trace


# --------------------------------
# Graph Generator
# --------------------------------

def create_ai_graph(facts, conclusions):

    try:

        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.DiGraph()

        for fact in facts:
            for conclusion in conclusions:
                G.add_edge(
                    fact,
                    conclusion
                )

        plt.figure(figsize=(8, 6))

        nx.draw(
            G,
            with_labels=True,
            node_size=3000
        )

        plt.savefig(
            "static/reasoning_graph.png"
        )

        plt.close()

    except Exception as e:
        print("Graph Error:", e)


# --------------------------------
# Home Route
# --------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    facts = []
    conclusions = []
    trace = []

    if request.method == "POST":

        question = request.form.get(
            "question",
            ""
        )

        try:

            facts, conclusions, trace = \
                get_ai_reasoning(question)

        except Exception as e:

            facts = [
                "AI service error"
            ]

            conclusions = [
                "Could not generate response"
            ]

            trace = [
                str(e)
            ]

        create_ai_graph(
            facts,
            conclusions
        )

        generate_pdf(
            conclusions,
            trace
        )

    return render_template(
        "index.html",
        facts=facts,
        conclusions=conclusions,
        trace=trace
    )


# --------------------------------
# Start Flask
# --------------------------------

if __name__ == "__main__":
    app.run(debug=True)