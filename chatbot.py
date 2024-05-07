
def greet():
    return "Hi there! Welcome to PizzaBot." 
def menu():
    return "Our menu includes: \n1. Margherita Pizza \n2. Pepperoni Pizza \n3. Vegetarian Pizza \n4. Hawaiian Pizza"

def order_pizza(pizza_choice):
    return f"You have ordered {pizza_choice}. It will be delivered to your address shortly."

def delivery_time():
    return "Your pizza will arrive in 30 minutes."

def goodbye():
    return "Thank you for choosing PizzaBot. Have a great day!"

def respond(message):
    if "hi" in message.lower() or "hello" in message.lower():
        return greet()
    elif "menu" in message.lower():
        return menu()
    elif "order" in message.lower():
        if "order " in message.lower():
            pizza_choice = message.split("order ")[1]
            return order_pizza(pizza_choice)
        else:
            return "Please specify which pizza you'd like to order."
    elif "delivery" in message.lower() or "time" in message.lower():
        return delivery_time()
    elif "bye" in message.lower() or "thank you" in message.lower():
        return goodbye()
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to PizzaBot! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print(goodbye())
            break
        else:
            print("PizzaBot:", respond(user_input))

if __name__ == "__main__":
    main()
