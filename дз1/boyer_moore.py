def boyer_moore(text, pattern):
    len_pattern = start_compare = pattern_pointer = text_pointer = len(pattern)
    count = 0
    while start_compare <= len(text):
        while pattern_pointer > 0:
            if text[text_pointer - 1] == pattern[pattern_pointer - 1]:
                text_pointer -= 1
                pattern_pointer -= 1
            elif start_compare == len(text):
                return count
            else:
                start_compare += 1
                pattern_pointer = len_pattern
                text_pointer = start_compare
        if pattern_pointer <= 0:
            count += 1
            start_compare += 1
            pattern_pointer = len_pattern
            text_pointer = start_compare
    return count
