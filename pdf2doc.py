from pdf2docx import Converter

old_pdf = "sample.pdf"
new_doc = "new_word_file.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()