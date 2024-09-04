def line_count():
    file = open('file.txt', 'r')
# opens the file in read mode
    lines = file.readlines()
# reads all lines in file into a list called lines
    line_count = 0
# creates a veriable that keeps track of the number of lines
    for line in lines:
# goes through each lines in the lines        
        line_count = line_count + 1
# increases the count by one for each line                          
    file.close()
# closes the file
    return(line_count)
# returns the count for how many lines

