import Utils.passenger as passenger

class plane:

    def __init__(self, name = None, company = None, nrSeats = 0, destination = None, listPassengers = None):
        """
        initialises the plane instance
        :param name: the name of the plane
        :param company: the airline company of the plane
        :param nrSeats: the number of seats of the plane
        :param destination: the destination of the plane
        :param listPassengers: the list of passengers bording the plne
        """
        self.__name = str(name)
        self.__company = str(company)
        self.__nrSeats = int(nrSeats)
        self.__destination = str(destination)
        self.__listPassengers = []
        if listPassengers != None:
            for passen in listPassengers:
                if isinstance(passen, passenger.Passenger):
                    self.__listPassengers.append(passen)

    @property
    def name(self):
        return self.__name

    @property
    def company(self):
        return self.__company

    @property
    def nrSeats(self):
        return self.__nrSeats

    @property
    def destinaton(self):
        return self.__destination

    @property
    def listOfPassengers(self):
        return self.__listPassengers

    @name.setter
    def name(self, other):
        self.__name = str(other)

    @company.setter
    def company(self, other):
        self.__company = str(other)

    @nrSeats.setter
    def nrSeats(self, other):
        self.__nrSeats = int(other)

    @destinaton.setter
    def destination(self, other):
        self.__destination = str(other)

    @listOfPassengers.setter
    def listOfPassengers(self, other = None):
        if listPassengers != None:
            for passen in listPassengers:
                if isinstance(passen, passenger.Passenger):
                    self.__listPassengers.append(passen)