import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_incorrect_genre(self):
        book_name = 'Дом-2 в 20 томах: полное издание'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Треш')

        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize("book_name, genre", [["Parks and recreation", "Комедии"], ["Shrek", "Мультфильмы"]])
    def test_get_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        book_name1 = "Lord of the pringles"
        book_name2 = "Two bottles"
        genre = 'Фантастика'
        collector = BooksCollector()
        collector.add_new_book(book_name1)
        collector.add_new_book(book_name2)
        collector.set_book_genre(book_name1, genre)
        collector.set_book_genre(book_name2, genre)

        assert collector.get_books_with_specific_genre(genre) == [book_name1, book_name2]

    def test_get_books_genre(self):
        book_name1 = "The wire"
        book_name2 = "The office"
        collector = BooksCollector()
        collector.add_new_book(book_name1)
        collector.add_new_book(book_name2)
        collector.set_book_genre(book_name1, "Детективы")
        collector.set_book_genre(book_name2, "Комедии")

        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_doesnt_return_horror(self):
        book_name = "It"
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')

        assert collector.get_books_for_children() == []

    def test_add_not_in_genre_dict_book_in_favorites(self):
        book_name = "Black book"
        collector = BooksCollector()
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize("book_name", ["PHIL-osophy of life", "Remember Modern Talking?", "Pudge"])
    def test_add_book_to_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        book_name = "White book"
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        name1 = "First book"
        name2 = "Second book"

        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.add_new_book(name2)

        collector.add_book_in_favorites(name1)
        collector.add_book_in_favorites(name2)

        assert collector.get_list_of_favorites_books() == [name1, name2]
