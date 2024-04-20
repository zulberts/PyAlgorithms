### Bubble Sort vs Selection Sort vs Insertion Sort vs Merge Sort vs Quick Sort

Przedstawione wykresy ilustrują jak zmieniają się czasy wykonania poszczególnych algorytmów w zależności od ilości posortowanych słów. Dla małych zestawów danych różnice w czasie sortowania są minimalne, ale w miarę zwiększania ilości danych do posortowania, algorytmy o niższej efektywności stają się znacznie wolniejsze. Algorytm Merge Sort i Quick Sort wykazują znacznie lepszą wydajność, szczególnie dla dużych zestawów danych.

Dla posortowanych list najgorzej sprawuje się Selection Sort, oraz Quick Sort i Merge Sort są wolniejsze w stosunku do Bubble Sort i Insertion Sort.
### Analiza wyników oraz wnioski

| Algorytm | Złożoność czasowa w przypadku średnim i najgorszym |
| -------- | ------------------------------------------------- |
| Bubble Sort | O(n^2) |
| Selection Sort | O(n^2) |
| Insertion Sort | O(n^2) |
| Merge Sort | O(n log n) |
| Quick Sort | O(n log n) |

Powyższe wyniki potwierdzają teoretyczne oczekiwania dotyczące wydajności algorytmów sortowania. Algorytmy o złożoności kwadratowej są odpowiednie dla mniejszych zestawów danych, jednak Bubble sort zawsze wypada najgorzej, chyba że lista jest posortowana, podczas gdy algorytmy o złożoności liniowo-logarytmicznej są bardziej wydajne dla większych zestawów danych.

Wniosek jest bardzo prosty: Dla list praktycznie posortowanych najlepiej stosować algorytmy jak Bubble Sort, Insertion Sort, natomiast dla nieznanych danych najlepiej
stosować algorytmy jak Merge Sort oraz Quick Sort. Przy małych ilościach danych dla człowieka różnica jest niewykrywalna ponieważ algorytmy wykonują swoje zadanie
w ciągu tysięcznych sekund. Przy większych ilościach danych w porównaniu z innymi algorytmami Quick Sort i Merge Sort nie ma praktycznie różnicy, jednak jak przyjrzymy
im się osobno to można zobaczyć że Quick Sort jest szybszy niż Merge Sort.
