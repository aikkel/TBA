class ArtReader:
    def __init__(self, file_path, firstLine=None, lastLine=None):
        self.file_path = file_path
        self.firstLine = firstLine
        self.lastLine = lastLine

    def titel(self):
        self.firstLine = 0
        self.lastLine = 7
        self.read_lines()

    def orc(self):
        self.firstLine = 9
        self.lastLine = 77
        self.read_lines()

    def snake(self):
        self.firstLine = 79
        self.lastLine = 132
        self.read_lines()

    def you_died(self):
        self.firstLine = 134
        self.lastLine = 139
        self.read_lines()

    def read_lines(self):
        if self.firstLine is None or self.lastLine is None:
            print("Please set the firstLine and lastLine before reading lines.")
            return

        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                for line_number in range(self.firstLine, self.lastLine + 1):
                    if line_number < len(lines):
                        print(lines[line_number].rstrip())
                    else:
                        print(f"Line {line_number} does not exist in the file.")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            
    

art_reader = ArtReader('Media/Art.txt')
# art_reader.titel()
# art_reader.orc()
# art_reader.read_lines(art_reader.firstLine, art_reader.lastLine)  # Reads Art.txt
