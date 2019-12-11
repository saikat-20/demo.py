
class Addressbook():
    def add_number(self):
        self.numbers = {}
        count = "y"
        while count.lower() == "y":
                name = input("Name: ")
                phone = input("Number: ")
                address = input("Address: ")
                email = input("Email: ")
                self.numbers[phone] = [name,address,email]
                cont = input("Do you want to Continuee(y/n) ")
                if cont == "n":
                    break
        print(self.numbers)

    def search_member_by_name(self):
        name = input("Search By Name: ")
        for key, value in self.numbers.items():
            if name in value[0]:
                print("The Search Name details : "+key,":",value)
                #fprint(difflib.get_close_matches(name,[value]))

    def search_member_by_address(self):
        address = input("Search By Address: ")
        for key,value in self.numbers.items():
            if address in value:
                print("The Search address Details : "+ key,":",value)


    def search_member_by_number(self):
        phone = input("Search By Phone: ")
        if phone in self.numbers.keys():
            print("The Search Number Details: ", self.numbers[phone])
        else:
            print(phone, "search number was not found")

    def demo(self):
        name=input("Enter your name: ")


addressbook=Addressbook()
addressbook.add_number()
addressbook.search_member_by_name()
addressbook.search_member_by_address()
addressbook.search_member_by_number()
