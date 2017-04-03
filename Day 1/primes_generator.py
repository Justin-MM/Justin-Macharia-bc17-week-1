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