import csv
import time
from datetime import datetime
from Dicts import pizzaDict, sauceDict

def main():
    with open('wo_gui/database.csv', 'w') as db_file: # TODO: dosyalama yaptıktan sonra burası değişecek
        field_names = ['Name', 'Surname', 'PhoneNumber',
                       'CardNumber', 'CVV', 'EndDate', 'OrderTime']
        csv_writer = csv.DictWriter(
            db_file, fieldnames=field_names, delimiter=',')
        csv_writer.writeheader()

        f = open("wo_gui/Menu.txt", "r") # TODO: dosyalama yaptıktan sonra burası değişecek
        print(f.read())
        print("\n")
        try:
            p_choice = int(input("Please choose a Pizza type: "))
            s_choice = int(input("Please choose a Sauce type: "))

            if not ((1 <= p_choice <= 4) and (11 <= s_choice <= 16)):
                raise Exception("Sorry, we do not have such an option.")

        except ValueError as te:              # if int() function fails to convert the input to an integer, a ValueError will be raised
            print("Only integers are allowed")
        except Exception as e:                # if the number is entered except for the options exception will be raised
            print(e)

        selectedClassforPizza = pizzaDict[p_choice]
        selectedClassforSauce = sauceDict[s_choice]

        pizzaObj = selectedClassforPizza()
        obj2 = selectedClassforSauce(pizzaObj)

        print("Order Amount: " + str(obj2.get_cost()) + "$" +
              "\n" + "You will be redirected to the pay page! ")

        time.sleep(0) # TODO: change the value

        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")

        print("\nWelcome to Pay Page!")
        checkValue= True
        user_info = {}
        while (checkValue):
            try:
                user_info['Name'] = str(input("Name: "))
                user_info['Surname'] = str(input("Surname: "))
                user_info['PhoneNumber'] = int(input("Phone Number: "))
                # if(len(str(user_info['PhoneNumber'])) != 10):
                #     raise Exception("Phone number must be exactly 11 digits long. Ex: (05413545455)")
                user_info['CardNumber'] = int(input("Card Number: "))
                # if(len(str(user_info['CardNumber'])) != 16):
                #     raise Exception("Card number must be exactly 16 digits long. Ex: (1234567890123456)")
                user_info['CVV'] = int(input("CVV: "))
                # if(len(str(user_info['CVV'])) != 3):
                #     raise Exception("Card CVV must be exactly 3 digits long. Ex: (123)")
                user_info['EndDate'] = input("End Date (MM/YY): ")
                # if len(user_info['EndDate']) != 5 or not user_info['EndDate'][0:2].isdigit() or not user_info['EndDate'][3:].isdigit():
                #     raise Exception("Please enter the end date in the format MM/YY")
                user_info['OrderTime'] = current_time
                checkValue = False
                csv_writer.writerow(user_info)
            except ValueError as te:              # if int() function fails to convert the input to an integer, a ValueError will be raised
                print("Only integers are allowed")
            except Exception as e:                # if the number is entered except for the options exception will be raised
                print(e)


main()
