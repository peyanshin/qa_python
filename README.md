# qa_python
Описание тестов:
test_add_new_book:                     проверяет, что метод add_new_book успешно добавляет новую книгу в словарь books_genre.
test_parametrized_add_new_book:        параметризованный тест, проверяющий различные сценарии добавления книги, включая проверку на длину названия и уникальность.
test_set_book_genre:                   проверяет, что метод set_book_genre корректно установливает жанр для книги.
test_set_non_existent_genre:           проверяет попытку установить несуществующий жанр (жанр книги остаётся пустым).
test_get_books_with_specific_genre:    параметризованный тест, проверяющий получение списка книг с определённым жанром.
test_add_book_in_favorites:            проверяет, что метод add_book_in_favorites добавляет книги в избранное.
test_add_duplicate_book_in_favorites:  проверяет, что попытка добавить одну и ту же книгу в избранное повторно не изменяет список избранного.
test_delete_book_from_favorites:       проверяет, что метод delete_book_from_favorites удаляет книги из избранного.
test_get_books_with_specific_genre:    проверяет, что метод get_books_with_specific_genre корректно возвращает список книг для заданного жанра.
test_get_list_of_favorites_books:      проверяет, что метод get_list_of_favorites_books корректно возвращает список избранных книг.
test_get_book_genre_by_name:           проверяет, что метод get_book_genre корректно возвращает жанр для заданной книги.
test_get_books_for_children:           проверяет, что метод get_books_for_children корректно возвращает книги, которые подходят детям (у жанра книги нет возрастного рейтинга), и не включает книги с жанрами, имеющими возрастной рейтинг.
test_add_new_two_books:                проверяет, что метод add_new_book добавляет две книги
test_get_books_name_by_genre:          проверяет, что метод get_book_genre корректно возвращает название для заданного жанра.
