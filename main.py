import json

def recommend_license(usage, allow_modifications, same_license):
    if usage == "commercial" and allow_modifications and not same_license:
        return "Apache License 2.0"
    elif usage == "community-driven" and allow_modifications:
        return "MIT License"
    elif usage == "personal" and not allow_modifications:
        return "All Rights Reserved"
    else:
        return "GPL-3.0 License"

def explain_license(license_name):
    explanations = {
        "Apache License 2.0": "A permissive license allowing commercial use with proper attribution.",
        "MIT License": "A simple and permissive license allowing wide freedom of use.",
        "All Rights Reserved": "No permissions are granted to others for use, distribution, or modification.",
        "GPL-3.0 License": "A strong copyleft license requiring open-source derivations."
    }
    return explanations.get(license_name, "No explanation available.")

def main():
    print("Welcome to AI License Buddy!")

    # Replacing input statements to handle EOFError during testing or non-interactive environments
    try:
        usage = input("What's the primary use of your project?  (e.g., personal use, commercial use, community-driven): ").strip()
        allow_modifications = input("Do you want to allow modifications? (yes/no): ").strip().lower() == "yes"
        same_license = input("Should modifications retain the same license? (yes/no): ").strip().lower() == "yes"
    except EOFError:
        print("Error: Input was not provided. Using default values for testing.")
        usage = "personal"
        allow_modifications = False
        same_license = True

    license_name = recommend_license(usage, allow_modifications, same_license)
    explanation = explain_license(license_name)

    print(f"\nRecommended License: {license_name}")
    print(f"Explanation: {explanation}")

if __name__ == "__main__":
    main()