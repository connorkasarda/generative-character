from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
GRAMMARS_DIR = PROJECT_DIR / "grammars"

def load_grammar(name: str) -> str:
    """
    Loads grammar rules from file to memory

    Args:
        name (str): Name of grammar file in grammars directory

    Returns:
        str: The grammar rules as a string
    """
    grammar_path = GRAMMARS_DIR / f"{name}.gbnf"

    with open(grammar_path, "r", encoding="utf-8") as grammar_file:
        return grammar_file.read()
