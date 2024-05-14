from main import BooksCollector
import pytest


class TestBooksCollector:

    # ADD_NEW_BOOK
    @pytest.mark.parametrize('book',
                             [
                                 'B',
                                 'This is test book',
                                 'This is test book with fourty 40 symbols'
                             ]
                             )
    def test_add_new_book_correct_length_book_added(self, book):
        """ Добавление книги корректной длины (1/2-39/40)"""
        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.books_genre[book] == ''

    @pytest.mark.parametrize('book',
                             [
                                 '',
                                 'It is test book with 41 different symbols',
                                 'This is test book with more than forty one symbols!'
                             ]
                             )
    def test_add_new_book_incorrect_length_book_not_added(self, book):
        """ Добавление книги некорректной длины (0/41/42+)"""
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_two_books_books_added(self):
        """ Добавление двух книг """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_new_book('Another test book')
        assert len(collector.books_genre) == 2

    def test_add_new_book_add_same_book_book_not_added(self):
        """ Добавление повторной книги """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_new_book('Test book')
        assert len(collector.books_genre) == 1

    # SET_BOOK_GENRE
    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
                             )
    def test_set_book_genre_genre_set(self, genre):
        """ Добавление существующего жанра к существующей книге """
        collector = BooksCollector()
        collector.add_new_book('Any test book')
        collector.set_book_genre('Any test book', genre)
        assert collector.books_genre['Any test book'] == genre

    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
                             )
    def test_set_book_genre_no_book_genre_not_set(self, genre):
        """ Добавление существующего жанра к несуществующей книге """
        collector = BooksCollector()
        collector.set_book_genre('Unknown test book', genre)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_no_genre_genre_not_set(self):
        """ Добавление несуществующего жанра к существующей книге """
        collector = BooksCollector()
        collector.add_new_book('Any test book')
        collector.set_book_genre('Any test book', 'Unknown genre')
        assert collector.books_genre['Any test book'] == ''

    # GET_BOOK_GENRE
    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
                             )
    def test_get_book_genre_book_exist_genre_got(self, genre):
        """ Получение жанра существующей книги """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.set_book_genre('Test book', genre)
        assert collector.get_book_genre('Test book') == genre

    def test_get_book_genre_book_not_exist_genre_not_got(self):
        """ Получение жанра несуществующей книги """
        collector = BooksCollector()
        assert collector.get_book_genre('Unknown book') == None

    # GET_BOOKS_WITH_SPECIFIC_GENRE
    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
                             )
    def test_get_books_with_specific_genre_true_data_books_list_returned(self, genre):
        """ Получение существующих книг существующего жанра """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.set_book_genre('Test book', genre)
        assert len(collector.get_books_with_specific_genre(genre)) == 1

    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
                             )
    def test_get_books_with_specific_genre_no_pair_empty_list_returned(self, genre):
        """ Получение несуществующих книг существующего жанра """
        collector = BooksCollector()
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    def test_get_books_with_specific_genre_no_genre_empty_list_returned(self):
        """ Получение существующих книг несуществующего жанра """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.set_book_genre('Test book', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Unknown genre')) == 0

    # GET_BOOK_GENRE
    def test_get_books_genre_books_dict_returned(self):
        """ Получение словаря всех книг и их жанров """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_new_book('Test book 2')
        collector.set_book_genre('Test book 2', 'Детективы')
        assert len(collector.get_books_genre()) == 2

    # GET_BOOKS_FOR_CHILDREN
    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Мультфильмы', 'Комедии']
                             )
    def test_get_books_for_children_books_for_child_in_dict_child_books_returned(self, genre):
        """ Получение детских книг, которые существуют в словаре """
        collector = BooksCollector()
        collector.add_new_book('Book for adults')
        collector.set_book_genre('Book for adults', 'Ужасы')
        collector.add_new_book('Book for children')
        collector.set_book_genre('Book for children', genre)
        assert collector.get_books_for_children() == ['Book for children']

    def test_get_books_for_children_no_books_for_child_empty_list_returned(self):
        """ Получение детских книг, если их нет в словаре """
        collector = BooksCollector()
        collector.add_new_book('Book for adults')
        collector.set_book_genre('Book for adults', 'Детективы')
        assert collector.get_books_for_children() == []

    # ADD_BOOK_IN_FAVORITES
    def test_add_book_in_favorites_book_added(self):
        """ Добавение существующей книги в избранное """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_book_in_favorites('Test book')
        assert collector.favorites == ['Test book']

    def test_add_book_in_favorites_no_such_book_book_not_added(self):
        """ Добавение несуществующей книги в избранное """
        collector = BooksCollector()
        collector.add_book_in_favorites('Unknown book')
        assert collector.favorites == []

    def test_add_book_in_favorites_book_already_in_favorites_book_not_added(self):
        """ Повторное добавение существующей книги, уже находящейся в избранном, в избранное """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_book_in_favorites('Test book')
        collector.add_book_in_favorites('Test book')
        assert len(collector.favorites) == 1

    # DELETE_BOOK_FROM_FAVORITES
    def test_delete_book_from_favorites_book_in_favorites_book_deleted(self):
        """ Удаление существующей книги из избранного """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_book_in_favorites('Test book')
        collector.delete_book_from_favorites('Test book')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_no_such_book_in_favorites_nothing_deleted(self):
        """ Удаление несуществующей книги из избранного """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_book_in_favorites('Test book')
        collector.delete_book_from_favorites('Any other test book')
        assert len(collector.favorites) == 1

    # GET_LIST_OF_FAVORITES_BOOKS
    def test_get_list_of_favorites_books_favorites_list_got(self):
        """ Получение списка избранных книг """
        collector = BooksCollector()
        collector.add_new_book('Test book')
        collector.add_book_in_favorites('Test book')
        assert collector.get_list_of_favorites_books() == ['Test book']
