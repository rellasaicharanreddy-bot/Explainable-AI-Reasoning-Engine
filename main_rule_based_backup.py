from flask import Flask, render_template, request

from reasoning.engine import Rule, forward_chain
from graph.graph_generator import create_graph
from reports.pdf_generator import generate_pdf

app = Flask(__name__)


def get_ai_reasoning(question):
    """
    Temporary AI reasoning function.
    Replace later with OpenAI API if desired.
    """

    question = question.lower()

    if "umbrella" in question or "rain" in question:

        facts = [
            "cloudy",
            "high_humidity"
        ]

        rules = [

            Rule(
                ["cloudy", "high_humidity"],
                "rain"
            ),

            Rule(
                ["rain"],
                "carry_umbrella"
            )
        ]

        conclusions, trace = forward_chain(
            facts,
            rules
        )

        return facts, conclusions, trace, rules

    facts = [
        "user_question_received"
    ]

    conclusions = [
        "No predefined reasoning available"
    ]

    trace = [
        "AI could not match a reasoning rule"
    ]

    rules = []

    return facts, conclusions, trace, rules


@app.route("/", methods=["GET", "POST"])
def home():

    facts = []
    conclusions = []
    trace = []

    if request.method == "POST":

        question = request.form.get("question")

        facts, conclusions, trace, rules = get_ai_reasoning(
            question
        )

        if rules:
            create_graph(rules)

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


if __name__ == "__main__":
    app.run(debug=True)