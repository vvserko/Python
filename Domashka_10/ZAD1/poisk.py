def find_book(books, item):
    a = []
    for element in books:
        if element.item == item:
            a.append(element)
        else:
            print('Совпадений не найдено')
