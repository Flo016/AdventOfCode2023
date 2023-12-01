from typing import List, Callable, Optional, Tuple
import aoc_helper.helper as helper
import aoc_days
import importlib

DayPart = Callable[[List[str]], Tuple[str, any]]
Day = List[DayPart]


class AdventOfCode:
    SYMBOL: str = "-"
    FILL_STR: str = SYMBOL * 50

    def __init__(self, nr_of_advent_days: int = 25):
        self.days: List[Day] = []
        self.nr_of_advent_days = nr_of_advent_days

    @classmethod
    def get_day_part_str(cls, day_part: DayPart, day_num: int):
        """
        Returns the Name and the result of the DayPart as a string,
        if the result is not None or -1 an empty string is returned
        :param day_part:
        :param day_num:
        :return:
        """
        day_part_str, day_part_result = day_part(cls.get_input_for_day(day_num))
        if day_part_result is None or day_part_result == -1:
            return ""
        return f"{day_part_str}: {day_part_result}"

    @staticmethod
    def get_input_for_day(day_num: int):
        """
        Returns the input from an dayXX_input.txt file for the given day
        :param day_num:
        :return:
        """
        return helper.get_clean_file_input(f'./aoc_days/day{day_num:02}_input.txt')

    def print_days(self):
        for idx, day in enumerate(self.days):
            day_num = idx + 1

            str_to_print = []
            has_any_part = False

            # print day header
            str_to_print.append(self.FILL_STR)
            str_to_print.append(f"Day {day_num}:")

            # display the parts
            for part_idx, part in enumerate(day):
                part_str = self.get_day_part_str(part, day_num)
                if part_str != "":
                    has_any_part = True
                    str_to_print.append(f"   {part_idx + 1}| {part_str}")
            if has_any_part:
                for line in str_to_print:
                    print(line)

    def add_day(self, *parts: DayPart):
        self.days.append(list(parts))

    def load_days(self):
        """Loads the days from the aoc_days package and adds them to the AdventOfCode object
        (every module with a name between: 'day01' - 'day24' gets loaded)
        """
        for day in range(1, self.nr_of_advent_days + 1):
            try:
                # Import the module with the name 'dayXX' (e.g. day01)
                importlib.import_module(f"aoc_days.day{day:02}")
                current_day = aoc_days.__getattribute__(f"day{day:02}")
                # Get all parts from the current day module (every function that starts with 'part')
                parts_from_dayfile = sorted(
                    [p for p in dir(current_day) if callable(getattr(current_day, p)) and p.startswith('part')])
                day_parts: List[DayPart] = []
                for aocpart in parts_from_dayfile:
                    day_parts.append(current_day.__getattribute__(aocpart))
                self.add_day(*day_parts)
            except AttributeError as e:
                print(f"Day {day:02} not found.", e)
                continue
