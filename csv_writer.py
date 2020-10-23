from csv import writer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def csv_header():
    # printing headers to csv
    list_1 = ['name', 'number']
    append_list_as_row('dps_list', list_1)


def clear_csv():
    # clearing csv file
    cleaning_csv = open('dps_list', 'w+')
    cleaning_csv.close()
