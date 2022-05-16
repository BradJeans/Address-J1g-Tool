import random 
class jigger():
    def __init__(self):
        self.Address1_valid = False
        while not self.Address1_valid:
            self.Address1  = input("Please Enter Address Line 1\n:")
            if self.Address1:
                if str(self.Address1):
                    try:
                        if int(self.Address1):
                            self.Address1_valid = False
                            print("You Have Input A Integer\nPlease Retry")

                    except:
                        self.Address1_valid = True
     
inst1 = jigger()
        