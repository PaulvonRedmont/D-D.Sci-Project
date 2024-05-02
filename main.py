import csv

# Input CSV file path
input_file = r"C:\Users\paul\Downloads\D&D Data Science Project.csv"

# Initialize lists to store data for each column
number = []  # Change this to a list
cha = []
con = []
dex = []
int_val = []
str_val = []
wis = []
result = []

# Open CSV file and read data column-wise
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Skip the header row
    next(reader)
    for row in reader:
        # Check if the 'Result' column is 'Failure'
        if row['Result'] != 'Failure':
            # Append values from each column to their respective lists
            number_str = row['Number']
            if number_str:  # Check if 'Number' is not empty
                number.append(int(number_str))  # Convert 'Number' to int before appending
            cha_str = row['Cha']
            if cha_str:  # Check if 'Cha' is not empty
                cha.append(int(cha_str))  # Convert 'Cha' to int before appending
            con_str = row['Con']
            if con_str:  # Check if 'Con' is not empty
                con.append(int(con_str))  # Convert 'Con' to int before appending
            dex_str = row['Dex']
            if dex_str:  # Check if 'Dex' is not empty
                dex.append(int(dex_str))  # Convert 'Dex' to int before appending
            int_val_str = row['Int']
            if int_val_str:  # Check if 'Int' is not empty
                int_val.append(int(int_val_str))  # Convert 'Int' to int before appending
            str_val_str = row['Str']
            if str_val_str:  # Check if 'Str' is not empty
                str_val.append(int(str_val_str))  # Convert 'Str' to int before appending
            wis_str = row['Wis']
            if wis_str:  # Check if 'Wis' is not empty
                wis.append(int(wis_str))  # Convert 'Wis' to int before appending
            result.append(row['Result'])

def calculate_averages():
    global number, cha, con, dex, int_val, str_val, wis, result
    
    total_cha = sum(cha)
    total_con = sum(con)
    total_dex = sum(dex)
    total_int_value = sum(int_val)
    total_str_value = sum(str_val)
    total_wis = sum(wis)
    
    number_of_entries = len(number)  # Calculate the number of entries
    
    # Calculate averages
    average_cha = total_cha / number_of_entries
    average_con = total_con / number_of_entries
    average_dex = total_dex / number_of_entries
    average_int = total_int_value / number_of_entries
    average_str = total_str_value / number_of_entries
    average_wis = total_wis / number_of_entries

    print(cha, con, dex, int_val, str_val, wis)
    print("================================================")
    print(f"Average Charisma Value: {average_cha}")
    print(f"Average Constitution Value: {average_con}")
    print(f"Average Dexterity Value: {average_dex}")
    print(f"Average Intelligence Value: {average_int}")
    print(f"Average Strength Value: {average_str}")
    print(f"Average Wisdom Value: {average_wis}")
    print("================================================")

calculate_averages()
