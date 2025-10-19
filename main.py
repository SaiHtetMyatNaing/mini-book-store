from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

books = [
  {"id": 2,  "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
  {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
  {"id": 4, "title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez","year": 1967},
  {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen","year": 1813}
]

class Book(BaseModel):
  titile : str
  author : str
  year : int

@app.get("/")
def read_root():
  return { "Hello" : "World" }


# POST - Create a new book
@app.post("/books")
def create_book( book : Book ):
  
  new_book = {
    "id" : 6 ,
    "title" : book.titile,
    "author" : book.author,
    "year" : book.year
  }
  books.append(new_book)
  
  return { "message" : "Book created successfully" , "Book" : books }
    
    
    
    

   


