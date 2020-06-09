# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JTrinh,6.2.2020,Modified code to complete assignment 8
# JTrinh,6.2.2020,Added methods to FileProcessor class
# JTrinh,6.4.2020,Added IO and while loop
# JTrinh, 6.8.2020, Troubleshooting entire script

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
        JTrinh,6.2.2020,Modified code to complete assignment 8
    """

#--Constructor--#
    def __init__(self, product_name: str, product_price: float):
        """ Getting name of product and price """
        #--Attributes--#
        try:
            self.__product_name = str(product_name) #privatize attribute using __
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Problem with types of values entered: ")
            print(str(e))

#--Property--#
    @property #getter - allows for indirect access to attributes
    def product_name(self):
        return str(self.__product_name).title() #privatize attribute with __ and title-case input

    @product_name.setter #setter - sets value of property (above)
    def product_name(self, value: str):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property #getter
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter #setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Invalid. Price should not have letters")

# --Methods--#
    @staticmethod
    def to_string(self):  # making custom method
        return self.__str__()

    def __str__(self):  # using built-in method
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JTrinh,6.4.2020,Modified code to complete assignment 8
        JTrinh,6.6.2020, changed formatting to include for loop
    """
    pass

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        '''
        Description: Reads existing file from text file
        :param file_name: products.txt
        :return: list of products
        '''
        lstOfProductObjects = []
        objFile = open(file_name, "r")
        for row in objFile:
            lstOfProductObjects.append(row.strip())
        objFile.close()
        return lstOfProductObjects

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name,table):
        '''
        Description: Takes file in list and saves to text file
        :param file_name: products.txt
        :param table: lstOfProductObjects
        :return: nothing
        '''
        objfile = open(file_name, "w")
        for row in table:
            objfile.write(str(row)+"\n")
        objfile.close()
        print("Your data has been saved to the text file")

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Methods involving input operations from end-user"""

    @staticmethod
    def MenuOptions():
        """
        Desc: Displays program options to user
        :return: nothing
        """
        print(
            """
            ***** Menu Options ***** \n
            [1] Display Current List
            [2] Add Product
            [3] Save List
            [4] Exit
        """
        )
        print()

    @staticmethod
    def UserChoice():
        '''
        Description: Asks user for input
        :return: menuChoice (user input)
        '''
        menuChoice = input("Choose a task to perform from the menu [1-4]: ").strip()
        return menuChoice

    @staticmethod
    def CurrentData(table):
        '''
        Description: Prints current items in a list-format
        :param table:
        :return: nothing
        '''
        print("\n******* Your Current List: *******")
        for row in table:
            print (row, sep="\n")
            # print(row["Product"] + " (" + str(row["Price"]) + ")")
        print("**********************************")
        print()  # Add an extra line for looks

    @staticmethod
    def GetProduct():
        '''
        Description: Asks user for product name and price input
        :return:
        '''
        try: #try block to catch mistakes in user input
            product_name = input("Product Name: ").title()
            if product_name.isalpha() == False:
                raise Exception("Not a name.")
            # product_price = str(float(input("Product Price: ")))
            product_price = input("Product Price: ")
            if product_price.isnumeric() == False:
                raise Exception("Price must be a number")
            objProd = Product(product_name,product_price)
            print(objProd.__str__())
            return objProd

        except Exception as e: #except block to display any errors found within try block
            print(e, type(e), e.__doc__, sep='\n')


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        # Show user a menu of options
        IO.MenuOptions()
        # Get user's menu option choice
        strChoice = IO.UserChoice()
        # Show user current data in the list of product objects
        if strChoice.strip() == '1':
            IO.CurrentData(lstOfProductObjects)
            continue
        # Let user add data to the list of product objects
        elif strChoice == '2':
            lstOfProductObjects.append(IO.GetProduct())
            continue
        # let user save current data to file and exit program
        elif strChoice == '3':
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue
        # let user exit program
        elif strChoice == '4':
            input("Thanks for using this program. Goodbye. \n(Press 'Enter' to exit)")
            break
        # if input not 1-4, ask user to enter choice again
        else:
            ("Please enter a valid number form the menu")

except FileNotFoundError as e:
    print("Please check to make sure the file exists")
    print(e, type(e),e.__doc__,sep='\n')


except TypeError as e:
    print(e, e.__doc__, type(e), sep ='\n')

except AttributeError as e:
    print("The object or class cannot perform attribute")
    print(e, type(e),e.__doc__,sep='\n')

except Exception as e:
    print(e, type(e),e.__doc__,sep='\n')



# Main Body of Script  ---------------------------------------------------- #
