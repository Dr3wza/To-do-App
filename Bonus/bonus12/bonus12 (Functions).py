from convertors12 import convert
from parsers12 import parse

# Prompt for user input
feet_inches = input("Enter feet and inches (e.g., 5 8): ")

# Parse the input using the parse function
parsed = parse(feet_inches)

# Validate parsed result to avoid issues if the parsing fails
if parsed and 'feet' in parsed and 'inches' in parsed:
    # Convert feet and inches to meters
    result = convert(parsed['feet'], parsed['inches'])

    # Display result
    print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result:.2f} meters")

    # Check if the kid can use the slide based on the height
    if result < 1:
        print("Kid is too small")
    else:
        print("Kid can use the slide.")
else:
    print("Invalid input. Please enter feet and inches in the correct format.")
