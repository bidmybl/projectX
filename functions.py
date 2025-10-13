#TODO: 
# Ввод матриц - complete✅
# Детерминант - complete✅
# Вычитание - complete✅
# Сложение - in process❌
# Союзная матрица - complete✅
# Обратная матрица - in process❌
# Умножение на число - complete✅
# Создание единичной матрицы любого порядка - in process❌
# Создание нуль матрицы - in process❌
# Красивый вывод - complete✅


def input_matrix_square() -> list[list[float]]:
    """Ввод матрицы n-го порядка с проверкой ввода"""    
    # Проверка ввода порядка матрицы
    while True:
        try:
            n = int(input("Введите порядок матрицы: "))
            if n <= 0:
                print("Порядок матрицы должен быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число для порядка матрицы!")
    
    print(f"Введите элементы матрицы {n}x{n} построчно:")
    matrix = []
    
    for i in range(n):
        while True:
            try:
                input_line = input(f"Строка {i+1}: ").strip()
                if not input_line:
                    print("Строка не может быть пустой!")
                    continue
                    
                elements = input_line.split()
                if len(elements) != n:
                    print(f"Ошибка: ожидается {n} элементов в строке, получено {len(elements)}")
                    continue
                
                # Пробуем преобразовать все элементы в числа
                row = []
                for j, element in enumerate(elements):
                    try:
                        num = float(element)
                        row.append(num)
                    except ValueError:
                        print(f"Ошибка: элемент '{element}' в позиции {j+1} не является числом!")
                        raise ValueError
                
                matrix.append(row)
                break
                
            except ValueError:
                print("Пожалуйста, введите только числа, разделенные пробелами!")
            except KeyboardInterrupt:
                print("\nВвод прерван пользователем")
                return None
            except Exception as e:
                print(f"Произошла ошибка: {e}")
    
    return matrix


def input_matrix_rectangular() -> list[list[float]]:
    """Компактная версия ввода прямоугольной матрицы"""
    # Ввод размеров с проверкой
    def get_positive_integer(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Число должно быть положительным!")
            except ValueError:
                print("Введите целое число!")
    
    rows = get_positive_integer("Введите количество строк: ")
    cols = get_positive_integer("Введите количество столбцов: ")
    
    print(f"\nВведите {rows} строк по {cols} чисел:")
    matrix = []
    
    for i in range(rows):
        while True:
            try:
                input_line = input(f"Строка {i+1}: ").strip()
                if not input_line:
                    print("Строка не может быть пустой!")
                    continue
                    
                elements = input_line.split()
                if len(elements) != cols:
                    print(f"Нужно {cols} чисел, получено {len(elements)}")
                    continue
                
                # Проверяем, что все элементы - числа
                row = []
                for element in elements:
                    try:
                        row.append(float(element))
                    except ValueError:
                        print(f"Элемент '{element}' не является числом!")
                        raise ValueError
                
                matrix.append(row)
                break
                
            except ValueError:
                print("Пожалуйста, вводите только числа!")
            except KeyboardInterrupt:
                print("\nВвод прерван")
                return None
    
    return matrix


def matrix_det(matrix: list[list[float]]) -> float:
    """
    Вычисляет детерминант матрицы любого порядка
    
    Аргументы: matrix - матрица в виде списка списков
    
    Возвращает: float - значение детерминанта матрицы
    """
    # Проверка, что матрица квадратная
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Детерминант бывает только у квадратной матрицы😢")
    
    # Базовые случаи для матриц малого порядка
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    if n == 3:
        # Правило треугольника(Саррюса) для матрицы 3x3
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                matrix[0][1] * matrix[1][2] * matrix[2][0] +
                matrix[0][2] * matrix[1][0] * matrix[2][1] -
                matrix[0][2] * matrix[1][1] * matrix[2][0] -
                matrix[0][1] * matrix[1][0] * matrix[2][2] -
                matrix[0][0] * matrix[1][2] * matrix[2][1])
    
    # Вычисление для матриц большего порядка
    determinant = 0
    # Разложение по первой строке
    for j in range(n):
        # Создаем минор - матрица без первой строки и j-го столбца
        minor = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            minor.append(row)
        
        # Рекурсивно вычисляем определитель минора
        minor_det = matrix_det(minor)
        
        # Добавляем к общей сумме с учетом знака
        sign = 1 if j % 2 == 0 else -1
        determinant += sign * matrix[0][j] * minor_det
    
    return determinant


def matrix_subtraction(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """Вычитание матриц
    Аргументы: matrix1, matrix2 - матрицы(первая минус вторая)
    Возвращает: матрицу-результат вычитания
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Размерности матриц не совпадают")
    
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] 
            for i in range(len(matrix1))]


def matrix_multiply_by_scalar(matrix:list[list[float]]) -> list[list[float]]:
    """
    Принимает матрицу, запрашивает число и возвращает матрицу, умноженную на это число
    
    Args:
        matrix: исходная матрица
    
    Returns:
        result: результирующая матрица
    """
    while True:
        try:
            scalar_input = input("Введите число для умножения матрицы: ").strip()
            if not scalar_input:
                print("Число не может быть пустым!")
                continue
                
            scalar = float(scalar_input)
            break
        except TypeError:
            print("Ошибка: введите корректное число!")
            
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    
    return result

def matrix_algebraic_complement(matrix: list[list[float]]) -> list[list[float]]:
    """Нахождение союзной матрицы(понадобится для нахождения обратной)
    Аргументы: matrix - матрица, для которой будет найдена союзная
    Возвращает: союзную матрицу
    """
    
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    def minor_det(mat, excl_row, excl_col):
        """Определитель минора"""
        minor = [row[:excl_col] + row[excl_col+1:] 
                for i, row in enumerate(mat) if i != excl_row]
        return matrix_det(minor)
    
    print("Алгебраическое дополнение введенной матрицы:", end='')
    return [[(1 if (i+j)%2==0 else -1) * minor_det(matrix, i, j) 
            for j in range(n)] for i in range(n)]


def print_matrix(matrix:list[list[float]], title="Матрица") -> None:
    """
    Красивый вывод матрицы
    
    Аргументы: matrix: матрица для вывода, title: заголовок
    """
    if not matrix:
        print("Матрица пуста")
        return
    
    print(f"\n{title} {len(matrix)}x{len(matrix[0])}:")
    print("─" * (len(matrix[0]) * 10))
    
    for row in matrix:
        # Форматируем числа для красивого вывода
        formatted_row = [f"{x:8.3f}" if isinstance(x, float) else f"{x:8}" for x in row]
        print(" ".join(formatted_row))
    
    print("─" * (len(matrix[0]) * 10))

# Некоторые тесты:

# print(f"Determinant = {matrix_det(input_matrix())}")
# print(f"Determinant = {print_matrix(matrix_subtraction(input_matrix_square(), input_matrix_square()))}")
# print(print_matrix(algebraic_complement_matrix_compact(input_matrix_square())))
# print(print_matrix(input_matrix_rectangular()))
# print_matrix(matrix_multiply_by_scalar(input_matrix_rectangular()))