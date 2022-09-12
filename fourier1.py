import numpy as np

# O sinal a ser analisado

sinal = np.array([1,2,3,4,5,6,7,8])

# Calcula a FFT do sinal

fft_sinal = np.fft.fft(sinal)

# Imprime os resultados

print(fft_sinal)