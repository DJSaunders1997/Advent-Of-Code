# https://adventofcode.com/2022/day/5

import re
import input
from copy import deepcopy

class stacker:
    def __init__(self, stacks_dict:dict, instructions:str, move_multi_items:bool=False) -> None:

        self.stacks_dict = deepcopy(stacks_dict) # Copy dict to stop it being passed by ref and updating original
        self.move_multi_items = move_multi_items
        
        # Replace from and to with , to separate numerical instructions
        instructions = re.sub(r'from', ',', instructions)
        instructions = re.sub(r'to', ',', instructions)
        instructions = re.sub(r'[^0-9,\n]', '', instructions) # Remove all characters other than numbers, comma, new lines

        instructions_split = instructions.split("\n")        
        self.instructions_list = [instruction.split(",") for instruction in instructions_split]

    def run_instructions(self, print:bool):
        """Runs through instructions as specified in input string

        Args:
            print (bool): flag whether to print output after each instruction
        """

        if print:
            self.print_dict()
        
        for instruction in self.instructions_list:
            
            num_to_move = int(instruction[0])
            from_stack = int(instruction[1])
            to_stack = int(instruction[2])

            self.move_stack(num_to_move, from_stack, to_stack)

            if print:
                self.print_dict()

    def move_stack(self, num_to_move:int, from_stack:int, to_stack:int):
        """Move item/s from top of one stack to another 

        Args:
            num_to_move (int): how many items to move from one stack to another
            from_stack (int): which stack to move from
            to_stack (int): which stack to move to
        """
        # If multiple items are to to be moved at once then create a list of items to be moved 
        # and append the reverse to the target stack
        # Otherwise move the items one by one
        if self.move_multi_items:
            items = []
            for i in range(num_to_move):
                items.append(self.stacks_dict[from_stack].pop())
                
            items.reverse()
            self.stacks_dict[to_stack].extend(items)
        else:
            for i in range(num_to_move):
                item = self.stacks_dict[from_stack].pop()
                self.stacks_dict[to_stack].append(item)

    def print_dict(self):
        """Print each key on its own line
        """
        print("Stacks:")
        print()
        for k in self.stacks_dict.keys():
            print(k, self.stacks_dict[k])
        print()

    def get_top_each_stack(self) -> str:
        print("Items at the top of each stack: ")
        res = ""
        for k in self.stacks_dict.keys():
            res+=self.stacks_dict[k][-1]

        return(res)

if __name__ == "__main__":

    print("Part 1: ")

    # Example stack
    #     [D]    
    # [N] [C]    
    # [Z] [M] [P]
    # 1   2   3 

    example_stack = {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }

    example_instructions = """move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2"""

    example_s = stacker(example_stack, example_instructions)
    example_s.run_instructions(print=True)
    
    # Actual Input Part 1
    actual_s = stacker(input.stacks, input.instructions)
    actual_s.run_instructions(print=False)
    print(actual_s.get_top_each_stack())

    # Part 2
    # Change default value of move_multi_items to True
    print("Part 2: ")

    example_s_multi = stacker(example_stack, example_instructions, move_multi_items=True)
    example_s_multi.run_instructions(print=True)

    print("Part 2 actual: ")
    actual_s_multi = stacker(input.stacks, input.instructions, move_multi_items=True)
    actual_s_multi.run_instructions(print=True)
    print(actual_s_multi.get_top_each_stack())