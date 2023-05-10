from vector import Vector


class Sketch:
    def __init__(self, text, k, d):
        freq = []
        for i in range(d):
            freq.append(0)
        for j in range(len(text) - k):
            kgram = text[j:j + k]
            freq[hash(kgram) % d] += 1
        vector = Vector(freq)
        self._sketch = vector.direction()

    def similarTo(self, other):
        return self._sketch.dot(other._sketch)

    def __str__(self):
        return str(self._sketch)
