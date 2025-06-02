def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()
    return price

print(discount_price(100,0))


