def greet(message):
    new_message = message.capitalize()
    print("Hey Hey")
    return new_message


# This calls the function
user_input = input("What greeting do you want? ")
greeting = greet(user_input)

# This prints the variable returned from the function
print(greeting)