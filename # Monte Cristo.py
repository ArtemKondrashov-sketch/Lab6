# Monte Cristo
def calculate_letter_case_percentage(file_path):
    with open(file_path, 'r', encoding='windows-1251') as f:  
        content = f.read()
        filtered_text = [char for char in content if char.isalpha()]
        lowercase_count = sum(1 for char in filtered_text if char.islower())
        uppercase_count = sum(1 for char in filtered_text if char.isupper())
        total_letters = len(filtered_text)
        lower_percentage = (lowercase_count / total_letters) * 100
        upper_percentage = (uppercase_count / total_letters) * 100
    
        print(f"Відсоток малих літер: {lower_percentage:.2f}%")
        print(f"Відсоток великих літер: {upper_percentage:.2f}%")

file_path = 'The Count of Monte Cristo.txt'
calculate_letter_case_percentage(file_path)