class UserInputValidator:
    def __init__(self):
        self._added_ints = []

    def validate_positive_integers(self, list):
        
        for item in list:
            if item.isdigit():
                num = int(item)
                if num >= 0:
                    self._added_ints.append(int(item))
        return self.list_validated()
        

    def list_validated(self):
        print(self._added_ints)
        
            
