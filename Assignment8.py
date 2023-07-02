class A:
    def __init__(self, a, b, c):
        self.__a = a  # Private member
        self._b = b   # Protected member
        self.c = c    # Public member

    def display(self):
        print("Class A:")
        print("Private member (a): Not Accessible")
        print("Protected member (b):", self._b)
        print("Public member (c):", self.c)


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def display(self):
        print("Class B:")
        print("Private member (a): Not Accessible")
        print("Protected member (b):", self._b)
        print("Public member (c):", self.c)


try:
    a = A(10, 20, 30)
    b = B(100, 200, 300)

    a.display()

    b.display()

    print("Trying to access private member 'a' from outside the class:", a._A__a)

except AttributeError as e:
    print("Error:", e)
