#Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
class Matrix:
    '''Класс Matrix обеспечивает базовые операции с матрицами.'''
    def __init__(self, rows, cols): 
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = str()
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"

        return result

    def __repr__(self):
        return f"Matrix({len(self.data)}, {len(self.data[0])})"

    def __eq__(self, other): 
        '''Метод, определяющий операцию "равно" для двух матриц.'''    
        if self.rows != other.rows or self.cols != other.cols:
            return False
        else:
            return all([self.data[i][j] == other.data[i][j] for j in range(self.cols) for i in range(self.rows)])

    def __add__(self, other): 
        '''Метод, определяющий операцию сложения двух матриц.'''
        if self.rows != other.rows or self.cols != other.cols:
            result = None
        else:        
            result = Matrix(self.rows, self.cols)
            result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]

        return result

    def __mul__(self, other): 
        '''Метод, определяющий операцию умножения двух матриц'''
        if self.cols != other.rows:
            result = None
        else: 
            result = Matrix(self.rows, other.cols)
            result.data = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data]

            matrix = Matrix(self.rows, other.cols)
            matrix.data = [[tuple(str(a) + 'x' + str(b) for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data]
            print(matrix)            
            
        return result


if __name__ == "__main__":
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)
    print(matrix2)

    print(repr(matrix1))
    print(repr(matrix2))

    # Сравниваем матрицы
    print(matrix1 == matrix2)

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    print(matrix3)
    print(matrix4)

    result = matrix3 * matrix4
    print(result)