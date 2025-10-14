from fastapi import FastAPI 

app = FastAPI()

books = [
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
  },
  {
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
  },
  {
    "id": 4,
    "title": "One Hundred Years of Solitude",
    "author": "Gabriel Garcia Marquez",
    "year": 1967
  },
  {
    "id": 5,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "year": 1813
  }
]


@app.get('/')
def read_root():
    return {  "hello" : "world"}


# GET - Retrieve all books
@app.get('/books')
def get_all_books():
    return books