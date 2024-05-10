# Type your code here
def list_from_file():
    # Make a connection to the file
    file_pointer = open('PythonReadWord.txt', 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    print(data)
    # new_data = []
    for a in data:
        print(a)
        # new_data = a + new_data
      
    # NOW CONTINUE YOUR CODE FROM HERE!!!

list_from_file()