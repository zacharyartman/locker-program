import os

files = os.listdir()
files.remove('.git')
files.remove('all_file_summary.py')

with open('all_file.txt', 'w') as all_file_path:
    for file in files:
        if file != 'all_file.txt':
            with open(f'./{file}', 'r') as f:
                all_file_path.write(f'\nFILENAME: {file}\n')
                for line in f:
                    all_file_path.write(line)