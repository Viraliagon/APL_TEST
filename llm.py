import requests

def explain_code(parsed_info):
    try:
        prompt = (
            "You are an expert in SimpliPy-Ja, a Jamaican-style pseudocode language.\n\n"
            "### Program to explain:\n"
            f"{parsed_info}\n\n"
            "Explain the program step-by-step in plain English. Use clear, concise language."
        )

        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "model": "dolphin-2.8-mistral-7b-v02",  # Or whatever your LM Studio model is called
                "messages": [
                    {"role": "system", "content": "You explain SimpliPy-Ja code to beginners."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }
        )

        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

    except requests.exceptions.ConnectionError:
        return "⚠️ LLM Error: Could not connect to LM Studio on http://localhost:1234. Is the server running?"

    except Exception as e:
        return f"⚠️ LLM Error: {e}"
