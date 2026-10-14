def get_age_group():
    print("\nSelect your age group:")
    print("1. Under 5 years")
    print("2. 5-17 years")
    print("3. 18-59 years")
    print("4. 60 years or above")

    while True:
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            return "young_child"
        elif choice == "2":
            return "child_teen"
        elif choice == "3":
            return "adult"
        elif choice == "4":
            return "older_adult"
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"


def give_activity_advice(age_group, aqi):
    category = get_aqi_category(aqi)

    print("\n========== SAANS SAATHI ==========")
    print("AQI:", aqi)
    print("Air quality category:", category)

    sensitive_group = age_group in (
        "young_child", "child_teen", "older_adult"
    )

    if aqi <= 50:
        print("\nAir quality is Good.")
        print("Walking and outdoor play are generally reasonable.")
        print("Check the weather and pay attention to symptoms.")

    elif aqi <= 100:
        print("\nAir quality is Satisfactory.")
        print("Light outdoor activities are generally reasonable.")
        print("Sensitive people should monitor symptoms.")

    elif aqi <= 200:
        print("\nAir quality is Moderate.")

        if sensitive_group:
            print("You are in an age group that needs extra caution.")
            print("Avoid prolonged or strenuous outdoor exercise.")
            print("Running, intense sports and vigorous cycling:")
            print("Better to postpone or move indoors.")
            print("A short, gentle walk is lower exertion,")
            print("but is not guaranteed to be risk-free.")
        else:
            print("Reduce prolonged or strenuous outdoor exercise.")
            print("Consider indoor exercise instead of running.")
            print("If going outside, keep activity light and shorter.")

    elif aqi <= 300:
        print("\nAir quality is Poor.")
        print("Avoid outdoor physical exertion where possible.")

        if sensitive_group:
            print("Prefer staying indoors and avoid outdoor exercise.")
        else:
            print("Move exercise indoors and limit outdoor exposure.")

    elif aqi <= 400:
        print("\nAir quality is Very Poor.")
        print("Avoid outdoor exercise and keep outdoor exposure low.")
        print("Children and older adults should take extra care.")

    else:
        print("\nAir quality is Severe.")
        print("Avoid outdoor physical activity.")
        print("Stay indoors where possible and follow official advice.")

    print("\nImportant:")
    print("- This is general guidance, not medical clearance.")
    print("- AQI can vary by location and time.")
    print("- Asthma or heart/lung conditions require extra caution.")
    print("- Stop activity if coughing, wheezing or breathing difficulty")
    print("  occurs, and seek medical help when needed.")


def main():
    print("===================================")
    print("       SAANS SAATHI MINI")
    print("  Outdoor Activity Safety Helper")
    print("===================================")

    age_group = get_age_group()

    while True:
        try:
            aqi = int(input("\nEnter current AQI (0-500): ").strip())

            if 0 <= aqi <= 500:
                break

            print("AQI must be between 0 and 500.")

        except ValueError:
            print("Invalid input. Enter a whole number, e.g. 170.")

    give_activity_advice(age_group, aqi)


if __name__ == "__main__":
    main()
