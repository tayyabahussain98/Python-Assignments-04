
def main():

    fruits = {
        "🍎 Apple": 10.0,
        "🌰 Durian": 25.0,
        "🍈 Jackfruit": 30.0,
        "🥝 Kiwi": 15.0,
        "🍓 Rambutan": 12.5,
        "🥭 Mango": 7.0
    }


    print('🍇 Welcome to the Fruit Shop! 🍇')
    print('Here are the available fruits and their prices (per piece):\n')

    for fruit, price in fruits.items():
        print(f'{fruit}: ${price}')

    print("\nPlease enter the quantity you'd like to buy:\n")

    total_cost: int = 0

    for fruit, price in fruits.items():
        while True:
            try:
                quantity: int = int(input(f'How many {fruit} do you want? '))
                if quantity < 0:
                    print('❌ Please enter a non-negative number.')
                    continue
                break
            except ValueError:
                print('❌ Invalid input. Please enter a number.')

        
        cost = quantity * price
        total_cost += cost

    print(f'\n🧾 Your total is: ${total_cost:.2f}')
    print('🛒 Thank you for shopping with us!')


if __name__ == '__main__':
    main()