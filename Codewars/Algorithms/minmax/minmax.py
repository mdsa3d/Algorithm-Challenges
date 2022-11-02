def min_max(lst):
      return [min(lst), max(lst)]

min_max = lambda l: [min(l), max(l)]
min_max = lambda _: [min(_),max(_)]

def min_max(lst):
    lst.sort()
    return [lst[0],lst[-1]]