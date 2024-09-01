# ============

"""
Налаштування розбивача PDF.

Розбиваємо велику PDF на багато маленьких фалйів однакового розміру.
Зараз тут значення для тестового pdf. 
"""

# Шлях до великого PDF файлу, який треба розбити
LARGE_PDF_PATH = "sample-large.pdf"

# Кількість сторінок у кожному маленькому PDF
NPAGES = 2;

# Шлях до теки, в яку помістити згенеровані маленькі PDF
OUTPUT_PDF_DIR = "out"

"""
Налаштування назв маленьких PDF файлів.

Можна помістити бажані імена файлів у файл filenames.txt щоб отримані
маленькі PDF файли мали певні назви (не впливає на закінчення .pdf).

Визначте цей параметр на YES щоб увімкнути цю функцію.
"""

# Можливі значення: "YES", "NO"
USE_FILENAMES_TXT = "YES"

# Шлях до файлу з іменами файлів
FILENAMES_TXT_PATH = "filenames.txt"

# ============

import os
import pymupdf
print(pymupdf.__doc__)
import pandas as pd

def read_xls_column(xls_path: str, sheet: int|str, column: int|str, max_rows: int =1000) -> list:
    data = pd.read_excel(xls_path, sheet, 
                         header=0, nrows=max_rows, 
                         parse_dates=True)
    if isinstance(column, str):
        return data[column]
    return data[data.columns[column]]


def split_pdf(large_pdf_path, npages_in_small_pdf, small_pdf_dir):
    print("Починаємо розбиття PDF")
    doc = pymupdf.open(large_pdf_path)
    npages = doc.page_count;
    assert npages % npages_in_small_pdf == 0, f"Кількість листів великого PDF ({npages}) не ділиться націло на бажану кількість сторінок у частині ({npages_in_small_pdf})"
    ndocs = npages // npages_in_small_pdf

    if USE_FILENAMES_TXT == "YES":
        print(f"Використовуватимемо файл {FILENAMES_TXT_PATH} для визначення назв маленьких файлів")
        filenames = pd.read_csv(FILENAMES_TXT_PATH, header=None)[0]
        assert len(filenames) == ndocs, f"Очікувана кількість документів ({ndocs}) не збігається із кількістю рядків ({len(filenames)}) у {FILENAMES_TXT_PATH}"

    print(f"Створюємо теку {small_pdf_dir} для маленьких PDF файлів")
    os.makedirs(small_pdf_dir, exist_ok=True)
    startpage = 0
    lastpage = npages_in_small_pdf - 1
    for i in range(ndocs):
        print(f"Частина №{i+1}. Опрацьовуємо сторінки {startpage+1}-{lastpage+1}...", end='')

        smalldoc = pymupdf.open()
        smalldoc.insert_pdf(doc, from_page=startpage, to_page=lastpage)
        if USE_FILENAMES_TXT == "YES":
            fname = f"{i+1:03d}_{filenames[i]}.pdf"
        else:
            fname = f"{i+1:03d}.pdf"
        
        print(f" -> {fname}")
        smalldoc.save(os.path.join(small_pdf_dir,fname))

        startpage += npages_in_small_pdf
        lastpage += npages_in_small_pdf
    
    print("Всі частини опрацьовані, кінець скрипту")

if __name__ == "__main__":
    split_pdf(
        LARGE_PDF_PATH, 
        NPAGES,
        OUTPUT_PDF_DIR
        )
