import sys
if len(sys.argv) >= 2: C = int(sys.argv[1])
else: C = 10

def metric(population, area):
    return population/area

import csv

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

if C <= 0: C = 1
elif C > len(countries): C = len(countries)

print('Big To Small')
print(print_format.format(*label_format))
print(*final[:-C-1:-1], sep='\n', end='\n\n')

print('Small To Big')
print(print_format.format(*label_format))
print(*final[:C], sep='\n', end='\n\n')

if len(sys.argv) >= 3:
    print('Custom')
    print(print_format.format(*label_format))
    for arg in sys.argv[2:]:
        for country in final:
            if arg in country: print(country)