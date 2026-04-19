def square_root_bisection(value, tolerance=0.1, iterations=1):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    low, high, result = 0, max(1, value), 0

    if value * value == value:  #Checks for 0 or 1
        result = value
        print(f'The square root of {value} is {result}')
        return result


    max_its = iterations
    its = 0
    while high - low > tolerance:
        if its == max_its:
            print(f'Failed to converge within {max_its} iterations')
            return None
        
        mid = (low + high) / 2
        if mid * mid == value:
            result = mid
            break
        if mid * mid < value:
            result = mid
            low = mid
        else:
            high = mid 
        its += 1

    print(f'The square root of {value} is approximately {result}')
    return result