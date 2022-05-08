


list_duplicate = ["a", "b", "c", "a", "d", "e", "b", "f", "a", 1, [1, 2], "b", 1, 10, [1, 2]]
list_duplicate_2 = ["a", "b", "c", "a", "d", "e", "b", "f", "a", 1, [1, 2], "b", 1, 10, [1, 2]]  # Temp list to view in print

list_not_duplicate = []

# Create new list with elements not duplicated and remove old
def create_list_from_duplicate_list(list_):
    while list_:
        element = list_.pop(0)
        if element not in list_not_duplicate:
            list_not_duplicate.append(element)


# Create new list, old list exist
def create_list_from_duplicate_list_2(list_):
    for i in list_:
        if i not in list_not_duplicate:
            list_not_duplicate.append(i)


# Generate element from list
def generator(list_):
    for i in list_:
        yield i

# Main function to remove element
def remover(list_):
    gen = generator(list_)
    counter = 0
    while counter != len(list_duplicate):
        gen_ = next(gen)
        remove_from_list(counter, gen_)
        counter += 1

# Check if generated element is in list and remove it
def remove_from_list(count, gen_):
    list_counter = count + 1
    while list_counter != len(list_duplicate):
        if list_duplicate[list_counter] == gen_:
            # list_duplicate.pop(list_counter)
            del list_duplicate[list_counter]
        list_counter += 1
        if list_counter > len(list_duplicate):
            break


remover(list_duplicate)

print(list_duplicate_2)
print(list_duplicate)