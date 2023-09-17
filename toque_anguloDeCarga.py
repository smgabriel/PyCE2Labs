import numpy as np
import matplotlib.pyplot as plt

# Dados do gerador
f = 60  # frequência em Hz
p = 4  # número de polos
V = 480  # tensão em V
Xd = 0.1  # reatância síncrona de eixo direto em Ω
Xq = 0.075  # reatância síncrona de eixo em quadratura em Ω
I = 1200  # corrente em A
pf = 0.8  # fator de potência atrasado
Ea = 524.5 # tensão em V

# Cálculo da velocidade síncrona
n_sync = 120 * f / p

# Vetor de ângulos δ
delta = np.linspace(-np.pi, np.pi, 100)

# Cálculo do torque para pólos lisos
torque = (3*Ea*V*np.sin(delta))/(Xd*n_sync)

# Cálculo do torque em função de δ para rotor de pólos salientes
torque_total = (3*Ea*V*np.sin(delta))/(Xd*n_sync) + ((3 * V**2) / (2 * n_sync)) *((Xd - Xq)/(Xd * Xq))*(np.sin(2*delta))

# Cálculo do torque em função de δ contribuição saliencia 
torque_saliente = ((3 * V**2) / (2 * n_sync)) *((Xd - Xq)/(Xd * Xq))*(np.sin(2*delta))

# Gráfico das curvas de torque x δ
plt.plot(delta, torque, label='Rotor de Pólos Cilíndricos')
plt.plot(delta, torque_total, label='Rotor de Pólos Salientes (total)')
plt.plot(delta, torque_saliente, label='Rotor de Pólos Saliente')
plt.xlabel('Ângulo de carga δ (rad)')
plt.ylabel('Torque (Nm)')
plt.title('Curvas Torque x δ')
plt.legend()
plt.grid()
plt.show()