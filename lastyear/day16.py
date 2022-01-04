from os import error
from typing import Dict, Set
from util import getlines,as_ints
file = "16"

rules = {}
my_ticket = []
nearby_tickets = []
mode = 0
for line in getlines(file):
    if line == 'your ticket:':
        mode = 1
    elif line == 'nearby tickets:':
        mode = 2
    elif mode == 0:
        field,values = line.split(": ")
        ranges = values.split(' or ')
        field_vals = set()
        for range_ in ranges:
            low,high = as_ints(range_.split('-'))
            for i in range(low, high + 1):
                field_vals.add(i)
        rules[field] = field_vals
        #print(f"Rule {field} {field_vals}")
    elif mode == 1:
        my_ticket = as_ints(line.split(','))
    elif mode == 2:
        nearby_tickets.append(as_ints(line.split(',')))

valid_tickets = []
error_rate = 0
total_count = len(nearby_tickets)
for ticket in nearby_tickets:
    all_valid = True
    for val in ticket:
        valid = False
        for field, valid_range in rules.items():
            if val in valid_range:
                valid = True
        if not valid:
            all_valid = False
            error_rate += val
            #print(f"Invalid value {val}")

    if all_valid:
        valid_tickets.append(ticket)
    #print(f"ticket {ticket} {valid}")

print(f"error rate is {error_rate}")

all_fields = set(range(len(valid_tickets[0])))
possibilities = {}

def get_possibilities(field, valid_nums, tickets):
    ret = set(range(len(tickets[0])))
    for i in range(len(tickets[0])):
        for ticket in tickets:
            if ticket[i] not in valid_nums:
                if i == 0:
                    print(f"Ticket {ticket} rules out {field} from {i} ({valid_nums})")
                ret.remove(i)
                break
    return ret

def greedy_bipartite(possibilities: Dict[str, Set[int]]):
    assignment = {}
    while possibilities:
        for field, potential in possibilities.items():
            if len(potential) > 1:
                continue
            assigned_value = potential.pop()
            assignment[field] = assigned_value
            print(f"Assigning {field} as {assigned_value}")
            del possibilities[field]
            for other_field, other_potential in possibilities.items():
                if assigned_value in other_potential:
                    other_potential.remove(assigned_value)
                    if len(other_potential) == 0:
                        print(f"ERROR CONFLICT SADPANDA {field} {other_field}")
                        return None
            break
    return assignment
for field in rules:
    possibilities[field] = get_possibilities(field, rules[field], valid_tickets)

print(possibilities)
assignment = greedy_bipartite(possibilities)
part2 = 1
for field, position in assignment.items():
    if 'departure ' in field:
        part2 *= my_ticket[position]
print(f"Part 2 solution is {part2}")

