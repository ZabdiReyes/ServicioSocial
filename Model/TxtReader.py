class TxtReader:
    directory_path = None
    file_path = None
    
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def read(self, file_path):
        file_path = self.directory_path + file_path
        try:
            with open(file_path, 'r') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"The file {super.file} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search(self, keyword):
        if not self.content:
            print("File content is empty. Please read the file first.")
            return []

        lines = self.content.split('\n')
        result = [line for line in lines if keyword in line]
        return result

# Example usage:
# reader = TxtReader('/path/to/your/file.txt')
# reader.read()
# matches = reader.search('keyword')
# print(matches)