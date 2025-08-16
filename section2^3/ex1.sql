Mini-zadanie 1: Klienci Gmail z końcówki listy

Masz tabelę users:

users
-----
id
name
email

Zadanie:
Wyświetl 5 ostatnich użytkowników (alfabetycznie po name) mających adres e-mail w domenie @gmail.com.

select * from users
where email like '%gmail.com'
order by name desc
limit 5


Mini-zadanie 2: Wyszukiwanie po fragmencie nazwiska

Masz tabelę customers:

customers
---------
id
name

Zadanie:
Wypisz wszystkich klientów, których imię lub nazwisko zawiera znak podkreślenia _. Zadbaj o to, żeby _ był potraktowany jak dosłowny znak, nie wildcard.
select * from customers
where name like '%_%'

orders
------
id
customer_id
total_amount

Wyświetl identyfikatory klientów (customer_id), którzy złożyli więcej niż 3 zamówienia i średnia wartość ich zamówienia wynosi ponad 300.
select customer_id,count(id),avg(total_amount) from orders
group by customer_id
having count(id) > 3 and avg(total_amount) > 300