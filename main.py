import os

# date format
DATE_FORMAT = "%d-%m-%Y"

# unique games
UNIQUE_GAMES = []

# Load all files in the current directory
def load_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and not filename.endswith('.py'):
            files.append(filename)
    return files

def is_date_or_time(part):
    # Check for date format dd-mm-yyyy i.e. 07-02-2025
    if len(part) == 10 and part[2] == '-' and part[5] == '-':
        day, month, year = part.split('-')
        if day.isdigit() and month.isdigit() and year.isdigit():
            return True
        
    # Check for time format hh_mm_ss i.e. 21_59_54
    if len(part) == 8 and part[2] == '_' and part[5] == '_':
        hour, minute, second = part.split('_')
        if hour.isdigit() and minute.isdigit() and second.isdigit():
            return True
        
    # Check for time format h_mm_ss i.e. 4_02_15
    if len(part) == 7 and part[1] == '_' and part[4] == '_':
        hour, minute, second = part.split('_')
        if hour.isdigit() and minute.isdigit() and second.isdigit():
            return True
        
    return False

# Delete date, time and extension from filenames & register unique games
def clean_filenames(filenames):
    cleanFiles = []
    for file in filenames:
        name, _ = os.path.splitext(file)
        parts = name.split(' ')
        print("parts",parts)
        clean_name = ' '.join(part for part in parts if not is_date_or_time(part))
        cleanFiles.append(clean_name)
        if clean_name not in UNIQUE_GAMES:
            UNIQUE_GAMES.append(clean_name)
    
    return cleanFiles

def clean(filename):
    name, _ = os.path.splitext(filename)
    parts = name.split(' ')
    print("parts",parts)
    return ' '.join(part for part in parts if not is_date_or_time(part))

# Create directory if it doesn't exist and add files to it
def reubicate_files(filenames):

    current_dir = os.getcwd()

    for file in filenames:
        # Create directory for new game
        cleanFile = clean(file)
        newDir = os.path.join(current_dir, cleanFile)

        if not os.path.exists(newDir):
            os.makedirs(newDir)

        # Move file
        src = os.path.join(current_dir, file)
        dst = os.path.join(newDir, file)
        os.rename(src, dst)

# Main
fileNames = load_files_in_directory(os.getcwd())
reubicate_files(fileNames)