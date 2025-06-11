# Auto Cleaner Script for AKIRA-related files
import os

def clean_akira_files(directory):
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.akira') or file == 'akira_readme.txt':
                full_path = os.path.join(root, file)
                try:
                    os.remove(full_path)
                    print(f"[DELETED] {full_path}")
                    count += 1
                except Exception as e:
                    print(f"[ERROR] Cannot delete {full_path}: {e}")
    print(f"Total files cleaned: {count}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python auto_cleaner.py <directory>")
        exit(1)

    clean_akira_files(sys.argv[1])
