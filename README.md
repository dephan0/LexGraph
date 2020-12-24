#LexGraph 
    Jest to narzędzie do automatycznego sporządzania wykresów 
    z podanego pliku tekstowego.
---
## Użycie
Aby użyć narzędzia, należy otworzyć okno konsoli (najlepiej
w folderze, w którym znajduje się program. Można to zrobić 
klikając prawym przyciskiem myszy w docelowym folderze i 
wybierając "otwórz terminal" lub coś w tym stylu).
Następnie należy wpisać `python lexgraph.py` i podać argumenty
oddzielone spacją, które zdefiniują co będzie robił program.

> Przykład: `python lexgraph.py l pl -s lalka.txt` 
>(program stworzy posortowany wykres wystąpień wszystkich polskich liter
>w tekście lalka.txt)
> - Pierwszym argumentem (po `python lexgraph.py`) jest
    tryb pracy programu, czyli `l` (letters). 
> - Kolejnym argumentem jest język alfabetu, z którego
    zliczane będą litery, czyli `pl` (alfabet polski
    ze znakami diakretycznymi)
> - Kolejnym argumentem jest argument **opcjonalny**, czyli
    `-s` (sortowanie) według **ilości wystąpień**. Jeśli nie 
    wpiszemy tego argumentu, to dane będą posortowane alfabetycznie
> - Kolejnym argumentem jest ścieżka do pliku **tekstowego**.
    Może mieć postać np. `/home/Downloads/lalka.txt`, ale jeśli plik
    znajduje się w tym samym folderze, co program, to możemy wpisać 
    wyłącznie nazwę pliku tj. `lalka.txt`
   
 