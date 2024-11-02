def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    # There was nop comma in the split Function
    parts = user_input.split(",")

    # Store the two values in variables
    # Converting the variables to floating variables works, but it should be an integer
    lower_bound = float(parts[0])
    upper_bound = float(parts[1])

    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}