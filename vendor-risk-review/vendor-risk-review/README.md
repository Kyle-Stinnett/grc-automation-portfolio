# Vendor Risk Review Automation

## Purpose
This project demonstrates a simple approach to automating vendor risk review processes by identifying potential issues in SOC 2 reports.

## Approach
- Uses keyword matching to detect:
  - Exceptions
  - Deficiencies
  - Qualified opinions

## Example
Input:
"The audit identified a control deficiency in access reviews."

Output:
Findings: ["deficiency"]

## Value
- Reduces manual review effort
- Improves consistency in vendor assessments
- Supports faster identification of potential risks
