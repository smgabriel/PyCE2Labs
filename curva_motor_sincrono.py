import numpy as np
import matplotlib.pyplot as plt

# Parâmetros iniciais
X_s = 2.5  # Reatância síncrona
V_phi = 208  # Tensão de fase
delta1 = -17.5 * np.pi / 180  # Conversão de ângulo para radianos
EA1 = 182 * (np.cos(delta1) + 1j * np.sin(delta1))  # Cálculo do fasor EA1

# Definição do intervalo da corrente de campo
IF = np.linspace(3.8, 5.8, 21)

# Inicialização do vetor da corrente de armadura com complexos
IA = np.zeros(21, dtype=complex)

# Iteração sobre cada valor de corrente de campo
for ii, current in enumerate(IF):
    # Cálculo do valor de EA2
    EA2 = 45.5 * current

    # Cálculo do ângulo delta2
    delta2 = np.arcsin(np.abs(EA1) / np.abs(EA2) * np.sin(delta1))

    # Cálculo do fasor EA2
    EA2 = EA2 * (np.cos(delta2) + 1j * np.sin(delta2))

    # Cálculo da corrente de armadura
    IA[ii] = (V_phi - EA2) / (1j * X_s)

# Cálculo da magnitude da corrente de armadura
IA = np.abs(IA)

# Configurações do gráfico
plt.figure(figsize=(10, 6))  # Definir o tamanho do gráfico
plt.plot(IF, IA, color='blue', linewidth=2.0)
plt.xlabel('Corrente de Campo (A)', fontsize=14, fontweight='bold')
plt.ylabel('Corrente de Armadura (A)', fontsize=14, fontweight='bold')
plt.title('Curva V do Motor Síncrono', fontsize=16, fontweight='bold')
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Exibir gráfico
plt.show()