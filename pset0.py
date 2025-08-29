# -*- coding: utf-8 -*-
"""
CS 1820 Problem Set 0: Python Coding Questions - Spring 2025
Due January 31, 2025 at 11:59pm
"""
# DO NOT ADD ANY OTHER IMPORT STATEMENTS
import random

#### Coding Problem Set General Instructions - PLEASE READ ####
# 1. All code should be written in python 3.7 or higher to be compatible with the autograder
# 2. Your submission file must be named "pset0.py" exactly
# 3. No outside packages can be referenced or called, they will result in an import error on the autograder
# 4. Function/method/class/attribute names should not be changed from the default starter code provided
# 5. All helper functions and other supporting code should be wholly contained in the default starter code declarations provided.
#    Functions and objects from your submission are imported in the autograder by name, unexpected functions will not be included in the import sequence


###################################
# Question 3.1: Hosoya's Triangle #
###################################

# Instructions: Write an iterative algorithm to generate the first n rows of Hosoya's triangle where indexing starts at 0. 
# E.g. the triangle corresponding to n=5 will have 6 rows in total, one for the 0th row, the 1st row, etc. up until the 
# 5th row. Complete the function below and test your function against the provided test cases to make sure that it is working.
# Do not use any external libraries or online solutions, please use only base python functions and data types.
# More info about Hosoya's Triangle can be found here: https://en.wikipedia.org/wiki/Hosoya%27s_triangle

# Complete the function below and test your function against the provided test cases.
# Do not use any external libraries, please use only base python functions and objects.

# Input: An integer n>=0 denoting the output triangle's depth, indexing starts at 0
# Output: A list of lists containing the first n rows of Hosoya's Triangle

# Example 1: If n = 0 then the return [1]
# Example 2: If n = 3 then the return [[1],[1,1],[2,1,2],[3,2,2,3]]


# ------------------------- #
#----- SAMPLE SOLUTION -----#
# ------------------------- #
# Below is one of many possible approaches that would produce the desired result:
    
def hosoya_triangle(n:int)->list:
    """Returns as a list of lists containing the 0 to n rows of Hosoya's Triangle"""
    #### YOUR CODE HERE ####
    pass


### Sample Test Cases ###
# The following assert statements below will run to test your function, all should run without raising an assertion error 
def test_hosoya():
    # Print Hosoya's Triangle in a visually appealing format
    print_hosoya_triangle(hosoya_triangle(3))
    print_hosoya_triangle(hosoya_triangle(5))
    print_hosoya_triangle(hosoya_triangle(10))
    assert hosoya_triangle(0) == [[1]] # Remember, you must return a list of lists!
    assert hosoya_triangle(3) == [[1],[1,1],[2,1,2],[3,2,2,3]]
    assert hosoya_triangle(10) == [[1],
                                     [1, 1],
                                     [2, 1, 2],
                                     [3, 2, 2, 3],
                                     [5, 3, 4, 3, 5],
                                     [8, 5, 6, 6, 5, 8],
                                     [13, 8, 10, 9, 10, 8, 13],
                                     [21, 13, 16, 15, 15, 16, 13, 21],
                                     [34, 21, 26, 24, 25, 24, 26, 21, 34],
                                     [55, 34, 42, 39, 40, 40, 39, 42, 34, 55],
                                     [89, 55, 68, 63, 65, 64, 65, 63, 68, 55, 89]]
    print("All sample test cases for hosoya_triangle passed!")

