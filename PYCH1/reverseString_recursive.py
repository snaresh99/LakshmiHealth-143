# Reverse a string
def reverse_string(text):
    # Recursive termination
    if len(text) <= 1:
        return text
    first_char = text[0]
    remaining = text[1:]
    print(remaining)
    return reverse_string(remaining) + first_char

if __name__ == "__main__":
    rstring = reverse_string("Hello")
    print(rstring)