def square_root_bisection(value, tolerance=0.1, iterations=10):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    if value > 4:
        high = value / 2
    else:
    high = max(1, value)    

    low, result = 0, 0

    if value * value == value:  #Checks for 0 or 1
        result = value
        print(f'The square root of {value} is {result}')
        return result

    its = 0
    while high - low > tolerance:
        if its == iterations:
            print(f'Failed to converge within {iterations} iterations')
            return None

        mid = (low + high) / 2
        sq_mid = mid * mid

        if sq_mid == value:
            result = mid
            break
        if sq_mid < value:
            result = mid
            low = mid
        else:
            high = mid 
        its += 1

    print(f'The square root of {value} is approximately {result}. Done in {its} iterations.')
    return result

square_root_bisection(1000, 0.1, 20)