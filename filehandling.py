def fileCreation():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Leah Sherley\n")
            file.write("23\n")
            file.write("Address: 56789\n")
    except Exception as e:
        print("An error occurred during file creation:", e)

def fileReading():
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print(f"Contents of the file:\n {contents}")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred during file reading:", e)

def appending():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Mobile Developer\n")
            file.write("Female\n")
            file.write("+254 790 555 432\n")
    except Exception as e:
        print("An error occurred during appending:", e)

def readFileAndDisplay():
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("Contents of the file:")
            print(contents)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred during file reading:", e)

try:
    fileCreation()
    fileReading()
    appending()
    readFileAndDisplay() 
except Exception as e:
    print("An error occurred:", e)
