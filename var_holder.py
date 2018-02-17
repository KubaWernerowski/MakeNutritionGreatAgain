class var_holder:

    def __init__(self):
        self.awake = True

    def toggleAwake(self):
        if self.awake is True:
            self.awake = False
        else:
            self.awake = True
