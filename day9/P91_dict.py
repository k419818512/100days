programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "loop":"the action doing something over and over again"
}

print(programming_dictionary["Bug"])

empty_dictionary = {}

# loop through a dictionary
for key in programming_dictionary: 
    print(f"{key}:{programming_dictionary[key]}")