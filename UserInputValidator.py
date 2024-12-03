class UserInputValidator:
    

    def validate_positive_integers(list):
        added_ints = []
        for item in list:
            if item.isdigit():
                num = int(item)
                if num >= 0:
                    added_ints.append(int(item))
    
        return added_ints
            
