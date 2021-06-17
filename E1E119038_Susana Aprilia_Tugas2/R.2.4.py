class Flower:
    def __init__(self, name='Flower_1', petals=1, price=1.0):
        self.name = name
        self.petals = petals
        self.price = price
        
    def __repr__(self):
        return 'Flower -> {}, {} petals, {} Rupiah'.format(self.name, self.petals, self.price)
 
    def set_name(self, name):
        self.name = name

    def set_petals(self, petals):
        self.petals = petals

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_petals(self):
        return self.petals

    def get_price(self):
        return self.price

if __name__ == '__main__':
    my_flower = Flower('Hibiscus',3,20)
    my_flower.set_price(2000)
    print(my_flower)
