Данные во всех 3-х таблицах:

```sql

table car_names;

 id |       name        | manufacturer_id 
----+-------------------+-----------------
  1 | AC 3000ME         |               0
  2 | AC/Shelby Cobra   |               0
  3 | Alfa Romeo 75     |               1
  4 | Alfa Romeo 156    |               1
  6 | BMW 326           |               4
  7 | Cadillac De Ville |               6
  8 | Cadillac ELR      |               6
  9 | Dodge Viper       |               8
  5 | Alpine A310       |               2

------------------------------------------

table models;

 id | year | car_id 
----+------+--------
  1 | 1979 |      1
  2 | 1961 |      2
  3 | 1985 |      3
  4 | 1997 |      4
  5 | 1971 |      5
  6 | 1936 |      6
  7 | 1959 |      7
  8 | 2013 |      8
  9 | 1992 |      9

--------------------

table manufacturer;

 id |    name    
----+------------
  1 | Alfa Romeo
  2 | Alpine
  3 | Audi
  4 | BMW
  5 | Bugatti
  6 | Cadillac
  7 | Chevrolet
  8 | Dodge

```

Джоиним все 3 таблицы:

```sql

select manufacturer.name, car_names.name, models.year from manufacturer inner join car_names on (manufacturer.id = car_names.manufacturer_id) inner join models on (car_names.id = models.car_id);

    name    |       name        | year 
------------+-------------------+------
 Alfa Romeo | Alfa Romeo 75     | 1985
 Alfa Romeo | Alfa Romeo 156    | 1997
 Alpine     | Alpine A310       | 1971
 BMW        | BMW 326           | 1936
 Cadillac   | Cadillac De Ville | 1959
 Cadillac   | Cadillac ELR      | 2013
 Dodge      | Dodge Viper       | 1992

``` 
