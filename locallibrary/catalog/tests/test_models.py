from django.test import TestCase

from catalog.models import Author, Book, Genre, Language, BookInstance
import datetime


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name="Big", last_name="Bob")

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_death").verbose_name
        self.assertEqual(field_label, "Died")

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "date of birth")

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f"{author.last_name}, {author.first_name}"
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), "/catalog/author/1")


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name="Cyberpunk")
        language = Language.objects.create(name="english")
        book = Book.objects.create(
            title="foundation",
            author=Author.objects.create(first_name="Isaac", last_name="Asimov"),
            summary="very cool",
            isbn="4569785231025",
            language=language,
        )
        book.genre.add(genre)

    def test_book_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_book_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_book_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("summary").verbose_name
        self.assertEqual(field_label, "summary")

    def test_book_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("summary").max_length
        self.assertEqual(max_length, 1000)

    def test_book_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("isbn").verbose_name
        self.assertEqual(field_label, "ISBN")

    def test_book_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("isbn").max_length
        self.assertEqual(max_length, 13)

    def test_book_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_book_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), "/catalog/book/1")

    def test_book_display_genre(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.display_genre(), "Cyberpunk")

    def test_object_return_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.title}"
        self.assertEqual(str(book), expected_object_name)


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Cyberpunk")

    def test_genre_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_genre_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field("name").max_length
        self.assertEqual(max_length, 200)

    def test_object_return_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = f"{genre.name}"
        self.assertEqual(str(genre), expected_object_name)


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name="english")

    def test_language_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_language_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field("name").max_length
        self.assertEqual(max_length, 20)

    def test_object_return_name(self):
        language = Language.objects.get(id=1)
        expected_object_name = f"{language.name}"
        self.assertEqual(str(language), expected_object_name)


class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        book = Book.objects.create(
            title="foundation",
            author=Author.objects.create(first_name="Isaac", last_name="Asimov"),
            summary="very cool",
            isbn="4569785231025",
            language=Language.objects.create(name="english"),
        )
        BookInstance.objects.create(book=book, status="a", imprint="first version")

    def test_bookinstance_status_label(self):
        instance = BookInstance.objects.get(status="a")
        field_label = instance._meta.get_field("status").verbose_name
        self.assertEqual(field_label, "status")

    def test_bookinstance_imprint_label(self):
        instance = BookInstance.objects.get(status="a")
        field_label = instance._meta.get_field("imprint").verbose_name
        self.assertEqual(field_label, "imprint")

    def test_bookinstance_imprint_max_length(self):
        instance = BookInstance.objects.get(status="a")
        field_label = instance._meta.get_field("imprint").max_length
        self.assertEqual(field_label, 200)

    def test_bookinstance_book_label(self):
        instance = BookInstance.objects.get(status="a")
        field_label = instance._meta.get_field("book").verbose_name
        self.assertEqual(field_label, "book")

    def test_bookinstance_book_title(self):
        instance = BookInstance.objects.get(status="a")
        expected_object_name = f"{instance.id} ({instance.book.title})"
        self.assertEqual(str(instance), expected_object_name)

    def test_bookinstance_due_back_label(self):
        instance = BookInstance.objects.get(status="a")
        field_label = instance._meta.get_field("due_back").verbose_name
        self.assertEqual(field_label, "due back")

    def test_bookinstance_is_overdue_false(self):
        instance = BookInstance.objects.get(status="a")
        instance.due_back = datetime.date.today()
        instance.status = "o"
        self.assertEqual(instance.is_overdue(), False)

    def test_bookinstance_is_overdue_true(self):
        instance = BookInstance.objects.get(status="a")
        instance.due_back = datetime.date.today() - datetime.timedelta(days=365.25 / 2)
        instance.status = "o"
        self.assertEqual(instance.is_overdue(), True)
