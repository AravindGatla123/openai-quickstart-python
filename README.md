# OpenRouter Quickstart for Python

This repository contains a few small Python examples wired to work with OpenRouter through the OpenAI Python SDK. By default, the examples use `stepfun/step-3.5-flash:free`.

## Included examples

- `examples/assistant-basic/assistant.py`: terminal chat loop
- `examples/chat-basic/app.py`: Flask chat UI with streaming responses
- `examples/assistant-flask/app.py`: Flask app using the Assistants API
- `examples/assistant-functions/functions.py`: function-calling example

## Basic API request

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_openrouter_api_key",
    base_url="https://openrouter.ai/api/v1",
)

completion = client.chat.completions.create(
    model="stepfun/step-3.5-flash:free",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)

print(completion.choices[0].message.content)
```

## Setup

1. Install Python 3 if it is not already available.
2. Clone this repository and move into it:

```bash
cd openai-quickstart-python
```

3. Create and activate a virtual environment.

macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```cmd
python -m venv venv
.\venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create your local environment file:

```bash
cp .env.example .env
```

6. Set your OpenRouter credentials in `.env`:

```env
OPENAI_API_KEY=your_openrouter_api_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=stepfun/step-3.5-flash:free
```

## Run an example

### Terminal assistant

```bash
python3 examples/assistant-basic/assistant.py
```

Type `exit` to stop the session.

### Basic Flask chat app

```bash
cd examples/chat-basic
flask --app app run
```

Open `http://127.0.0.1:5000`.

### Flask Assistants app

```bash
cd examples/assistant-flask
flask --app app run
```

Open `http://127.0.0.1:5000`.

## Notes

- The Flask examples read environment variables from your shell, so make sure your virtual environment is active and your `.env` values are available before starting them.
- `examples/assistant-flask` uses the Assistants API, while `examples/chat-basic` uses chat completions with streaming.
