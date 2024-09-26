import os
import sys
import csv
import Model.CSVReader as csvr

# global variables
route = os.getcwd()
input_route = os.getcwd() + "\\Samples\\"
output_route = os.getcwd() + "\\SamplesTxt\\"
input_name = "Profile"
output_name = "Profile"
encode = "-enc UTF-8"
mode = ""
file_invitations = os.getcwd() + "\\Invitations.csv"
file_connections = os.getcwd() + "\\Connections.csv"

mode_name = mode[1:]
files_processed = 0
        
# Numbering Files in Samples Directory as Profile + number.pdf
#* possible damage to the files in the directory, must be revised *
def number_files():
    for i, filename in enumerate(os.listdir("Samples")):
        os.rename("Samples/" + filename, "Samples/Profile" + str(i) + ".pdf")
  
#move all txts to SamplesTxt
def move_files():
    for filename in os.listdir("Samples"):
        # If the file is a txt file, move it to the SamplesTxt directory if it exists. If not, create it and move it there.
        if filename.endswith(".txt"):
            if not os.path.exists("SamplesTxt"):
                os.makedirs("SamplesTxt")
            os.rename("Samples/" + filename, "SamplesTxt/" + filename)
        
# Main function
def main():
    
    
    for filename in os.listdir("Samples"):
        if filename.endswith(".pdf"):
            name = filename.split(".")[0]
            os.system("pdftotext " + encode + " " + mode + " " + input_route + filename + " " + output_route + mode_name + name + ".txt")
            print("File " + filename + " converted to " + mode_name + name + ".txt")
    
    #Instantiate a CSVReader for Invitations.csv
    
    file = file_invitations  # Define the variable 'file'
    #file = file_connections  # Redefine the variable
    
    if file == file_invitations:
        csv_reader = csvr.CSVReader(file_invitations)
        print(f'Total rows: {csv_reader.rows}')
        names = csv_reader.get_from_invitations(row=0, elements=1)
        print(names)
    else:
        csv_reader = csvr.CSVReader(file_connections)
        print(f'Total rows: {csv_reader.rows}')
        names = csv_reader.get_from(row=0,column=1, elements=3)
        print(names)
    
    
if __name__ == "__main__":
    main()
    move_files()