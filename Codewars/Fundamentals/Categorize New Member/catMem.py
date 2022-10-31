def open_or_senior(data):
    return ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]