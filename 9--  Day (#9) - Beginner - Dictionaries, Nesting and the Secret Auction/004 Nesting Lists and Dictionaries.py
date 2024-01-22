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
    "Yaman" :  ["Yaman ", "Yaman", "Yaman ", "Yaman"]
}
 # print(Travle_log)


# Nested Dictionary in a dictionary.
Visiting_Log = {
    "Egypt ": {"visited_cites": ["Cairo ", "Giza ", "ALex ", "RedSea"], "Total visit":  42},
    "Palstine": {"Visited Cites ": ["Gaza ", "He fa", "Ya-fa ", "Rafa"], "Total Visit": 14},
    "Yaman": {" Visited Cities ": ["Yaman ", "Yaman", "Yaman ", "Yaman"], "Total VIsit": 75}
}
print(Visiting_Log)