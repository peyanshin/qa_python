import pytest

from main import BooksCollector

def test_add_new_book():
    books_collector = BooksCollector()
    books_collector.add_new_book("Книга1")
    assert "Книга1" in books_collector.books_genre

@pytest.mark.parametrize("book_name, expected_result", [
    ("Книга1", True),
    ("ДлинноеНазваниеКнигиПревышающееМаксимальнуюДопустимуюДлину40Символов", False),
    ("СуществующаяКнига", True)
])
def test_parametrized_add_new_book(book_name, expected_result):
    books_collector = BooksCollector()
    books_collector.add_new_book(book_name)
    assert (book_name in books_collector.books_genre) == expected_result

def test_set_book_genre():
    books_collector = BooksCollector()
    books_collector.add_new_book("Детектив1")
    books_collector.set_book_genre("Детектив1", "Детективы")
    assert books_collector.get_book_genre("Детектив1") == "Детективы"

def test_set_non_existent_genre():
    books_collector = BooksCollector()
    books_collector.add_new_book("ЖанрНеНайдено")
    books_collector.set_book_genre("ЖанрНеНайдено", "НеизвестныйЖанр")
    assert books_collector.get_book_genre("ЖанрНеНайдено") == ""  # Жанр не установлен

@pytest.mark.parametrize("genre, expected_books", [
    ("Фантастика", ["КнигаФантастика"]),
    ("Комедии", [])
])
def test_get_books_with_specific_genre(genre, expected_books):
    books_collector = BooksCollector()
    if expected_books:
        books_collector.add_new_book(expected_books[0])
        books_collector.set_book_genre(expected_books[0], genre)
    assert books_collector.get_books_with_specific_genre(genre) == expected_books

def test_add_book_in_favorites():
    books_collector = BooksCollector()
    books_collector.add_new_book("ЛюбимаяКнига")
    books_collector.add_book_in_favorites("ЛюбимаяКнига")
    assert "ЛюбимаяКнига" in books_collector.favorites

@pytest.mark.parametrize("book_name", ["ПовторяющаясяКнига"])
def test_add_duplicate_book_in_favorites(book_name):
    books_collector = BooksCollector()
    books_collector.add_new_book(book_name)
    books_collector.add_book_in_favorites(book_name)
    books_collector.add_book_in_favorites(book_name)  # Попытка добавить повторно
    assert len(books_collector.favorites) == 1  # Проверяем, что книга добавлена только один раз

def test_delete_book_from_favorites():
    books_collector = BooksCollector()
    books_collector.add_new_book("КнигаДляУдаления")
    books_collector.add_book_in_favorites("КнигаДляУдаления")
    books_collector.delete_book_from_favorites("КнигаДляУдаления")
    assert "КнигаДляУдаления" not in books_collector.favorites
