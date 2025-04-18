import xml.etree.ElementTree as ET

def process_library(xml_file):
    try:
        # Загрузка XML
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Вывод списка книг
        print("Список книг:")
        books = root.findall('book')
        total_price = 0
        for book in books:
            title = book.find('title').text
            author = book.find('author').text
            year = book.find('year').text
            genre = book.find('genre').text
            price = float(book.find('price').text)
            total_price += price
            print(f"Название: {title}, Автор: {author}, Год: {year}, Жанр: {genre}, Цена: {price:.2f}")

        # Средняя цена
        avg_price = total_price / len(books)
        print(f"\nСредняя цена книг: {avg_price:.2f}")

        # Фильтрация по жанру
        genre_filter = input("\nВведите жанр для фильтрации: ")
        print(f"\nКниги в жанре '{genre_filter}':")
        for book in books:
            if book.find('genre').text.lower() == genre_filter.lower():
                title = book.find('title').text
                author = book.find('author').text
                print(f"Название: {title}, Автор: {author}")

    except FileNotFoundError:
        print("Файл не найден.")
    except ET.ParseError:
        print("Ошибка парсинга XML.")
    except Exception as e:
        print(f"Ошибка: {e}")

# Вызов функции
process_library('library.xml')