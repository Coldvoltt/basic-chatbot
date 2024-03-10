from functions import load_memory, save_memory, get_best_match, get_response


# Create a chatbot
def chat_bot():
    memory: dict = load_memory('brain.json')

    while True:
        user_input: str = input('User: ')

        if any(phrase in user_input.lower() for phrase in ['bye', 'Okay', 'great', 'thank']) and len(user_input.split()) <= 3:
            break

        best_match: str | None = get_best_match(
            user_input, [q["query"] for q in memory["queries"]])

        if best_match:
            response: str = get_response(best_match, memory)
            print(f'AI: {response}')
        else:
            print('AI: I don\'t know the answer. Please teach me how to answer!.')
            new_response: str = input(
                'Provide the answer or "Skip" to move on: ')

            if new_response.lower() != 'skip':
                memory["queries"].append(
                    {"query": user_input, "response": new_response})
                save_memory('brain.json', memory)
                print('AI: Thanks! I learnt something new!')


if __name__ == '__main__':
    chat_bot()
