"""Write a program that asks the user for an input 'n'
(assume that the user enters a positive integer)
and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines.
For example if 'n' is equal to 4 then the output should look like the following:
1
10
100
1000
10000"""

# def power_ten():
#     n = int(input("Enter the nuber :"))
#     for i in range(0, n+1):
#         print(10 ** i)
#
# power_ten()


m = 0
for x in [3,5,3]:
   for y in range (10,11):
      m = m + x + y
print (m)