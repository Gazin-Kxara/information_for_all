# TODO Найдите количество книг, которое можно разместить на дискете
mass = 1.44
lists =  100
stroks = 50
simbol = 25
code = 4
mass_book = (code * simbol * stroks * lists) / (1024 * 1024)
numbers = mass // mass_book

print("Количество книг, помещающихся на дискету:", int(numbers))
