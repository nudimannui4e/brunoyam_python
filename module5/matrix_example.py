# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

class Matrix:
    """
    Сложение матриц. Возможно только при равном кол-ве элементов
            [ 4 10  ]     [ 3  21 ]    [4+3       10+21 ]
    a + b = | 1 -9  |  +  | -4 10 | =  |1+(-4) (-9) + 10|
            [ 0  50 ]     [ 5  11 ]    [0+5       5+11  ]
    """

    def __init__(self, data):
        self.data = data
        self.n = len(data)      # Кол-во строк
        self.m = len(data[0])   # Кол-во столбцов

    def __add__(self, other):
        """
        __add__ - что-то типа сумматора
        тут сравниваются 2 матрицы, если они
        имеют одинаковое кол-во строк \ столбцов
        """

        if self.m == other.m and self.n == other.n:
            # Сюда пойдут элементы, после сложения
            data1 = []
            # Идем по строкам
            for i in range(self.n):
                # список текущих элементов
                curr_data = []
                # Идем по столбцам
                for j in range(self.m):
                    # Складываем элементы
                    curr_data.append(self.data[i][j] + other.data[i][j])
                data1.append(curr_data)
            return Matrix(data1)
        else:
            return 'False'


m1 = Matrix([[1,2], [1,2]])
m2 = Matrix([[1,0], [0,1]])
m3 = m1 + m2

print(m3.data)