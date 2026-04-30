def recommend_license(project_type, allow_modifications, commercial_use):
    if allow_modifications not in ["yes", "no"] or commercial_use not in ["yes", "no"]:
        raise ValueError("Invalid inputs. 'yes' or 'no' expected for modifications and commercial use.")

    if project_type.lower() == "library":
        if allow_modifications == "yes" and commercial_use == "yes":
            return "MIT License"
        elif allow_modifications == "no":
            return "GPLv3"
        else:
            return "Apache 2.0"
    elif project_type.lower() == "application":
        if commercial_use == "no":
            return "Non-Commercial Creative Commons"
        return "BSD 3-Clause"
    else:
        return "Please check supported project types in documentation."