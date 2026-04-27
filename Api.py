# Endpoint 1: GET /books
#Purpose:
#Retrieve all books in the library.
#Input:
#No input required.

#Output (Example):
{
  "status": "success",
  "data": [
    { "id": 1, "title": "Things Fall Apart", "available": True },
    { "id": 2, "title": "Purple Hibiscus", "available": False }
  ]
}

#Endpoint 2: POST /books
#Purpose:
#Add a new book to the library.

#Input (Example):
{
  "title": "The River Between",
  "author": "Ngugi wa Thiong'o"
}

#Output:
{
  
  "status": "success",
  "message": "Book added successfully",
  "book_id": 3
}

#Endpoint 3: POST /borrow

#Purpose:
#Allow a user to borrow a book.

#Input (Example):
{
  "user_id": 101,
  "book_id": 1
}

#Output (Success):
{
  "status": "success",
  "message": "Book borrowed successfully"
}

#Output (Error):
{
  "status": "error",
  "message": "Book not available"
}

# Endpoint 4: POST /retur

#Purpose:
#Return a borrowed book.

#Input (Example):
{
  "user_id": 101,
  "book_id": 1
}

#Output:
{
  "status": "success",
  "message": "Book returned successfully"
}
#testing
