class Matrix:

    def __init__(self, array):
        self.array = array

    def __str__(self):
        str_array = ""
        for arr_string in self.array:
            for arr_number in arr_string:
                str_array += str(arr_number) + "   "
            str_array += "\n"
        return str_array

    def __add__(self, other):
        sum_matrix = [[0 for _ in range(len(self.array))] for _ in range(len(self.array))]
        """PyCharm сам предложил заменить переменные на _. И это работает.)))"""

        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                sum_matrix[i][j] = (self.array[i][j] + other.array[i][j])
        return Matrix(sum_matrix)


my_array1 = [[1, 22, 3], [34, 5, 6], [7, 8, 49]]
my_array2 = [[1, 1, 7], [2, 5, 38], [39, 6, 1]]
my_matrix1 = Matrix(my_array1)
my_matrix2 = Matrix(my_array2)

print("Матрица № 1:")
print(my_matrix1)
print("Матрица № 2:")
print(my_matrix2)

my_matrix3 = my_matrix1 + my_matrix2

print("Сумма матриц:")
print(my_matrix3)
