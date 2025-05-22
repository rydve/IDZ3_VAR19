import numpy as np
import matplotlib.pyplot as plt
# Исходные данные (уже отсортированные)
data = [-10.37, -9.52, -6.71, -6.30, -6.03, -5.95, -5.72, -5.36, -5.25, -5.24,
        -4.05, -4.00, -3.94, -3.63, -3.45, -3.38, -2.78, -2.73, -2.53, -2.16,
        -1.94, -1.75, -1.67, -1.59, -0.30, 0.05, 0.15, 0.34, 0.35, 0.63,
        1.00, 1.82, 2.78, 2.86, 3.26, 3.85, 4.12, 4.63, 4.67, 4.74, 4.90,
        5.04, 5.08, 5.44, 6.37, 6.84, 7.60, 8.13, 9.67, 11.25] #вариационный ряд

# Вычисляем эмпирическую функцию распределения
F_x = np.arange(1, len(data) + 1) / len(data)

# Выводим результаты
for x_i, F_i in zip(data, F_x):
    print(f"F({x_i}) = {F_i:.2f}")

n = len(data)

F_emp = np.arange(1, n + 1) / n

plt.step(data, F_x, where="post", linestyle="-", color="blue", label="F(x)")
plt.xlabel("Значение X")
plt.ylabel("F(x)")
plt.title("Эмпирическая функция распределения")
plt.grid(True)
plt.legend()
plt.savefig("empirical_function.png")