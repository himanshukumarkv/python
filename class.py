# class computer:
#     def __init__(self):
#         print("hello")
# comp1=computer()


# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(self.name,self.age)
# comp2=dog("tomy", 5)
# comp2.greet()
# def p(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("not a prime")
#             else:
#                 print("prime number")
#             break
#     else:
#         print("not a prime number")
# n=int(input())
# p(n)
# class student:
#     school="g"
#     @classmethod
#     def info(cls):
#         return cls.school
# print(student.info())
# class University:
#     def __init__(self, name):
#         self.name = name

#     def display_university_info(self):
#         print(f"University: {self.name}")
#
#     class Department:
#         def __init__(self, name):
#             self.name = name
#
#         def display_department_info(self):
#             print(f"Department: {self.name}")
#
# # Creating instances of University and Department classes
# university_instance = University("Example University")
# department_instance = university_instance.Department("Computer Science")
#
# # Calling instance methods
# university_instance.display_university_info()
# department_instance.display_department_info()
# class H:
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
# obj=H(7,8,9)
# print(obj.avg())
# class H:
#
#     @staticmethod
#     def name():
#         print("jj")
#
# obj=H()
# obj.name()
# try:
#     # Code that may raise an exception
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#
# except ValueError:
#     # Handling a specific type of exception (ValueError)
#     print("Invalid input. Please enter valid numbers.")
#
# except ZeroDivisionError:
#     # Handling another specific type of exception (ZeroDivisionError)
#     print("Cannot divide by zero.")
#
# else:
#     # Code to execute if no exceptions are raised
#     print("Division result:", result)
#
# finally:
#     # Code to execute regardless of whether an exception occurred
#     print("Execution completed. Cleaning up resources.")
# try:
#     # Code that may raise an exception
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#
# except ValueError as ve:
#     # Handling a specific type of exception (ValueError)
#     print(f"Invalid input: {ve}")
#
# except ZeroDivisionError as zde:
#     # Handling another specific type of exception (ZeroDivisionError)
#     print(f"Cannot divide by zero: {zde}")
#
# except (TypeError, ArithmeticError) as e:
#     # Handling multiple exception types in a single except block
#     print(f"An error occurred: {e}")

# else:
#     # Code to execute if no exceptions are raised
#     print("Division result:", result)
#
# finally:
#     # Code to execute regardless of whether an exception occurred
#     print("Execution completed.")
import threading
import time

def print_cube(num):
	# function to print cube of given num
        for i in range(5):
            print("Cube: {}" .format(num * num * num))
            #time.sleep(1)
def print_square(num):
	# function to print square of given num
        for i in range(5):
            print("Square: {}" .format(num * num))
            #time.sleep(4)

t1 = threading.Thread(target=print_square, args=(6,))
t2 = threading.Thread(target=print_cube, args=(9,))
t1.start()
t2.start()
# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()
print("Done!")



