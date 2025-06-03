from knowledge import load_knowledge, get_answer, learn
from nlp_utils import clean_text

def chatbot():
    print("Chatbot: Hello! Ask me anything. Type 'bye' to exit.")
    knowledge = load_knowledge()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Bye!")
            break

        question = clean_text(user_input)
        answer = get_answer(knowledge, question)

        if answer:
            print("Chatbot:", answer)
        else:
            print("Chatbot: I don't know that. Can you teach me?")
            new_answer = input("You (answer): ").strip()
            if new_answer.lower() in ["no", "i don't know"]:
                print("Chatbot: Okay, maybe next time.")
            else:
                learn(knowledge, question, new_answer)
                print("Chatbot: Thanks! I’ve learned something new.")

if __name__ == "__main__":
    chatbot()
