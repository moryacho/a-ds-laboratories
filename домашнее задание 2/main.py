from crc32_IEEE import crc32
from division_func import hash_division

text = input("Введите текст: ")
print("Выберете метод хэширование: \n"
      "1. Деление \n"
      "2. CRC-32 ")
choice = input("Введите номер: ")

if choice == "1":
    text_hash = hash_division(text)
    print(*text_hash)
    print(f"Количество слов: {len(text_hash)} \n"
          f"Количество уникальных хэшей: {len(set(text_hash))}")
elif choice == "2":
    text_hash = crc32(text)
    print(text_hash)