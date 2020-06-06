# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kate Golenkova,06/04/2020,Created code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kate Golenkova,06/04/2020, Modified code to complete assignment 8
    """
    # pass
    # TODO: Add Code to the Product class
    # --Fields--

    # --Constructor--
    def __init__(self, product_name: str, product_price: float):
        # --Attributes--
        self.product = product_name
        self.price = product_price

    # --Properties--
    # Product name
    @property
    def product_name(self): # (getter or accessor)
        return str(self.product).title() # Title case

    @product_name.setter # The Name matches the property
    def product_name(self, value): # (setter or mutator)
        if str(value).isdigit() == False:
            self.product = value
        else:
            raise Exception("Product name cannot be number!")

    # Product price
    @property
    def product_price(self):  # (getter or accessor)
        return float(self.price)

    @product_price.setter  # The Name matches the property
    def product_price(self, value):  # (setter or mutator)
        self.price = value


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name, list_of_product_objects) -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kate Golenkova, 06/04/2020, Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file
    # --Methods--
    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects): # Reads data from a file into a list
        list_of_product_objects = []
        try:
            file = open(file_name, "r")
            for i in file:
                objProduct = Product('', 0.0)  # object of Product class
                data = i.split(" | ")
                objProduct.product_name = data[0]
                objProduct.product_price = data[1]
                list_of_product_objects.append(objProduct)
            file.close()
            return list_of_product_objects

        except FileNotFoundError as e:
            print("There is nothing in this file. Please use option '2' to add new data.")
            return []

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects): # Save data to a file in proper format
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write("{0} | {1}\n".format(row.product_name, row.product_price))
        file.close()
        return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Perfoms Inputs and Outputs:

    methods:
        show_menu() - show menu to user

        input_menu_choice() - ask user for an option

        show_current_data(list_of_product_objects)

        input_new_data(new_data)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kate Golenkova, 06/06/2020, Modified code to complete assignment 8
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def show_menu(): # Display menu
        print('''
                Choose an Option:
                    1. Show Current Data 
                    2. Add New Data
                    3. Save New Data 
                    4. Exit
            ''')

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice(): # Get user choice input
        choice = input("Please enter an Option: ")
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_data(list_of_product_objects): # Show current data (list_of_objects)
        if list_of_product_objects == []:
            print("There is nothing in the file, please use option 2 to add data.")
        else:
            for p in list_of_product_objects:
                print(p.product_name + " | " + str(p.product_price))

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_data(): # Get user input new data
        objProduct = Product('', 0.0) # object of Product class
        while True:
            product_name = input('Please enter Product Name: ')
            try: # Check if name is str
                objProduct.product_name = product_name
                break
            except:
                print("Error. Please enter valid Product Name!")
        while True:
            product_price = input('Please enter Product Price: ')
            try: # Check if price is float
                objProduct.product_price = float(product_price)
                break
            except ValueError as e:
                print("Error. Please use numbers only for Price.")

        return objProduct

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

try:
    # Load data from file into a list of product objects when script starts
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
    print("Welcome to Assignment 08.")
    print("Please use this program to add Product and Price into file.")
    # While loop to display Menu with options
    while True:
        # Show user a menu of options
        IO.show_menu()
        # Get user's menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.show_current_data(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            try:
                new_data = IO.input_new_data()
                lstOfProductObjects.append(new_data)
            except ValueError as e:
                print(e)
            continue
        elif strChoice.strip() == '3':
            # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue
        elif strChoice.strip() == '4':
            # Let user exit the program
            print("Goodbye!")
            break
#
except Exception as e:
     print("There was an error!")
     print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script  ---------------------------------------------------- #