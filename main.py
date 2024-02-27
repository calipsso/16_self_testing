import math

class Kalkulacka:

    def sucetFunc(self, a, b):
        sucet = a+b
        return sucet

    def sucinFunc(self, a, b):
        sucin = a*b
        return sucin

    def delFunc(self, a, b):
        delenie = a//b
        return delenie

    def defPrepona(self,a, b):
        prepona = a**2 + b**2
        return prepona

    def defQuadRov(self, a, b, c):

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) // (2 * a)
            root2 = (-b - math.sqrt(discriminant)) // (2 * a)
            return (root1, root2)

        elif discriminant == 0:
            root = -b / (2 * a)
            return (root)
        else:
            pass


kalkulacka = Kalkulacka()


print(f"sucet {kalkulacka.sucetFunc(8, 12)}")
print(f"sucin {kalkulacka.sucinFunc(78, 66)}")
print(f"delenie {kalkulacka.delFunc(789, 45)}")
print(f"prepona je: {kalkulacka.defPrepona(2, 3)}")
print(f"delenie je: {kalkulacka.delFunc(12, 9)}")
print(f"korene kv rovnice {kalkulacka.defQuadRov(1, -3, 1)}")


