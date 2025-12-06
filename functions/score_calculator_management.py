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
    # 1 - to add a new mark
    # 2 - update a mark, [ 12, 12, 13...]
    # 3 - remove a mark
    # 4 - calculate the scoring
    # 5 - Empty the table
    # 6 - Show all the marks with index
    # 0 - Quite
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
    else:
        print("Error ")
        continue



