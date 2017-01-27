import random

items = [5, 2, 3, 1]
items_probability = [i/sum(items) for i in items]


def get_random_based_on_probability(items, items_probability):
    probability = random.uniform(0, 1)
    cumulative_probability = 0
    for item, item_probability in zip(items, items_probability):
        cumulative_probability += item_probability
        if probability <= cumulative_probability:
            return item

print(get_random_based_on_probability(items, items_probability))