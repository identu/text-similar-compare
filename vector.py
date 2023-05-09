import math


class vector:

    def __init__(self, d) -> None:
        # vector's dimension
        self._coords = d
        # a list to store all dimension num
        self._dimension = len(d)

    def __str__(self):
        # remove empty after comma
        return ",".join(str(x) for x in self._coords)

    def __len__(self):
        return self._dimension

    def __getitem__(self, index):
        return self._coords[index]

    def __add__(self, other):
        result = []
        for i in range(0, self._dimension):
            result.append(self._coords[i] + other._coords[i])
        return vector(result)

    def __sub__(self, other):
        result = []
        for i in range(0, self._dimension):
            result.append(self._coords[i] - other._coords[i])
        return vector(result)

    def __abs__(self):
        sum = 0
        for m in self._coords:
            sum += m * m
        return math.sqrt(sum)

    # multiply a number
    def scale(self, scale):
        result = []
        for i in range(0, self._dimension):
            result.append(self._coords[i] * scale)
        return vector(result)

    # dot multiply
    def dot(self, other):
        sum = 0
        for i in range(0, self._dimension):
            sum += self._coords[i] * other._coords[i]
        return sum

    def direction(self):
        length=abs(self)
        result = []
        for i in range(0, self._dimension):
            result.append(self._coords[i] / length)
        return vector(result)


