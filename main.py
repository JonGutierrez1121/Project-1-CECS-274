import Calculator
import BookStore

def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    while option != '0':
        print ("""
        1 Check mathematical expression 
        0 Return to main menu
        """)
        option=input() 
        if option=="1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")

        ''' 
        Add the menu options when needed
        '''

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by prefix to shopping cart
        9 Search best-sellers with infix 
        10 Sort the catalog
        11 Search book by prefix
        12 Display the first n books of catalog
        0 Return to main menu
        """)
        option=input() 
        if option=="r":
            bookStore.setRandomShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
           # bookStore.pathLength(0, 159811)
        elif option=="2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="4":
            bookStore.removeFromShoppingCart()
        elif option=="5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option =='7':
            key = input("Introduce the book key: ")
            bookStore.addBookByKey(key)
        elif option == "8":
            prefix = input("Please enter a prefix: ")
            bookStore.addBookByPrefix(prefix)
        elif option == "9":
            best_seller = input("Enter infix: ")
            structure = input("Enter structure (1 or 2): ")
            n = input("Enter max number of titles: ")
            bookStore.bestsellers_with(best_seller, structure, n)
        elif option == "10":
            algorithm = input("Choose an algorithm:\n   1 - Merge Sort\n   2 - Quick Sort (first element pivot)\n   3 - Quick Sort(random element pivot)\n Your selection: ")
            bookStore.sort_catalog(algorithm)
        elif option == "11":
            key = input("Enter prefix: ")
            algorithm = input("Choose an algorithm:\n   1 - Linear Search\n   2 - Binary Search\nYour selection: ")
            bookStore.search_by_prefix(key, algorithm)
        elif option == "12":
            key = int(input("Enter the number of books to display: "))
            bookStore.display_catalog(key)
        ''' 
        Add the menu options when needed
        '''

#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()    

if __name__ == "__main__":
  main()
