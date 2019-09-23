students = ['Peter', 'Eugene', 'Kate', 'Alex', 'Dmitry', 'Tatyana', 'Victoria', 'Maria']

scores = [(10, 8, 9), (9, 7, 9), (8, 6, 8), (7, 9, 9), (10, 8, 5), (5, 4, 3), (7, 7, 3), (7, 9, 2)]

dictionary = dict(zip(students, scores))

def maxmin(d):
    new_dict = {}
    for key, value in d.items():
        average = sum(value) / len(value)
        new_dict[key] = int(average)
    maximum = max(new_dict, key=new_dict.get)
    minimum = min(new_dict, key=new_dict.get)
    return {'max': (maximum, new_dict[maximum]), 'min': (minimum, new_dict[minimum])}

print(maxmin(dictionary))