def shopping_bill(cart_amount):

    def calculate_discount():
        if cart_amount >= 5000:
            return cart_amount * 0.20  # 20 percent
        elif cart_amount >= 3000:
            return cart_amount * 0.10  # 10 percent
        else:
            return 0

    def calculate_delivery():
        if cart_amount >= 1000:
            return 0
        else:
            return 50

    def generate_bill(discount, delivery):
        final_amount = cart_amount - discount + delivery

        print("\n------ SHOPPING BILL ------")
        print("Cart Amount: Rs.", cart_amount)
        print("Discount: Rs.", discount)
        print("Delivery Charges: Rs.", delivery)
        print("---------------------------")
        print("Final Bill: Rs.", final_amount)

    discount = calculate_discount()
    delivery = calculate_delivery()

    generate_bill(discount, delivery)


amount = float(input("Enter total cart amount: Rs. "))
shopping_bill(amount)
