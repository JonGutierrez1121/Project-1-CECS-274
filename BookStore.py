import Book
import ArrayList
import ArrayQueue
import algorithms
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time

class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()
        

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = DLList.DLList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.bookIndices.add(key, self.bookCatalog.size()-1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)

            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def sort_catalog(self, s):
        start_time = time.time()
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
        if s == 2:
            algorithms.quick_sort(self.bookCatalog, False)
        if s == 3:
            algorithms.merge_sort(self.bookCatalog)
        elapsed_time = time.time() - start_time
        print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")


    def search_by_prefix(self, prefix, algo):
        if algo == 1:
            a = ArrayList.ArrayList()
            for i in self.bookCatalog:
                a.append(i)
            book = Book.Book(None, prefix, None, 1, None)
            while True:
                index = algorithms.linear_search(a, book)
                if index == -100:
                    break
                print(a.get(index))
        elif algo == 2:
            a = ArrayList.ArrayList()
            b = ArrayList.ArrayList()
            for i in self.bookCatalog:
                a.append(i)
            book = Book.Book(0, prefix, 0, 0, 0)
            while True:
                index = algorithms.binary_search(a, book)
                if index == -100:
                    break
                b.append(a.get(index))
                a.remove(index)
            algorithms.quick_sort(b)
            for i in b:
                print(i)



    def display_catalog(self, n):
        if n <= self.bookCatalog.size():
            for i in range(n):
                print(self.bookCatalog.get(i))

    def getCartBestSeller(self):
        print(self.shoppingCart.max().title)

    def bestsellers_with(self, infix, structure, n=0):
        data = None
        if infix == "":
            print("Invalid infix.")
        else:
            if structure != 1 and structure != 2:
                print("Invalid data structure.")
            else:
                start_time = time.time()
                if structure == 1:
                    data = BinarySearchTree.BinarySearchTree()
                    count = 0
                    for book in self.bookCatalog:
                        if count == n:
                            break
                        if infix in book.title:
                            data.add(book.rank, book)
                            count += 1
                    new_list = data.in_order()
                    for i in range(len(new_list) - 1, -1, -1):
                        print(new_list[i])
                else:
                    data = BinaryHeap.BinaryHeap()
                    count = 0
                    for book in self.bookCatalog:
                        if count == n:
                            break
                        if infix in book.title:
                            book.rank *= -1
                            data.add(book)
                            data.trickle_down(data.size() - 1)
                            count += 1
                    for i in range(data.size()):
                        one_book = data.remove()
                        one_book.rank *= -1
                        print(one_book)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix: str):
        if len(prefix) == 0:
            print("Book not found.")
            return False
        temp = self.sortedTitleIndices.find(prefix)
        if temp is not None:
            book = self.bookCatalog.get(temp.v)
            self.shoppingCart.add(book)
            print("Added Title", book.title)
        else:
            print("Book not Found.")
        
    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, key):
        start_time = time.time()
        temp = self.bookIndices.find(key)
        if temp != None:
            s = self.bookCatalog.get(temp)
            self.shoppingCart.add(s)
            print(s.title)
        else:
            print("Book not found")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey in {elapsed_time} seconds")

    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        # todo
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")