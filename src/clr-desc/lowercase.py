"""
Python program to make the first letter 
of each word capitalized in a string. 
Respects the '/' separator.
"""

from join import join_string
from split import split_string


# Driver Function
if __name__ == "__main__":
  user_input = input()
  # tests
  # user_input = "a100A SOME COLOR/ANOTHER COLOR"
  # user_input2 = "100 SOME COLOR/ANOTHER COLOR/THIRD COLOR"

  # Splitting the string into a list
  word_list = split_string(user_input)

  # Joining the list of strings
  string = join_string(word_list, "capitalize")
  print(string)