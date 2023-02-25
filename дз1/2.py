import docx
import wikipedia

doc = docx.Document("Жизнь.docx")
text_par = []
for paragraph in doc.paragraphs:
    text_par.append(paragraph.text)

text = ' '.join(text_par)

wikipedia.set_lang("ru")
wiki_page = wikipedia.page("Жизнь").content
