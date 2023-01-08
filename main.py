import pyttsx3, PyPDF3


pdfreader = PyPDF3.PdfFileReader(open('PythonTextPdfFile.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'pythoninfo.mp3')
speaker.runAndWait()

speaker.stop()
