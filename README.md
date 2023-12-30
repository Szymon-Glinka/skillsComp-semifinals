<p align="center">
  <img src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/61ca9152-2164-4cfa-b2b0-14bd25c4e0f3">
</p>
<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/skillsComp-Robotyka_Mobilna-blue">
  <img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/m/Szymon-Glinka/skillsComp">
  <img alt="GitHub repo file count (file type)" src="https://img.shields.io/github/directory-file-count/Szymon-Glinka/skillsComp">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Szymon-Glinka/skillsComp">
  <img alt="GitHub License" src="https://img.shields.io/github/license/Szymon-Glinka/skillsComp">
</p>


# O projekcie
To repzytorium zawiera rozwiązane wszystkie zadania półfinałowe [SkillsComp - Robotyka Mobilna](https://skillscomp.itee.radom.pl/service/robotyka-mobilna/) razem z wszystkimi plikami użytymi podczas tworzenia tych programów (foldery ```test```). Dodatkowo znajduje się jeden program, który jest połączeniem wszystkich czterech zadań w jedną aplikację.  
*logo zostało wygenerowane przy pomocy [simple logo generator](https://creecros.github.io/simple_logo_gen/)*

# Spis treści:
* [Maze Solver](#MazeSolver)
* [PID](#PID)
* [Color Recognition](#ColorRecognition)
* [Reading QR codes](#ReadingQR)
* [All in one](#All_in-one)

# MazeSolver
### Informacje o programie
Program ten jest rozwiązaniem pierwszego zadania, znajduje się w folderze **_maze_**.
Algorytm rozwiązujący labirynty składa się z dwóch plików Python'a: ```mazeSolver.py``` i ```backendSolvable.py``` 
W pliku ```backendSolvable.py``` znajdują się wszystkie funkcje używane do rozwiązania labiryntu, importowania labiryntu z pliku tekstowego, przygotowywania zaimportowanego labiryntu do rozwiązania oraz znajdowania początku labiryntu.  
W pliku ```mazeSolver.py``` znajduje się funckja rozwiązująca labirynt (sprawdzanie czy da się go rozwiązać, jeśli się nie da to dlaczego), która kożysta z wszystkich funkcji w pliku ```backendSolvable.py```.   

### Zasada działania
Program sprawdza czy dookoła obecnego położenia są wolne komórki (" "), jeżeli tak zapisuje wszystkie pozycje do których jest w stanie *przejść* w następnym kroku. Następnie wykonuje możliwy ruch usuwając go jednocześnie z listy ruchów mopżliwych do wykonania, a poprzednią pozycje dodaje do tabeli z poprzednimi ruchami. Jeżeli dana pozycja nie ma żadnego możliwego ruchu do wykonania, progam wraca do innych możliowych pozycji (jeżeli takie zostały zapisane podczas np. jakiegoś rozwidlenia).  
Algorytm zwraca ```True``` jeżeli dotarł do wyjścia ```E```. Jeżeli nie jest we stanie wykonać żadnych ruchów program zwróci ```False```. Dodatkowo jeżeli labirynt jest niemożliwy do rozwiązania program również zwróci dlaczego, np. ```False, E5 - No solution found``` - oznacza, to że w podanym labiryncie znajduje się więcej niż jedno rozpoczęcie (więcej niż jedna litera, od której program ma zacząć rozwiązywanie)

### Używanie programu do rozwiązania labiryntu
Aby rozwiązać wybrany labirynt należy wpisać lokalizację pliku tekstowego z tym labiryntem   
```maze = getMazeFromTXT(r"TUTAJ LOKALIZACJA PLIKU")```   
NP.  
```maze = getMazeFromTXT(r"F:\skillscomp\z1textFiles\labirynt9.txt") #get maze from txt file```  
Następine należy wpisać jaka litera oznacza pozycję od której program ma zacząć rozwiązywanie labiryntu  
```solvable, info = mazeSolver(maze, "LITERA")```   
NP.   
```solvable, info = mazeSolver(maze, "r") #solve the maze``` - Program rozwiąże labirynt dla małej litery *r*  
Aby wyświetlić dane do debagowania należy w poniższej lini   
```logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M")```   
zmienić ```level=logging.ERROR``` na ```level=logging.DEBUG```

# PID

# ColorRecognition
### Informacje o programie
Ten program jest rozwiązaniem 3 zadania, znajduje się w folderze **_colorRecogniotion_** i składa się zx dwóch plików.  
Aplikacji ```app.py``` oraz algorytmów rozpoznających oraz zaznaczających kolory w pliku ```backend.py```

### Zasada działania
Kiedy użytkownik zaimportuje wyprany obraz, program wykona dwie funkcje:  
* Funkcja pierwsza ```detectColor_markOutlines()```. Wykryje kolor, stworzy maskę, gdzie tylko ten kolor jest zaznaczony, wyznaczy zarys i doda ten zarys do ostatecznej grafiki (same obrysy na czarnym tle). Ta część wkona się 4 razy dla każdego z zdefiniowanego koloru (czerwony, zielony, niebieski, żółty). Ta funkcja również zwraca jakie kolory zostały wykryte.
* Funckja druga ```detectPositionsOfColors()```. Wykrywa kolory i je zaznacza ale na tym samym zdjęciu, z którego kolory zostały wykryte. Dodatkowo funkcja ta zwraca słownik - nazwa koloru jako klucz, a jako wartość tuple, w którym znajdują się: odległość środka prostokąta, którym jest oznaczony wykryty przedmiot w daynym kolorze, od lewego górnego rogu w osi X oraz w osi Y, pozycja tego zaznaczenia w odniesieniu od środka ekrany (lef, right, top, left) oraz odległość tego zaznaczenia od środka obrazu w osi X i Y,
  
# ReadingQR

# All_in-one
