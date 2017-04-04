def prime_function(n):
    try:
        if isinstance(n, int) is False:
            raise TypeError
        if n <= 0 or n == 1:
            return 'Invalid input'
        prime_list = []
        for i in range(2, n+1):
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                if i in [2, 3, 5, 7]:
                    prime_list.append(i)
            else:
                prime_list.append(i)
    except TypeError:
        raise TypeError("The provided input is not an integer!")
    return prime_list

# The first seven lines leading up to the for loop for a constant execution time.
# This means that regardless of the size of n, the execution time of those lines of code does not increase
# The For loop in my function runs n-2 times and the code therein increases in execution time by the size of n.
# The larger the size of n, the longer it takes. The Execution times increases linearly.
# Other code outside the for loop has constant execution time per statement
# Hence the complexity of our function can be said to be O(n) as time increases directly proportional to input.