import os

def scan_for_akira(path):
    akira_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".akira"):
                akira_files.append(os.path.join(root, file))
    return akira_files

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python akira_scanner.py <directory>")
        exit(1)

    target_dir = sys.argv[1]
    infected = scan_for_akira(target_dir)

    if infected:
        print("[!] Found potential AKIRA-infected files:")
        for f in infected:
            print(f)
    else:
        print("[✓] No AKIRA-infected files detected.")
