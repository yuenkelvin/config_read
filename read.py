import csv

with open('./text', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {}'.format(",".join(row)) )
            line_count += 1
        print('\t{} works in the {} department, and was born in {}.'.format(row['name'], row['department'], row['birthday month']))
        line_count += 1
    print('Processed {} lines.'.format(line_count))
