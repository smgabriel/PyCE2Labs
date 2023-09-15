import numpy as np
import matplotlib.pyplot as plt

# Dados do problema
p = 4  # polos
f = 60  # Hz
V_L = 480  # V
X_d = 0.1  # Ω
X_q = 0.075  # Ω
I_f = 1200  # A
pf = 0.8  # fator de potência atrasado
V_ph = V_L / np.sqrt(3)

# a) Curva torque x δ para rotor de pólos cilíndricos com reatância Xd
delta = np.linspace(0, 2 * np.pi, 1000)
E_a = V_ph + I_f * X_d * np.exp(1j * np.arccos(pf))

T_cilindricos = (3 * np.abs(E_a) * V_ph * np.sin(delta)) / (2 * np.pi * f * X_d)

# b) Curva torque x δ para rotor de pólos salientes
T_salientes = (3 * np.abs(E_a) * V_ph * (X_d - X_q) * np.sin(2 * delta)) / (4 * np.pi * f * X_d * X_q)

# c) Ângulo de carga δ no qual o torque da máquina de polos salientes é máximo
delta_max_torque = np.degrees(0.5 * np.arcsin(X_d / (X_q + X_d)))

# Plotando as curvas
plt.figure()
plt.plot(np.degrees(delta), T_cilindricos, label='Rotor de pólos cilíndricos')
plt.plot(np.degrees(delta), T_salientes, label='Rotor de pólos salientes')
plt.axvline(x=delta_max_torque, linestyle='--', color='r', label=f"δ máximo: {delta_max_torque:.2f}°")
plt.xlabel("Ângulo de carga δ (°)")
plt.ylabel("Torque (N·m)")
plt.title("Curva Torque x δ")
plt.legend()
plt.grid()
plt.show()