def reverse_string_task():
    print("--- : Reverse a String ---")
    
    # Get input from the user
    original = input("Enter a word or sentence: ")
   
    reversed_text = original[::-1]
    
    # Output the result
    print(f"Original: {original}")
    print(f"Reversed: {reversed_text}")
    print("-" * 46)

if __name__ == "__main__":
    reverse_string_task()
