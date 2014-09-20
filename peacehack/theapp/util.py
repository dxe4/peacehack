import csv


def read_file(fpath):
    with open(fpath, 'rb') as csvfile:
        # , quotechar='|'
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            print(', '.join(row))
            break
