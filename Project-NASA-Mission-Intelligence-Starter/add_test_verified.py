import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"Result: {add(int(sys.argv[1]), int(sys.argv[2]))}")
    else:
        print("Please provide two numbers as arguments.")
