buckets = [{"name": "customer-data", "public": True, "encrypted": False}, {"name": "internal-logs", "public": False, "encrypted": True}]
iam_roles = [{"name": "ReadOnlyAnalytics", "policies": ["s3:GetObject", "s3:ListBucket"]}, {"name": "OverPoweredAdmin", "policies": ["*:*"]}]

def check_buckets(buckets):
    print("=== Checking S3 Buckets ===")
    for bucket in buckets:
        name = bucket["name"]

        if bucket["public"]:
            print(f"[RISK] Bucket: {name}")
            print(f"       - What is wrong: Bucket is public")
            print(f"       - Fix: Make this bucket private and restrict access with bucket policies.")

        if not bucke["public"] and bucket["encrypted"]:
            print(f"[OK] Bucket: {name} - No misconfigurations found.")

def check_iam_roles(iam_roles):
    print("\n=== Checking IAM Roles ===") 
    for role in iam_roles:
        name = role["name"]
        found_risk = False
        for policy in role["policies"]:
            if "*:*" in policy or policy == "*":
                print(f"[RISK] Role: {name}")
                print(f"       - What is wrong: Policy '{policy}' is too powerful - violates least privilege")
                print(f"       - Fix: Replace wildcard with specific actions, e.g., only allow required S3 actions.")
                found_risk = True

        if not found_risk:
            print(f"[OK] Role: {name} - No overly permissive policies found.")

def main():
    check_buckets(buckets)
    check_iam_roles(iam_roles)

if __name__ == "__main__":
    main()
