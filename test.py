def decorator():
    def innner_function():
        print("Inside the inner_function()!!")
    return inner_function

        
index = decorator
print(index())
