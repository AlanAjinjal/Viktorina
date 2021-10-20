import sqlite3
import random

conn = sqlite3.connect("mydatabaskn.db")
cursor = conn.cursor()

def sozdP():
    cursor.execute("""CREATE TABLE albums
                  (level int, ran int, vopros text, vart text,
                    pravotv text)
               """)
    cursor.execute(f"""INSERT INTO albums VALUES (1, 1, 'Сколько будет 2+2?', '2, 3, 4, 5', '4')""")
    cursor.execute(f"""INSERT INTO albums VALUES (1, 2, 'Сколько будет 3+3?', '5, 6, 7, 8', '6')""")
    cursor.execute(f"""INSERT INTO albums VALUES (2, 1, 'Столица России', 'Москва, Россия, Токио, Япония', 'Москва')""")
    cursor.execute(f"""INSERT INTO albums VALUES (2, 2, 'Какое образование ты получаешь?', 'Москва, СПО, СПбПУ, Высшее', 'СПО')""")
    cursor.execute(f"""INSERT INTO albums VALUES (3, 1, 'Сколько дней в неделе', 'Больше чем нужно, 7 пятниц, 56, 7', '7')""")
    cursor.execute(f"""INSERT INTO albums VALUES (3, 2, 'Сколько часов в сутках', 'Зависит от энергетика, 25, 24, 23', '24')""")
    cursor.execute(f"""INSERT INTO albums VALUES (4, 1, 'Цвет желтка в курином яйце', 'Желтый, зеленый, зависит от энергетика, цвет звезды по имени Солнце', 'Желтый')""")
    cursor.execute(f"""INSERT INTO albums VALUES (4, 2, 'Имя преподавателя по питону', 'Тенигин, Альберт, Фетисов, Алексей', 'Альберт')""")
    cursor.execute(f"""INSERT INTO albums VALUES (5, 1, 'Сколько лапок у слона', '4, 6, 7, 8', '4')""")
    cursor.execute(f"""INSERT INTO albums VALUES (5, 2, 'Сколько ушек у жирафа', '2, 6, 7, 8', '2')""")

sozdP()

def viktorina(level):
    while level < 6:
        index = random.randrange(2)
        cursor.execute("""SELECT vopros FROM albums WHERE level = {} AND ran = {}""".format(level, index))
        print(cursor.fetchall())
        print("Варианты:")
        cursor.execute("""SELECT vart FROM albums WHERE level = {} AND ran = {}""".format(level, index))
        print(cursor.fetchall())
        otv = input()
        cursor.execute("""SELECT pravotv FROM albums WHERE level = {} AND ran = {}""".format(level, index))
        if otv == cursor.fetchone():
            print("Ответ правильный")
            level += 1
            viktorina(level)
        else:
            print("Вы проиграли")
            return 0
    return 1

if viktorina(1) == 1:
    print("Победа!")
