def reverse_string_short(text):
    return text if len(text) <= 1 else \
        reverse_string_short(text[1:]) + text[0]

if __name__ == "__main__":
    rstring_short = reverse_string_short("Atomic Habbits")
    print(rstring_short)