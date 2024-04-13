import csv
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

