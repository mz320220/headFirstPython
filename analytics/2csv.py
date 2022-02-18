import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_input:
    with open(output_file, 'w', newline='') as csv_output:
        filereader = csv.reader(csv_input, delimiter=',')
        filewriter = csv.writer(csv_output, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)
