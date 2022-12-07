def check_brackets(line):
    ind_wrong_bracket = 0
    counter = 0
    for i in range(len(line)):
        if line[i] == '(':
            counter += 1
        elif line[i] == ')':
            counter -= 1
            if counter < 0:
                ind_wrong_bracket = i
                break

        if counter == 0:
            ind_wrong_bracket = i + 1

    if counter == 0:
        return -1
    return ind_wrong_bracket + 1
