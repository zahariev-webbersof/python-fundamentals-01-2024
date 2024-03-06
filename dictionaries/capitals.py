countries = input().split(', ')
capitals = input().split(', ')

country_capital_dict = dict(zip(countries, capitals))

for country, capital in country_capital_dict.items():
    print(f'{country} -> {capital}')