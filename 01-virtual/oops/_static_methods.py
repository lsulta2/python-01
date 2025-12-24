class Flowers:

    @staticmethod
    def types_flowers(text):
        return[items.strip() for items in text.split(",")]

flower_shop = '  lily , rose , sunflower , belly '
vase = Flowers.types_flowers(flower_shop)
print(vase)


# static method does not require to create obj, it has own utilites

