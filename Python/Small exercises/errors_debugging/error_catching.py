def divide(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        return "Please do not divide by zero"
    except TypeError:
        return "Please provide two integers or floats"
    return result


print(divide(4,0))