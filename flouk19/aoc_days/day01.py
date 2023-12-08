from typing import List, Tuple
# Copy the input for this day in the file dayXX_input.txt (where XX is the day number) in the same folder as this file

def find_boyer_moore(text: list, pattern: list) -> bool:
        n, m = len(text), len(pattern)
        if m == 0 or m > n:
            return False, None  # if pattern doesnt exist or is longer than text
    
        # create dictionary  for each letter in pattern
        last = {}
        for k in range(m):
            last[pattern[k]] = k
    
        # create indexes to start from last element in pattern(j)
        # and 'possible' last element of pattern in text (i)
        i = m - 1
        j = m - 1
        while i < n:
            if text[i] == pattern[j]:
                # check if last characters match, if they do, check second last characters
                if j == 0:
                    return True, i  # if last characters match, pattern has been found
                else:
                    i -= 1
                    j -= 1
            # should characters not match, go len(pattern) to the right and try again.
            else:
                # essentially: k exists to to shift the index more, if letter text[i] is not in pattern
                # otherwise it is shifted by m-j. on some occasion k is lower than j even if the character is in the text, which also speeds up the algorithm a bit.
                k = last.get(text[i], -1)
                i += m - min(j, k + 1)
                j = m - 1
        return False, None


def part_1(lines: List[str]) -> Tuple[str, any]:
    # code for the first part:

    result = 1
    numbers =  []
    
    for line in lines:
        first_number = ""
        first_number_index = 0
        second_number = ""
        for i in range(len(line)):

            try:
                first_number = str(int(line[i]))
                break
            except ValueError:
                pass
        
        for i in range(-1, (len(line)+1)* -1, -1):
            try:
                second_number = str(int(line[i]))
                break
            except ValueError:
                pass
        numbers.append(int(first_number+second_number))
        """print(first_number)
        print(second_number)
        print(first_number + second_number)
        print(str(int(first_number+second_number)))
        input("Wait")"""
    result = sum(numbers)
    print(result)
    return 'If only numbers are included', result


def part_2(lines: List[str]) -> Tuple[str, any]:
    # code for the second part (if exists):
    result = -1
    written_number = {"three":"3", "seven":"7", "eight":"8", "four":"4", "five":"5", "nine":"9", "one":"1", "two":"2", "six":"6"}
                           
    numbers =  []
    
    for line in lines:
        first_number = ""
        first_number_index = None
        second_number = ""
        second_number_index = None
        # get first actual number
        for i in range(len(line)):

            try:
                first_number = str(int(line[i]))
                first_number_index = i
                break
            except ValueError:
                pass
        # determine if potential first number is really the first number
        smallest_index = first_number_index
        if smallest_index is None: smallest_index = len(line)-1 #when no number is contained within the line.
        for pattern in written_number.keys():
            a, b = find_boyer_moore(line[:first_number_index], pattern) # True/False, None/#Number
            if a:
                if smallest_index > b:
                    smallest_index = b
                    first_number = written_number[pattern]



        # now that the leftmost number exists, do the same but from the right.
        for i in range(-1, (len(line)+1)* -1, -1):
            try:
                second_number = str(int(line[i]))
                second_number_index = len(line) + i
                break
            except ValueError:
                pass
        # determine that potential last number is really the last number. 
        biggest_index = second_number_index
        if biggest_index is None: biggest_index = 0 #when no number is contained within the line.
        if (len(line)-1 - biggest_index) < 5:
            sliding_window_size = len(line)-1 - biggest_index
        else:
            sliding_window_size = 5
         # every pattern can only be contained once within the sliding window.
        pattern_found = False
        for i in range(len(line)-sliding_window_size-1, biggest_index-1, -1):
            for pattern in written_number.keys():
                a, b = find_boyer_moore(line[i:i+sliding_window_size], pattern) # True/False, None/#Number
                if a:
                    if biggest_index < i+b:
                        biggest_index = i+b
                        second_number = written_number[pattern]
                        pattern_found = True
                        break # since sliding window is 5 and only one number can be contained within, as soon as a pattern has been found, you can stop searching
            if pattern_found:
                break
        numbers.append(int(first_number+second_number))
        
    
    result = sum(numbers)
    print(result)

    # find numbers first, then look left and right of them. if index_lenght from border is longer than 3, start searching for strings from these borders.
    return 'If written Numbers are included: ', result
