def divide(a,b):
    try:
        return int(a/b)
    except:
        return "Divide by zero is not possible"
    finally:
        print( "in the final")


print(divide(1,0))
