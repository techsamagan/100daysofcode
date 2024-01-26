country = input()
visits = input()
list_of_cities = eval(input())

#Nested dictionary in a list
travel_log = [
    {
        "country": "France", 
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12
    },

    {
     "country":"Germany",
      "cities": ["Berlin", "Hamburg", "Stuttgart"],
      "visits": 5
    },
]



def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I have been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favourite city was {travel_log[2]['cities']}.")