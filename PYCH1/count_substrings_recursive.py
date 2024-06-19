def count_substrings(text, value_to_find):
    # recursive termination
    if len(text) < len(value_to_find):
        return 0
    count = 0
    remaining = ""

    # does the test start with search string?
    if text.startswith(value_to_find):
        # match: continue the search for the found
        # term after the locaiton where it was found.
        remaining = text[len(value_to_find):]
        count = 1
    else:
        # remove first character and search again
        remaining = text[1:]
    # recursive descent
    return count_substrings(remaining, value_to_find) + count

if __name__ == "__main__":
    substring = count_substrings("JoyfulljoyJoyyojJoy", "Joy")
    print(" Number of times substring was found is %d", substring)
