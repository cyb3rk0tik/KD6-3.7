import csv

def read_csv_like_dict(name):
    with open(name, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
        return data
        
def check_string_type(string):
    string_type = ''
    for s in string:
        if s.isdecimal():
            if string_type.find('d') == -1: 
                string_type += 'd'
                
        if s.isalpha() or s in ['-', '+']:
            if string_type.find('a') == -1: 
                string_type += 'a'
    return string_type
