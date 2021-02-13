#  Like other languages, python also provides the runtime errors via exception handling method with the help of try-except. Some of the standard exceptions which are
# most frequent include IndexError, ImportError, IOError, ZeroDivisionError, TypeError.
#Let us try to access the array element whose index is out of bound and handle the corresponding exception.
'''
a = [2, 5, 6, 8]

try:
    print('Second element is 5')

    print('Fifth element is 9')

except IndexError:
    print('An error occured')
    '''

# Program to handle multiple error with one except statement.

'''
try :  
    a = 3
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print ('Value of b = ', b) 
  
# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
    print ('\nError Occurred and Handled')
    '''

#In python, you can also use else clause on try-except block which must be present after all the except clauses.The code enters the else block only  if the try
# clause doesnot raise an exception.

# Program to depict else clause with try-except

# Function which returns a/b 
def AbyB(a , b): 
    try: 
        c = ((a+b) / (a-b)) 
    except ZeroDivisionError: 
        print ('a/b result in 0')
    else: 
        print(c) 
  
# Driver program to test above function 
AbyB(2.0, 3.0) 
AbyB(3.0, 3.0) 
