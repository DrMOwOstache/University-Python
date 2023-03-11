class Passenger:

    def __init__(self, firstName = "Bob", lastName = "Mc'Frail", passport = "0"):
        """
        initialises the passanger instance
        :param firstName: the first name of the passenger
        :param lastName: the last name of the passenger
        :param passport: the passport number of the passenger
        """
        self.__firstName = str(firstName)
        self.__lastName = str(lastName)
        self.__passport = str(passport)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"The {self.__lastName} {self.__firstName} with the passport number {self.__passport}"

    @property
    def firstName(self):
        """
        :return: the first name of the passenger
        """
        return self.__firstName

    @property
    def lastName(self):
        """
        :return: the last name of the passenger
        """
        return self.__lastName

    @property
    def passport(self):
        """
        :return: the passport number of the passenger
        """
        return  self.__passport

    @firstName.setter
    def firstName(self, other):
        """
        set a new name for the first name of the passenger
        :param other: the new name
        """
        self.__firstName = other

    @lastName.setter
    def lastName(self, other):
        """
        set a new name for the last name of the passenger
        :param other: the new name
        """
        self.__lastName = other

    @passport.setter
    def passport(self, other):
        """
        set a new passport number for the passport of the passenger
        :param other: the passport number
        """
        self.__passport = other
