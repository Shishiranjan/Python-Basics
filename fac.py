'''
This module defines the classes for exception raised by urllib.request. Whenever there is an error in fetching a URL,this module helps in raising exceptions.
The following are the exceptions raised :
URLError – It is raised for the errors in URLs, or errors while fetching the URL due to connectivity, and has a ‘reason’ proprty that tells a user the reason of error.
HTTPError – It is raised for the exotic HTTP errors, such as the authentication request errors. It is a subclass or URLError.Typical errors include ‘404’ (page not
found)403’ (request forbidden),
and ‘401’ (authentication required).
'''

num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
