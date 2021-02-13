def LongestWordLength(str): 
  
    n = len(str) 
    res = 0; curr_len = 0
      
    for i in range(0, n): 
         
        if (str[i] != ' '): 
            curr_len += 1
   
        else: 
            res = max(res, curr_len) 
            curr_len = 0

    return max(res, curr_len) 
  
s = "Python is the most used language in the world"
print(LongestWordLength(s)) 
