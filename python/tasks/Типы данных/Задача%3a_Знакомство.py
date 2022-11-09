age = 18
street = 'Ленина'
first_name = 'Олег'
house = 58
city_r = 'Москве'

voc = {
    "name" : first_name,
    "let" : age,
    "city" : city_r,
    "street" : street,
    "house" : house
}

hello = "Привет! Меня зовут %(name)s, мне %(let)d лет. Я живу в %(city)s, на улице %(street)s, дом %(house)d." % voc

print(hello)