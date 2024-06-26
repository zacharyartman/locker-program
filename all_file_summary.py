import os

for file in os.listdir():
  with open(file, 'r') as f:
    with open('all_file.txt', 'w') as all_file_path:
      all_file_path.write(f'\nFILENAME: {file}\n')
      for line in f:
        all_file_path.write(line)