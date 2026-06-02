class Rule:

    def __init__(self, conditions, result):

        self.conditions = conditions
        self.result = result


def forward_chain(facts, rules):

    known_facts = set(facts)

    trace = []

    changed = True

    while changed:

        changed = False

        for rule in rules:

            if all(condition in known_facts for condition in rule.conditions):

                if rule.result not in known_facts:

                    known_facts.add(rule.result)

                    trace.append(
                        f"Rule Applied: {' + '.join(rule.conditions)} -> {rule.result}"
                    )

                    changed = True

    return list(known_facts), trace