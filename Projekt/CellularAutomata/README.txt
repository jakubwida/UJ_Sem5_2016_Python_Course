INSTRUKCJA OBSŁUGI AUTOMATU SYMULACJI WODY:

I: aby uruchomić symulator:

	komenda: "python simple_auto_display.py map_1.txt 10"

	Powyższa komenda uruchamia symulację, czytając dane z pliku "map_1.txt"
	i wyświetlając ją z prędkością 10 klatek(kroków) na sekundę.
	
	Nie jet wymagane podanie ilości klatek na sekundę. 
	Domyślną wartością jest 25

	Pozostałe pliki przykładowe to:
		map_2.txt
		map_3.txt
		map_4.txt

II: aby uruchomic edytor:
	komenda: "python simple_auto_editor.py map_5.txt 20 20"

	Powyższa komenda utworzy pustą mapę, zpisywaną na plik "map_5.txt" o rozmiarze 20x20 (kolejno x,y).
	Jesli plik map_5.txt istnieje i został stworzony przy uzyciu edytora i w nim zapisany to
	zostanie on otwarty. Nie bedzie konieczne w takich sytuacjach podawać argumentów
	rozmiaru mapy. Edytor nie otwiera plików pustych.
	
	Edytor obsługuje sie myszką - kliknięcie lewym przycikiem "stawia" "trzymany" bloczek, 
	kliknięcie prawym przyciskiem zmienia "trzymany" bloczek. Aktualnie "trzymany" bloczek jest
	wyświetlany obok kursora. Jeśli jest niewidoczny, to jest możliwe że zlewa się z wyświetlanymi 
	na mapie bloczkami- kliknięcie prawego przycisku pokaże inny, odróżniający się.

	Aby zapisać mapę, należy wcisnąć przycisk "s" na klawiaturze. Tylko zapisane mapy
	mogą zostać otwarte w wyświetlaczu jak i w edytorze.

	UWAGA: mapy które są utworzone z różnymi rozmiarami X i Y (tj. x!=y) mogą nie zostać otwarte 
	przez wyświetlacz, wywołując błąd przy uruchominiu.
	
