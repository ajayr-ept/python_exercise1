'''Write a Python program to get a string which is n
 (non-negative integer) copies of a given string.
'''

def myfunc(str, n):
   ans = "" # emty variable
   for i in range(n): #define for loop and range
      ans = ans + str #here logic
   return ans

print(myfunc('Ajay,', 2))
