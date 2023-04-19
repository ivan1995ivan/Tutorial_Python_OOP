languages = ['english', 'french', 'deutsch']

class Country:
    population = 5e6
    regime = 'democracy'
    square = 3e5


arr = [Country() for _ in range(3)]
for count, country in enumerate(arr):
    country.language = languages[count]

print([arr[index].language for index in range(3)])