# GRC Automation Portfolio

## Overview

This repository demonstrates how automation can be used to support governance, risk, and compliance (GRC) activities in a SaaS environment.

The focus is on improving efficiency, reducing manual effort, and enabling continuous monitoring of security controls.

## Projects

### 1. Vendor Risk Review Automation

**Location:** `vendor-risk-review/`

**Purpose:**
Automate the review of vendor security documentation to identify potential control gaps prior to onboarding.

**Problem Solved:**
Manual vendor reviews are time-consuming and inconsistent, increasing the risk of onboarding vendors with insufficient security controls.

**GRC Value:**
- Improves consistency in vendor assessments  
- Reduces review time  
- Supports third-party risk management programs  

**Framework Alignment:**
- SOC 2: CC3 (Risk Assessment), CC6 (Access Control)  
- ISO 27001: A.15 (Supplier Relationships)  
- NIST 800-53: SA (System and Services Acquisition)  

---

### 2. Compliance Drift Detection

**Location:** `compliance-drift/`

**Purpose:**
Continuously monitor system configurations to detect deviations from required security controls.

**Problem Solved:**
Point-in-time audits fail to detect changes that occur after initial validation, leading to compliance gaps.

**GRC Value:**
- Enables continuous monitoring  
- Identifies control failures early  
- Reduces audit findings  

**Framework Alignment:**
- SOC 2: CC7 (Monitoring Activities)  
- ISO 27001: A.12 (Operations Security)  
- NIST 800-53: CA (Continuous Monitoring)  

---

## Technical Approach

- Python-based scripts for validation and analysis  
- Simple configuration checks to simulate real-world environments  
- Designed to be extendable for integration with APIs or cloud platforms  

## Key Takeaway

This repository demonstrates how GRC processes can be enhanced through automation, enabling scalable and efficient compliance in modern cloud environments.
