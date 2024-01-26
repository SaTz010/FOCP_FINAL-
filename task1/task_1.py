# use of the function: To check if the user input Y or N and to correct them if user is wrong
def get_yes_no_input(prompt):
    while True:
        res = input(prompt).strip().lower()  # line 45 46 47 
        if res == 'y' or res == 'n':
            return res
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

# use of the function: this is the function where we assign the retes and work on the condition
def calculate_pizza_price(its_tuesday, num_pizzas, is_delivery, is_app_order):
    Pizza_Cost = 12.00
    Delivery_Cost = 2.50
    Discount_Tuesday = 0.50
    Discount_App_Order = 0.25

    # Condition: Tuesday discount
    if its_tuesday: 
        total_cost = num_pizzas * (Pizza_Cost * (1 - Discount_Tuesday)) 
    else:
        total_cost = num_pizzas * Pizza_Cost
    # Condition: Delivery is required                                                                             
    if is_delivery:
        # Condition: Free Delivery 
        if num_pizzas < 5:
            total_cost += Delivery_Cost 


    if is_app_order:
        total_cost *= (1 - Discount_App_Order)

    return round(total_cost, 2)

#use of the function: This is where we call all the necessary fucntions we have defined earlier 
def main():
    print("BPP Pizza Price Calculator")
    print("=" * 30 )

    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas <= 0:
                raise ValueError("Please enter a positive integer!")

            is_delivery = get_yes_no_input("Is delivery required? (Y/N) ") == 'y'
            its_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ") =='y' 
            is_app_order = get_yes_no_input("Did the customer use the app? (Y/N) ") == 'y'

            total_price = calculate_pizza_price(its_tuesday, num_pizzas, is_delivery, is_app_order)
            print(f"\nTotal Price: £{total_price}")
            break

        except ValueError as e:
            print(f"{e}\nPlease enter a valid input.")

if __name__ == "__main__":
    main()
