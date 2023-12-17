from decimal import Decimal, getcontext
import math

getcontext().prec = 50

float_number = float(input("Enter a floating-point number: "))

# Convert the input to a Decimal for precise calculations
decimal_number = Decimal(str(float_number))

square = float_number**2

square_root = decimal_number ** Decimal('0.5')

sin_result = math.sin(float_number)

cos_result = math.cos(float_number)

tan_result = math.tan(float_number)

print(f"Exponential (power of 2) of {float_number} is: {square}")
print(f"Square root of {float_number} is: {square_root}")
print(f"Sine of {float_number} is: {sin_result}")
print(f"Cosine of {float_number} is: {cos_result}")
print(f"Tangent of {float_number} is: {tan_result}")


