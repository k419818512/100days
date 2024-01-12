def add_new_country(country, visits, list_of_cities):
    dict1={}
    dict1 = {"country": country, "total_visits": visits, "cities_visited": list_of_cities}
    travel_log2.append(dict1)

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12}, 
    "Germany": ["Berlin", "Hamburg","Stuttgart"],
}

# Nesting Dictionary in a  list

travel_log2 = [
    {"country": "France", "cities_visited": ["Paris","Lille","Dijon"], "total_visits":12},
    {"country": "Germany", "cities_visited":["Berlin", "hamburg","Stuttgart"], "total_visits":5}
]

country=input()
visits=input()
list_of_cities=input()
add_new_country(country, visits, list_of_cities)

print(f"I have been to {travel_log2[2]['country']} {travel_log2[2]['total_visits']}")

print(f"My favorite city was {travel_log2[0]['cities_visited'][0]}")

