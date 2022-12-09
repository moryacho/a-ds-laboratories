from check_brackets import check_brackets

tests = {
    "()": -1,
    "(())()": -1,
    "()()": -1,
    "((()))": -1,
    ")(": 1,
    "())(()": 3,
    "(": 1,
    ")": 1,
    "))))": 1,
    "((()": 1,
}


def run_tests():
    test_number = 1
    for line, expected in tests.items():
        actual = check_brackets(line)
        if expected == actual:
            print(f"Test #{test_number} - passed")
        else:
            print(f"Test #{test_number} - failed. line = {line}, expected = {expected}, actual = {actual}")
        test_number += 1


run_tests()
