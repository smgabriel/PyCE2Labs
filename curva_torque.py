import numpy as np
import matplotlib.pyplot as plt

# Inicialização dos parâmetros do motor
r1 = 0.641  # Resistência do estator [Ohms]
x1 = 1.106  # Reatância do estator [Ohms]
r2 = 0.332  # Resistência do rotor [Ohms]
x2 = 0.464  # Reatância do rotor [Ohms]
xm = 26.3  # Reatância de magnetização [Ohms]
v_phase = 460 / np.sqrt(3)  # Tensão de fase [Volts]
n_sync = 1800  # Velocidade síncrona [RPM]
w_sync = 188.5  # Velocidade síncrona [rad/s]

# Cálculo da tensão e impedância de Thévenin
v_th = v_phase * (xm / np.sqrt(r1**2 + (x1 + xm)**2))  # Tensão de Thévenin [Volts]
z_th = (1j*xm * (r1 + 1j*x1)) / (r1 + 1j*(x1 + xm))  # Impedância de Thévenin [Ohms]
r_th = z_th.real  # Resistência de Thévenin [Ohms]
x_th = z_th.imag  # Reatância de Thévenin [Ohms]

# Definição do escorregamento e cálculo da velocidade mecânica
s = np.linspace(0.001, 1, 51)  # Escorregamento
nm = (1 - s) * n_sync  # Velocidade mecânica [RPM]

# Cálculo do torque para a resistência do rotor original
t_ind1 = [(3 * v_th**2 * r2 / si) / (w_sync * ((r_th + r2/si)**2 + (x_th + x2)**2)) for si in s]

# Cálculo do torque para a resistência do rotor duplicada
t_ind2 = [(3 * v_th**2 * (2*r2) / si) / (w_sync * ((r_th + (2*r2)/si)**2 + (x_th + x2)**2)) for si in s]

# Criação do gráfico de torque versus velocidade de rotação
plt.figure(figsize=(10, 6))
plt.plot(nm, t_ind1, label='Resistência original do rotor', color='darkblue', linewidth=2.0)
plt.plot(nm, t_ind2, label='Resistência duplicada do rotor', color='darkorange', linewidth=2.0, linestyle='-.')
plt.xlabel('Velocidade de rotação (RPM)', fontsize=12, fontweight='bold')
plt.ylabel('Torque (N.m)', fontsize=12, fontweight='bold')
plt.title('Curva de Torque versus Velocidade de Rotação', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True)
plt.show()