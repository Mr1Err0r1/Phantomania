translations = {
    "timer_started": {
        "en": "Timer started for {time}.",
        "de": "Timer gestartet für {time}.",
        "ru": "Таймер запущен на {time}."
    },
    "time_up": {
        "en": "⏰ Time is up!",
        "de": "⏰ Zeit ist um!",
        "ru": "⏰ Время вышло!"
    },
    "current_time": {
        "en": "Current time: {time}",
        "de": "Aktuelle Uhrzeit: {time}",
        "ru": "Текущее время: {time}"
    }
}

def get_translation(key, locale, **kwargs):
    lang = "en"  # Default Englisch
    if "de" in locale:
        lang = "de"
    elif "ru" in locale:
        lang = "ru"

    return translations.get(key, {}).get(lang, "").format(**kwargs)
