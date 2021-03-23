from Polynomial import Polynomial

factorial = lambda i: 1 if i in [0, 1] else int(i) * factorial(int(i) - 1)
e = sum(1 / factorial(n) for n in range(10000))

class Logarithm(Polynomial):
    def __init__(self, base=e, coef=1, fac=1):
        self.b = base
        super().__init__(arr=[0] + [1 / k for k in range(1, 10000)], coef=coef, freq=fac)

    __call__ = lambda s: super().__call__((s - 1) / s)


class Exponential:
    def __init__(self, base=e, coef=1, fac=1):
        self.b, self.c, self.f = base, coef, fac

    _str__ = lambda self: f'{self.b}^({self.c}s)'

    __call__ = lambda self, s: self.b ** (self.c * s)

    integral = lambda self: self

    derivative = lambda self: Sin(self.f, -self.c * self.f)


ln, log2, log10 = [lambda s: Logarithm(base=b) for b in (e, 2, 10)]
exp = Exponential()