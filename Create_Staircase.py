#Funtion to iterate of file and get number/word pairs for dictionary.  Returns the completed dictionary
def decode(message_file):
    num_word_pair = {}
    with open(message_file) as file:
       for line in file:
            line_list = line.split()
            num = int(line_list[0])
            word = line_list[1]
            num_word_pair[num] = word
    return num_word_pair
        
#Function to build the pyramid of numbers to pull the last number of each level.  Returns a list of the numbers in the last position of each level
def build_pyramid(limit):
    current_number = 1
    row = 1
    last_num_list = []
    while current_number <=limit:
        for x in range(row):
            print(current_number, end=" ")
            current_number += 1
            if current_number > limit:
                break
        last_num_list.append(current_number-1)
        print()
        row += 1
    return(last_num_list)

#Function to take in the list of the last numbers and the sorted dictionary to build the phrase using the associated words.  Returns the final string
def solve_puzzle(key_list, sorted_dic):
    puzzle_string = ""
    for x in key_list:
        next_word = sorted_dic[x]
        puzzle_string = puzzle_string + " " + next_word
    print(puzzle_string)
     
#Calls function with inital file
num_word_dic = decode("coding_qual_input.txt")

#Sorts the return dictionary of number/word pairs
sorted_dic = dict(sorted(num_word_dic.items(), key=lambda item:item[0]))

#Gets last key number for range to pyramid.  Used to find the levels of the pyramid structure
last_key = None
for key,value in reversed(sorted_dic.items()):
     last_key = key
     break

#Runs the pyramid to get the last numbers from the levels
key_list = build_pyramid(last_key)

#Solves the puzzle using the key list and sorted dictionary
solve_puzzle(key_list, sorted_dic)