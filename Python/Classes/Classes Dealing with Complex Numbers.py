import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = round(real,2)
        self.imaginary = round(imaginary,2)
    def __add__(self, no):
        real_sum = self.real + no.real
        imaginary_sum = self.imaginary + no.imaginary
        if imaginary_sum >= 0:
            result = "%.2f+%.2fi" % (real_sum, imaginary_sum)
        else:
            result = "%.2f-%.2fi" % (real_sum, abs(imaginary_sum))
        return result
    def __sub__(self, no):
        real_diff = self.real - no.real
        imaginary_diff = self.imaginary - no.imaginary
        if imaginary_diff >= 0:
            result = "%.2f+%.2fi" % (real_diff, imaginary_diff)
        else:
            result = "%.2f-%.2fi" % (real_diff, abs(imaginary_diff))
        return result
    def __mul__(self, no):
        real_sum = (self.real*no.real) - (self.imaginary*no.imaginary)
        imaginary_sum = (self.real*no.imaginary) + (self.imaginary*no.real)
        if imaginary_sum >= 0:
            result = "%.2f+%.2fi" % (real_sum, imaginary_sum)
        else:
            result = "%.2f-%.2fi" % (real_sum, abs(imaginary_sum))
        return result
    def __truediv__(self, no):
        real_sum = (self.real*no.real + self.imaginary*no.imaginary)/(no.real**2 + no.imaginary**2)
        imaginary_sum = (self.imaginary*no.real - self.real*no.imaginary)/(no.real**2 + no.imaginary**2)
        if imaginary_sum >= 0:
            result = "%.2f+%.2fi" % (real_sum, imaginary_sum)
        else:
            result = "%.2f-%.2fi" % (real_sum, abs(imaginary_sum))
        return result
    def mod(self):
        real_sum = (self.real**2+self.imaginary**2)**(1/2)
        result = "%.2f+0.00i" % (real_sum)
        return result
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')