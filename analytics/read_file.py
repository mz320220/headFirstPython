import sys

# 读取文件
input_file = sys.argv[1]
print('Output #143:')
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()

# 使用with读取文件
print('Output #144:')
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print('{}'.format(row.strip()))

