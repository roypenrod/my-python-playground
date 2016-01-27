def squared(number):
    try:
        integer = int(number)
    except ValueError:
        string = number * len(number)
        return string
    else:
        return integer ** 2


print("squared(5):")
print(squared(5))
print(" ")

print("squared(2):")
print(squared(2))
print(" ")

print("squared(\"tim\"):")
print(squared("tim"))
print(" ")

print("squared(\"xxx_\"):")
print(squared("xxxx_"))
print(" ")
