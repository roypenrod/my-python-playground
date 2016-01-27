import random

def random_item(iterable):
  index = random.randint(0, len(iterable) -1)
  return iterable[index]


# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"

selection = random_item("Treehouse")
print(selection)
