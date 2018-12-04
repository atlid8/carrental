#Teddi sér um þennan fæl
from datetime import date
HOMECOMMANDS = ["h", "s"]
POSSIBLE_ACTIONS = "\t1. Pantanir\n\t2. Bílayfirlit\n\
\t3. Viðskiptavinir\n\t4. Starfsmenn\n\t5. Verðlisti\n\t6. Tekjur\n"

class BossUI(object):
    #Sér um viðmót yfirmanns
    def __init__(self, username):
        self.__username = username #strengur sem inniheldur notendanafn
    
    def print_header(self):
        '''prints header for sign-in screen'''
        print("{:40s} {:>54}".format(
            "Yfirmaður - notandi: {}".format(self.__username), str(date.today())))
        print(("-"*100))

    def show_menu(self, possible_operations):
        self.print_header()
        print(possible_operations)

        choice = input("Veldu síðu: ")
        # Inn í þetta vantar að prenta út það sem er fyrir neðan
        return choice

    def main_menu(self):
        #Sýnir upphafsviðmót yfirmanns
        choice = ""
        while choice.lower() != HOMECOMMANDS[1]:
            choice = self.show_menu(POSSIBLE_ACTIONS)
            if choice == "1":
                choice = self.show_all_orders()
            elif choice == "2":
                choice = self.car_menu()
            elif choice == "3":
                self.show_customers()
            elif choice == "4":
                self.show_employees()
            elif choice == "5":
                self.price_menu()
            elif choice == "6":
                self.revenue()

    def show_all_orders(self):
        #from services import orderservice
        self.print_header()
        print("\tdagsetning  |  Pönt.nr.  |  Nafn  |  Kennitala  |  Tegund  |  Bílnr.  |  Staða\n"+("-")*100)
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice
        
    def car_menu(self):
        #Sýnir bílayfirlitsviðmót yfirmanns og kallar á klasa eftir því sem við á
        """Prints car menu and follows up on commands"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""")
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                pass
        return choice

    def show_customers(self):
        """Prints all customers for boss"""
        self.print_header()
        print("\tKennitala  |  Nafn  |  Sími\n"+("-")*100)
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice
    
    def show_employees(self):
        self.print_header()
        print("\tNotendanafn  |  Hlutverk  |  Nafn  |  Sími  |  Heimilisfang\n"+("-")*100)
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice

    def price_menu(self):
        #Sýnir verðlistaviðmót yfirmanns og kallar á klasa eftir því sem við á
        self.print_header()
        print("Verðlisti\n\t{:<12} | {:<12}".format("Jeppi","10000/dag"))
        print("\t{:<12} | {:<12}".format("Fólksbíll","500/dag"))
        print("\t{:<12} | {:<12}".format("Sendibíll","7000/dag"))
        print("\t{:<12} | {:<12}".format("Aukatrygging","5000/dag"))
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("\nBreyta verði (F)ólksbíll, (J)eppi, (S)endibíll, (A)uka trygging: ")
        return choice
    
    def revenue(self):
        self.print_header()
        print("Tekjur\n\t{:<25} | {:<10}\n\t".format("Pöntunarnúmer","Tekjur")+("-")*38)
        print("\t{:<25} | {:>10}".format("000001", "120.000 kr"))
        print("\t{:<25} | {:>10}".format("000002", "10.000 kr"))
        print("\n\t{:<25} | {:<10}\n\t".format("Mánuður","Tekjur")+("-")*38)
        print("\t{:<25} | {:>10}".format("11", "130.000 kr"))
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = input("")
        return choice

    def quit(self):
        #Fer á upphafsskjá
        pass

k1 = BossUI("User1")
k1.main_menu()


    
    