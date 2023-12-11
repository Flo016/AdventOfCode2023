from typing import List, Tuple
# Copy the input for this day in the file dayXX_input.txt (where XX is the day number) in the same folder as this file

def extract_adjacent_numbers(line, center_index):
    # given

    # 21.43 -> now ** will be checked
    # ..$..
    # .....

    # **.43 -> left ** will be checked first
    # ..$..
    # .....
    first_number = ""
    for i in range(center_index-1, -1, -1):
        try: 
            first_number = str(int(line[i])) + first_number # build the number to the left as far as possible.
        except ValueError:
            break
    # either no value has been found, or all numbers that are to the left of the center have been found. it can either be one number or no number

    # 21*** -> now *** will be checked
    # ..$..
    # .....
    # check if middle is a number. if it is, there can only be one number connected within that line.
    second_number = ""
    second_number_exists = False
    for i in range(center_index, len(line), 1):
        if i == center_index or (i > center_index and not second_number_exists):
            try: 
                first_number = first_number + str(int(line[i]))  # build the number to the left as far as possible.
            except ValueError:
                if i == center_index:
                    # if the center is not a number, a potential second number could exist on center_index +1, therefore we need to check it and continue the for loop.
                    second_number_exists = True
                    continue
                break
        elif i > center_index and second_number_exists:
            try: 
                second_number = second_number + str(int(line[i]))  # build the number to the left as far as possible.
            except ValueError:
                if i == center_index+1:
                    second_number_exists = False
                break # we are at the rightmost number. once we dont find any numbers there cannot start another number adjacent to the center.
    if second_number_exists:
        try:
            int(first_number)
            int(second_number)
            #print("first number: " + first_number)
            #print("second number:c" + second_number)
            return int(first_number) + int(second_number)
        except ValueError:
            #print("second number: " + second_number)
            return int(second_number) # there is no first number
    else:
        try:
            int(first_number)
            #print("first number: " + first_number)
            return int(first_number)
        except ValueError:
            return 0 # there is no first or second number
        

def multiply_adjacent_numbers(line, center_index):
    # given

    # 21.43 -> now ** will be checked
    # ..$..
    # .....

    # **.43 -> left ** will be checked first
    # ..$..
    # .....
    first_number = ""
    for i in range(center_index-1, -1, -1):
        try: 
            first_number = str(int(line[i])) + first_number # build the number to the left as far as possible.
        except ValueError:
            break
    # either no value has been found, or all numbers that are to the left of the center have been found. it can either be one number or no number

    # 21*** -> now *** will be checked
    # ..$..
    # .....
    # check if middle is a number. if it is, there can only be one number connected within that line.
    second_number = ""
    second_number_exists = False
    for i in range(center_index, len(line), 1):
        if i == center_index or (i > center_index and not second_number_exists):
            try: 
                first_number = first_number + str(int(line[i]))  # build the number to the left as far as possible.
            except ValueError:
                if i == center_index:
                    # if the center is not a number, a potential second number could exist on center_index +1, therefore we need to check it and continue the for loop.
                    second_number_exists = True
                    continue
                break
        elif i > center_index and second_number_exists:
            try: 
                second_number = second_number + str(int(line[i]))  # build the number to the left as far as possible.
            except ValueError:
                if i == center_index+1:
                    second_number_exists = False
                break # we are at the rightmost number. once we dont find any numbers there cannot start another number adjacent to the center.
    if second_number_exists:
        try:
            int(first_number)
            int(second_number)
            #print("first number: " + first_number)
            #print("second number:c" + second_number)
            return [int(first_number), int(second_number)]
        except ValueError:
            #print("second number: " + second_number)
            return [int(second_number)] # there is no first number
    else:
        try:
            int(first_number)
            #print("first number: " + first_number)
            return [int(first_number)]
        except ValueError:
            return [] # there is no first or second number
        




def part_1(lines: List[str]) -> Tuple[str, any]:
    # code for the first part:

    result = 0
    nonsymbols = "0123456789."
    for line_index in range(len(lines)):
        
        #print("-------------------------")
        for symbol_index in range(len(lines[line_index])):
            if lines[line_index][symbol_index] not in nonsymbols:
                # input("Found one")
                #print(result)
                if line_index == 0:
                    #print(line_index)
                    #print(lines[line_index])
                    #print(lines[line_index+1])

                    for adj_line_indicie in range(line_index, line_index+2, 1): # line_index+2 because then it will stop at line_index+2 but still includes line_index+1, which is is the final one we need.
                        result = result + extract_adjacent_numbers(lines[adj_line_indicie], symbol_index)
                    #print("this is the result: " + str(result))

                elif line_index >= 1 and line_index != (len(lines)-1):
                    #print(line_index)
                    #print(lines[line_index-1])
                    #print(lines[line_index])
                    #print(lines[line_index+1])

                    for adj_line_indicie in range(line_index -1, line_index+2, 1): # line_index+2 because then it will stop at line_index+2 but still includes line_index+1, which is is the final one we need.
                        result = result + extract_adjacent_numbers(lines[adj_line_indicie], symbol_index)
                    #print("this is the result: " + str(result))

                elif line_index >= (len(lines)-1):
                    #print(lines[line_index-1])
                    #print(lines[line_index])

                    for adj_line_indicie in range(line_index-1, line_index+1, 1): # line_index+2 because then it will stop at line_index+2 but still includes line_index+1, which is is the final one we need.

                        result = result + extract_adjacent_numbers(lines[adj_line_indicie], symbol_index)
                    #print("this is the result: " + str(result))


        
    return '<Name/Short Description of this part>', result # 543064 is too low 


def part_2(lines: List[str]) -> Tuple[str, any]:
    result = 0
    nonsymbols = "*"
    for line_index in range(len(lines)):
        
        for symbol_index in range(len(lines[line_index])):
            if lines[line_index][symbol_index] in nonsymbols:
                # input("Found one")
                results = []
                if line_index == 0:

                    for adj_line_indicie in range(line_index, line_index+2, 1): # line_index+2 because then it will stop at line_index+2 but still includes line_index+1, which is is the final one we need.
                        numbers = multiply_adjacent_numbers(lines[adj_line_indicie], symbol_index)
                        for number in numbers:
                            results.append(number)

                elif line_index >= 1 and line_index != (len(lines)-1):

                    for adj_line_indicie in range(line_index -1, line_index+2, 1): # line_index+2 because then it will stop at line_index+2 but still includes line_index+1, which is is the final one we need.
                        numbers = multiply_adjacent_numbers(lines[adj_line_indicie], symbol_index)
                        for number in numbers:
                            results.append(number)

                elif line_index >= (len(lines)-1):
                    for adj_line_indicie in range(line_index-1, line_index+1, 1): # line_index+2 because then it will stop at line_index+2 but still includes line_index+1, which is is the final one we need.
                        numbers = multiply_adjacent_numbers(lines[adj_line_indicie], symbol_index)
                        for number in numbers:
                            results.append(number)
                #print(len(results))
                #print(results)
                if len(results) == 2:
                    result = result + (results[0] * results[1])
    return '<Name/Short Description of this part>', result


