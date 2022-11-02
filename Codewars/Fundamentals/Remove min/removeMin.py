def remove_smallest(numbers):
    new = []
    if numbers is None or len(numbers) <= 1:
        return new
    i = numbers.index(min(numbers))
    return numbers[:i] + numbers[i+1:]


def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

def remove_smallest(numbers):
    if not numbers:
        return numbers
    else:
        new = numbers[:]
        new.remove(min(numbers))
    return new


def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []


def remove_smallest(numbers):
    if len(numbers) <= 1: return []
    numbers.remove(min(numbers))
    return numbers