# Глава 3 — матрица как преобразование
import numpy as np
import matplotlib.pyplot as plt

# Исходный вектор (синий)
v = np.array([2, 1])

# Матрица поворота на 90 градусов против часовой стрелки
M = np.array([[0, -1],
              [1,  0]])

# Применяем преобразование
v_transformed = M @ v  # @ означает умножение матрицы на вектор

print("Исходный вектор v:", v)
print("Матрица поворота M:")
print(M)
print("M @ v =", v_transformed)

# Визуализация
plt.figure(figsize=(6, 6))

# Исходный вектор
plt.arrow(0, 0, v[0], v[1], head_width=0.15, head_length=0.15, fc='blue', ec='blue', label=f'v = {v}')

# Преобразованный вектор
plt.arrow(0, 0, v_transformed[0], v_transformed[1], head_width=0.15, head_length=0.15, fc='red', ec='red', label=f'M @ v = {v_transformed}')

# Настройки
plt.xlim(-3, 3)
plt.ylim(-1, 3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.grid(alpha=0.3)
plt.legend()
plt.title('Матрица как преобразование (поворот на 90°)')

plt.savefig('matrix_transform.png', dpi=150)
plt.show()

print("\nКартинка сохранена как matrix_transform.png")
