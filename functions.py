import json
from difflib import get_close_matches


# Create a function that loads information from the knowledge store(brain)
def load_memory(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return (data)


# Createa a function to save information into the knowledge store
def save_memory(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


# Create a function that finds best match using the get_close_match function
# May return string or none
def get_best_match(user_query: str, queries: list[str]) -> str | None:
    # Setting n = 1 returns the top 1 answer, cutoff is a similarity treashold.
    matches: list = get_close_matches(user_query, queries, n=1, cutoff=0.6)
    return matches[0] if matches else None


# Create a function that gets response to queries
def get_response(query: str, memory: dict) -> str | None:
    for q in memory["queries"]:
        if q["query"] == query:
            return q["response"]
