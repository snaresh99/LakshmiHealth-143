# First function (Note the use of xrange since this is in Python 2)
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1): 
        final_sum += x
    
    return final_sum

# Better approach:
def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2


You'll notice both functions have the same result, but completely different algorithms. You'll note that the first function iteratively adds the numbers, while the second function makes use of:
 

So how can we objectively compare the algorithms? We could compare the amount of space they take in memory or we could also compare how much time it takes each function to run. We can use the built in %timeit magic function in jupyter to compare the time of the functions. The %timeit magic in Jupyter Notebooks will repeat the loop iteration a certain number of times and take the best result. Check out the link for the documentation.

Let's go ahead and compare the time it took to run the functions:

Objective for Big O notation:
1. objectively compare the algorithms?
    * We could also compare how much time it takes each function to run.
    * We can use built in %timeit magic function in jupyter to compare the time of the functions.
    * %timeit magic in jupyter notebooks will repeat the loop iteration of a certain number of times and take the best result.

    example: %timeit sum1(100)

    
