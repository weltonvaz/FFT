import matplotlib.pyplot as plt
import numpy as np
import cmath

# O sinal a ser analisado

sinal = np.array([1,2,3,4,5,6,7,8])

# Calcula a FFT do sinal

fft_sinal = np.fft.fft(sinal)

# Cria o gráfico

plt.plot(fft_sinal)

# Exibe o gráfico

plt.show()