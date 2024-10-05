# Travel_log
# Nesting
travel_log = [
    {"country": "Egypt",
     "visit": 12,
     "cities": ["paris", "Lille", "Dijon"]
     }
]

# Nesting in a list of dictionary.

travel_log1 = {
    "Egypt": ["Cairo", "ALex", "Giza", "Red Sea"],
    "Saudi": ["Mecca", "Madina", " Read"]
}

# Nested Dictionary in a Dictionary.

travel_log3 = {
    "Egypt": {"Visited Cities": ["Cairo", "ALex", "Giza", "Red Sea"], "total_Visit": 12},
    "Saudi": {"Visited Cities": ["Mecca", "Madina", " Read"],  "total_visit ": 12}
}
print(travel_log, travel_log3)

