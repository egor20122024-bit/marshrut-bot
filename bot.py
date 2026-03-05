import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

# Загружаем токен из .env файла
load_dotenv()
TOKEN = "8764344636:AAHuixQ9P4CSgUm4B_axFlvPkquwAxWwYhk"            

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ========== ВСЕ МАРШРУТЫ ==========
ROUTES = {
    "route_1": {
        "name": "🚴 Терновский канал",
        "folder": "Терновский канал",
        "length": "2,5 км",
        "difficulty": "🟢 Легкий",
        "start": "Терновка"
    },
    "route_2": {
        "name": "🚴 Терновский канал (короткая версия)",
        "folder": "Терновский канал (короткая версия)",
        "length": "2,1 км",
        "difficulty": "🟢 Легкий",
        "start": "Терновка"
    },
    "route_3": {
        "name": "🚴 Терновка - Северный",
        "folder": "Терновка - Северный",
        "length": "3,6 км",
        "difficulty": "🟢 Легкий",
        "start": "Терновка"
    },
    "route_4": {
        "name": "🚴 Терновка - Северный (версия 2)",
        "folder": "Терновка - Северный (версия 2)",
        "length": "3,9 км",
        "difficulty": "🟢 Легкий",
        "start": "Терновка"
    },
    "route_5": {
        "name": "🛹 Терновка - Скейт парк",
        "folder": "Терновка - Скейт парк",
        "length": "2,5 км",
        "difficulty": "🟢 Легкий",
        "start": "Терновка"
    },
    "route_6": {
        "name": "🌊 Терновка - р. Южный Буг",
        "folder": "Терновка - р. Южный Буг",
        "length": "5,7 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_7": {
        "name": "🏖 Терновка - Пляж Коларово",
        "folder": "Терновка - Пляж Коларово",
        "length": "7,9 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_8": {
        "name": "🌳 Терновка - Парк победы",
        "folder": "Терновка - Парк победы",
        "length": "7,4 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_9": {
        "name": "🚴 Терновка - Капустино",
        "folder": "Терновка - Капустино",
        "length": "8,4 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_10": {
        "name": "🚴 Терновка - Капустино (версия 2)",
        "folder": "Терновка - Капустино (версия 2)",
        "length": "5,9 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_11": {
        "name": "🚇 Терновка - Метро",
        "folder": "Терновка - Метро",
        "length": "6,5 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_12": {
        "name": "⚽ Метро - Стадион",
        "folder": "Метро - Стадион",
        "length": "1,4 км",
        "difficulty": "🟢 Легкий",
        "start": "Метро"
    },
    "route_13": {
        "name": "🎯 Терновка - Стрелка",
        "folder": "Терновка - Стрелка",
        "length": "8 км",
        "difficulty": "🟡 Средний",
        "start": "Терновка"
    },
    "route_14": {
        "name": "🏛 Терновка - Дикий Сад",
        "folder": "Терновка - Дикий Сад",
        "length": "8,8 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_15": {
        "name": "⭐ Терновка - Стелла Миколаїв",
        "folder": "Терновка - Стелла Миколаїв",
        "length": "8,6 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_16": {
        "name": "🚩 Терновка - Флагшток",
        "folder": "Терновка - Флагшток",
        "length": "10,2 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_17": {
        "name": "⚓ Терновка - 8 Причал",
        "folder": "Терновка - 8 Причал",
        "length": "11,1 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_18": {
        "name": "🍔 Терновка - Макдональдс",
        "folder": "Терновка - Макдональдс",
        "length": "10 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_19": {
        "name": "🎪 Терновка - Сказка",
        "folder": "Терновка - Сказка",
        "length": "10,4 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_20": {
        "name": "🏪 Терновка - Епицентр",
        "folder": "Терновка - Епицентр",
        "length": "10,4 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_21": {
        "name": "🏝 Терновка - Варваровка пляж",
        "folder": "Терновка - Варваровка пляж",
        "length": "13,8 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_22": {
        "name": "🚴 Терновка - Константиновка",
        "folder": "Терновка - Константиновка",
        "length": "14,2 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_23": {
        "name": "⛱ Терновка - Намыв коса",
        "folder": "Терновка - Намыв коса",
        "length": "15 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
    "route_24": {
        "name": "🏡 Терновка - Добрая Надия",
        "folder": "Терновка - Добрая Надия",
        "length": "15,1 км",
        "difficulty": "🔴 Сложный",
        "start": "Терновка"
    },
}

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    
    # Добавляем кнопки для всех маршрутов
    for route_id, route_data in ROUTES.items():
        keyboard.button(text=route_data["name"], callback_data=route_id)
    
    keyboard.adjust(2)  # По 2 кнопки в ряд
    
    await message.answer(
        f"🚴 Веломаршруты Николаева\n\n"
        f"📋 Всего маршрутов: {len(ROUTES)}\n"
        f"👇 Выбери маршрут:",
        reply_markup=keyboard.as_markup()
    )

@dp.callback_query()
async def route_handler(callback: types.CallbackQuery):
    route_id = callback.data
    
    # Если это кнопка "back_to_menu"
    if route_id == "back_to_menu":
        keyboard = InlineKeyboardBuilder()
        for route_id_inner, route_data in ROUTES.items():
            keyboard.button(text=route_data["name"], callback_data=route_id_inner)
        keyboard.adjust(2)
        
        await callback.message.answer(
            f"🚴 Веломаршруты Николаева\n\n"
            f"📋 Всего маршрутов: {len(ROUTES)}\n"
            f"👇 Выбери маршрут:",
            reply_markup=keyboard.as_markup()
        )
        await callback.answer()
        return
    
    # Обычная обработка маршрута
    if route_id in ROUTES:
        route = ROUTES[route_id]
        
        # Формируем описание
        description = (
            f"{route['name']}\n\n"
            f"📏 Длина: {route['length']}\n"
            f"⚡ Сложность: {route['difficulty']}\n"
            f"📍 Старт: {route['start']}"
        )
        
        # Пути к файлам
        folder = route["folder"]
        folder_path = f"route/{folder}"
        
        try:
            # Проверяем что папка существует
            if not os.path.exists(folder_path):
                await callback.message.answer(f"❌ Папка {folder} не найдена!")
                await callback.answer()
                return
            
            # 1. ИЩЕМ ФОТО (jpg ИЛИ png)
            photo_path = None
            for file in os.listdir(folder_path):
                if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
                    photo_path = f"{folder_path}/{file}"
                    print(f"Найдено фото: {file}")
                    break
            
            # 2. ИЩЕМ KML ФАЙЛ
            kml_path = None
            for file in os.listdir(folder_path):
                if file.lower().endswith('.kml'):
                    kml_path = f"{folder_path}/{file}"
                    print(f"Найден KML: {file}")
                    break
            
            # 1. Сначала фото
            if photo_path and os.path.exists(photo_path):
                photo = FSInputFile(photo_path)
                await callback.message.answer_photo(photo=photo)
            else:
                await callback.message.answer("📸 Фото временно отсутствует")
            
            # 2. Потом KML файл
            if kml_path and os.path.exists(kml_path):
                kml = FSInputFile(kml_path)
                await callback.message.answer_document(
                    document=kml,
                    caption="📍 Открой в Google Earth"
                )
            else:
                await callback.message.answer("🗺 KML файл временно отсутствует")
            
            # 3. Потом описание
            await callback.message.answer(description)
            
            # 4. КНОПКА "Посмотреть другой маршрут"
            back_keyboard = InlineKeyboardBuilder()
            back_keyboard.button(text="🔍 Посмотреть другой маршрут", callback_data="back_to_menu")
            await callback.message.answer(
                "👇 Хочешь выбрать другой маршрут?",
                reply_markup=back_keyboard.as_markup()
            )
                
        except Exception as e:
            await callback.message.answer(f"❌ Ошибка: {e}")
            print(f"Ошибка: {e}")
    
    await callback.answer()

async def main():
    print("✅ Бот запущен!")
    print(f"📋 Маршрутов: {len(ROUTES)}")
    
    # Проверяем файлы
    print("\n🔍 Проверка файлов:")
    for route_id, route in ROUTES.items():
        folder = route["folder"]
        folder_path = f"route/{folder}"
        
        print(f"\n📁 {folder}:")
        
        if os.path.exists(folder_path):
            photo_found = False
            kml_found = False
            
            for file in os.listdir(folder_path):
                if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
                    photo_found = True
                    print(f"  ✅ Фото: {file}")
                if file.lower().endswith('.kml'):
                    kml_found = True
                    print(f"  ✅ KML: {file}")
            
            if not photo_found:
                print(f"  ❌ Фото не найдено (нужен .jpg или .png)")
            if not kml_found:
                print(f"  ❌ KML не найдено")
        else:
            print(f"  ❌ Папка не найдена!")
    
    print("\n" + "="*50)
    print("🚀 Бот готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())