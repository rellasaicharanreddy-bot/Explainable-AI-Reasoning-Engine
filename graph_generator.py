import networkx as nx
import matplotlib.pyplot as plt


def create_graph(rules):

    G = nx.DiGraph()

    for rule in rules:

        for cond in rule.conditions:

            G.add_edge(
                cond,
                rule.result
            )

    plt.figure(figsize=(8,6))

    nx.draw(
        G,
        with_labels=True,
        node_size=3000
    )

    plt.savefig(
        "static/reasoning_graph.png"
    )

    plt.close()