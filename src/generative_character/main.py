import requests

API_URL = "http://localhost:8080/completion"


def generate(prompt: str) -> str:
    try:
        response = requests.post(
            API_URL,
            json={"prompt": prompt},
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("content", "").strip()

    except requests.exceptions.RequestException as e:
        return f"[Error communicating with LLM: {e}]"


def main():
    prompt = """
             You are a princess.
             The player approaches you.
             You need saving.
             Please respond to the player with a sentence.
             Mention how you need saving from the tower.
             Do not produce examples of any kind.
             Respond as the princess only.
             """
    result = generate(prompt)
    print(result)


if __name__ == "__main__":
    main()
