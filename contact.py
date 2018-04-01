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