# Helper function DO NOT EDIT
def print_hosoya_triangle(triangle_rows):
    """This function prints out a Hosoya Triangle list of lists to the console in a readable format"""
    largest_length=len(str(triangle_rows[-1]))
    for e in range(0,len(triangle_rows)):
        current_row_length=len(str(triangle_rows[e]))
        print("["+str(e)+"]",end="")
        for i in range(0,(largest_length-current_row_length)//2):
            print(" ",end="")
        print(triangle_rows[e])

    

###########################################
# Question 3.2: Sum Nested Lists Function #
###########################################

# Write a recursive algorithm that calculates the sum of all integers within a nested structure of 
# lists. Your function should return a single integer that is the sum of all numbers within the nested 
# lists. For example if the input is [1,2,[3,4],[[5],6,7]] then return 28. Please be 
# sure to use recursion for this exercise. 

# Complete the function below and test your function against the provided test cases.
# Do not use any external libraries, please use only base python functions and data types.

# Input: A nested structure built as a list of lists and/or integers
# Output: A single integer that is the sum of all numbers in the lists

# Example 1: If input_list = [1,2,[3,4],[[5],6,7]] then the return 28
# Example 2: If input_list = [[1,2],[[3]],5,6] then return 17

# ------------------------- #
#----- SAMPLE SOLUTION -----#
# ------------------------- #
# Below is one of many possible approaches that would produce the desired result:
    
def sum_nested_lists(input_list:list)->list:
    """Recursive function that the sum from a nested structure of lists"""
    #### YOUR CODE HERE ####
    pass


### Sample Test Cases ###
# The following assert statements below will run to test your function, all should run without raising an assertion error 
def test_sum_nested():
    assert sum_nested_lists([1,2,[3,4],[[5],6,7]]) == 28
    assert sum_nested_lists([[1,2],[[3]],5,6]) == 17
    assert sum_nested_lists([2,4,6]) == 12
    assert sum_nested_lists([]) == 0
    assert sum_nested_lists([[[[[[[[4]]]]]]]]) == 4
    print("All sample test cases for sum_nested_lists passed!")


####################################
# Question 4.1: Sentiment Analyzer #
####################################

# Instructions: Complete the class declaration in below to create a custom, user-defined data structure that can save 
# perform basic sentiment analysis on a given text. Include a method analyze_sentiment() that takes a text string as input 
# and returns an score of it's overall sentiment. Use a dictionary of positive and negative words (provided to you) to determine 
# the sentiment score by counting positive and negative words in the text. If the number of positive words exceeds negative words, return positive; if negative words are more, return negative; otherwise, return neutral.

# Do not change the names of the methods or class. Do not use external libraries of data structures. 

# Your code should include the following methods:

# __init__: Write a constructor method that takes 4 input arguments specifying the positive, negative, negation, and 
# intensifer word lists. All should be stored as attributes. 

# analyze_sentiment: Write a method that takes in a sentence string and returns the sentiment score. The sentiment
# score is calculated by rules outlined in the pset pdf. All words in the word lists are lowercase, and make sure to
# remove any punctuation in the sentence before splitting the sentence into each word.   
# Input: sentence string. Output: score int

###############################################
# Question 4.2: Sentiment Scoring #
###############################################

# get_sentiment_summary: Write a method that takes in a text string return the summary metrics
# (overall sentiment, positive/negative sentence percentage, most postiive/negative sentence
# for a given text). For the text string, each sentence will be separated by a period. More
# details on the metrics can be found in the pset pdf.
# Input: text string. Output: summary dictionary

### Part 1 and 2: Sentiment Analyzer ###

class SentimentAnalyzer:
    def __init__(self, positive_words, negative_words, negations, intensifiers):
        #### YOUR CODE HERE ####
        pass

    def analyze_sentiment(self, sentence):
        punctuation = "!#$%&'()*+,./:;<=>?@[\]^_`{|}~)"
        #### YOUR CODE HERE ####
        pass
   
    def get_sentiment_summary(self, text): 
        summary = {
          "Overall Sentinment": "",
          "Positive Sentence Percenterage": 0,
          "Negative Sentence Percenterage": 0,
          "Most Positive Sentence": "",
          "Most Negative Sentence": ""
        }

        #### YOUR CODE HERE ####
        pass

    # Helper function DO NOT EDIT
    def print_summary(self, summary):
        for key, value in summary.items():
            print(f"{key}: {value}")


### Sample Test Cases ###
# The following assert statements below will run to test your function, all should run without raising an assertion error 
def test_sentiment_analyzer():
  # Words list
    positive_words = open("positive_words.txt",'r').readlines()
    positive_words = [word.rstrip("\n") for word in positive_words]

    negative_words = open("negative_words.txt",'r').readlines()
    negative_words = [word.rstrip("\n") for word in negative_words]

    negations = ["not", "never", "rarely", "barely"]
    intensifiers = ["very", "really", "extremely", "incredibly", "especially", "so"]

    # Text list
    comments = open("comments.txt",'r').read().replace("\n", " ")
    test_analyzer = SentimentAnalyzer(positive_words, negative_words, negations, intensifiers)
    assert test_analyzer.analyze_sentiment("HUDS food is delicious.") == 1
    assert test_analyzer.analyze_sentiment("The movie was fun, but the dinner was dissappointing") == 0
    assert test_analyzer.analyze_sentiment("Today drained me.") == -1
    assert test_analyzer.analyze_sentiment("I'm not satisfied with your answer.") == -1
    assert test_analyzer.analyze_sentiment("Remy is a really cute cat.") == 2
    assert test_analyzer.analyze_sentiment("Spot is not a puppy anymore, but still adorable.") == 1

    target_summary = {'Overall Sentinment': 'Positive', 
                      'Positive Sentence Percenterage': 0.6, 
                      'Negative Sentence Percenterage': 0.2, 
                      'Most Positive Sentence': 'The professors are SERIOUSLY INCREDIBLE, like so overqualified, inspiring, accomplished, and sufficiently engaging', 
                      'Most Negative Sentence': 'It was by far the most time-consuming and difficult, out of four undergraduate computer science department classes I took this semester'}

    assert test_analyzer.get_sentiment_summary(comments) == target_summary

    test_analyzer.print_summary(test_analyzer.get_sentiment_summary(comments))
    print("All sample test cases for SentimentAnalyzer passed!")

###########################
# Question 5: Tic-Tac-Toe #
###########################

# Instructions: Implement a class-based Tic-Tac-Toe by completing the starter code for TicTacToe below. 
# The board should only contain either only 'X', 'O', or ' ', representing the valid marks or an empty cell.

# Do not change the names of the methods or class. Do not use external libraries of data structures. 

# Your code should include the following methods:

# __init__: Write a constructor method that initializes an empty 3x3 Tic-Tac-Toe board, and sets the
# first player to be the 'X' player

# make_move: Write a method that takes in a row and column value and updates the board if the move
# is valid. If the move is successful, make sure to update the current player to the other player.  
# If the row or column value are invalid, return "Invalid move: Out of bounds"
# If the cell is already taken, return "Invalid move: Cell already taken"
# Otherwise, return "Move successful"
# Input: row int and col int. Output: result string

# check_status: Write a method that returns the status of the board. 
# If a player has 3 marks in a row, return the corresponding "X wins" or "O wins". You can assumme 
# that there will at most be one winner. 
# If the board is full and no player has 3 marks in a row, return "Draw"
# Otherwise, return "In Progress"
# Output: status string

### Bonus Problem: Design a computer algorithm for Tic-Tac-Toe that can win at least 75% of games 
# against a random agent. 

# algo_move: Make a move valid move on the current board, with an algorithm of your choice. You can 
# assume that this method is always called when it is the 'O' player's turn

# Hint: You should be calling make_move() in this method, see random_move() for example. Also take
# a look at play_game to see you algo_move() is called

### Part 3: TicTacToe Game ###

class TicTacToe: 
    
    def __init__(self):
        #### YOUR CODE HERE ####
        self.board = []
        pass

    def make_move(self, row, col):
        #### YOUR CODE HERE ####
        pass

    def check_game_status(self):
        #### YOUR CODE HERE ####
        pass
    
    ### Bonus Problem ###
    def algo_move(self):
        #### YOUR CODE HERE ####
        return self.random_move()

    # Helper function DO NOT EDIT
    def random_move(self): 
        # Makes a random move, filling an open space on the board
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    valid_moves.append((i, j))
        r, c = random.choice(valid_moves)
        self.make_move(r, c)

    # Helper function DO NOT EDIT
    def play_game(self, debug=True): 
        # Plays one game of TicTacToe, with the random agent being the 'X' player and your agent is the 'O' player
        current_player = 0
        status = self.check_game_status()
        while status not in ["X wins", "O wins", "Draw"]:
            if current_player == 0: 
                self.random_move()
                current_player = 1
                if debug:
                    print("Random moves:")
            else:
                self.algo_move()
                current_player = 0
                if debug:
                    print("Computer moves:")
            if debug:
                self.print_board()
      
            status = self.check_game_status()
        if debug:
            print(status)
        return status
    
    # Helper function DO NOT EDIT
    def print_board(self):
        # Display the board
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
# Helper function DO NOT EDIT
def run_games(numGames=1000): 
    # Runs 1000 games of TicTacToe of your agent against the random agent, returning number of wins by your agent
    wins = 0
    for _ in range(numGames):
        game = TicTacToe()
        if game.play_game(debug=False) == "O wins":
            wins += 1
    return wins
                

### Sample Test Cases ###
# The following assert statements below will run to test your function, all should run without raising an assertion error 
def test_TicTacToe():
    game = TicTacToe()
    test_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert game.board == test_board

    test_board[0][0] = 'X'
    assert game.make_move(0, 0) == "Move successful" and game.board == test_board
    assert game.make_move(3, 3) == "Invalid move: Out of bounds" and game.board == test_board
    test_board[2][1] = 'O'
    assert game.make_move(2, 1) == "Move successful" and game.board == test_board
    assert game.make_move(0, 0) == "Invalid move: Cell already taken" and game.board == test_board

    game.make_move(0, 1)
    game.make_move(2, 0)
    game.make_move(0, 2)
    game.print_board()
    assert game.check_game_status() == "X wins"
    
    game.board = [
        ['X', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert game.check_game_status() == "Draw" 
    
    print("All sample test cases for TicTacToe passed!")

    # Bonus question sample-test case  - uncomment to run
    # test_game = TicTacToe()
    # test_game.play_game()
    # assert (run_games() >= 750)

def main(): 
    # Runs all of the sample test cases
    test_hosoya()
    test_sum_nested()
    test_sentiment_analyzer()
    test_TicTacToe()
    
if __name__ == '__main__':
    main()