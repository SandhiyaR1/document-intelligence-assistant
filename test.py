from rag.pipeline import ask_question


while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    response = ask_question(question)

    print("\nAnswer:\n")

    print(response["answer"])

    print("\nPages:", response["pages"])