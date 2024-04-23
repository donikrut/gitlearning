import hashlib


def calculate_hash(data):
    # Преобразуем строку данных в байтовый формат
    data_bytes = data.encode('utf-8')

    # Создаем объект хеша SHA-256
    hasher = hashlib.sha256()

    # Обновляем хеш с данными
    hasher.update(data_bytes)

    # Получаем хеш в виде шестнадцатеричной строки
    hash_result = hasher.hexdigest()

    return hash_result


# Пример использования функции для вычисления хеша для строки
data_to_hash = "Hello, World!"
hash_result = calculate_hash(data_to_hash)
print("Хеш строки '{}': {}".format(data_to_hash, hash_result))
