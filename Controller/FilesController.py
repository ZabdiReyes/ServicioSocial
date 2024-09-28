import os

class FilesController:
    directory_path = None
    file_path = None
    encode = "-enc UTF-8"
    
    def __init__(self,directory_path):
        self.directory_path = directory_path
    
    # Legacy function
    @staticmethod    
    def move_files(source, destiny,extension = ".txt"):
        for filename in os.listdir(source):
            # If the file is a txt file, move it to the destiny directory if it exists. If not, create it and move it there.
            if filename.endswith(extension):
                if not os.path.exists(destiny):
                    os.makedirs(destiny)
                os.rename(os.path.join(source, filename), os.path.join(destiny, filename))
    
    @staticmethod
    def pdf_to_txt(input_path, output_path, mode):
        
        # Method to convert a PDF to a TXT file
        for filename in os.listdir(input_path): # input_path is the path to the directory where the pdfs are located "Samples"
            if filename.endswith(".pdf"):
                name = filename.split(".")[0]
                os.system("pdftotext " + FilesController.encode + " -" + mode + " " + input_path + filename + " " + output_path + mode + name + ".txt")
                print("File " + filename + " converted to " + mode + name + ".txt")
    
    