import argparse

def main():
    parser = argparse.ArgumentParser(description='GUI Application')
    parser.add_argument('--version', action='store_true', help='Display the version information')
    parser.add_argument('--start', action='store_true', help='Display the version information')
    args = parser.parse_args()

    if args.version:
        print("Version: 0.1b")
    elif args.start: 
        print("Running gui.exe")

if __name__ == "__main__":
    main()