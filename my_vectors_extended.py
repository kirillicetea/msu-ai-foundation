v =  [2,3]
w = [-1,2]

def add_vectors(v, w):
    result = []
    for i in range(len(v)):
        result.append(v[i] + w[i])
    return result

def subtract_vectors(v, w):
    result = []
    for i in range(len(v)):
        result.append(v[i] - w[i])
    return result

def scalar_multiply(v, scalar):
    result = []
    for i in range(len(v)):
        result.append(v[i] * scalar)
    return result

# Проверки
print(add_vectors([2, 3], [-1, 2]))       # [1, 5]
print(subtract_vectors([2, 3], [-1, 2]))  # [3, 1]
print(scalar_multiply([2, 3], 3))         # [6, 9]
