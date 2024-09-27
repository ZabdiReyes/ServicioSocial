import os
import re


class PDFController:
    directory_path = None
    file_path = None
    def __init__(self,directory_path):
        self.directory_path = directory_path

    def delete(self, file_path):
        # Method to delete a PDF at the specified file path
        pass
    
    def rename_with_index(self, new_name= None):
        
        if self.__is_ordered():
            print("Files are already ordered")
            
        else:
            print("Ordering files")
            
            if new_name is None:
                #renames current file to default_name without () and reorders it with an index
                for i, filename in enumerate(os.listdir(self.directory_path)):
                        cropped_filename = self.__extract_name(filename)
                        os.rename(self.directory_path+filename,self.directory_path + cropped_filename+ str(i) + ".pdf")
            else:    
                #renames current file to new_name + i + .pdf
                for i, filename in enumerate(os.listdir(self.directory_path)):   
                    os.rename(self.directory_path+filename,self.directory_path + new_name+ str(i) + ".pdf")
            
                    
    def __is_ordered(self):
        # Method to check if the files are allready ordered
        res = False
        count = 0
        exists = 0
        files = []
        for i, filename in enumerate(os.listdir(self.directory_path)):
            count = i+1
            files.append(filename)
        
        for i in range(count):
            if (self.__extract_name(filename)+str(i)+".pdf") in files:
                #print(self.__extract_name(filename)+str(i)+".pdf exist in files")
                exists += 1
            else:
                #print(self.__extract_name(filename)+str(i)+".pdf does not exist in files")        
                exists = -1
    
        if count == exists:
            res = True
                
        return res
    
    def __extract_name(self, filename):
        pattern = r'\(.*?\)'                                        # Regular expression to remove anything inside parentheses
        cropped_filename = re.sub(pattern, '', filename)
        pattern = r'\d+'                                            # Regular expression to remove any numbers
        cropped_filename = re.sub(pattern, '', cropped_filename)    # Remove numbers from the filename
        cropped_filename = cropped_filename.replace(" ", "")        # Remove spaces from the filename
        cropped_filename = cropped_filename.replace(".pdf", "")     # Remove the .pdf extension
        ##print(cropped_filename)
        return cropped_filename