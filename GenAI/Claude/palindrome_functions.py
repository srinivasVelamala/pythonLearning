def is_palindrome(text):
    """
    Check if a given string is a palindrome.
    Ignores case, spaces, and punctuation.
    """
    # Convert to lowercase and keep only alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the string reads the same forwards and backwards
    return cleaned == cleaned[::-1]

def is_palindrome_number(num):
    """
    Check if a given number is a palindrome.
    """
    # Convert number to string and check if it's a palindrome
    num_str = str(abs(num))  # Use absolute value to handle negative numbers
    return num_str == num_str[::-1]

def find_palindromes_in_range(start, end):
    """
    Find all palindromic numbers in a given range.
    """
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome_number(num):
            palindromes.append(num)
    return palindromes

def generate_palindromes(length):
    """
    Generate palindromic numbers of a specific length.
    """
    palindromes = []
    
    if length == 1:
        return list(range(0, 10))
    
    # For even length palindromes
    if length % 2 == 0:
        half_length = length // 2
        start = 10 ** (half_length - 1)
        end = 10 ** half_length
        
        for i in range(start, end):
            palindrome = int(str(i) + str(i)[::-1])
            palindromes.append(palindrome)
    
    # For odd length palindromes
    else:
        half_length = length // 2
        start = 10 ** (half_length - 1) if half_length > 0 else 1
        end = 10 ** half_length if half_length > 0 else 10
        
        for i in range(start, end):
            for middle in range(0, 10):
                palindrome = int(str(i) + str(middle) + str(i)[::-1])
                palindromes.append(palindrome)
    
    return sorted(palindromes)

def print_palindrome_results(text_list, number_list):
    """
    Print palindrome check results for lists of text and numbers.
    """
    print("=" * 50)
    print("PALINDROME CHECKER RESULTS")
    print("=" * 50)
    
    print("\n📝 TEXT PALINDROMES:")
    print("-" * 30)
    for text in text_list:
        result = is_palindrome(text)
        status = "✅ YES" if result else "❌ NO"
        print(f"'{text}' → {status}")
    
    print("\n🔢 NUMBER PALINDROMES:")
    print("-" * 30)
    for num in number_list:
        result = is_palindrome_number(num)
        status = "✅ YES" if result else "❌ NO"
        print(f"{num} → {status}")

# Sample usage and demonstration
if __name__ == "__main__":
    
    # Test strings
    test_strings = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        "hello",
        "Madam",
        "Was it a car or a cat I saw?",
        "python",
        "level"
    ]
    
    # Test numbers
    test_numbers = [121, 12321, 123, 1001, 7337, 12345, 9009, 1234321]
    
    # Print results
    print_palindrome_results(test_strings, test_numbers)
    
    # Find palindromes in a range
    print("\n🔍 PALINDROMES IN RANGE 1-200:")
    print("-" * 35)
    range_palindromes = find_palindromes_in_range(1, 200)
    print(f"Found {len(range_palindromes)} palindromes:")
    print(range_palindromes)
    
    # Generate palindromes of specific length
    print("\n🏗️ GENERATED PALINDROMES:")
    print("-" * 30)
    
    for length in [2, 3, 4]:
        generated = generate_palindromes(length)[:10]  # Show first 10
        print(f"{length}-digit palindromes (first 10): {generated}")
    
    print("\n" + "=" * 50)
    print("SAMPLE FUNCTION CALLS:")
    print("=" * 50)
    
    # Individual function demonstrations
    sample_word = "racecar"
    sample_number = 12321
    
    print(f"\nis_palindrome('{sample_word}') = {is_palindrome(sample_word)}")
    print(f"is_palindrome_number({sample_number}) = {is_palindrome_number(sample_number)}")
    print(f"find_palindromes_in_range(100, 150) = {find_palindromes_in_range(100, 150)}")
    
    print("\n📋 FUNCTION FEATURES:")
    print("• Case-insensitive text checking")
    print("• Ignores spaces and punctuation") 
    print("• Handles both positive and negative numbers")
    print("• Can find palindromes in any range")
    print("• Can generate palindromes of specific lengths")
    print("• Provides formatted output with visual indicators")
