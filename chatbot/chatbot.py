import json
import random
from chatbot.nlp import preprocess_text

# Carregar os dados de intenções
def load_intents(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        intents = json.load(f)
    return intents

# Função para encontrar a intenção com base na similaridade simples (palavra-chave)
def get_intent(user_input, intents):
    tokens = preprocess_text(user_input)
    for intent, data in intents.items():
        for pattern in data['patterns']:
            # Processa o padrão da mesma forma que o input
            pattern_tokens = preprocess_text(pattern)
            # Se houver interseção de palavras, considera que houve correspondência
            if set(tokens) & set(pattern_tokens):
                return intent
    return None

# Função principal que recebe o input e retorna uma resposta
def generate_response(user_input, intents):
    intent = get_intent(user_input, intents)
    if intent:
        responses = intents[intent]['responses']
        return random.choice(responses)
    else:
        return "Desculpe, não entendi. Pode reformular a pergunta?"
