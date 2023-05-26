# type hint
# 間違っていてもエラーにならない
price: int = 100
tax: float = 1.1

def calc_price(price: int, tax: float) -> int:
    return int(price * tax)

if __name__ == "__main__":
    print(f'prise is {calc_price(price=price, tax=tax)}')

