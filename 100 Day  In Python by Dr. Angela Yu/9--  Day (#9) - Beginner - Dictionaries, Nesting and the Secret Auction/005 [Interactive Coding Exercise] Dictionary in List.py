# 005 [Interactive Coding Exercise] Dictionary in List

Travle_log = [
    {
        "Country": "Egypt",
        "Visits": 166,
        "Cities": ["Cairo", "ALex", "Giza"]
    }
    ,
    {
        "Country": "Morocco",
        "Visits": 166,
        "Cities": ["Kazanlak", "Dar white", "Monaco"]
    }
    ,
    {
        "Country": "Egypt",
        "Visits": 166,
        "Cities": ["Cairo", "ALex", "Giza"]
    }
]


# The function of adding new country.
# is going to be here
def add_new_country(Country_visited, Times_visited, Cities_visited):
    New_country ={}
    New_country["Country"] = Country_visited
    New_country["Visits"] = Times_visited
    New_country["Cities"] = Cities_visited
    Travle_log.append(New_country)


# Here is the add of the New country
add_new_country("مصر", 343, ["القاهرة", "الجيزة ", " اليكس"])
print(Travle_log)
