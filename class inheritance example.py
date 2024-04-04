class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_x_and_y(self):
        print(f"x: {self.x}, y: {self.y}")

class B(A):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show_z(self):
        print(f"z: {self.z}")

class C(B):
    def __init__(self, x, y, z, p):
        super().__init__(x, y, z)
        self.p = p

    def show_p(self):
        print(f"p: {self.p}")

# Example usage:
obj_c = C(1,2,3,4)
obj_c.show_x_and_y()
obj_c.show_z()
obj_c.show_p()