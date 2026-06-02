from flask import Flask, render_template

from reasoning.engine import Rule
from reasoning.engine import forward_chain

from graph.graph_generator import create_graph

from reports.pdf_generator import generate_report

app = Flask(__name__)


@app.route("/")
def home():

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

    create_graph(rules)

    generate_report(
        conclusions,
        trace
    )

    return render_template(
        "index.html",
        conclusions=conclusions,
        trace=trace
    )


if __name__ == "__main__":
    app.run(debug=True)