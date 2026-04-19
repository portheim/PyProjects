def square_root_bisection(value, tolerance=0.1, iterations=1):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    low, high, result = 0, max(1, value), 0

    if value * value == value:  #Checks for 0 or 1
        result = value
        print(f'The square root of {value} is {result}')
        return result


    while high - low > tolerance:
        mid = (low + high) / 2

        if mid * mid == value:
            result = mid
            break

        if mid * mid < value:
            result = mid
            low = mid
        else:
            high = mid

    for _ in range(iterations):
        if (result + tolerance) * (result + tolerance) > value:
            break
        while (result + tolerance) * (result + tolerance) <= value:
            result += tolerance
        tolerance /= 10
    else:
        print(f'Failed to converge within {iterations} iterations')
        return None

    print(f'The square root of {value} is approximately {result}')
    return result
