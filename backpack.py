items = {
    "food": {"weight": 15, "value": 20},
    "bottle": {"weight": 5, "value": 15},
    "first-aidKit": {"weight": 5, "value": 15},
    "headlamp": {"weight": 3, "value": 10},
    "jacket": {"weight": 8, "value": 10},
    "map": {"weight": 2, "value": 8},
    "book": {"weight": 10, "value": 5},
    "pen": {"weight": 1, "value": 6}
}

def knapsack(capacity, items):
    weight = 0
    value = 0
    contents = []
    for key, stuff in items.items():
      #sort the dictionary?
      #then do the following:
        if stuff["weight"] + weight < capacity:
            contents.append(key)
            weight = weight + stuff["weight"]
            value = value + stuff["value"]
    return {"capacity": capacity, "items": items, "weight": weight, "value": value}

knapsack(50, items)

result = knapsack(50, items)
print(result)
print(result["weight"], result["value"])
