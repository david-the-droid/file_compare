import sys

if __name__ == "__main__":
    file1_pathname = sys.argv[1]
    file2_pathname = sys.argv[2]

    file1 = open(file1_pathname, 'r')
    file2 = open(file2_pathname, 'r')

    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

    file1.close()
    file2.close()

    print("***********************************")
    print("*************REPORT****************")
    print("***********************************\n")

    for i in range(len(file1_lines)):
        if file1_lines[i] != file2_lines[i]:
            print("Line " + str(i+1) + " doesn't match.")
            print("------------------------")
            print("File1: " + file1_lines[i])
            print("File2: " + file2_lines[i])

