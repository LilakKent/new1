# import cmath
#
# def light_math():
#     summa =


#
# def logicalc(self, operation):
#     if operation == "C":
#         self.formula = ""
#     elif operation == "DEL":
#         self.formula = self.formula[0:-1]
#     elif operation == "X^2":
#         self.formula = str((eval(self.formula))**2)
#     elif operation == "=":
#         self.formula = str(eval(self.formula))
#     else:
#         if self.formula == "0":
#             self.formula = ""
#         self.formula += operation
#     self.update()
#
# def update(self):
#     if self.formula == "":
#         self.formula = "0"
#     self.lbl.configure(text=self.formula)
#
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero"
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = addition(num1, num2)
    operation = "+"
elif choice == '2':
    result = subtraction(num1, num2)
    operation = "-"
elif choice == '3':
    result = multiplication(num1, num2)
    operation = "*"
elif choice == '4':
    result = division(num1, num2)
    operation = "/"
else:
    print("Invalid operation choice")
    result = None

if result is not None:
    print(f"Result: {num1} {operation} {num2} = {result}")



