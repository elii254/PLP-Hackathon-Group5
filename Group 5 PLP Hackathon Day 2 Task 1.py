
def book_points():
  no_of_books = int(input("Enter the number of books purchased this month:\n"))

  if no_of_books <= 0:
    print("Total points: 0\n")

  elif no_of_books == 1:
    print("Total points: 6\n")

  elif no_of_books == 2:
    print("Total points: 16\n")

  elif no_of_books == 3:
    print("Total points: 32\n")

  else:
    print("Total points: 60\n")

book_points()
