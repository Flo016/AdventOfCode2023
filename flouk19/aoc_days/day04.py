from typing import List, Tuple
# Copy the input for this day in the file dayXX_input.txt (where XX is the day number) in the same folder as this file


def part_1(lines: List[str]) -> Tuple[str, any]:
    # code for the first part:

    result = 0

    for line in lines: # Game 1: 10 red, ....
        line = line.split(": ")
        games = line[1].split(" | ") 
        winning_numbers = games[0].split(" ")
        winning_numbers = [x for x in winning_numbers if x] # deleted [""] that are created if the array contains single digit numbers
        scratched_numbers = games[1].split(" ")
        scratched_numbers = [x for x in scratched_numbers if x] # deleted [""] that are created if the array contains single digit numbers
        
        has_winning_number = False
        current_ticket_value = 0

        for scratched_number in scratched_numbers:
            if scratched_number in winning_numbers:
                if has_winning_number:
                    current_ticket_value *= 2
                else:
                    current_ticket_value = 1
                    has_winning_number = True
        
        result = result + current_ticket_value
    return '<Name/Short Description of this part>', result


def part_2(lines: List[str]) -> Tuple[str, any]:
   
    result = 0
    card_amount = [1 for _ in range(len(lines))]
    for i in range(len(lines)): # Game 1: 10 red, ....
        line = lines[i].split(": ")
        games = line[1].split(" | ") 
        winning_numbers = games[0].split(" ")
        winning_numbers = [x for x in winning_numbers if x] # deleted [""] that are created if the array contains single digit numbers
        scratched_numbers = games[1].split(" ")
        scratched_numbers = [x for x in scratched_numbers if x] # deleted [""] that are created if the array contains single digit numbers
        

        has_winning_number = False
        current_ticket_value = 0

        for scratched_number in scratched_numbers:
            if scratched_number in winning_numbers:
                has_winning_number = True
                current_ticket_value += 1
        if has_winning_number:
            for j in range(1, current_ticket_value+1, 1):
                for _ in range(card_amount[i]):
                    if i+j < len(lines)-1:
                        card_amount[i+j] += 1
                    else: 
                        card_amount[-1] += 1
    print(i)
    print(lines[i])
    result = sum(card_amount)

    return '<Name/Short Description of this part>', result # 5581085 too low 5833065 correct answer


