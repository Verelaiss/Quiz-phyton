# Funções do sistema: o que se repete no processamento lógico

# Bloco de leitura, formatação e validação de resposta
def ler_resposta():
    while True:
        resposta = input("Digite sua resposta: ")
        resposta = resposta.upper()
        resposta = resposta.strip()

        if resposta in ["A", "B", "C", "D"]:
            return resposta

        print("Resposta inválida, digite A, B, C ou D")


# Bloco de pergunta e validação de resposta
def fazer_pergunta(
    pergunta,
    alternativa_a,
    alternativa_b,
    alternativa_c,
    alternativa_d,
    resposta_certa
):
    print(pergunta)
    print("A -", alternativa_a)
    print("B -", alternativa_b)
    print("C -", alternativa_c)
    print("D -", alternativa_d)

    resposta = ler_resposta()

    if resposta == resposta_certa:
        print("RESPOSTA CERTA!")
        return True
    else:
        print("VOCÊ ERROU! A resposta certa é:", resposta_certa)
        return False


# Início do QUIZ
print("Bem-vindo ao Quiz!")

ponto = 0

nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "! Vamos iniciar o quiz!")


# Pergunta 1
resultado = fazer_pergunta(
    "Qual a capital do Brasil?",
    "São Paulo",
    "Rio de Janeiro",
    "Brasília",
    "Salvador",
    "C"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 2
resultado = fazer_pergunta(
    "Qual o maior planeta do sistema solar?",
    "Marte",
    "Júpiter",
    "Saturno",
    "Netuno",
    "B"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 3
resultado = fazer_pergunta(
    "Quem pintou a obra Mona Lisa?",
    "Michelangelo",
    "Vincent van Gogh",
    "Leonardo da Vinci",
    "Pablo Picasso",
    "C"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 4
resultado = fazer_pergunta(
    "Em que ano terminou a Segunda Guerra Mundial?",
    "1939",
    "1945",
    "1918",
    "1950",
    "B"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 5
resultado = fazer_pergunta(
    "Qual é o animal terrestre mais rápido do mundo?",
    "Guepardo",
    "Leão",
    "Antilope",
    "Falcão-peregrino",
    "A"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 6
resultado = fazer_pergunta(
    "Quantos ossos tem o corpo humano adulto?",
    "180",
    "206",
    "210",
    "212",
    "B"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 7
resultado = fazer_pergunta(
    "Qual é o livro mais vendido de todos os tempos depois da Biblia?",
    "O senhor dos Anéis",
    "Harry Potter e a Pedra Filosofal",
    "Dom Quixote",
    "O Pequeno Príncipe",
    "C"
)

# Regra de pontuação
ponto = ponto + resultado

# Pergunta 8
resultado = fazer_pergunta(
    "Qual a fórmula da água?",
    "H2O",
    "CO2",
    "NaCl",
    "C6H12O6",
    "A"
)

# Regra de pontuação
ponto = ponto + resultado

# Pergunta 9
resultado = fazer_pergunta(
    "Qual pais possui a maior extensão territorial do mundo?",
    "Brasil",
    "China",
    "EUA",
    "Rússia",
    "D"
)

# Regra de pontuação
ponto = ponto + resultado


# Pergunta 10
resultado = fazer_pergunta(
    "Em qual país surgiram os Jogos Olímpicos?",
    "Roma",
    "Egito",
    "Grécia",
    "Pérsia",
    "C"
)

# Regra de pontuação
ponto = ponto + resultado


print("Sua pontuação é:", ponto)