import re

import docx
import wikipedia


def normalize_string(string):
    string_without_spec = re.sub('[^А-ЯЁа-яёA-Za-z\s]+', '', string).lower()
    string_with_normal_space = re.sub('[\s]+', ' ', string_without_spec)
    normalized_string = string_with_normal_space.replace('ё', 'е')
    return normalized_string


def get_ord(symbol):
    if symbol != " ":
        return ord(symbol) - 1072
    return 33


def hash_code(word):
    hash = 0
    for s in word:
        hash += hash * 37 + get_ord(s)
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
abstract_triples = [" ".join(abstract[i: i + 3]) for i in range(len(abstract) - 2)]
hash_abstract_triples = []
for triple in abstract_triples:
    hash_abstract_triples.append(hash_code(triple))

wiki_page_triples = [" ".join(wiki_page[i: i + 3]) for i in range(len(wiki_page) - 2)]
hash_wiki_page_triples = []
for triple in wiki_page_triples:
    hash_wiki_page_triples.append(hash_code(triple))
hash_wiki_page_triples = set(hash_wiki_page_triples)

# 6. Осталось всего лишь посчитать процент плагиата...(
count_words = 0
is_last_triple_plagiarized = False
for triple in hash_abstract_triples:
    if triple in hash_wiki_page_triples:
        count_words += 1 if is_last_triple_plagiarized else 3
        is_last_triple_plagiarized = True
    else:
        is_last_triple_plagiarized = False

print(len(abstract))
print(count_words)
print("Процент плагиата:", round(100 * count_words / len(abstract), 2))
