import re

import docx
import wikipedia


def normalize_string(string):
    string_without_spec = re.sub('[^А-ЯЁа-яёA-Za-z\s]+', '', string).lower()
    string_with_normal_space = re.sub('[\s]+', ' ', string_without_spec)
    normalized_string = string_with_normal_space.replace('ё', 'е')
    return normalized_string


def hash_code(word):
    hash = 0
    for s in word:
        hash += hash * 37 + ord(s)
    return hash


# 1. Читаем реферат из файла
doc = docx.Document("Жизнь.docx")
text_par = []
for paragraph in doc.paragraphs:
    text_par.append(paragraph.text)

# 2. Нормализуем текст
abstract = normalize_string(' '.join(text_par))

# 3. Читаем вики-страницу и нормализуем текст
wikipedia.set_lang("ru")
wiki_page = normalize_string(wikipedia.page("Жизнь").content)

# 4. Разделяем тексты по словам
abstract = abstract.split(" ")
wiki_page = wiki_page.split(" ")

# 5. Для каждого слова вычисляем хэш
hash_abstract = []
for word in abstract:
    hash_abstract.append(hash_code(word))

hash_wiki_page = []
for word in wiki_page:
    hash_wiki_page.append(hash_code(word))

# 6. Осталось всего лишь посчитать процент плагиата..
triple_hash_abstract = []
for i in range(len(hash_abstract) - 2):
    triple_hash_abstract.append(hash_abstract[i] + hash_abstract[i + 1] + hash_abstract[i + 2])

triple_hash_wiki_page = []
for i in range(len(hash_wiki_page) - 2):
    triple_hash_wiki_page.append(hash_wiki_page[i] + hash_wiki_page[i + 1] + hash_wiki_page[i + 2])

triple_hash_wiki_page_set = set(triple_hash_wiki_page)

count_words = 0
is_last_triple_plagiarized = False
for triple in triple_hash_abstract:
    if triple_hash_wiki_page_set.__contains__(triple):
        count_words += 1 if is_last_triple_plagiarized else 3

# не учитываем, что некоторые слова и тройки могут давать одинаковый хэш :(
print(len(hash_abstract))
print(count_words)
