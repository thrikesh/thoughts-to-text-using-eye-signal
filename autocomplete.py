# autocomplete.py
# Minimal autocomplete module compatible with main.py

WORDS = []

def load():
    """
    Loads autocomplete resources.
    In full version, this could load a dictionary or NLP model.
    Here, we keep it simple.
    """
    global WORDS
    WORDS = []
    print("Autocomplete loaded (mock mode)")

def predict(word):
    """
    Returns a list of predicted words.
    """
    if not word:
        return []
    return [word]
