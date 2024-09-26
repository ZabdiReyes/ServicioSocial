import csv
import os

file_invitations = os.getcwd() + "\\Invitations.csv"
file_connections = os.getcwd() + "\\Connections.csv"

#assumed to be the last column or the second to last column
def get_csv_at(row):
    if row and row[-1] != "https://www.linkedin.com/in/rafael-rivera-lópez-465712220":
        return row[-1]
    else:
        return row[-2]

#get a specific column element from a row    
def get_csv_at(row,column):
    if row:
        return row[column]

#espesific for invitations.csv file
def get_csv_invitations(file_path, start_row=None, end_row=None):
    results = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for index, row in enumerate(reader):
            if start_row is not None and index < start_row:
                continue
            if end_row is not None and index > end_row:
                break
            result = get_csv_at(row)
            results.append(result)
    return results

#general function to get a csv file content
def get_csv(file_path, start_row=None, end_row=None, column = None):
    results = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for index, row in enumerate(reader):
            if start_row is not None and index < start_row:
                continue
            if end_row is not None and index > end_row:
                break
            result = get_csv_at(row,column)
            results.append(result)
    return results

def count_rows_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return sum(1 for row in reader) - 1  # Subtract 1 for the header row

def main():
    #rows = count_csv_rows(file_invitations)
    rows = count_rows_csv(file_connections)
    #print(f'Total rows: {rows}')
    
    #results = process_csv_invitations(file_invitations, start_row=1, end_row=rows)
    results = get_csv(file_connections, start_row=1, end_row=rows, column = 0)
    for result in results:
        print(result)
       
if __name__ == "__main__":
    main()