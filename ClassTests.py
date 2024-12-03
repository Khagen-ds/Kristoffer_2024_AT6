from UserInputValidator import UserInputValidator

test1 = UserInputValidator()
test1.validate_positive_integers(["1", "567", "-32", "-15", "100", "Fredrick", "8.9"])


test2 = UserInputValidator()
test2.validate_positive_integers(["-1", "-567", "32", "15", "10000", "Bob", "-8.9"])