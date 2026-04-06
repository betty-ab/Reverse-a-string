def generate_fibonacci():
    print("---Fibonacci Sequence ---")
    try:
        n = int(input("How many terms? "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    generate_fibonacci()
