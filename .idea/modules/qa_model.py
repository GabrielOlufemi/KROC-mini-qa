from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question: str, context: str) -> str:
    result = qa_pipeline(question = question, context = context)

    return result
