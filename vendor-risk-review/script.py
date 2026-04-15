import re

def find_exceptions(text):
    keywords = ["exception", "qualified", "deficiency"]
    findings = []

    for word in keywords:
        if re.search(word, text, re.IGNORECASE):
            findings.append(word)

    return findings

sample_report = "The audit identified a control deficiency in access reviews."

results = find_exceptions(sample_report)

print("Findings:", results)
