import json

# Predefined hierarchical topics
TOPICS = {
    "Technology": {
        "Programming": {
            "Python": "Python is a versatile scripting language used in many fields.",
            "JavaScript": "JavaScript primarily powers dynamic behavior on web pages."
        },
        "Artificial Intelligence": {
            "Machine Learning": "Machine learning enables computers to learn from data.",
            "Deep Learning": "Deep learning uses neural networks with many layers to model complex patterns."
        }
    },
    "Health": {
        "Nutrition": {
            "Vitamins": "Vitamins are organic molecules essential for metabolism.",
            "Diets": "Balanced diets provide the energy and nutrients required for health."
        },
        "Exercise": {
            "Cardio": "Cardio workouts improve heart health and endurance.",
            "Strength": "Strength training builds muscle and increases metabolism."
        }
    }
}

def prompt_selection(options):
    """Prompt the user to select from a dict of options."""
    keys = list(options.keys())
    for idx, name in enumerate(keys, start=1):
        print(f"{idx}. {name}")
    while True:
        choice = input("Select an option by number (or 'q' to quit): ")
        if choice.lower() == 'q':
            return None
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(keys):
                return keys[num - 1]
        print("Invalid choice. Try again.")

def main():
    while True:
        print("\n== Top-Level Topics ==")
        topic = prompt_selection(TOPICS)
        if topic is None:
            print("Exiting. Goodbye!")
            break

        print(f"\n-- {topic} Subtopics --")
        subtopic = prompt_selection(TOPICS[topic])
        if subtopic is None:
            continue

        print(f"\n** {subtopic} Detailed Topics **")
        detail = prompt_selection(TOPICS[topic][subtopic])
        if detail is None:
            continue

        response = TOPICS[topic][subtopic][detail]
        print(f"\n>>> {detail}: {response}\n")

if __name__ == "__main__":
    main()
