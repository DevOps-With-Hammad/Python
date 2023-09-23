# Heads and tails with module random.

import random
random_size = random.randint(0, 1)
if random_size == 1:
    print(f"Here is your answer {random_size} good news you've got Head")
else:
    print("Here is your answer you've got tail ")
