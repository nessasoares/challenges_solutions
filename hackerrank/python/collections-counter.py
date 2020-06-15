from collections import Counter

class ShoeShop():
    def __init__(self, sizes):
        self.stock = Counter(sizes)
        self.total_amount = 0

    def calculate_total_amount(self, costumers):
        total = 0
        for costumer in costumers:
            size = costumer[0]
            price = costumer[1]

            shoe_qtd = 0 if not self.stock.get(size) else self.stock.get(size)
            if shoe_qtd > 0:
                total += int(price)
                self.stock.update({size: -1})

        self.total_amount = total

if __name__ == '__main__':
    x = int(input())
    sizes = list(input().split())
    costumers = int(input())

    shop = ShoeShop(sizes)

    costumers_shoes = []
    for i in range(costumers):
        size, price = input().split()
        costumers_shoes.append((size, price))

    shop.calculate_total_amount(costumers_shoes)
    print(shop.total_amount)
