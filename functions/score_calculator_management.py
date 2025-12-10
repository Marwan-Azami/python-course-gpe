# - Please choose an action
# 1 - to add a new mark
# 2 - update a mark, [ 12, 12, 13...]
# 3 - remove a mark
# 4 - calculate the scoring
# 5 - Empty the table
# 6 - Show all the marks with index

from score_calculator_utilities import  get_mark, avg_of_tableau, score

tab_notes = [] # Where we will save mark

#---------------------------------------------------

def select_choice():
    message = """
    # *** Please choose an action ***
    # 0 - Quite
    # 1 - to add a new mark
    # 2 - update a mark, [ 12, 12, 13...]
    # 3 - remove a mark
    # 4 - calculate the scoring
    # 5 - Empty the table
    # 6 - Show all the marks with index
    # 7 - Save in score.txt
    # 8 - Read from score.txt
    # *******************************
    """
    choice = input(message)
    return choice

def show_marks_with_index():
    print("*******************************")
    for index, note in enumerate(tab_notes):
        print("Index = ", index, "Mark = ", note)
    print("*******************************")
#---------------------------------------------------

# To save tab notes in a filed called score.txt
def save_tab_notes():
    _file = open("score.txt", "a+")
    for note in tab_notes:
        _file.write(str(note)+"\n")
    _file.close()

# to read from a file and put these information in the tab_note
def read_tab_notes_from_file():
    _file = open("score.txt", "r")
    for note in _file.readlines():
        tab_notes.append(float(note.strip())) # remove  \n from characters
    _file.close()

while True:
    # Ask the user for an action
    choice = int(select_choice())
    if choice == 1: # to add a mark
        mark = get_mark()
        tab_notes.append(mark)
    elif choice == 2: # to update a mark
        show_marks_with_index()
        index = int(input("Please provide an index"))
        new_mark = get_mark()
        tab_notes[index] = new_mark # tab_notes = [1, 2, 3]
    elif choice == 3: # Remove a mark
        show_marks_with_index()
        index = int(input("Please provide an index"))
        tab_notes.pop(index)
        show_marks_with_index()
    elif choice == 4: # scoring
        calculated_score = avg_of_tableau(tab_notes)
        print(score(calculated_score))
    elif choice == 5: # Empty
        tab_notes.clear()
    elif choice == 6: # Show all marks
        show_marks_with_index()
    elif choice == 0: # Quite
        break
    elif choice == 7: # Save notes
        save_tab_notes()
    elif choice == 8:
        read_tab_notes_from_file()
    else:
        print("Error ")
        continue



