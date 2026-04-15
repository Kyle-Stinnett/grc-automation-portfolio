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
## Business Impact

This automation reduces manual effort required to review vendor SOC 2 reports and helps identify potential risks earlier in the vendor onboarding process.

## Future Enhancements
- Integrate with vendor management systems
- Expand keyword detection using NLP techniques
- Automate reporting of identified risks
