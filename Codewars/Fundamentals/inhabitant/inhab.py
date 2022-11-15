def nb_year(p0, percent, aug, p):
    years = 1
    while True:
        temp = p0 + (p0 * (percent/100)) + aug
        if temp < p:
            p0 = temp
            years +=1
        else:
            return years
            break
    
years = nb_year(1500, 5, 100, 5000)
print("years", years)