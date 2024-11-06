from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def word_to_pdf(input_file, output_file):
    # Открываем документ Word
    doc = Document(input_file)
    pdf = canvas.Canvas(output_file, pagesize=letter)
    
    # Задаем начальные координаты для текста
    width, height = letter
    y = height - 40
    
    # Проходим по всем параграфам документа и добавляем их в PDF
    for paragraph in doc.paragraphs:
        if y < 40:  # Если мы достигли нижней границы страницы
            pdf.showPage()
            y = height - 40
        pdf.drawString(40, y, paragraph.text)
        y -= 20  # Расстояние между строками
    
    # Сохраняем PDF
    pdf.save()
    print("Конвертация завершена!")

# Укажите путь к вашему Word файлу и имя выходного PDF файла
input_file = "example.docx"
output_file = "output.pdf"

word_to_pdf(input_file, output_file)
