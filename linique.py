import sys

quiet_mode = False
dry_run = False
trim = False
help_mode = False

# Parse command-line arguments
for arg in sys.argv[1:]:
    if arg == '-q':
        quiet_mode = True
    elif arg == '-d':
        dry_run = True
    elif arg == '-t':
        trim = True
    elif arg == '-h':
        help_mode = True
    else:
        filename = arg

if help_mode:
    print("Usage: python3 script.py [-q] [-d] [-t] [-h] [filename]")
    print("-q: quiet mode (no output at all)")
    print("-d: don't append anything to the file, just print the new lines to stdout")
    print("-t: trim leading and trailing whitespace before comparison")
    print("-h: display this help message")
    print("filename: optional argument, the name of the file to append lines to")
    sys.exit(0)

lines = set()

# Read lines from file into set if filename is provided
if 'filename' in locals():
    try:
        with open(filename, 'r') as file:
            for line in file:
                if trim:
                    lines.add(line.strip())
                else:
                    lines.add(line)
    except FileNotFoundError:
        pass

# Open file for appending new content if not dry run
if not dry_run and 'filename' in locals():
    try:
        file = open(filename, 'a')
    except IOError as e:
        print(f"Failed to open file for writing: {e}", file=sys.stderr)
        sys.exit(1)

# Read lines from stdin, append to file and print if new
for line in sys.stdin:
    line = line.strip() if trim else line
    if line not in lines:
        lines.add(line)
        if not quiet_mode:
            print(line, end="")
        if not dry_run and 'filename' in locals():
            file.write(line)

# Close the file if not dry run
if not dry_run and 'filename' in locals():
    file.close()
