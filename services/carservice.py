# Teddi á að massa þennan fæl
from repositories.carrepo import CarRepo
from models.car import Car


class CarService(object):
    """ Sér um aðgerðir með bíla """
    def __init__(self):
        self.__car_repo = CarRepo()
   
    def make_car(self, new_car):
        """ Nýskráir bíl í kerfi """
        self.__car_repo.add_car(new_car)

    def remove_car(self, licence_plate):
        """ Fjarlægir bíl úr kerfi """
        self.__car_repo.remove_car(licence_plate)

    def change_status(self, licence_plate, new_status):
        """ Breytir stöðu bíls """
        self.__car_repo.change_status(licence_plate, new_status)

    def show_cars(self, licence_plate):
        """ Fall sem sýnir upplýsingar um bíl """
        self.__car_repo.get_car(licence_plate)

    def get_list_of_cars(self, a_type, status):
        """ Fall sem sækir lista af öllum bílum """

        """ dict = self.__car_repo.get_all_cars() 
        cars = ""
        for licence_plate, car in dict.items():
            car_string = car.__str__()
            cars += car_string + "\n"
            print(cars)
        return cars """
        
        
        dict = self.__car_repo.get_all_cars()
        string = ""
        for licence_plate, item in dict.items():
            type_of_car = item.get_type()
            status_of_car = item.get_status()
            if type_of_car in a_type and status_of_car in status:
                car_string = item.__str__()
                string += car_string + "\n"
                """ if car[1] in a_type and car[2] in status:
                    car_class = Car(
                        car[0], car[1], car[2])
                    car_list.append(car_class) """    
        return string
