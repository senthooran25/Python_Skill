"""Using a for loop, write a program which asks the user to type an integer,
n, and then prints the sum of the square of all numbers form 1 to n (including both 1 and n).
For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14"""
def sum_square():
    total_square = 0
    user_input = int(input("Enter the number :"))
    for i in range(0, user_input+1):
        total_square = (i*i) + total_square
    print("Total sum of the ", user_input, "square is ", total_square)

sum_square()