class ArtReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self, start_line, end_line):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                for line_number in range(start_line, end_line + 1):
                    if line_number < len(lines):
                        print(lines[line_number].rstrip())
                    else:
                        print(f"Line {line_number} does not exist in the file.")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")

# Usage example
art_reader = ArtReader('Media/Art.txt')
art_reader.read_lines(79, 132)  # This will print lines 1 to 8 (0-indexed), needs to replace with parameters for actual output, remember to subtract 1 from the line number