#1. Co oznacza SELECT * i jakie są zagrożenia związane z jego użyciem?
    # oznacza ze wybierz wszystko, zagrozenia sa takie ze jesli zbyt duza ilosc danych jest w bazie danych to bedzie to obciazajace zapytanie
# 2.Czy WHERE age = NULL zwróci jakiekolwiek wiersze? Dlaczego?
# zwroci te wiersze gdzie age jest rowne null xd
# 3.Co zwróci zapytanie:
# SELECT COUNT(*) FROM employees WHERE salary BETWEEN 4000 AND 6000
# jeśli salary zawiera wartości NULL?
# zwroci liczbe wierszy ktore nie sa null i spelniaja warunek
# Jak działa DISTINCT w zapytaniu z wieloma kolumnami?
# zwraca unikalne pary dwoch kolumn
# Co się stanie, gdy użyjesz ORDER BY z kolumną, która nie istnieje?
# zwystapi blad ktory mowi ze trzeba wywowlac w select kolumne poprzez ktora robimy orderby
# Jak działa LIMIT w połączeniu z ORDER BY?
# zwraca top x najmniejszych lub najwiekszych wierszy
# Czy ORDER BY 2 DESC oznacza sortowanie po drugiej kolumnie SELECT?
# nie
# Jak działa LIKE '%test%' w odniesieniu do indeksów i wydajności?
#nie wiem
# Jaka jest różnica między WHERE price IN (100, 200) a WHERE price = 100 OR price = 200?
# nie ma zadnej roznicy, jest to to samo zapytanie innymi slowami
# Co się stanie, jeśli WHERE zawiera warunek z NULL, np. WHERE category IN ('A', NULL)?
# no wtedy rowy jest jest null daja true czyli przechodzi przez filter


# Jak działa ILIKE i w jakich systemach bazodanowych jest dostępne?
# dziala jak like tylko nie jest casesensitive, jest tylko w postgresie
# Co się stanie, jeśli w GROUP BY użyjesz kolumny zawierającej NULL?
# null jest traktowane jako jakby grupa
# Czym różni się HAVING COUNT(*) > 1 od WHERE COUNT(*) > 1?
# niczym, Jest to to samo dzialanie
# Czy HAVING można stosować bez GROUP BY? Jeśli tak, to kiedy?
# mozna zastosowac bez grupby, no jesli chcemy dac warunek na aggregujace funkcje na danej kolumnie
# Co zwróci zapytanie:
# SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 5?
#zwroci pogrupowane deparment z countem rowow jesli dany deparment ma wiecej niz 5 rowow
# Jakie dane zwróci SELECT COUNT(*) FROM users WHERE email LIKE '%@gmail.com'?
# zwroci tylko emaile z domena @gmail.com
# Czy LIMIT może spowodować pominięcie danych? Wyjaśnij.
# tak, jesli np limit 5 a jest 10 takich samych wartosci
# Jak zachowuje się DISTINCT w połączeniu z ORDER BY?
# dziala jak groupby
# Co oznacza WHERE name LIKE 'J%' i co może pójść nie tak przy jego użyciu?
# oznacza to ze bierz wszystkie imiona ktore zaczynaja sie od J. nie wiem co moze pojsc nie tak
# Jak GROUP BY agreguje dane z NULL? Czy traktuje je jako jedną grupę?
# tak, traktuje je jako jedna grupe
# Jak działa ORDER BY w przypadku danych tekstowych zawierających liczby (np. "10", "2", "1")?
# nie wiem
# Co oznacza SELECT COUNT(city) i czym różni się od SELECT COUNT(*)?
#niczym sie nie rozni to i to zwroci liczbe rowow
# Czy LIKE 'A%' i ILIKE 'A%' zadziałają tak samo w MySQL i PostgreSQL?
# nie poniewazj ilike jest unikalne tylko dla postgres
# Co się stanie, gdy spróbujesz użyć aliasu (AS something) w klauzuli WHERE?
# wystapi blad?
# Jakie problemy logiczne mogą wystąpić przy użyciu GROUP BY bez zrozumienia danych źródłowych?
# mozemy nie rozumiec grupowania a nastepnie zle zastosowac funkcje aggregujace