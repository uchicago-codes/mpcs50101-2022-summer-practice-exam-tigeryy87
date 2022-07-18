# Write a function that replaces a string within a string and 
# returns the new string

def replace(original, replace, new):
    """Docstring here"""
    #
    # Your code here
    #

    new_str = ''
    remove_space = original.split()
    for word in remove_space:
        if word == replace:
            new_str += new
        else:
            new_str += word
    return new_str



# Test your function
greeting = "Today is Monday!"
revised = replace(greeting, "Monday", "Funday")

# Test for failure
assert revised != "Today is Monday!"

# Test for success
assert revised == "Today is Funday!"
assert replace("Hello World", "Hello", "Goodbye Cruel") == "Goodbye Cruel World"