# Глава 1 — сложение векторов
import numpy as np
import matplotlib.pyplot as plt

# Два вектора (как в видео 3Blue1Brown)
v = np.array([2, 3])   # зелёный
w = np.array([-1, 2])  # синий

# Сложение векторов
v_plus_w = v + w       # красный

# Умножение на скаляр
v_scaled = v * 1.5     # оранжевый

# Вывод в консоль
print("Вектор v:", v)
print("Вектор w:", w)
print("v + w =", v_plus_w)
print("1.5 * v =", v_scaled)

# Визуализация
plt.figure(figsize=(6, 6))

# Стрелки
plt.arrow(0, 0, v[0], v[1], head_width=0.15, head_length=0.15, fc='green', ec='green', label='v = [2, 3]')
plt.arrow(0, 0, w[0], w[1], head_width=0.15, head_length=0.15, fc='blue', ec='blue', label='w = [-1, 2]')
plt.arrow(0, 0, v_plus_w[0], v_plus_w[1], head_width=0.15, head_length=0.15, fc='red', ec='red', label='v + w = [1, 5]')
plt.arrow(0, 0, v_scaled[0], v_scaled[1], head_width=0.15, head_length=0.15, fc='orange', ec='orange', label='1.5 * v = [3, 4.5]')

# Настройки графика
plt.xlim(-3, 5)
plt.ylim(-1, 7)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.grid(alpha=0.3)
plt.legend()
plt.title('Сложение векторов (Глава 1)')

# Сохранить картинку
plt.savefig('vectors_plot.png', dpi=150)
plt.show()

print("\nКартинка сохранена как vectors_plot.png")
