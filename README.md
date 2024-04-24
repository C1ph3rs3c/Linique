# Unique Line Appender

This script reads lines from standard input, appends them to a file, and ensures that only unique lines are appended. It supports optional features such as trimming leading and trailing whitespace and controlling output verbosity.

# Usage 
python3 linique.py [-q] [-d] [-t] [-h] [filename]
```
- -q: quiet mode (no output at all)
- -d: don't append anything to the file, just print the new lines to stdout
- -t: trim leading and trailing whitespace before comparison
- -h: display help message
- filename: optional argument, the name of the file to append lines to
```
## Examples
Append unique lines from `input.txt` to `output.txt`:
```
python3 linique.py output.txt < input.txt
```

# License
This project is licensed under the MIT License.
