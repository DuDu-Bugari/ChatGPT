def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Bem-vindo ao playground do ChatGPT."

if __name__ == "__main__":
    print(saudacao("Eduardo"))

# quero uma função que converta Celsius para Fahrenheit
def celsius_para_fahrenheit(c: float) -> float:
    """Converte Celsius para Fahrenheit."""
    return c * 9 / 5 + 32
print("30ºC =", celsius_para_fahrenheit(30), "ºF")