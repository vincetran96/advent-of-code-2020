import re # could be slow
from typing import Iterable
INPUT = "day/7/input"

def extract_child_parent(s: str) -> tuple:
    '''Extracts child and parent from a line
    '''
    bags = r" *bags*"
    numbas = r".*\d+ +"

    p, c = s.split("contain")
    p_color = re.split(bags, p.strip())[0].strip()
    c_colors = re.split(bags, c.strip())
    c_colors_tup = ()
    for c in c_colors:
        if re.search(numbas, c):
            c_colors_tup = (*c_colors_tup, re.split(numbas, c)[1])
    return p_color, c_colors_tup

def extract_parent_numchild(s: str) -> tuple:
    '''Extracts parent, children and number of each child
    '''
    bags = r" *bags*"
    numbas = r"\d+ +"

    p, c = s.split("contain")
    p_color = re.split(bags, p.strip())[0].strip()
    c_colors = re.split(bags, c.strip())
    child_num = ()
    for c in c_colors:
        numba = re.search(numbas, c)
        if numba:
            child_num = (
                *child_num, (int(numba[0].strip()), re.split(numbas, c)[1].strip()))
    return p_color, child_num

def build_chash(iter: Iterable):
    '''Builds a hash with children as keys,
    tuples of parents as values
    '''
    result = {}
    for line in iter:
        parent, children = extract_child_parent(line)
        for child in children:
            if child not in result:
                result[child] = {parent}
            else:
                result[child].add(parent)
        if parent not in result:
            result[parent] = set()
    return result

def build_phash(iter: Iterable):
    '''Builds a hash with parents as keys,
    children and its numbers as values
    '''
    result = {}
    for line in iter:
        parent, num_child = extract_parent_numchild(line)
        if parent not in result:
            result[parent] = {t[1]: t[0] for t in num_child}
        else:
            result[parent] = {**result[parent], **{t[1]: t[0] for t in num_child}}
    return result

def find_parents(h: dict, child: str, found: set = set()):
    '''Finds the set of parents for the `child` in hash `h`
    '''
    parents = h[child]
    if parents:
        found.update(parents)
        for p in parents:
            found.update(find_parents(h, p, found))
        return found
    else:
        return set()

def find_num_children(h: dict, parent: str):
    '''Finds the total number of bags for `parent` in hash `h`
    '''
    children = h[parent]
    if children:
        return sum(
            num + num * find_num_children(h, color) for color, num in children.items()
        )
    else:
        return 0

def part1(input: str):
    with open(input, "r") as openfile:
        h = build_chash(openfile.readlines())
        return len(find_parents(h, "shiny gold"))

def part2(input: str):
    with open(input ,"r") as openfile:
        h = build_phash(openfile.readlines())
        return find_num_children(h, "shiny gold")

if __name__ == "__main__":
    print(part1(INPUT))
    print(part2(INPUT))
