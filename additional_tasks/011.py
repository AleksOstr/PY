# Функция поворота матрицы на 90 градусов

def rotate(matrix: list, direction: str):
    if direction == 'clockwise':
        matrix.reverse()
        return list(map(list, list(zip(*matrix))))
    elif direction == 'counter-clockwise':
        return list(map(list, list(zip(*list(map(reversed, matrix))))))

arr = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate(rotate(arr, 'counter-clockwise'), 'clockwise'))




