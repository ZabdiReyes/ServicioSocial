import os
import sys
import csv
import Model.CSVReader as csvr
import Model.TxtReader as txtr
import Controller.PDFController as pdfc
import Controller.FilesController as fc

# global variables
route = os.getcwd()
input_path = os.getcwd() + "\\Samples\\"
output_path = os.getcwd() + "\\SamplesTxt\\"
input_name = "Profile"
output_name = "Profile"
test_path = os.getcwd() + "\\Test\\"
mode = "layout"

model_path = os.getcwd()+"\\Model\\"
file_csv_invitations = model_path + "\\Invitations.csv"
file_csv = model_path + "\\Connections.csv"

files_processed = 0
        
# Main function
def main():
    
    fc.FilesController.pdf_to_txt(input_path, output_path, mode)
    
    file = file_csv_invitations  # Define the variable 'file'
    #file = file_connections  # Redefine the variable
    
    if file == file_csv_invitations:
        csv_reader = csvr.CSVReader(file_csv_invitations)
        print(f'Total rows: {csv_reader.rows}')
        names = csv_reader.get_from_invitations(row=0, elements=1)
        print(names)
        
    else:
        csv_reader = csvr.CSVReader(file_csv)
        print(f'Total rows: {csv_reader.rows}')
        names = csv_reader.get_from(row=0,column=1, elements=3)
        print(names)
    
    i= "0"
    
    #txt = txtr.TxtReader(output_path+mode+output_name+i+".txt")
    #txt.read()
    #print(txt.search('keyword'))
    
if __name__ == "__main__":
    main()
    