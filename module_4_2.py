def test_function():  # 1. Создаем новую функцию test_function
    def inner_function():  # 2. Создаем внутри test_function другую функцию - inner_function.
        # Эта функция печатает значение "Я в области видимости функции test_function"
        print("Я в области видимости функции test_function")
    inner_function()  # 3. Вызываем функцию inner_function внутри функции test_function

test_function()  # Вызываем функцию test_function
inner_function()  # 4. Пробуем вызывать inner_function вне функции test_function - результат 'Ошибка'
                  # имя функции 'inner_function' не определено, из-за попытки доступа к функции вне ее области видимости
