import json

def check_security_settings(config):
    issues = []

    if not config.get("require_signed_commits", False):
        issues.append("Signed commits are not enforced")

    if not config.get("mfa_required", False):
        issues.append("MFA is not required")

    return issues


# Simulated configuration (like a system or repo setting)
sample_config = {
    "require_signed_commits": False,
    "mfa_required": True
}

results = check_security_settings(sample_config)

if results:
    print("Compliance Drift Detected:")
    for issue in results:
        print("-", issue)
else:
    print("All controls are compliant")
