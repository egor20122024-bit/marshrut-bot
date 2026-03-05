import os

# Создаем папку для файлов если её нет
if not os.path.exists("route_files"):
    os.makedirs("route_files")
    print("✅ Папка route_files создана")

# Список всех маршрутов и их файлов
files_to_create = [
    # 1. Терновский канал
    ("kanal.jpg", "Фото Терновского канала"),
    ("kanal.kml", "KML файл Терновского канала"),
    
    # 2. Терновский канал (короткая версия)
    ("kanal_short.jpg", "Фото короткого канала"),
    ("kanal_short.kml", "KML короткого канала"),
    
    # 3. Терновка - Северный
    ("severniy.jpg", "Фото маршрута Северный"),
    ("severniy.kml", "KML Северный"),
    
    # 4. Терновка - Северный (версия 2)
    ("severniy_v2.jpg", "Фото Северный v2"),
    ("severniy_v2.kml", "KML Северный v2"),
    
    # 5. Терновка - Скейт парк
    ("skate.jpg", "Фото Скейт парка"),
    ("skate.kml", "KML Скейт парка"),
    
    # 6. Терновка - р. Южный Буг
    ("bug.jpg", "Фото Южного Буга"),
    ("bug.kml", "KML Южного Буга"),
    
    # 7. Терновка - Пляж Коларово
    ("kolarovo.jpg", "Фото Коларово"),
    ("kolarovo.kml", "KML Коларово"),
    
    # 8. Терновка - Парк победы
    ("park_pobedy.jpg", "Фото Парка Победы"),
    ("park_pobedy.kml", "KML Парка Победы"),
    
    # 9. Терновка - Капустино
    ("kapustino.jpg", "Фото Капустино"),
    ("kapustino.kml", "KML Капустино"),
    
    # 10. Терновка - Капустино (версия 2)
    ("kapustino_v2.jpg", "Фото Капустино v2"),
    ("kapustino_v2.kml", "KML Капустино v2"),
    
    # 11. Терновка - Метро
    ("metro.jpg", "Фото Метро"),
    ("metro.kml", "KML Метро"),
    
    # 12. Метро - Стадион
    ("stadion.jpg", "Фото Стадиона"),
    ("stadion.kml", "KML Стадиона"),
    
    # 13. Терновка - Стрелка
    ("strelka.jpg", "Фото Стрелки"),
    ("strelka.kml", "KML Стрелки"),
    
    # 14. Терновка - Дикий Сад
    ("dikiy_sad.jpg", "Фото Дикого Сада"),
    ("dikiy_sad.kml", "KML Дикого Сада"),
    
    # 15. Терновка - Стелла "Миколаїв"
    ("stella.jpg", "Фото Стеллы"),
    ("stella.kml", "KML Стеллы"),
    
    # 16. Терновка - Флагшток
    ("flag.jpg", "Фото Флагштока"),
    ("flag.kml", "KML Флагштока"),
    
    # 17. Терновка - 8 Причал
    ("prichal8.jpg", "Фото 8 Причала"),
    ("prichal8.kml", "KML 8 Причала"),
    
    # 18. Терновка - Макдональдс
    ("mac.jpg", "Фото Макдональдса"),
    ("mac.kml", "KML Макдональдса"),
    
    # 19. Терновка - Сказка
    ("skazka.jpg", "Фото Сказки"),
    ("skazka.kml", "KML Сказки"),
    
    # 20. Терновка - Епицентр
    ("epicentr.jpg", "Фото Епицентра"),
    ("epicentr.kml", "KML Епицентра"),
    
    # 21. Терновка - Варваровка пляж
    ("varvarivka_plyazh.jpg", "Фото Варваровка пляж"),
    ("varvarivka_plyazh.kml", "KML Варваровка пляж"),
    
    # 22. Терновка - Константиновка
    ("konstantinovka.jpg", "Фото Константиновки"),
    ("konstantinovka.kml", "KML Константиновки"),
    
    # 23. Терновка - Намыв коса
    ("namiv.jpg", "Фото Намыв косы"),
    ("namiv.kml", "KML Намыв косы"),
    
    # 24. Терновка - Добрая Надия
    ("dobra_nadiya.jpg", "Фото Доброй Надии"),
    ("dobra_nadiya.kml", "KML Доброй Надии"),
]

print("📁 Создаю файлы в папке route_files:")
print("=" * 50)

for filename, description in files_to_create:
    filepath = os.path.join("route_files", filename)
    try:
        # Создаем пустой файл
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Это временный файл для {description}. Замени его на настоящий!")
        print(f"✅ {filename}")
    except Exception as e:
        print(f"❌ Ошибка при создании {filename}: {e}")

print("=" * 50)
print(f"✅ Всего создано файлов: {len(files_to_create)}")
print("📂 Папка: route_files")
print("\n📝 Теперь тебе нужно:")
print("1. Положить настоящие фото в папку route_files")
print("2. Положить настоящие KML файлы в папку route_files")
print("3. Исправить пути в bot.py (я помогу)")
print("4. Запустить бота командой: python bot.py")