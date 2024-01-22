class MatrixNxN:
    @staticmethod
    def zeroes(n: int):
        assert n >= 0 or n % 1, f"n = {n} is not a natrual number."
        elements = []

        for _ in range(n):
            elements.append([0] * n)

        return MatrixNxN(elements)

    def __init__(self, elements):
        assert type(elements) is list, f"type of elements is {type(elements)} when it should be a list"

        self.elements = elements
        self.n = len(self.elements)

        if self.n == 0:
            self.__class__ = EmptyMatrix
            return
        elif self.n == 1:
            self.__class__ = Matrix1x1
            self.element = self.elements[0][0]
            return

        assert all(type(row) is list for row in elements), f"elements should be deep list, instead got {elements}"
        assert all([len(row) == self.n for row in elements]), "matrix is not square"

    def __str__(self):
        out = '['

        for i in range(self.n):
            for j in range(self.n):
                out += str(self[i, j]) + ' '
            out += '\n '

        return out[:-3] + ']'

    def __getitem__(self, items):
        if type(items) is int:
            return self.elements[items]
        elif len(items) == 1:
            return self.elements[items[0]]
        elif len(items) == 2:
            return self.elements[items[0]][items[1]]
        else:
            raise AssertionError(f"{len(items)}D matrices not supported, only up to 2D")

    def __setitem__(self, key, value):
        if len(key) == 1:
            self.elements[key] = value
        elif len(key) == 2:
            self.elements[key[0]][key[1]] = value
        else:
            raise AssertionError(f"{len(key)}D matrices not supported, only up to 2D")

    def __add__(self, mat2):
        """ O(n^2) time, optimal """
        assert type(mat2) is MatrixNxN, "Non-square matrix addition not yet supported."
        assert self.n == mat2.n, f"({self.n} X {self.n}) matrix not addable to ({mat2.n} X {mat2.n}) matrix."

        out = MatrixNxN.zeroes(self.n)

        for i in range(self.n):
            for j in range(self.n):
                out[i, j] = self[i, j] + mat2[i, j]

        return out

    def __mul__(self, obj2):
        """ Only works with scalar multiplication """
        assert type(obj2) is int or type(obj2) is float

        out = MatrixNxN.zeroes(self.n)

        # Scalar multiplication
        if type(obj2) is int or type(obj2) is float:
            for i in range(self.n):
                for j in range(self.n):
                    out[i, j] = self[i, j] * obj2
            return out

        raise AssertionError(f"Type of obj2 should be int, float, or Matrix, instead got {type(obj2)}.")

    def __sub__(self, mat2):
        return self + -1 * mat2


class EmptyMatrix(MatrixNxN):
    def __init__(self):
        self.elements = []
        self.n = 0

    def __str__(self):
        return '[]'

    def __add__(self, mat2):
        return mat2

    def __mul__(self, obj2):
        return EmptyMatrix()

    def __sub__(self, mat2):
        return super().__sub__(mat2)


class Matrix1x1(MatrixNxN):
    def __init__(self, element):
        self.element = element
        self.n = 1

    def __str__(self):
        return f"[{self.element}]"

    def __add__(self, other):
        assert type(other) in [Matrix1x1, int, float], f"The second object must be a Matrix1x1, int, or float. Instead got {type(other)}"
        if type(other) is Matrix1x1:
            return Matrix1x1(self.element + other.element)
        return self.element + other

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        assert type(other) in [Matrix1x1, int, float], f"The second object must be a Matrix1x1, int, or float. Instead got {type(other)}"
        if type(other) is Matrix1x1:
            return Matrix1x1(self.element * other.element)
        return self.element * other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + -1 * other

    def __rsub__(self, other):
        return other + -1 * self

if __name__ == '__main__':
    # Syntax for zero vector matrices
    zero = MatrixNxN.zeroes(2)
    print(zero)

    zero[0, 0] = 1
    print(zero)

    # 1x1 vector arithmetic
    one_by_one = MatrixNxN([[1]])
    one_by_one2 = MatrixNxN([[2]])

    # Automatic type-setting
    print(type(one_by_one))
    print(type(one_by_one2))

    # Vector-vector arithmetic
    print(one_by_one + one_by_one2)
    print(one_by_one * one_by_one2)
    # Vector-scalar arithmetic
    print(one_by_one + 1)
    print(1 + one_by_one)
    print(one_by_one * 10)
    print(10 * one_by_one)

    # 2x2 vector arithmetic
    four_by_four = MatrixNxN([[1, 2],
                              [3, 4]])
    in_n_out = MatrixNxN([[3, 1],
                          [4, 1]])
    zero4x4 = MatrixNxN([[0, 0],
                         [0, 0]])

    print(four_by_four + zero4x4)
    print(in_n_out + four_by_four)

    # NxN vector arithmetic for N > 2

    big_boy = MatrixNxN([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
    scalar = 10

    print(big_boy * scalar)

    mat1 = MatrixNxN([[-2, 5, 1],
                      [0, 8, -7],
                     [9, -4, -3]])
    mat2 = MatrixNxN([[3, -4, 6],
                      [-5, 2, -1],
                      [8, 9, 0]])

    print(mat1 * mat2)









