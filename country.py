def metric(population, area):
    return population/area

C_CONSTANT = 10

import sys
import csv
if len(sys.argv) >= 2: 
    try:
        C = int(sys.argv[1])
        g = 1
    except:
        C = 0
        g = 0
else: C = C_CONSTANT

area = {}
with open('area.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    f = True
    for row in csvreader:
        if len(row) == 64:
            if row[-3] and not f:
                area[row[0]] = float(row[-3])
            f = False

population = {}
with open('population.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    f = True
    for row in csvreader:
        if len(row) == 64:
            if row[-2] and not f:
                population[row[0]] = int(row[-2])
            f = False

countries = set(population).intersection(set(area))

label_format = ['Country', 'Population', 'Area', 'Metric']
print_format = '{:<40s}{:>10s}{:>20s}{:>24s}'

final = list(map(lambda country: print_format.format(country[:40],
                                                     str(population[country]),
                                                     str(area[country]),
                                                     str(metric(population[country], 
                                                                area[country]))),
                 sorted(countries,
                        key=lambda country: metric(population[country], 
                                                   area[country]))))

if C <= 0: C = 0
elif C > len(countries): C = len(countries)

if C:
    print('Big', 'To Small'*(C>1))
    print(print_format.format(*label_format))
    print(*final[:-C-1:-1], sep='\n', end='\n\n')

    print('Small', 'To Big'*(C>1))
    print(print_format.format(*label_format))
    print(*final[:C], sep='\n', end='\n\n')

if len(sys.argv) >= g+2:
    print('Custom Printing')
    print(print_format.format(*label_format))
    for arg in sys.argv[g+1:]:
        for country in final:
            if arg in country: print(country)