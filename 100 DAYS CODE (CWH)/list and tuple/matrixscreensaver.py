# import random, sys, time

# WIDTH = 70  # The number of columns

# try:
#     # For each column, when the counter is 0, no stream is shown.
#     # Otherwise, it acts as a counter for how many times a 1 or 0
#     # should be displayed in that column.
#     columns = [0] * WIDTH
#     while True:
#         # Loop over each column:
#         for i in range(WIDTH):
#             if random.random() < 0.02:
#                 # Restart a stream counter on this column.
#                 # The stream length is between 4 and 14 characters long.
#                 columns[i] = random.randint(4, 14)

#             # Print a character in this column:
#             if columns[i] == 0:
#                 # Change this ' '' to '.' to see the empty spaces:
#                 print(' ', end='')
#             else:
#                 # Print a 0 or 1:
#                 print(random.choice([0, 1]), end='')
#                 columns[i] -= 1  # Decrement the counter for this column.
#         print()  # Print a newline at the end of the row of columns.
#         time.sleep(0.1)  # Each row pauses for one tenth of a second.
# except KeyboardInterrupt:
#     sys.exit()  # When Ctrl-C is pressed, end the program.
    
    
import random, sys, time
from colorama import init, Fore

init()  # Initialize colorama

WIDTH = 170  # Number of columns

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                columns[i] = random.randint(4, 14)

            if columns[i] == 0:
                print(' ', end='')
            else:
                # Use bright green text for Matrix effect
                print(Fore.GREEN + str(random.choice([0, 1])), end='')
                columns[i] -= 1
        print()  # Go to the next line
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
