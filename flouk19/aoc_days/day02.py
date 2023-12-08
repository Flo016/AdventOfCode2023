from typing import List, Tuple
# Copy the input for this day in the file dayXX_input.txt (where XX is the day number) in the same folder as this file


def part_1(lines: List[str]) -> Tuple[str, any]:
    # code for the first part:
    colour_limits = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for line in lines: # Game 1: 10 red, ....
        line = line.split(": ")
        games = line[1].split("; ") 
        game_valid = True
        for game in games: # ["10 red, 5 blue, 3 green", ... ]
            balls = game.split(", ")
            for game_balls in balls:
                game_balls = game_balls.split(" ")
                #if game_balls[1]
                if int(game_balls[0]) > colour_limits[game_balls[1]]:
                    # print("Invalid, because " + game_balls[1] + " are " + game_balls[0] + " but can only be " + str(colour_limits[game_balls[1]]) + " at maximum")
                    game_valid = False
                    break
            if not game_valid:
                break
        if game_valid:
            # print("Valid Game: " + line[0].split(" ")[1])

            result = result + int(line[0].split(" ")[1]) # ["Game", "100"]
            # print(str(result))
        
    return 'Sum of Game ID\'s that are valid games', result


def part_2(lines: List[str]) -> Tuple[str, any]:
    # code for the second part (if exists):


    result = 0
    powers = []
    for line in lines: # Game 1: 10 red, ....
        line = line.split(": ")
        games = line[1].split("; ") 
        colour_limits = {"red": 0, "green": 0, "blue": 0}
        for game in games: # ["10 red, 5 blue, 3 green", ... ]
            
            balls = game.split(", ")
            for game_balls in balls:
                game_balls = game_balls.split(" ")
                #if game_balls[1]
                if int(game_balls[0]) > colour_limits[game_balls[1]]:
                    colour_limits[game_balls[1]] = int(game_balls[0])
        b = 1
        for value in colour_limits.values():
            b = b * value
        powers.append(b)
            
    result = sum(powers)

    return 'Sum of all Powers of lowest ball amounts possible in each game ', result
