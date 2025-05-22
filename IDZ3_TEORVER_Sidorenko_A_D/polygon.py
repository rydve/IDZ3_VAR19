import numpy as np
import matplotlib.pyplot as plt
# Определяем интервалы
bins = np.arange(-10.37, 11.25 + 2.00, 2.00)

# Вычисляем середины интервалов
bin_centers = (bins[:-1] + bins[1:]) / 2

# Вывод результатов
print("Середины интервалов:", bin_centers)

# Частоты из гистограммы
frequencies = [2, 1, 7, 9, 5, 7, 4, 9, 3, 1, 2]


# Построение полигона частот
plt.plot(bin_centers, frequencies, marker='o', linestyle='-', color='blue', label="Полигон частот")
plt.xlabel("Середины интервалов")
plt.ylabel("Частота")
plt.title("Полигон частот")
plt.grid(True)
plt.legend()

plt.savefig("polygon.png")