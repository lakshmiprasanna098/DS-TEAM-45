import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import neuralcoref
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
model = SentenceTransformer('all-MiniLM-L6-v2')

MODEL_ANSWER = "Artificial intelligence is the simulation of human intelligence in machines."

def check_plagiarism(answer):
    plagiarism_score = random.uniform(10, 50)  
    return plagiarism_score


def check_grammar(answer):
    doc = nlp(answer)
    num_errors = sum([token.pos_ == 'PUNCT' for token in doc])  
    grammar_score = 100 - (num_errors * 5)  
    return max(0, grammar_score)

def check_coherence(answer):
    doc = nlp(answer)
    if doc._.has_coref:  
        coherence_score = 100  
    else:
        coherence_score = 60  
    return coherence_score


def check_relevance(answer, model_answer):
    answer_embedding = model.encode([answer])[0]
    model_embedding = model.encode([model_answer])[0]
    similarity_score = cosine_similarity([answer_embedding], [model_embedding])[0][0]
    relevance_percentage = similarity_score * 100  # Convert to percentage
    return relevance_percentage

def check_accuracy(answer, model_answer):
    return check_relevance(answer, model_answer)
def evaluate_answer(answer):

    plagiarism = check_plagiarism(answer)
    if plagiarism > 30:
        return {"error": "Plagiarism detected. Answer rejected."}
    grammar_score = check_grammar(answer)
    coherence_score = check_coherence(answer)
    relevance_score = check_relevance(answer, MODEL_ANSWER)
    accuracy_score = relevance_score
    return {
        "plagiarism": plagiarism,
        "grammar_score": grammar_score,
        "coherence_score": coherence_score,
        "relevance_score": relevance_score,
        "accuracy": accuracy_score
    }
