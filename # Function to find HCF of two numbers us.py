# Function to find HCF of two numbers using prime factorization method
def find_hcf(number1, number2):
# Find the factors of both numbers
    factors_num1 = set(i for i in range(1, number1+1) if number1%i == 0)
    factors_num2 = set(i for i in range(1, number2+1) if number2%i == 0)
# Find the common factors of both numbers
    common_factors = factors_num1.intersection(factors_num2)
# Return the maximum value from the common factors
    return max(common_factors)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
HCF = find_hcf(number1, number2)
print("The HCF of the first number",number1,"and the secondnumber",number2,"is",HCF)