fav_movie = []
fav_books = []
print("_______________Favourite's List_______________")
print("            1.Insert Favourite book")
print("            2.Remove book from list")
print("            3.Insert Favourite movie")
print("            4.Remove movie from list")
print("            5.Display books and movies list")
print("            0.Exit Program")
print("______________________________________________")

while True:
    ch = int(input("Enter Your choice: "))
    if ch == 0:
        break
    elif ch == 1:
        book = input("Enter name of the book")
        if book not in fav_books:
            fav_books.append(book)
    elif ch == 2:
        fav_books.remove(input("Enter the book you want to remove: "))
    elif ch == 3:
        movie = input("Enter the name of the movie: ")
        if movie not in fav_movie:
            fav_movie.append(movie)
    elif ch == 4:
        fav_movie.remove(input("Enter the movie you want to remove: "))
    elif ch == 5:
        print("Favourite books: ")
        for i in fav_books:
            print(i, end='\n')
        print("Favourite movies: ")
        for i in fav_movie:
            print(i, end='\n')
    else:
        print("Wrong choice! Enter again")
