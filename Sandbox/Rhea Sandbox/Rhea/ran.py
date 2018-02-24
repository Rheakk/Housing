import random
random.seed (42)
print (random.sample (range (100), 20))
random.seed (12)
print (random.sample (range (100), 20))
random.seed (None)