from Classes import Product, Item, Rectangle, Point, Potato, Carrot, Berry

def Prooduct_splitting():
    prodlist = [prodline.rstrip().split(' ') for prodline in open("ProductList.txt", encoding="utf-8").readlines()]

    allProducts = [Product(name=line[0], date=line[1], amount=line[2]) for line in prodlist]
    allProductsString = "\n  Список продуктов:"
    for product in allProducts:
        allProductsString += f"\n{product}"

    print(allProductsString)


def Potato_splitting():
    potatolist = [potatoline.rstrip().split(' ') for potatoline in open("PotatoList.txt", encoding="utf-8").readlines()]

    allPotato = [Potato(name=line[0], variety=line[1], date=line[2], amount=line[3]) for line in potatolist]
    allPotatoString = "\n  Список картошки:"
    for potato in allPotato:
        allPotatoString += f"\n{potato}"

    print(allPotatoString)

def Carrot_splitting():
    carrotlist = [carrotline.rstrip().split(' ') for carrotline in open("CarrotList.txt", encoding="utf-8").readlines()]

    allCarrot = [Carrot(name=line[0], length=line[1], date=line[2], amount=line[3]) for line in carrotlist]
    allCarrotString = "\n  Список моркови:"
    for carrot in allCarrot:
        allCarrotString += f"\n{carrot}"

    print(allCarrotString)


def Berry_splitting():
    berrylist = [berryline.rstrip().split(' ') for berryline in open("BerryList.txt", encoding="utf-8").readlines()]

    allBerry = [Berry(name=line[0], date=line[1], amount=line[2], size=line[3]) for line in berrylist]
    allBerryString = "\n  Список моркови:"
    for berry in allBerry:
        allBerryString += f"\n{berry}"

    print(allBerryString)


Prooduct_splitting()
Potato_splitting()
Carrot_splitting()
Berry_splitting()


# def task1():
#
#     rectangle1 = Rectangle(point1=Point(12, 11),
#                            point2=Point(7, 23))
#
#     rectangle2 = Rectangle(point1=Point(4, 13),
#                            point2=Point(8, 10))
#
#     new_min_x = min(rectangle1.point1.x, rectangle1.point2.x)
#     new_min_y = min(rectangle1.point1.y, rectangle1.point2.y)
#     new_max_x = max(rectangle1.point1.x, rectangle1.point2.x)
#     new_max_y = max(rectangle1.point1.y, rectangle1.point2.y)
#
#     rectangle1.point1 = Point(new_min_x, new_min_y)
#     rectangle1.point2 = Point(new_max_x, new_max_y)
#
#     #далее код не дописан 🤷‍♂️
#
# task1()