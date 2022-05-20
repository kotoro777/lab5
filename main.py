import numpy as np
import random
import time

print("\n-------Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 3 до 184: "))
    while (row_q < 4) and (row_q > 183):
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 3 до 184: "))
    K = int(input("Введите число К= "))
    start = time.time()
    A = np.zeros((row_q, row_q), dtype=int)        # Задаем матрицы A и F = 0
    F = np.zeros((row_q, row_q), dtype=int)

    t0 = time.time()
    for i in range(row_q):     # Формируем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)
    t1 = time.time()
    print("Matrix A:\n", A, "\ntime:", t1 - t0)

    for i in range(row_q):      # Формируем матрицу F
        for j in range(row_q):
            F[i][j] = A[i][j]

    t0 = time.time()
    E = np.zeros((row_q // 2, row_q // 2), dtype=int)   # Формируем матрицу Е
    for i in range(row_q // 2):
        for j in range(row_q // 2):
            E[i][j] = A[i][j]
    t1 = time.time()
    print("Matrix Е:\n", E, "\ntime:", t1 - t0)

    cnt = 0
    mult = 1

    for i in range(row_q // 2):
        for j in range(row_q // 2):
            if j % 2 != 0 and E[i][j] > K:
                cnt += 1
            if i % 2 != 0:
                mult *= E[i][j]
    print("Кол-во нулей в нечетных столбцах:", cnt, "\nПроизведение чисел в нечетных строках:", mult)

    if cnt > mult:
        print("Меняем C и B симметрично")
        for i in range(row_q // 2):
            for j in range(row_q // 2):
                F[i][row_q // 2 + j] = A[row_q - 1 - i][row_q // 2 + j]
                F[row_q - 1 - i][row_q // 2 + j] = A[i][row_q // 2 + j]
    else:
        print("Меняем C и Е несимметрично")
        for i in range(row_q):
            for j in range(row_q):
                F[i][j] = A[row_q + i][row_q + j]
                F[row_q + i][row_q + j] = A[i][j]
    print("Matrix A:\n", A, "\nMatrix F:\n", F)

    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("Матрица A или F вырождена\n вычисления невозможны")
    elif np.linalg.det(A) > np.trace(F):
        print("1 formula: A*A^T – K * F^-1")
        A = np.dot(A, np.transpose(A)) - (K * np.linalg.inv(F))
    else:
        print("2 formula: (A^-1 +G-F^Т)*K")
        A = (np.linalg.inv(A) + np.tril(A) - np.transpose(F)) * K   # (A^-1 +G-F^T)*K

    print("\nResult: ")
    for i in A:      # Делаем перебор всех строк матрицы # Вывод результата
        for j in i:     # Перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except ValueError:
    print("\nЭто не число!")
