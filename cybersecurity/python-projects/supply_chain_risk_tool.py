# supply_chain_risk_tool.py
# This program simulates a basic internal security tool used by organizations
# to understand supply chain risks and recommended controls.

# 1. Create a dictionary where each threat includes:
# - A short description
# - The impact or consequence
# - At least two mitigations
# - A simple risk level (High, Medium, Low)

# Dictionary containing at least six threats from the list provided
threats = {
    1: {
        "name": "Dependency Confusion",
        "description": "Attacker publishes a malicious package with same name as an internal package to a public registry.",
        "impact": "Internal build system pulls malicious public package, leading to remote code execution and data theft.",
        "risk": "High", # Simple risk level assignment
        "mitigations": [
            "Use scoped packages and configure private registry to prioritize internal packages", # Mitigation 1
            "Reserve private package names on public registries and enforce dependency hashing" # Mitigation 2
        ]
    },
    2: {
        "name": "Typosquatting",
        "description": "Attacker creates packages with names similar to popular legitimate packages (e.g., 'reqests' vs 'requests').",
        "impact": "Developers accidentally install malicious package, resulting in credential theft or backdoor.",
        "risk": "Medium",
        "mitigations": [
            "Use lock files and always verify package names before installation",
            "Implement typo-detection tools and provide developer security training"
        ]
    },
    3: {
        "name": "Malicious Commits",
        "description": "Attacker or compromised insider pushes malicious code directly into source repository.",
        "impact": "Backdoor or vulnerability is introduced and distributed to all customers.",
        "risk": "High",
        "mitigations": [
            "Require GPG-signed commits and mandatory peer code review",
            "Enforce branch protection rules and monitor commit history for anomalies"
        ]
    },
    4: {
        "name": "Build Pipeline Compromise",
        "description": "Attacker gains access to CI/CD pipeline to inject malicious steps or alter build artifacts.",
        "impact": "Compromised software builds are deployed to production, affecting all releases.",
        "risk": "High",
        "mitigations": [
            "Harden CI/CD with least privilege, MFA, and isolated build agents",
            "Use ephemeral runners and verify build integrity with SLSA provenance"
        ]
    },
    5: {
        "name": "Update Tampering",
        "description": "Attacker intercepts or modifies software updates in transit to deliver malicious version.",
        "impact": "Users install compromised updates, leading to mass compromise of downstream systems.",
        "risk": "High",
        "mitigations": [
            "Sign all updates with strong cryptographic signatures and verify before install",
            "Use secure distribution channels with TLS and checksum validation"
        ]
    },
    6: {
        "name": "Open-Source Poisoning",
        "description": "Attacker contributes malicious code to widely used open-source projects via pull requests.",
        "impact": "Malicious code spreads to thousands of dependent projects and organizations.",
        "risk": "Medium",
        "mitigations": [
            "Vet open-source dependencies using Software Composition Analysis (SCA) tools",
            "Pin dependencies to known good versions and review changelogs carefully"
        ]
    },
    7: {
        "name": "Firmware Tampering",
        "description": "Device firmware is modified during manufacturing or distribution to include backdoor.",
        "impact": "Persistent low-level backdoor that survives OS reinstalls and is hard to detect.",
        "risk": "High",
        "mitigations": [
            "Implement secure boot and firmware attestation",
            "Source hardware from trusted suppliers and verify firmware hashes"
        ]
    },
    8: {
        "name": "Hardware Trojans",
        "description": "Malicious circuitry intentionally added to hardware during fabrication.",
        "impact": "Hardware-level data leakage or system failure that bypasses software security controls.",
        "risk": "Low",
        "mitigations": [
            "Perform hardware inspection and use only trusted foundries",
            "Implement runtime hardware behavior monitoring"
        ]
    }
}

# 2. Display all threat names, numbered
# This matches the example format: "1. Dependency Confusion"
print("Available Supply Chain Threats:")
for threat_id, data in threats.items():
    print(f"{threat_id}. {data['name']}") # Print numbered threat name

# Allow the user to choose multiple threats at once, e.g., 1,3,5
# Prompt is exactly as shown in the task
user_input = input("\nEnter the threats you want to assess (e.g., 1,3,5): ")

# Parse the comma-separated input into a list of valid threat IDs
selected_ids = []
for part in user_input.split(","): # Split by comma
    part = part.strip() # Remove spaces
    if part.isdigit(): # Check if entry is a number
        num = int(part)
        if num in threats: # Validate that threat exists
            selected_ids.append(num)

# Initialize counters for step 4 summary
high_risk = 0
medium_risk = 0
low_risk = 0

# 3. For each chosen threat, print description, impact, mitigations, and risk level
# Format is readable and professional as required
for tid in selected_ids:
    t = threats[tid] # Get the threat data for selected ID

    print(f"\n=== {t['name']} ===") # Section header for each threat
    print(f"Description: {t['description']}") # Print short description
    print(f"Impact: {t['impact']}") # Print impact or consequence
    print(f"Risk Level: {t['risk']}") # Print assigned risk level
    print("Mitigations:") # Print at least two mitigations
    for m in t['mitigations']:
        print(f"- {m}")

    # Count risk levels for summary in next step
    if t['risk'] == "High":
        high_risk += 1
    elif t['risk'] == "Medium":
        medium_risk += 1
    elif t['risk'] == "Low":
        low_risk += 1

# 4. After printing details for all selected threats, print a summary
print("\nSummary:")
print(f"High-risk threats: {high_risk}")
print(f"Medium-risk threats: {medium_risk}")
print(f"Low-risk threats: {low_risk}")

# 5. Generate an Overall Recommendation based on simple logic
# Logic from screenshot:
# - If 3 or more high-risk threats -> urgent attention
# - If mostly medium risks -> moderate but needs improvement
# - If mostly low risks -> stable but needs monitoring
print("\nOverall Recommendation:")
if high_risk >= 3:
    # Condition for critical supply chain risk
    print("Your software supply chain requires urgent attention.")
elif medium_risk > high_risk and medium_risk > low_risk:
    # Condition when medium risks dominate
    print("Your supply chain posture is moderate but needs improvement.")
elif low_risk > high_risk and low_risk > medium_risk:
    # Condition when low risks dominate
    print("Your supply chain appears stable, but continuous monitoring is required.")
else:
    # Fallback for tie cases
    if high_risk >= 1:
        print("Your supply chain posture is moderate but needs improvement.")
    else:
        print("Your supply chain appears stable, but continuous monitoring is required.")
