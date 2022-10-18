# place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i == True:
            counter += 1
    print(f'Number of sheep/s:\n{counter}')

count_sheeps([True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True])
