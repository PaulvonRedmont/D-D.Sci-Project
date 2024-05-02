import csv

input_file =  "C:\Users\paul\Downloads\D&D.Sci.txt"
output_file = "C:\Users\paul\Downloads\D&D Data Science Project.csv"

headers = ['Number', 'Cha', 'Con', 'Dex', 'Int', 'Str', 'Wis', 'Result']

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create CSV writer
    writer = csv.writer(outfile)
    
    # Write headers to CSV file
    writer.writerow(['Number', 'Cha', 'Con', 'Dex', 'Int', 'Str', 'Wis', 'Result'])
    
    # Read each line from input file
    for line in infile:
        # Split line into values
        values = line.strip().split(',')
        
        # Arrange values in desired order
        number = values[0]
        cha = values[1]
        con = values[2]
        dex = values[3]
        int_val = values[4]
        str_val = values[5]
        wis = values[6]
        result = values[7]
        
        # Write values to CSV file
        writer.writerow([number, cha, con, dex, int_val, str_val, wis, result])
