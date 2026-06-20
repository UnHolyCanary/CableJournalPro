class EquipmentDetector:

    @staticmethod
    def detect(block_name):
        name = block_name.lower()
        #правила добавили буду дополнять по мере необходимости
        RULES = {
     "камера": "📹 Камера",
     "коммутатор": "🌐 Коммутатор",
     "шкаф": "🗄️ Шкаф",
     "турникет": "🚪 Турникет",
     "дип": "🔥 Пожарный извещатель",
}
        # Камеры
        if "камера" in name or "camera" in name:
            return "📹 Камера"

        # Коммутаторы
        if "коммутатор" in name or "switch" in name:
            return "🌐 Коммутатор"

        # Шкафы
        if "шкаф" in name or "rack" in name:
            return "🗄️ Шкаф"

        # Турникеты
        if "турникет" in name:
            return "🚪 Турникет"

        # Контроллеры
        if "контроллер" in name:
            return "🎛️ Контроллер"

        # Извещатели
        if "дип" in name or "извещ" in name:
            return "🔥 Пожарный извещатель"

        # Кабель
        if "кабель" in name or "utp" in name or "ftp" in name:
            return "🔌 Кабель"

        return "❓ Не определено"