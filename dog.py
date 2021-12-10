class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []
    def get_name(self):
        return self.name
    def sit(self):
        print(self.name," sits.")
        self.trick_list.append("sit")
    def stay(self):
        print(self.name," stays.")
        self.trick_list.append("stay")
    def do_backflip(self):
        print(self.name, " does a backflip.")
        self.trick_list.append("does a backflip")
    def print_trick_list(self):
        if len(self.trick_list) == 0:
            print(self.name," has not performed any tricks.")
        else:
            for trick in self.trick_list:
                print(self.name + " has performed " + trick)





