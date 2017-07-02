import os
import glob
import json

"""Reading in text files."""

def read_file(filename):
    """Read a plain text file and return the contents as a string."""
    with open(filename, "r") as f:
        text = f.read()
        return text

def read_files(path):
    """Read all files that match given path and return a dict with their contents."""
    
    # TODO: Get a list of all files that match path (hint: use glob)
    files_in_path = []
    for filename in glob.iglob(os.path.join(os.getcwd() + '/' + path)):
        files_in_path.append(filename)
    print("files_in_path: ", files_in_path)

    # TODO: Read each file using read_file()
    # TODO: Store & return a dict of the form { <filename>: <contents> }
    # Note: <filename> is just the filename (e.g. "hieroglyph.txt") not the full path ("data/hieroglyph.txt")
    
    file_contents_mapping = {}
    for path in enumerate(files_in_path):
        path = path[1]
        extracted_filename_from_path = path.split("/")[-1]
        file_contents_mapping[extracted_filename_from_path] = read_file(path)
    # print(json.dumps(file_contents_mapping, indent=2))
    return file_contents_mapping

def test_run():
    # Test read_file()
    print("Hieroglyph file contents: ", read_file("data/hieroglyph.txt"))
    
    # Test read_files()
    texts = read_files("data/*.txt")
    for name in texts:
        print("\n***", name, "***")
        print(texts[name])


if __name__ == '__main__':
    test_run()
