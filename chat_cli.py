# Simple command-line chat interface

TOPICS = {
    "Technology": {
        "AI": "Artificial Intelligence is the simulation of human intelligence processes by machines.",
        "Robotics": "Robotics involves designing, constructing, operating, and applying robots."
    },
    "Science": {
        "Physics": "Physics is the natural science that studies matter, energy, and the fundamental forces.",
        "Biology": "Biology is the study of living organisms and their vital processes."
    }
}


def get_choice(options):
    """Prompt the user to select from a list of options."""
    for idx, name in enumerate(options, start=1):
        print(f"  {idx}. {name}")
    while True:
        choice = input("User: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        print("Bot: Please enter a valid option number.")


def chat():
    print("Bot: Hi! Let's pick a topic.")
    topic_names = list(TOPICS.keys())
    chosen_topic = get_choice(topic_names)
    print(f"Bot: You chose {chosen_topic}. Now pick a subtopic.")
    subtopic_names = list(TOPICS[chosen_topic].keys())
    chosen_subtopic = get_choice(subtopic_names)
    answer = TOPICS[chosen_topic][chosen_subtopic]
    print(f"Bot: {answer}")


if __name__ == "__main__":
    chat()
