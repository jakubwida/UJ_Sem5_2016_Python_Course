set term pdf
set output "sort1.pdf"

set title "Sortowanie X"
set xlabel "numer pozycji"              # opis osi x
set ylabel "liczba na pozycji"          # opis osi y
unset key                               # bez legendy

plot "sort1.dat" using 1:2 with points pt 5
