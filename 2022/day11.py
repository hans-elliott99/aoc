#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 11: Monkey in the Middle
# hans elliott
import math
import copy

class Monkey:
    def __init__(self, text) -> None:
        self.items        = []
        self.op_value     = (None,None)
        self.test_divisor = None
        self.if_true_to   = None
        self.if_false_to  = None
        
        self._parse_text(text)
        self.items_inspected = 0

    def _parse_text(self, text) -> None:
        """Parse the data which defines the monkey's params.
        """
        for string in text:
            key, value = string.strip().split(':')
            match key:
                case "Starting items":
                    #ex: 65, 84, 76
                    self.items = [int(n) for n in value.strip().split(',')]
                    
                case "Operation":
                    #ex: "new = old + n"
                    _, _, _, op, n = value.strip().split(" ") 
                    self.op_value = (op, n)
                        
                case "Test":
                    #ex: "divisible by n"
                    _,_,n = value.strip().split(" ")
                    self.test_divisor = int(n)

                case "If true":
                    #ex: "throw to monkey n"
                    _,_,_,n = value.strip().split(" ")
                    self.if_true_to = int(n)

                case "If false":
                    #ex: "throw to monkey n"
                    _,_,_,n = value.strip().split(" ")
                    self.if_false_to = int(n)


    def _operation(self, item) -> int: ##new item value
        """Modify the item's worry-level based on the operation type and value.
        """
        if self.op_value[0] == "*":
            new = item * int(self.op_value[1]) if self.op_value[1] != "old" else item*item
            return new
        else:
            new = item + int(self.op_value[1]) if self.op_value[1] != "old" else item+item
            return new

    def _test_divisibility(self, item) -> bool:
        """Test if item is divisible by the 'test_divisor' value.
        """
        if item % self.test_divisor != 0:
            return False
        return True 


    def _inspect_next_item(self, worry_coef:int=1, modulus:int=0) -> tuple[int, int]:
        """Inpsect the next item in posession. Perform inpsection operation and test to
        determine which monkey to throw the item to.
        """
        item = self.items.pop(0) 
        item = int( self._operation(item) / worry_coef )
        if modulus > 0:
            item %= modulus
        test = self._test_divisibility(item)
        
        if test:
            return self.if_true_to, item
        return self.if_false_to, item


    def throw_items(self, worry_coef:int=1, modulus:int=0) -> list[tuple[int,int]]:
        """Do one turn. Inpsect all items and return list of tuples:
        (monkey to throw item to, item value).
        """
        output = []
        if self.items:
            for _ in range(len(self.items)):
                output.append( self._inspect_next_item(worry_coef, modulus) )
                self.items_inspected += 1

        return output
    
    def catch_item(self, item:int):
        """Receive item and append to end of items list.
        """
        self.items.append(item)


def monkey_a_round(monkeys_:list[Monkey], worry_coef=1, modulus=0):
    """Perform one round: each monkey takes a turn inspecting and then throwing all items,
    including any items received from other monkeys before their turn began.
    """
    monkeys = monkeys_.copy()

    for i in range( len(monkeys) ):
        pass_ons = monkeys[i].throw_items(worry_coef, modulus)

        for j in range(len(pass_ons)):
            monkeys[pass_ons[j][0]].catch_item(pass_ons[j][1])

    return monkeys



def p1(monkeys):
    # Item values are divided by 3 during each inspection
    monks = copy.deepcopy(monkeys)
    for _ in range(20):
        monks = monkey_a_round(monks, worry_coef=3)

    # Return the monkey business level:
    # the product of the # of inspections made by the 2 most active monkeys
    tot_insp = sorted([m.items_inspected for m in monks], reverse=True)
    return tot_insp[0] * tot_insp[1]


def p2(monkeys):
    # Item values no longer divided by 3, leading to overflow if values are not
    # reduced somehow. Can keep the values small by using:
    #   item % LeastCommonMultiple(test_divisors for all monkeys),
    # because testing if (item % LCM) is divisible by some number is equivalent to
    # testing if (item) is divisible by some number. 
    # Simulate finding least common multiple by finding the list's inner product,
    # since all divisors are prime numbers.
    monks = copy.deepcopy(monkeys)
    mod   = math.prod([m.test_divisor for m in monkeys])
    for _ in range(10_000):
        monks = monkey_a_round(monks, worry_coef=1, modulus=mod)

    # Return the monkey business level:
    # the product of the # of inspections made by the 2 most active monkeys
    tot_insp = sorted([m.items_inspected for m in monks], reverse=True)
    return tot_insp[0] * tot_insp[1]


if __name__=="__main__":
        
    monkeys :list[Monkey] = []
    monki   :list[str]    = []
    with open("advent-of-code/inputs/day11.txt") as f:
        for line in f:
            if line.strip().startswith("Monkey"):
                if monki:
                    monkeys.append( Monkey(monki[:-1]) ) ##remove blank newline
                monki = []
            else:
                monki.append(line.strip())

        else:
            monkeys.append( Monkey(monki) ) ##append final monkey, no newline


    print("Part 1 - monkey business level:", p1(monkeys))
    print("Part 2 - monkey business level:", p2(monkeys))