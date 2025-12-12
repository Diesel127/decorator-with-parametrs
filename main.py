def get_first_matching_obj(predicate, objects=None):
    for obj in objects:
        if predicate(obj):
            return obj
    return None

print(get_first_matching_obj(lambda x: x == 1, [2, 3, 4, 5, 1]))