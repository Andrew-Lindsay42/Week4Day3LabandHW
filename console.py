import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J.R.R.", "Tolkein")
author_repository.save(author1)


book1 = Book("The Lord of the Rings", "Fantasy", author1, "Penguin") 
book_repository.save(book1)
book2 = Book("The Hobbit", "Fantasy", author1, "Penguin")
book_repository.save(book2)