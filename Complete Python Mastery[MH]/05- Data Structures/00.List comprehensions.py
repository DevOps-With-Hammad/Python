# List comprehensions
multiples = []
for x in range(0,7):
  multiples.append(x*7)

print(multiples)

# 01
multiples = [x*7 for x in range(0,7)]
print(multiples)

# 02
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
len(languages)
print(len(languages))
print(len(languages[0]))
print(len(languages[1]))
print(len(languages[2]))
print(len(languages[3]))
print(len(languages[4]))
lengths = [len(language) for language in languages]
print(lengths)

# 03
z = [x for x in range(0,101) if x %3 == 0 ]
print(z)

# we will reuse this code to do primary numbers finder

def primary():
    y = [w for w in range(2, 101) if all(w % i != 0 for i in range(2, int(w ** 0.5) + 1))]
    return y

print(primary(), "nice ")
print(" This is your code ")

# another list comprehensions

xvalue=  []
for v in range (1,5):
    xvalue.append(v*7)
print(xvalue)

# also you can write it in one line like this
xvalues = [m*3 for m in range (1,5)]
print(xvalues)

# List Comprehensions Let us create new list based on sequences or ranges
# we can use ot in creating functions for even numbers form 1 to 100
def even ():
    evens= [c for c in range(1, 101 ) if c%2 ==0 ]
    return  evens

print(even())


# another example for odd_number .
def odd_numbers(n):
	return [x for x in range(0,n+1 ) if x %2 !=0 ]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
