# ChatBot

This repository is a minimal starting point for a command-line chatbot written in Python.

## Prerequisites

- Python 3.8 or higher
- `pip` for installing dependencies

## Running the chatbot

1. Clone the repository and navigate into it:

   ```bash
   git clone <repository-url>
   cd ChatBot
   ```
2. (Optional) create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies if a `requirements.txt` file is present:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the chatbot script:

   ```bash
   python bot.py
   ```

## Adding new topics and responses

Topics and responses are typically stored in a JSON or text file (for example `topics.json`). To add a new topic:

1. Open the topics file in your editor.
2. Add a new entry with your trigger phrase and response.
3. Save the file and run the bot again to see the new topic in action.

Example JSON entry:

```json
{
  "greetings": {
    "hi": "Hello!",
    "bye": "Goodbye!"
  }
}
```

## Contributing

1. Fork the repository on GitHub and create a new branch for your changes.
2. Make your modifications (for example adding features or fixing bugs).
3. Ensure your code follows standard Python formatting conventions (`black` or `flake8`).
4. Commit your changes and push the branch to your fork.
5. Open a pull request describing your changes.

Feel free to submit issues or suggestions for improving the chatbot!
=======

This repository contains a simple command-line chat interface implemented in `chat_cli.py`.

## Running the chat

Run the script with Python 3:

```bash
python3 chat_cli.py
```

Follow the prompts to select a topic and subtopic. The bot will respond with a predefined answer.
=======
This project provides a simple command-line interface allowing users to explore pre-defined topics in a hierarchical manner. Run the script with:

```bash
python src/main.py
```

Follow the on-screen prompts to choose a topic, subtopic, and detailed topic.

