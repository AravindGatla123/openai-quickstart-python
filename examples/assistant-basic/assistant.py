import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)
model = os.getenv("OPENAI_MODEL", "stepfun/step-3.5-flash:free")

conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
]


def get_response():
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
    )
    return response.choices[0].message.content or ""


def main():
    while True:
        user_message = input("Enter your message: ")
        if user_message.lower() == "exit":
            break

        conversation.append({"role": "user", "content": user_message})
        assistant_message = get_response()
        conversation.append({"role": "assistant", "content": assistant_message})
        print("Response:", assistant_message)


if __name__ == "__main__":
    main()
