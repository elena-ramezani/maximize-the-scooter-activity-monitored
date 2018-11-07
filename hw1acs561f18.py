
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

lines = input_file.readlines()

for line in lines:
    line = line.replace('\n', '')
    Location, Status = line.split(',')
    if Status == 'Dirty':
        output_file.write('Suck\n')
    elif Location == 'A':
        output_file.write('Right\n')
    elif Location == 'B':
        output_file.write('Left\n')

input_file.close()
output_file.close()