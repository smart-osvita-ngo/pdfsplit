# pdfsplit 
Python Скрипт для розділення PDF на однакові шматки

## Встановлення (MacOS, без git)
1. Завантажте останню версію з https://github.com/smart-osvita-ngo/pdfsplit/releases та розпакуйте архів у бажану теку
2. Зайдіть у теку pdfsplit та запустіть `run` подвійним кліком
3. Скрипт самостійно встановить усе необхідне програмне забезпечення та виконає тестове розбиття pdf

## Інструкція (MacOS)
1. Відкрийте `pdfsplit.py` у текстовому редакторі та вкажіть бажані налаштування: 
    - шлях до файлу який треба розбити (LARGE_PDF_PATH)
    - кількість сторінок в одній частині  (NPAGES)

    Зверніть увагу, що можна скопіювати шлях до файлу сполученням клавіш `Option + Command + C` або у меню файла якщо натиснути `Alt`.
2. Для налаштування назв результуючих файлів, відредагуйте файл `filenames.txt`, один рядок на файл. Або видаліть всі рядки, щоб файли називались просто порядковим номером.
3. Запустіть скрипт натиснувши на файл `run` двічі 
