import asyncio
from typing import Dict

# Simulated database
books: Dict[int, bool] = {
    1: True,   # True = available
    2: True,
    3: True
}

# Async function to borrow a book
async def borrow_book(user_id: int, book_id: int) -> str:
    print(f"User {user_id} is trying to borrow Book {book_id}...")
    await asyncio.sleep(1)  # simulate delay

    if books.get(book_id):
        books[book_id] = False
        return f"User {user_id} successfully borrowed Book {book_id}"
    else:
        return f"User {user_id} failed: Book {book_id} is not available"


# Async function to return a book
async def return_book(user_id: int, book_id: int) -> str:
    print(f"User {user_id} is returning Book {book_id}...")
    await asyncio.sleep(1)  # simulate delay

    books[book_id] = True
    return f"User {user_id} returned Book {book_id}"


# Main async function to simulate multiple users
async def main() -> None:
    tasks = [
        borrow_book(101, 1),
        borrow_book(102, 1),  # same book → conflict
        borrow_book(103, 2),
        return_book(101, 1),
        borrow_book(104, 1)   # tries again after return
    ]

    results = await asyncio.gather(*tasks)

    print("\n--- Results ---")
    for result in results:
        print(result)


# Run the program
if __name__ == "__main__":
    asyncio.run(main())