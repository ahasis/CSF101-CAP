#---------------------------------------------------------------
# Name: Ahasis Ghimiray
# Department: Mechanical Engineering Department
# Student Id: 02230259
#---------------------------------------------------------------
# Reference 
'''
1. https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
2. https://www.w3schools.com/python/python_functions.asp
3. https://www.programiz.com/python-programming/recursion
'''
#---------------------------------------------------------------
# Solution
# Solution Score: 50267
# Number: 9
#---------------------------------------------------------------

# The following Function is Used to read the input in " input_9_cap1.txt " file. 
def read_input(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content
# Read input from file via the given file path.
file_path = '/Users/ahasis/Desktop/CAP1 Solution/input_9_cap1.txt'
content = read_input(file_path)

# Initialize total score
total_score = 0
# Defined a function to calculate the score for each round based on player's choice, opponent's choice, and result
def calculate_score(player_choice, opponent_choice, result):
    # Assigned  numerical values to the choices
    choices = {'A': 1, 'B': 2, 'C': 3}  
    # Assigned scores based on results
    results = {'X': 0, 'Y': 3, 'Z': 6}
    # Calculated player's score for the round
    player_score = choices[player_choice] + results[result]
    # Return the player's score for the round
    return player_score

# Iterate through each line of content
for line in content:
    # Split the line into opponent's choice and result
    opponent_choice, result = line.strip().split()
    # Determine player's choice based on opponent's choice and result
    if opponent_choice == "A" and result == "X":
        player_choice = 'C'  
    elif opponent_choice == "A" and result == 'Y':
        player_choice = 'A' 
    elif opponent_choice == "A" and result == 'Z':
        player_choice = 'B'  
    elif opponent_choice == "B" and result == 'X':
        player_choice = 'A'
    elif opponent_choice == "B" and result == 'Y':
        player_choice = 'B'
    elif opponent_choice == "B" and result == 'Z':
        player_choice = 'C'
    elif opponent_choice == "C" and result == 'X':
        player_choice = 'B'
    elif opponent_choice == "C" and result == 'Y':
        player_choice = 'C' 
    else:
        player_choice = 'A' 
    # Calculate the round score using the defined function
    round_score = calculate_score(player_choice, opponent_choice, result)
    # Add the round score to the total score
    total_score += round_score

# Print the total score
print("Total Score:", total_score)
