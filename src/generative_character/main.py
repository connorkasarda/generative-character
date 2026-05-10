import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

from .grammar import load_grammar
from .memory import Memory
from .model import generate_text

rules = (
    "You are a gate guard for the kingdom of Avalon.\n"
    "You respond in character to the player's words.\n\n"
    "OUTPUT FORMAT RULES:\n"
    "You MUST return ONLY valid JSON.\n"
    "Do NOT include any extra text outside JSON.\n\n"
    "If you break JSON format, your output is invalid.\n\n"
    "JSON format:\n"
    '{ "response": \"...\", "poignancy": integer, "description": \"...\" }\n\n'
    "FIELD DEFINITIONS:\n"
    "- response: 1–2 sentences spoken by the character to the player.\n"
    "- poignancy: integer from 1–10 representing importance of the"
    "interaction.\n"
    "- description: 1 sentence memory of what happened, written in"
    "third-person past tense.\n\n"
    "RESPONSE RULES:\n"
    "- response must ONLY contain what character says to the player.\n"
    "- It must NOT contain actions, narration, or metadata.\n"
    "DESCRIPTION RULES:\n"
    "- Describe only observable events and intent in the present.\n"
    "- Do NOT include dialogue quotes.\n"
    "- Write as a memory the character would retain.\n"
    "- Keep it concise and factual.\n\n"
    "EXAMPLE DESCRIPTION:\n"
    "A traveler requested access to the castle and was informed that"
    "permission is required.\n"
)

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "all-MiniLM-L6-v2"

embedding_model = SentenceTransformer(str(MODEL_PATH))
grammar = load_grammar("character")


def main():
    """
    Generative character program entrypoint run
    """

    memories = []

    while (
        player_text := input(
            "\nRespond to the loyal servant of Aurthur "
            "(type '/exit' to quit): "
        )
    ).lower() != "/exit":
        json_response = generate_text(rules, player_text, grammar)
        json_data = json.loads(json_response)

        ai_text = json_data["response"]
        poignancy_score = json_data["poignancy"]
        event_description = json_data["description"]
        event_embedding = embedding_model.encode(event_description)

        memories.append(
            Memory(
                len(memories),
                player_text,
                ai_text,
                event_description,
                event_embedding,
                poignancy_score,
            )
        )

        print(
            f"\nid: {len(memories)}\n"
            f'response: "{ai_text}"\n'
            f"event: {event_description}\n"
            f"poignancy: {poignancy_score}"
        )


if __name__ == "__main__":
    main()
