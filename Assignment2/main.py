import data
import sandwich_maker
import cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

# Pay attention sandwich_maker class has a constructor variable (resources) [cite: 9]
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large/ off/ report): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            units = {
                "bread": "slice(s)",
                "ham": "slice(s)",
                "cheese": "pound(s)"
            }
            # Updated to use the new sandwich_maker_instance
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item.capitalize()}: {amount} {units.get(item)}")

        elif choice in recipes:
            sandwich = recipes[choice]

            # Updated to use sandwich_maker_instance
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                # Updated to use cashier_instance
                payment = cashier_instance.process_coins()

                # Updated to use cashier_instance
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    # Updated to use sandwich_maker_instance
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
