class ComplexNumber:    def __init__(self, real, imag):        self.real = real        self.imag = imag    def __str__(self):        return '\n'.join(f"{attr}: {value}" for attr, value in self.__dict__.items())    def conjugate(self) -> 'ComplexNumber':        return ComplexNumber(self.real, self.imag*(-1))    def __abs__(self):        return ((self.real)**2 + (self.imag)**2)    def __lt__(self, other):        return abs(self) < abs(other)    def __gt__(self, other):        return abs(self) > abs(other)    def __eq__(self, other):        return self.real == other.real and self.imag == other.imag    def __ne__(self, other):        return not self.__eq__(other)    def __add__(self, other):        return ComplexNumber(self.real+ other.real, self.imag + other.imag)    def __sub__(self, other):        return ComplexNumber(self.real-other.real, self.imag-other.imag)    def __mul__(self, other):        return ComplexNumber(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)    def __truediv__(self, other):        c = ComplexNumber(self.real, self.imag) *other.conjugate()        c.real /= abs(other)        c.imag /= abs(other)        return cc1 = ComplexNumber(3, 4)c2 = c1.conjugate()print(abs(c1))z1 = ComplexNumber(4, 5)z2 = ComplexNumber(1, -2)print(z1*z2)print(abs(z2))print(z1 / z2)print(z1* z2.conjugate())print(z1 != z2)print(z1 == z1)