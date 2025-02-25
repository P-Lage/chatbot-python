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

last_responses = {}

# Respostas padrão para mensagens não reconhecidas
respostas_padrao = [
    "Desculpe, não entendi. Pode reformular?",
    "Poderia dizer isso de outra forma?",
    "Ainda estou aprendendo. Poderia tentar outra vez?"
]

# Função para registrar erros
def registrar_erro(mensagem):
    with open("erros_nao_identificados.txt", "a") as file:
        file.write(mensagem + "\n")

# Função principal que recebe o input e retorna uma resposta
def generate_response(user_input, intents):
    intent = get_intent(user_input, intents)
    if intent:
        responses = intents[intent]['responses']

        # Verifica se já enviamos alguma resposta dessa intenção antes
        if intent in last_responses:
            previous_response = last_responses[intent]
            available_responses = [r for r in responses if r != previous_response]

            # Se houver outras respostas disponíveis, escolhemos uma nova
            if available_responses:
                response = random.choice(available_responses)
            else:
                response = previous_response  # Se não, repetimos (evita erro)
        else:
            response = random.choice(responses)

        # Armazena a resposta usada
        last_responses[intent] = response
        return response
    else:
        # Se a intenção não foi encontrada, retorna uma resposta padrão e registra o erro
        response = random.choice(respostas_padrao)
        registrar_erro(user_input)
        return response