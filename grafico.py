import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# DATOS DEL ENSAYO
# ==========================================
# 1. Curva teórica nominal (B = 3950 K, R0 = 10 kOhm @ 25 °C)
T_teo = np.linspace(-10, 85, 300)
T_teo_k = T_teo + 273.15
R_teo = 10.0 * np.exp(3950.0 * (1.0 / T_teo_k - 1.0 / 298.15))

# Tabla 1: Multímetro + Termocupla (Calibración)
T_t1 = [20.0, 1.0, 78.0]
R_t1 = [8.12, 17.0, 6.20]

# Tabla 2: Arduino con parámetros nominales
T_t2 = [21.6, 3.2, 71.0]
R_t2 = [12.164, 29.203, 1.701]

# Tabla 4: Arduino con coeficientes experimentales
T_t4 = [-7.1, 146.6, -901.4]
R_t4 = [11.694, 30.610, 2.171]

condiciones = ['Ambiente', 'Frío', 'Caliente']

# ==========================================
# FIGURA 1: Rango Operativo Físico (R vs T)
# ==========================================
plt.figure(figsize=(4.6, 3.0))

plt.plot(
    T_teo,
    R_teo,
    label='Teórica nominal ($B=3950\\text{ K}$)',
    color='#1f77b4',
    linewidth=1.4,
    alpha=0.85,
)
plt.scatter(
    T_t1,
    R_t1,
    color='#d62728',
    s=35,
    zorder=4,
    marker='o',
    label='T1: Calibración multímetro',
)
plt.scatter(
    T_t2,
    R_t2,
    color='#2ca02c',
    s=35,
    zorder=4,
    marker='s',
    label='T2: Arduino (nominales)',
)
plt.scatter(
    T_t4,
    R_t4,
    color='#9467bd',
    s=35,
    zorder=4,
    marker='^',
    label='T4: Arduino (experimentales)',
)

plt.xlim(-15, 88)
plt.ylim(0, 35)
plt.title('Curva Característica y Puntos en Rango Operativo', fontsize=8.5)
plt.xlabel('Temperatura [°C]', fontsize=8)
plt.ylabel('Resistencia [k$\\Omega$]', fontsize=8)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tick_params(labelsize=7.5)
plt.legend(fontsize=6.8, loc='upper right', frameon=True)
plt.tight_layout()

# ==========================================
# FIGURA 2: Comparación y Divergencia de Temperaturas
# ==========================================
plt.figure(figsize=(4.8, 3.0))

x = np.arange(len(condiciones))
ancho = 0.25

# Barras para cada serie
plt.bar(
    x - ancho,
    T_t1,
    width=ancho,
    label='T1: Termocupla patrón',
    color='#d62728',
    alpha=0.9,
)
plt.bar(
    x,
    T_t2,
    width=ancho,
    label='T2: Arduino (nominales)',
    color='#2ca02c',
    alpha=0.9,
)
plt.bar(
    x + ancho,
    T_t4,
    width=ancho,
    label='T4: Arduino (experimentales)',
    color='#9467bd',
    alpha=0.9,
)

# Etiquetas con el valor exacto sobre/debajo de las barras divergentes
for i in range(len(condiciones)):
  plt.text(
      x[i] + ancho,
      T_t4[i] + (25 if T_t4[i] < 0 else 15),
      f'{T_t4[i]:.1f} °C',
      ha='center',
      va='bottom',
      fontsize=7,
      fontweight='bold',
      color='#4a148c',
  )

plt.axhline(0, color='black', linewidth=0.7, linestyle='--')
plt.xticks(x, condiciones, fontsize=8)
plt.ylabel('Temperatura calculada [°C]', fontsize=8)
plt.title('Divergencia de Temperatura por Modelo Implementado', fontsize=8.5)
plt.ylim(-980, 220)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tick_params(labelsize=7.5)
plt.legend(fontsize=7, loc='upper right', frameon=True)
plt.tight_layout()

plt.show()