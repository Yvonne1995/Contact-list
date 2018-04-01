# class Contact:
#     """
#     Class that generates new instances of contacts
#     """
#     contact_list = [] # Empty contact list
#     def __init__(self,first_name,last_name,number,email):
#         # '''
#         # __init__method that helps us define properties for our objects.
#         #
#         # Arg:
#         #     first_name: New contact first name.
#         #     last_name: New contact last name.
#         #     number: New contact phone number.
#         #     email : New contact email address.
#         # '''
#         # docstring removed for simplicity
#
#         self.first_name = first_name
#         self.last_name = last_name
#         self.number = number
#         self.email = email

class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    contact_list = [] #Empty contact list
#Init contact list
    def save_contact(self):
        '''
        save_contact method saves contact objects int contact_list
        '''

        Contact.contact_list.append(self)

    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number

        Args:
            number: Phone number to search for
        Returns:
            Contact of person that matches that number.
        '''

        for contact in cls.contact_list:
            if contact.number == number:
                return contact


    # @classmethod
    # def contact_exist(cls, number):
    #     '''
    #     Method that checks if a contact exists from the contact list.
    #     Args:
    #         number: Phone number to search if it exists
    #     Returns :
    #         Boolean: True or false depending if the contact exists
    #     '''
    #     for contact in cls.contact_list:
    #         if contact.number == number:
    #                 return True
    #
    #     return False
    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the cntact list.
        Arg:
            number: Phone number to search if it exists
        Returns:
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.number == number:
                return True

        return False
