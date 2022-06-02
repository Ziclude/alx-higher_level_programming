#!/usr/bin/python3
if __name__ == "__main__":
    """Print the numbe and list of arguments."""
    import sys
    cy = len(sys.argv) - 1
    if cy == 0:
        print("0 arguments.")
    elif cy == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cy))
    for a in range(cy):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))
