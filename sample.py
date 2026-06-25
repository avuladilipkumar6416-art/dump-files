class MovieBooking:
    def __init__(self):
        self.movies = {
            "Avengers": 10,
            "Batman": 8,
            "Spiderman": 12
        }

    def show_movies(self):
        for m, seats in self.movies.items():
            print(m, "- Seats:", seats)

    def book_ticket(self):
        movie = input("Choose movie: ")
        tickets = int(input("Tickets: "))

        if movie in self.movies:
            if tickets <= self.movies[movie]:
                self.movies[movie] -= tickets
                print("Booking Successful")
            else:
                print("Not enough seats")
        else:
            print("Movie not found")


# ---- Main ----
app = MovieBooking()

while True:
    print("\n1. Show Movies\n2. Book Ticket\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        app.show_movies()

    elif choice == "2":
        app.book_ticket()

    elif choice == "3":
        break

    else:
        print("Invalid choice")