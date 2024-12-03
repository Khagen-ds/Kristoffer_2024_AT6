from UserInputValidator import UserInputValidator

test1 = UserInputValidator()
test1.validate_positive_integers(["1", "567", "-32", "-15", "100", "Fredrick", "8.9"])


test2 = UserInputValidator()
test2.validate_positive_integers(["-1", "-567", "32", "15", "10000", "Bob", "-8.9"])

# Since I allready had called the method with lists, i will provide a 3rd test as well. 
# This one will call all the methods in the class, printing the list twice

test3 = UserInputValidator()
test3.validate_positive_integers(["0", "55", "-2", "55.6", "-78.2", "Cody", "#¤%", "3", "77"])
test3.list_validated()