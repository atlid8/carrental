from models.car import Car
from services.carservice import CarService
from ui.ui_standard_functions import UIStandard
HOMECOMMANDS = ["h", "H", "s", "S"]


class CarUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name):
        self.__name = name
        self.__car_service = CarService()
        self.__uistandard = UIStandard(name)

    def print_car_header(self, status_of_car):
        self.print_header()
        print("Bílayfirlit - {}".format(status_of_car))
        print("\t{:<20} | {:<20} | {:<20}".format(
            "Tegund", "Bílnúmer", "Staða"))
        print("\t{}".format("-"*60))

    def print_cars(self, status):
        os.system('cls')
        self.print_car_header(status)
        # sækja upplýsingar til prentunar út frá "status" í parameter

        print("\t{:<20} | {:<20} | {:<20}".format(
            "Jeppi", "K1NG", "þriggjaDekkja"))
        # prenta upplýsingar um bíl

    def car_menu(self):
        '''Bílayfirlit menu fyrir Kerfisstjóra'''
        choice = ""
        while choice not in HOMECOMMANDS:
            os.system('cls')
            choice = self.show_menu(
                "Bílayfirlit\n\t1. Allir bílar\n\t2. Lausir bílar\n\t3. Í útleigu\n\t\
4. Nýskrá bíl\n\t5. Afskrá bíl\n", "Veldu aðgerð: ")
            if choice == "1":
                self.print_cars("Allir bílar")
            elif choice == "2":
                self.print_cars("Lausir bílar")
            elif choice == "3":
                self.print_cars("Í útleigu")
            elif choice == "4":
                new_car = self.add_new_car()
                self.__car_service.make_car(new_car)
            elif choice == "5":
                licence_plate = input("Númer bíls til afskráningar: ")
                print()
                approve_remove_car = input(
                    "Viltu eyða bíl með bílnúmerið {} ((J)á/(N)ei): ".format(
                        licence_plate))
                if approve_remove_car.lower() == 'j':
                    self.__car_service.remove_car(licence_plate)
                    print("\nBíl með númerið {} hefur verið eytt!".format(
                        licence_plate))
                time.sleep(2)

    def add_new_car(self):
        os.system('cls')
        approve_plate = ""
        while approve_plate.lower() != "j":
            os.system('cls')
            self.print_header()
            print("\tFlokkar\n\t{}".format("-"*10))
            print("\t(J)eppi\n\t(F)ólksbíll\n\t(S)endibíll\n")
            a_type = input("Flokkur: ")
            if a_type.lower() == 'j':
                a_type = "Jeppi"
            elif a_type.lower() == 'f':
                a_type = "Folksbill"
            elif a_type.lower() == 's':
                a_type = "Sendibill"
            license_plate = input("Bílnúmer: ")
            print()
            approve_plate = input("Skrá {} með númerið {}\
 ((J)á/(N)ei)? ".format(
                a_type, license_plate))
            new_car = Car(a_type, license_plate)
        else:
            print("\nBíll hefur verið skráður!")
            time.sleep(2)
            return new_car

    def boss_and_salesman_car_menu(self):
        """Pprentar bílayfirlits viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.__uistandard.show_menu(
                """Bílayfirlit\n\t1. Allir Bílar
\t2. Lausir Bílar\n\t3. Í útleigu""")
            if choice == "1" or "2" or "3":
                if choice == "1":
                    menu = "sem eru lausir eða í útleigu"
                    listi1 = ["Fratekinn", "Laus"]
                if choice == "2":
                    menu = "sem eru lausir "
                    listi1 = ["Laus"]
                if choice == "3":
                    menu = "sem eru í útleigu"
                    listi1 = ["Fratekinn"]
                second_choice = input(
                    "\t1. Allar gerðir\n\t2. Jeppar\n\t3. Fólksbílar"
                    "\n\t4. Sendibílar")
                if second_choice == "2":
                    the_type = "Jeppar"
                    listi2 = ["Jeppi"]
                elif second_choice == "3":
                    the_type = "Fólksbílar"
                    listi2 = ["Fólksbill"]
                elif second_choice == "4":
                    the_type = "Sendibílar"
                    listi2 = ["Sendibill"]
                else:
                    the_type = "all_cars"
                    listi2 = ["Sendibill", "Folksbill", "Jeppi"]
            choice = self.second_car_menu(the_type, menu, listi1, listi2)
        return choice

    def second_car_menu(self, the_type, menu, listi1, listi2):
        self.__uistandard.print_header()
        print("Bílayfirlit - {} {}".format(the_type, menu))
        print("\tTegund | Bílnúmer | Staða\n\t", "-"*23)
        strengur = self.__car_service.get_list_of_cars(listi2, listi1)
        print(strengur)
        choice = input("Veldu aðgerð: ")
        return choice