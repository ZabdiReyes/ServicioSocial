import csv

class CSVReader:
    directory_path = None
    file_path = None
    rows = None
    def __init__(self, directory_path):
        self.file_path = directory_path
        self.rows = self.count_rows()
    
    def read(self, file_path):
        self.file_path = self.file_path + file_path

    #assumed to be the last column or the second to last column
    def _get_at_invitations(self,row):
        if row and row[-1] != "https://www.linkedin.com/in/rafael-rivera-lópez-465712220":
            return row[-1]
        else:
            return row[-2]

    # get a specific element from a row and column
    def _get_at(self,row,column):
        if row:
            return row[column]

    #espesific for invitations.csv file
    def get_from_invitations(self,row=None, elements=None):
        start_row = row
        end_row = elements - 1
        results = []
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for index, row in enumerate(reader):
                if start_row is not None and index < start_row:
                    continue
                if end_row is not None and index > end_row:
                    break
                result = self._get_at_invitations(row)
                results.append(result)
        return results

    #general function to get a csv file content
    def get_from(self, row=None, column = None, elements=None):
        start_row = row
        end_row = row + elements - 1
        results = []
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for index, row in enumerate(reader):
                if start_row is not None and index < start_row:
                    continue
                if end_row is not None and index > end_row:
                    break
                result = self._get_at(row,column)
                results.append(result)
        return results

    def count_rows(self):
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return sum(1 for row in reader) - 1  # Subtract 1 for the header row        
