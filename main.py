import os  # Moduł do pracy z systemem plików
import time  # Moduł do obsługi czasu

def usun_stare_pliki(folder, jednostka_czasu="dni", prog_czasu=2):
    """
    Funkcja usuwa pliki starsze niż określony próg czasu z podanego folderu.

    Parametry:
    folder (str): Ścieżka do folderu, w którym mają być usunięte stare pliki.
    jednostka_czasu (str): Jednostka czasu, np. "sekundy", "dni", "miesiace", "lata".
    prog_czasu (int): Próg czasu w wybranej jednostce.
    """
    teraz = time.time()  # Pobiera aktualny czas w sekundach od epoki Unix (1 stycznia 1970)

    # Konwersja jednostek czasu na sekundy
    konwersja = {
        "sekundy": 1,
        "minuty": 60,
        "godziny": 3600,
        "dni": 86400,
        "miesiace": 2592000,  # Przyjmując miesiąc = 30 dni
        "lata": 31536000      # Przyjmując rok = 365 dni
    }

    if jednostka_czasu not in konwersja:
        print(f"Nieznana jednostka czasu: {jednostka_czasu}. Dostępne: {', '.join(konwersja.keys())}")
        return

    prog_czasu_w_sekundach = prog_czasu * konwersja[jednostka_czasu]

    # Sprawdzenie, czy folder istnieje za pomocą obsługi wyjątku
    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"Podany folder '{folder}' nie istnieje.")
    except FileNotFoundError as e:
        print(e)
        return

    # Iteracja po wszystkich plikach w folderze
    for nazwa_pliku in os.listdir(folder):
        sciezka_pliku = os.path.join(folder, nazwa_pliku)  # Tworzy pełną ścieżkę do pliku

        # Sprawdzenie, czy jest to plik (a nie folder)
        if os.path.isfile(sciezka_pliku):
            czas_modyfikacji = os.path.getmtime(sciezka_pliku)  # Pobiera czas ostatniej modyfikacji pliku

            # Sprawdzenie, czy plik jest starszy niż określony próg czasu w sekundach
            if teraz - czas_modyfikacji > prog_czasu_w_sekundach:
                try:
                    os.remove(sciezka_pliku)  # Usuwa plik
                    print(f"Usunięto plik: {nazwa_pliku}")
                except Exception as e:
                    print(f"Błąd podczas usuwania pliku {nazwa_pliku}: {e}")

# Przykład użycia
folder_do_sprawdzenia = r"C:\\Users\\zglre\\PycharmProjects\\KasowaniePlikow\\smieci"  # Ścieżka do folderu
usun_stare_pliki(folder_do_sprawdzenia, jednostka_czasu="dni", prog_czasu=2)
