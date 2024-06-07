import random
import time
import matplotlib.pyplot as plt

# Geração de dados aleatórios para temperatura, pH e oxigênio
random.seed(10)  # Define a semente para garantir a reprodutibilidade dos resultados
temperatura = [random.uniform(24.0, 29.0) for _ in range(10)]  # Dados de temperatura entre 24°C e 29°C
ph = [random.uniform(6.8, 7.4) for _ in range(10)]  # Dados de pH entre 6.8 e 7.4
oxigenio = [random.uniform(6.0, 8.0) for _ in range(10)]  # Dados de oxigênio dissolvido entre 6 mg/L e 8 mg/L

# Definição dos limites para os sensores
limite_temperatura = (25.0, 28.0)
limite_ph = (7.0, 8.0)
limite_oxigenio = (6.0, 8.0)


# Função para verificar os limites e gerar alertas
def verificar_limites(temperatura, ph, oxigenio):
    alertas = []

    for i in range(len(temperatura)):
        if temperatura[i] < limite_temperatura[0] or temperatura[i] > limite_temperatura[1]:
            alertas.append(f"Leitura {i + 1}: Temperatura fora do limite ({limite_temperatura[0]}°C - {limite_temperatura[1]}°C)")
        if ph[i] < limite_ph[0] or ph[i] > limite_ph[1]:
            alertas.append(f"Leitura {i + 1}: pH fora do limite ({limite_ph[0]} - {limite_ph[1]})")
        if oxigenio[i] < limite_oxigenio[0] or oxigenio[i] > limite_oxigenio[1]:
            alertas.append(f"Leitura {i + 1}: Oxigênio dissolvido fora do limite ({limite_oxigenio[0]} mg/L - {limite_oxigenio[1]} mg/L)")

    return alertas


# Função para exibir alertas, se houver
def exibir_alertas(alertas):
    if alertas:
        for alerta in alertas:
            print("ALERTA: " + alerta)
    else:
        print("Nenhum alerta encontrado.")


# Função para plotar gráficos
def plotar_graficos(temperatura, ph, oxigenio):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.plot(temperatura)
    plt.title('Temperatura')

    plt.subplot(1, 3, 2)
    plt.plot(ph)
    plt.title('pH')

    plt.subplot(1, 3, 3)
    plt.plot(oxigenio)
    plt.title('Oxigênio Dissolvido')

    plt.tight_layout()
    plt.show()


# Função principal
def main():
    # Verificação dos limites
    alertas = verificar_limites(temperatura, ph, oxigenio)

    # Exibição de alertas
    exibir_alertas(alertas)

    # Plotar gráficos
    plotar_graficos(temperatura, ph, oxigenio)


# Chamada da função principal
main()
