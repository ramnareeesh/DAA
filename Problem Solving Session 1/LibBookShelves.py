# Consider the problem of storing n books on shelves in a library. The order of the books is fixed by the cataloging
# system and so cannot be rearranged. Therefore, we can speak of a book bi, where 1 ≤ i ≤ n, that has a thickness ti
# and height hi. The length of each bookshelf at this library is L. Suppose all the books have the same height h (
# i.e. , h = hi = hj for all i,j) and the shelves are all separated by a distance of greater than h, so any book fits
# on any shelf. The greedy algorithm would fill the first shelf with as many books as we can until we get the
# smallest i such that bi does not fit, and then repeat with subsequent shelves. Show that the greedy algorithm
# always finds the optimal shelf placement, and analyze its time complexity.

def arrange(books, l):
    shelves = []
    list_books = []
    sum_thickness = 0
    for i in books:
        if (sum_thickness + i) < l:
            list_books.append(i)
            sum_thickness += i
        else:
            shelves.append(list_books)
            list_books = []
            sum_thickness = 0
            list_books.append(i)
            sum_thickness += i
    shelves.append(list_books)
    return shelves


def main():
    no_books = 9
    book_shelves_length = 10
    books = [3, 4, 1, 5, 4, 8, 3, 2, 1]
    print(arrange(books, book_shelves_length))


main()
