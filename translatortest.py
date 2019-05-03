from py_translator import Translator

while True:
    s = Translator().translate(text='Bugün hava gözümü ağrıdır.', dest='en').text
print(s)
