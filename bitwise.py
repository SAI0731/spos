def bitwise_operations_on_string(input_string):
    # Perform AND and XOR with 127 on each character
    and_results = []
    xor_results = []
    
    for char in input_string:
        char_value = ord(char)
        
        and_result = char_value & 127  # AND with 127
        xor_result = char_value ^ 127  # XOR with 127
        
        and_results.append(chr(and_result))  # Convert the result back to character
        xor_results.append(chr(xor_result))  # Convert the result back to character

    # Print results
    print(f"Original String: {input_string}")
    print(f"AND 127 Results: {''.join(and_results)}")
    print(f"XOR 127 Results: {''.join(xor_results)}")

# Input string
input_string = "Hello World"

# Call the function
bitwise_operations_on_string(input_string)
