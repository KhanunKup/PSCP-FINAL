"""inverter"""
def main(binary_str):
    """main"""
    result = ''.join('1' if bit == '0' else '0' for bit in binary_str).lstrip('0')
    # Return a space if result is empty, otherwise return the result
    return result or " "
binary_input = input()
print(main(binary_input))
