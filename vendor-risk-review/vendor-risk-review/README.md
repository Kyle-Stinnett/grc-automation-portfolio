# Vendor Risk Review Automation

## Purpose
This project demonstrates a simple approach to automating vendor risk review processes by identifying potential issues in SOC 2 reports.

## GRC Workflow Integration

This script would be used during vendor risk assessments to quickly identify potential issues in SOC 2 reports before manual review.

### Example Workflow
1. Vendor submits SOC 2 report  
2. Script scans report for keywords (exceptions, deficiencies)  
3. Flags potential risk areas  
4. GRC analyst performs detailed review  

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

## Business Impact

- Reduces manual review time  
- Improves consistency in vendor evaluations  
- Enables earlier identification of potential risks  

## Limitations

- Keyword matching may not capture all nuanced findings  
- Requires human validation for final assessment  

## Risk Considerations

- False positives may occur due to simple keyword matching  
- Over-reliance on automation could miss contextual findings  
- Requires periodic tuning of keyword sets

## Risk Mitigation Value

This automation supports vendor risk management by ensuring that security reports are reviewed consistently and that potential control deficiencies are identified early.

By introducing automated pre-screening:
- Vendors without sufficient controls can be flagged before onboarding  
- Review time is reduced, improving scalability of vendor assessments  
- Risk of onboarding non-compliant vendors is minimized  
