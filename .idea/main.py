from modules.file_reader import chunk_text, read_text_file
from modules.qa_model import answer_question

def main():
    text = read_text_file()
    print("File Content Loaded")

    #didn't need to add extra variables as i've harcoded values for them in their respective functions
    chunks = chunk_text(text)
    print("Chunks created")

    # #Outputing chunks
    # for i, chunk in enumerate(chunks, 1):
    #     print(f"Chunk {i}: ")
    #     print(chunk)
    #     print()

    #Q & A
    while True:

        question = input("Enter your question (or type exit to stop): ")

        if(question.lower() == "exit"):
            print("KROC... stopped")
            break

        bestAnswer = None
        bestScore = 0.0

        for i, chunk in enumerate(chunks, 1):
            result = answer_question(question, chunk)
            print(f"Chunk {i} -> {result['answer']} (score = {result['score']:.3f})")

            if (result['score'] > bestScore):
                bestScore = result['score']
                bestAnswer = result['answer']

        print("\nBest Answer Across All Chunks:")
        print(f"A: {bestAnswer} (score={bestScore:.3f})")



if __name__ == "__main__":
    main()