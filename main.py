import os
from chunks import search_similar
from gpt4all import GPT4All

base_path = "/Users/Faizanimran/Library/Application Support/nomic.ai/GPT4All/"

models_list = [
    os.path.join(base_path, "Llama-3.2-1B-Instruct-Q4_0.gguf"),
    os.path.join(base_path, "mistral-7b-instruct-v0.1.Q4_0.gguf"),
]

for model_path in models_list:
    if os.path.exists(model_path):
        print(f"Loaded path: {model_path}")
    else:
        print(f"Missing: {model_path}")


def function_run(model_path):
    model_name = os.path.basename(model_path)

    model = GPT4All(model_name, model_path=base_path, allow_download=False)
    model._chat_session = None

    print("\nPress Ctrl+C to stop\n")

    try:
        while True:
            user_input = input("You: ")
            context = search_similar(user_input)

            if context:
                prompt = f"""Context:
{context}

User Question:
{user_input}

Answer based on context:
"""
            else:
                prompt = f"""User Question:
{user_input}

Answer normally:
"""

            output = model.generate(
                prompt,
                temp=0.2,
                max_tokens=120,
                repeat_penalty=1.1,
                top_k=5,
                top_p=0.7,
            )

            print("AI:", output)

    except KeyboardInterrupt:
        print("\nStopped by user")


function_run(models_list[0])
