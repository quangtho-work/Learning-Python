
class car:
    def __init__(self, name, price, color):
        self._name = name
        self._price = price
        self._color = color
    def __str__(self):
        return f"Car name: {self._name}\nCar price: {self._price}\nCar color: {self._color}\n----------------------------------------------------"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @name.deleter #xóa thuộc tính chứ không phải xóa giá trị
    def name(self):
        del self._name
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
    @price.deleter
    def price(self):
        del self._price
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = value
    @color.deleter 
    def color(self):
        del self._color

if __name__ == "__main__":
    c1 = car("BMW", 2000000, "Red")
    print(c1)
    c1.name = "Audi"
    print(c1)
    print(c1.name)
    del c1.name
    c1.name = "Toyota"
    print(c1)