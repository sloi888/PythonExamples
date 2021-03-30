def convertToInt(value):
    try:
        int(value)
        print(f"{value} converted to int")
        return int(value)

    except:
        print(f"Could not convert {value} to an int")
        return 0

    finally:
        print("Thanks for using convertToInt()")

print(convertToInt("apple"))
print(convertToInt("1"))
print(convertToInt("3.5"))
