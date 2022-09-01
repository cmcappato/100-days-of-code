import functions
is_machine_on = True


while is_machine_on:
    choice = str(input("    What would you like? (espresso/latte/cappuccino): ")).lower()

    if choice == "espresso":
        enough_resources = functions.manage_resources("espresso")
        if enough_resources:
            coins = functions.process_coins()
            functions.make_coffee(coins, "espresso")
    elif choice == "latte":
        enough_resources = functions.manage_resources("latte")
        if enough_resources:
            coins = functions.process_coins()
            functions.make_coffee(coins, "latte")
    elif choice == "cappuccino":
        enough_resources = functions.manage_resources("cappuccino")
        if enough_resources:
            coins = functions.process_coins()
            functions.make_coffee(coins, "cappuccino")
    elif choice == "report":
        functions.print_report()
    else:
        print("Turning machine off...")
        is_machine_on = False
