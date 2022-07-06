def sum(x,y):
    return(x + y)

def divide(x,y):
    try:
        return(x / y)
    except(ZeroDivisionError):
        return("Error")