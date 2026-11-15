import library as library_

def main():

    library = library_.Library()

    while True:

        print("\n================================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Register Member")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Issued Books")
        print("8. Remove Book")
        print("9. Exit")

        try:
            choice = int(input("\nEnter your choice (1-9): "))

            match choice:

                case 1:
                    library.add_book()

                case 2:
                    library.view_books()

                case 3:
                    library.search_book()

                case 4:
                    library.register_member()

                case 5:
                    library.issue_book()

                case 6:
                    library.return_book()

                case 7:
                    library.view_issued_books()

                case 8:
                    library.remove_book()

                case 9:
                    print("Thank you for using our Library System!")
                    break

                case _:
                    print("Invalid choice! Enter 1-9.")

        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main()
