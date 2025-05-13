from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from classes
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Use a condition and set it to true so the loop can run and then to stop the loop, set it to false.
is_on = True

while is_on:  # using a loop
    options = menu.get_items()
    choice = input(
        f"What drink would you like ({options}): \n").lower()  # asking the user to order a drink by using the variable in 'menu.py' and then storing the choice in a variable called 'choice'.

    if choice == "off":  # in case a maintenance crew enters an 'off' command.
        print("Goodbye, shutting down now.")  # View shutting down message.
        is_on = False  # condition gets false, loop stops hence the machine shuts down.

    elif choice == "report":  # if the maintenance crew wants a report, then they will simply type in the machine 'report'.
        coffee_maker.report()
        money_machine.report()

    elif choice == "refill":  # Option to refill the resources in the coffee machine
        coffee_maker.refill()  # Call the refill method to refill all resources

    else:
        # Find the drink based on user input
        drink = menu.find_drink(choice)

        if drink is None:  # If the drink is not found in the menu, inform the user
            print("Sorry, we don't have that drink on the menu. Please try again.")
        elif coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)