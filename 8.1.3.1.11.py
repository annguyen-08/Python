#function to multiply 2 numbers
def challenge2_multiplication (x, y):
    result = x*y
    return result

#function to add 2 numbers
def challenge3_addition (x, y):
    result = x+y
    if result % 2 == 1:
        result += result
    return result

def main ():
    x = True
    while x:
        try:
            num1 = int(input ("Enter the first number: "))
            num2 = int(input ("Enter the second number: "))
            product = challenge2_multiplication(num1, num2)
            print ("The product of your 2 numbers is", product)
            sum = challenge3_addition(num1, num2)
            print ("The sum of your 2 numbers (plus 1 if odd) is", sum)
            x = False
        except ValueError:
            print ("Type in numbers!")
main ()
