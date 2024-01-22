# 004 Nesting Lists and Dictionaries
# Nesting

Caps = {
    "France ": "Paris",
    "England ": "London",
    "Egypt ": "Cairo"
}
# print("the capital of egypt is " + str(Caps))


# How to Nest a list ??
Travle_log = {
    "Egypt ": ["Cairo ", "Giza ", "ALex ", "RedSea"],
    "Plstine": ["Gaza ", "He fa", "Ya-fa ", "Rafa"],
    "Yaman": ["Taizz ", "Sana's", "Zidd ", "Aden"]
}
# print(Travle_log)


# Nested Dictionary in a dictionary.
Visiting_Log = {
    "Egypt ": {"visited_cites": ["Cairo ", "Giza ", "ALex ", "RedSea"], "Total visit": 42},
    "Palstine": {"Visited Cites ": ["Gaza ", "He fa", "Ya-fa ", "Rafa"], "Total Visit": 14},
    "Yaman": {" Visited Cities ": ["Taizz ", "Sana's", "Zidd", "Aden"], "Total VIsit": 75}
}
# print(Visiting_Log)

# Nesting Dict in lists

travvle_trace = [
    {
        "Country": "Egypt",
        "Cities ": ["Cairo", "Alex", "GIza"],
        "Total Visit": 12
    }
    ,
    {
        "Country": "Yaman",
        "Cities ": ["Zidd", "Sana's", "Aden"],
        "Total Visit": 44
    }
    ,
    {
        "Country": "Palastin",
        "Cities ": ["Gaza", "Rafa", "Hefaa"],
        "Total Visit": 42
    }
]
