count = 1
iteration = 1
current = 1
limit = 500

def getCount(num):
    count = 2
    for i in range(2, int(num**(.5))):
        if num%i == 0:
            count += 2
    return count


while count < limit:
    iteration += 1
    current += iteration
    get_count = getCount(current)
    if get_count > count:
        count = get_count

print(current, count)
