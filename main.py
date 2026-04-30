import argparse
from license_recommender.logic import recommend_license
from license_recommender.utils import handle_input_error

def main():
    parser = argparse.ArgumentParser(description="AI License Buddy: Recommend the best open-source license for your project.")
    parser.add_argument("--noninteractive", action="store_true", help="Run in non-interactive mode with predefined inputs.")
    args = parser.parse_args()

    if args.noninteractive:
        print("Non-interactive mode is not yet implemented.")
        return

    try:
        print("Welcome to AI License Buddy!")
        project_type = input("What type of project is this? (e.g., library, application)\n")
        allow_modifications = input("Do you want to allow modifications? (yes/no)\n")
        commercial_use = input("Is commercial use allowed? (yes/no)\n")

        result = recommend_license(project_type, allow_modifications, commercial_use)
        print(f"Recommended License: {result}")
    except Exception as e:
        handle_input_error(e)

if __name__ == "__main__":
    main()