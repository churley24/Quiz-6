#Camryn Hurley

import dbm

photo_category = dbm.open("captions", "c")

photo_category["animals.png"] = "animals in action in the wild"

photo_category["food.png"] = "yummy food on a plate"

photo_category["cars.png"] = "driving a sports cars"

for item in photo_category:
    print(item, photo_category[item])
