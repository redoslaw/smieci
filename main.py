import os  # Moduł do pracy z systemem plików
import time  # Moduł do obsługi czasu

def usun_stare_pliki(folder):
    """
    Funkcja usuwa pliki starsze niż 2 dni z podanego folderu.

    Parametry:
    folder (str): Ścieżka do folderu, w którym mają być usunięte stare pliki.
    """
    teraz = time.time()  # Pobiera aktualny czas w sekundach od epoki Unix (1 stycznia 1970)

    # Sprawdzenie, czy folder istnieje
    if not os.path.exists(folder):
        print(f"Podany folder '{folder}' nie istnieje.")
        return

    # Iteracja po wszystkich plikach w folderze
    for nazwa_pliku in os.listdir(folder):
        sciezka_pliku = os.path.join(folder, nazwa_pliku)  # Tworzy pełną ścieżkę do pliku

        # Sprawdzenie, czy jest to plik (a nie folder)
        if os.path.isfile(sciezka_pliku):
            czas_modyfikacji = os.path.getmtime(sciezka_pliku)  # Pobiera czas ostatniej modyfikacji pliku

            # Sprawdzenie, czy plik jest starszy niż 2 dni (172800 sekund)
            if teraz - czas_modyfikacji > 172800:
                try:
                    os.remove(sciezka_pliku)  # Usuwa plik
                    print(f"Usunięto plik: {nazwa_pliku}")
                except Exception as e:
                    print(f"Błąd podczas usuwania pliku {nazwa_pliku}: {e}")

# Przykład użycia
folder_do_sprawdzenia = r"C:\\Users\\zglre\\PycharmProjects\\Roomba\\smieci"  # Ścieżka do folderu
usun_stare_pliki(folder_do_sprawdzenia)
