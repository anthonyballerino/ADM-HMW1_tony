#FIRST LINK https://www.hackerrank.com/domains/python/py-introduction
#ex1 Say "Hello, World!" With Python___________________________________________________________________________________
if __name__ == '__main__':
    print("Hello, World!")
#ex2 Python If-Else____________________________________________________________________________________________________________
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n > 1 and n < 6:
            print("Not Weird")
        if n > 5 and n < 21:
            print("Weird")
        if n > 20:
            print("Not Weird")
#ex3 Arithmetic Operators____________________________________________________________________________________________________________
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    absum = a + b
    abdiff = a - b
    abproduct = a*b
    print(absum)
    print(abdiff)
    print(abproduct)
#ex4 Python: Division____________________________________________________________________________________________________________
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    int_division = a//b
    float_division = a/b
    print(int_division)
    print(float_division)
#ex5 Loops____________________________________________________________________________________________________________
if __name__ == '__main__':
    n = int(input())
    non_integer_ints = range(0, n)
    for el in non_integer_ints:
        el = el*el
        print(el)
#ex6 Write a function____________________________________________________________________________________________________________
def is_leap(year):
    leap = False
    if int(year) % 400 == 0:
        leap = True
    else:
        if int(year) % 4 == 0 and int(year) % 100 != 0:
            leap = True
        else:
            leap = False
    return leap

year = int(input())
#ex7 Print Function____________________________________________________________________________________________________________
if __name__ == '__main__':
    n = int(input())
    string_num = ""
    for num in range(1,n+1):
        string_num = string_num + str(num)
print(string_num)


#SECOND LINK https://www.hackerrank.com/domains/python/py-basic-data-types
# Find the runner-up score!___________________________________________________________________________________
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_of_scores = []
    for el in arr:
        list_of_scores.append(el)
    list_of_scores.sort()
    first_score = list_of_scores[-1]
    filtered_los = [] #filtered list of scores
    for el in list_of_scores:
        if el != first_score:
            filtered_los.append(el)
    filtered_los.sort()
    print(filtered_los[-1])
# List comprehension____________________________________________________________________________________________________________
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x_ints = [i for i in range(x+1)]
    y_ints = [i for i in range(y+1)]
    z_ints = [i for i in range(z+1)]
    array = [[xx, yy, zz] for xx in x_ints for yy in y_ints for zz in z_ints]
    filtered_array = []
    for xyz in array:
        sum_xyz = 0
        for el in xyz:
            sum_xyz = el + sum_xyz
        if sum_xyz != n:
            filtered_array.append(xyz)
    print(filtered_array)
#ex Nested Lists____________________________________________________________________________________________________________
if __name__ == '__main__':
    list_of_names = []
    list_of_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_of_names.append(name)
        list_of_grades.append(score)
    lists_to_dict = dict(zip(list_of_names, list_of_grades))
    list_of_grades.sort()
    min_score = list_of_grades[0]
    second_list = []
    for grade in list_of_grades:
        if grade != min_score:
            second_list.append(grade)
    second_lowest_grade = second_list[0]
    people_with_second_lowest_grade = []
    for (key, value) in lists_to_dict.items():
        if value == second_lowest_grade:
            people_with_second_lowest_grade.append(key)
    people_with_second_lowest_grade.sort()
    for name in people_with_second_lowest_grade:
        print(name)
#ex Finding the percentage____________________________________________________________________________________________________________
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for (key, value) in student_marks.items():
        if key == query_name:
            list_with_grades = value
    total = 0
    length = len(list_with_grades)
    for el in list_with_grades:
        total = el + total
    avg = total/length
    #print(avg)
    avg_to_string = str(avg)
    listed_avg = avg_to_string.split(".")
    string_of_decimals = listed_avg[1]
    #print(string_of_decimals)
    definitive_string_of_decimals = ""
    if len(string_of_decimals) < 2:
        definitive_string_of_decimals = string_of_decimals + "0"
    else:
        definitive_string_of_decimals = string_of_decimals[:2]
    definitive_result = listed_avg[0] + "." + definitive_string_of_decimals
    print(definitive_result)
#ex Lists____________________________________________________________________________________________________________
if __name__ == '__main__':
    N = int(input())
    list_of_commands = []
    output_list = []
    for _ in range(N):
        commands = input()
        list_of_commands.append(commands)
    for command in list_of_commands:
        listed_command = command.split()
        if listed_command[0] == "insert":
            output_list.insert(int(listed_command[1]),int(listed_command[2]))
        if listed_command[0] == "print":
            print(output_list)
        if listed_command[0] == "remove":
            if int(listed_command[1]) in output_list:
                output_list.remove(int(listed_command[1]))
        if listed_command[0] == "append":
            output_list.append(int(listed_command[1]))
        if listed_command[0] == "sort":
            output_list.sort()
        if listed_command[0] == "pop":
            output_list.pop()
        if listed_command[0] == "reverse":
            output_list.reverse()

#ex Tuples____________________________________________________________________________________________________________
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_integer_list = tuple(integer_list)
    print(hash(tuple_integer_list))

# 3 LINK https://www.hackerrank.com/domains/python/py-strings______________________________________________________________________________________________________
#ex sWAP cASE____________________________________________________________________________________________________________
def swap_case(s):
    swapped_string = ""
    for char in s:
        if char.isupper() == True:
            swapped_string += char.lower()
        else:
            swapped_string += char.upper()
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#ex string split and join___________________________________________________________________________________________________
ef split_and_join(line):
    listed_line = line.split(" ")
    joined_line = "-".join(listed_line)
    return joined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#ex What's your name?____________________________________________________________________________________________________________
def print_full_name(first, last):
    str(first)
    str(last)
    message = "Hello "+first+" "+last+"! You just delved into python."
    print(message)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
#ex Mutations___________________________________________________________________________________________________
def mutate_string(string, position, character):
    listed_string = list(string)
    listed_string[position] = character
    def_string = "".join(listed_string)
    return def_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
#ex Find a string____________________________________________________________________________________________________________
def count_substring(string, sub_string):
    ls = len(string)
    lss = len(sub_string)
    loss = []  # list of sub strings
    while ls >= lss:
        loss.append(string[:lss])
        string = string[1:]
        ls -= 1
    count = 0
    for el in loss:
        if el == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
#ex String validators____________________________________________________________________________________________________________
if __name__ == '__main__':
    s = input()
    alphanum = 0
    alpha = 0
    num = 0
    lower = 0
    upper = 0
    for char in s:
        if char.isalnum() == True:
            alphanum += 1
        if char.isalpha() == True:
            alpha += 1
            if char.islower() == True:
                lower += 1
            if char.isupper() == True:
                upper += 1
        if char.isdigit() == True:
            num += 1
    if alphanum > 0:
        print("True")
    else:
        print("False")
    if alpha > 0:
        print("True")
    else:
        print("False")
    if num > 0:
        print("True")
    else:
        print("False")
    if lower > 0:
        print("True")
    else:
        print("False")
    if upper > 0:
        print("True")
    else:
        print("False")
#ex text Wrap_________________________________________________________________________________________________
import textwrap

def wrap(string, max_width):
    list_string = []
    while len(string) > max_width:
        list_string.append(string[:max_width])
        string = string[max_width:]
    #if len(string) <= max_width:
    #    list_string.append(string)
    for el in list_string:
        print(el)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

