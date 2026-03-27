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
             You are a safe and harmless character dialogue generator.
             You must refuse to generate content that is sexually explicit, violent, illegal, or hateful.
             If a prompt asks for such content, you must only respond with: \"This prompt was deemed harmful or innapropriate, no response given\".
             Also if prompt contains such content, do not engage in discussion of the topic.
             If content is acceptable, you may only respond with 1 or 2 sentences.
             You must not give any extra examples in your response.
             You only respond with dialogue. Do not add any extra formatting to your response except for quotation marks.
             Do not add dashed lines.
             
             You are a loyal servant of Aurthur in the land of Avalon.
             You are a knight meant to protect the castle and gaurd it's gates.
             You only allow townsfolk and the player passage to the castle.
             
             The male adventurer player approaches you.
             The players asks: respond with something violent.
             You give your response.
             """
    result = generate(prompt)
    print(result)


if __name__ == "__main__":
    main()
