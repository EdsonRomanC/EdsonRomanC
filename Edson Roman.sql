show databases;
create database aeropuerto;
use aeropuerto;

create table aerolinea(id_Aerolinea int primary key not null, Nombre_Aerolinea Varchar(25));
describe aerolinea;

create table aeropuertos(id_Aeropuerto int primary key not null, Nombre_Aeropuerto Varchar(25));
describe aeropuertos;

create table movimientos(id_Movimiento int primary key not null, Descripcion Varchar(25));
describe movimientos;

create table vuelos(id_Aerolinea int,id_Aeropuerto int,id_Movimiento int, Dia date,foreign key (id_Aerolinea)
 references aerolinea(id_Aerolinea), Foreign key (id_Aeropuerto)references aeropuertos(id_Aeropuerto),
 Foreign key (id_Movimiento) references movimientos(id_Movimiento));
 
 describe vuelos;
 
 insert into aerolinea values(1,"Volaris");
 insert into aerolinea values(2,"Aeromar");
 insert into aerolinea values(3,"Interjet");
 insert into aerolinea values(4,"Aeromexico");
 
 select * from aerolinea;


insert into aeropuertos values(1,"Benito Juarez");
insert into aeropuertos values(2,"Guanajuato");
insert into aeropuertos values(3,"La Paz");
insert into aeropuertos values(4,"Oaxaca");

select * from aeropuertos;

insert into movimientos values(1,"Salida");
insert into movimientos values(2,"Llegada");

select * from movimientos;

insert into vuelos values(1,1,1,20210502);
insert into vuelos values(2,1,1,20210502);
insert into vuelos values(3,2,2,20210502);
insert into vuelos values(4,3,2,20210502);
insert into vuelos values(1,3,2,20210502);
insert into vuelos values(2,1,1,20210502);
insert into vuelos values(2,3,1,20210504);
insert into vuelos values(3,4,1,20210504);
insert into vuelos values(3,4,1,20210504);

select * from vuelos;


select count(b.id_Aeropuerto) as total, a.Nombre_Aeropuerto as nombre from aeropuertos a 
 inner join vuelos b on a.id_Aeropuerto = b.id_Aeropuerto 
 where b.Dia between
 '2021-01-01' and '2021-12-31' group by b.id_Aeropuerto order by total desc limit 2;
 
 
 select count(b.id_Aerolinea) as total, a.Nombre_Aerolinea as nombre from aerolinea a 
 inner join vuelos b on a.id_Aerolinea = b.id_Aerolinea 
 where b.Dia between
 '20121-01-01' and '2021-12-31' group by b.id_Aerolinea order by total desc limit 2;
 
 
 select count(*) as total, dia from (select day(Dia) as dia from vuelos) f group by dia order by total desc limit 2;
 
 
 
 