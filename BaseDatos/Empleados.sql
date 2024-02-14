CREATE DATABASE bd_empleados;
USE bd_empleados;
create table emple(
 emp_no INTEGER PRIMARY KEY,
 apellido VARCHAR(50) NOT NULL,
 oficio VARCHAR(30),
 dir INTEGER,
 fecha_alt DATE,
 salario INTEGER,
 comision INTEGER,
 dept_no INTEGER
);
INSERT INTO emple VALUES (7369,'SÁNCHEZ', 'EMPLEADO', 7902,
'1990/12/17', 1040, NULL, 20);
INSERT INTO emple VALUES (7499,'ARROYO', 'VENDEDOR', 7698,
'1990/02/20', 1500, 390, 30);
INSERT INTO emple VALUES (7521,'SALA', 'VENDEDOR', 7698,
'1991/02/22', 1625, 650, 30);
INSERT INTO emple VALUES (7566,'JIMÉNEZ', 'DIRECTOR', 7839,
'1991/04/02', 2900, NULL, 20);
INSERT INTO emple VALUES (7654,'MARTÍN', 'VENDEDOR', 7698,
'1991/09/29', 1600, 1020, 30);
INSERT INTO emple VALUES (7698,'NEGRO', 'DIRECTOR', 7839,
'1991/05/01', 3005, NULL, 30);
INSERT INTO emple VALUES (7782,'CEREZO', 'DIRECTOR', 7839,
'1991/06/09', 2885, NULL, 10);
INSERT INTO emple VALUES (7788,'GIL', 'ANALISTA', 7566,
'1991/11/09', 3000, NULL, 20);
INSERT INTO emple VALUES (7839,'REY', 'PRESIDENTE', NULL,
'1991/11/17', 4100, NULL, 10);
INSERT INTO emple VALUES (7844,'TOVAR', 'VENDEDOR', 7698,
'1991/09/08', 1350, 0, 30);
INSERT INTO emple VALUES (7876,'ALONSO', 'EMPLEADO', 7788,
'1991/09/23', 1430, NULL, 20);
INSERT INTO emple VALUES (7900,'JIMENO', 'EMPLEADO', 7698,
'1991/12/03', 1335, NULL, 30);
INSERT INTO emple VALUES (7902,'FERNÁNDEZ','ANALISTA', 7566,
'1991/12/03', 3000, NULL, 20);
INSERT INTO emple VALUES (7934,'MUÑOZ', 'EMPLEADO', 7782,
'1992/01/23', 1690, NULL, 10);

create table depart(
 dept_no INTEGER,
 dnombre VARCHAR(30),
 loc VARCHAR(30)
);
INSERT INTO depart VALUES (10, 'CONTABILIDAD', 'SEVILLA');
INSERT INTO depart VALUES (20, 'INVESTIGACIÓN', 'MADRID');
INSERT INTO depart VALUES (30, 'VENTAS', 'BARCELONA');
INSERT INTO depart VALUES (40, 'PRODUCCIÓN', 'BILBAO');

/*Consultas*/
SELECT apellido,oficio,dept_no FROM emple;
SELECT dept_no,dnombre,loc FROM depart;
SELECT * FROM emple;
SELECT * FROM emple ORDER BY apellido;
SELECT * FROM emple ORDER BY dept_no DESC;
SELECT * FROM emple ORDER BY dept_no DESC, apellido;
SELECT * FROM emple WHERE  salario > 2000;
SELECT * FROM emple WhERE oficio = 'analista';
SELECT apellido,oficio FROM emple WHERE dept_no = 20;
SELECT * FROM emple ORDER BY apellido;
SELECT * FROM emple WHERE oficio = 'VENDEDOR' ORDER BY apellido;
SELECT * FROM emple WHERE DEPT_NO = 20 AND oficio = 'EMPLEADO' ORDER BY apellido;
SELECT * FROM emple WHERE salario > 20000 OR dept_no =20;
SELECT * FROM emple ORDER BY oficio,apellido;
SELECT * FROM emple WHERE apellido LIKE 'A%';
SELECT * FROM emple WHERE apellido LIKE '%z'; 
SELECT * FROM emple WHERE apellido LIKE 'A%' AND oficio like '%E%';
SELECT * FROM emple WHERE salario BETWEEN 1000 AND 2000;
SELECT * FROM emple WHERE oficio = 'VENDEDOR' AND comision >1000;
SELECT * FROM emple ORDER BY dept_no,apellido;
SELECT emp_no,apellido FROM emple WHERE apellido LIKE '%Z' AND  salario > 2000;
SELECT * FROM depart WHERE loc LIKE 'B%';
SELECT * FROM emple WHERE oficio = 'EMPLEADO' AND salario > 1100 AND dept_no =10;
SELECT apellido FROM emple WHERE comision IS NULL;
SELECT apellido FROM emple WHERE comision IS NULL OR comision = 0;
SELECT apellido FROM emple WHERE comision IS NULL AND apellido LIKE 'J%';
SELECT apellido FROM emple WHERE oficio IN ('VENDEDOR','ANALISTA','EMPLEADO');
SELECT apellido FROM emple WHERE oficio NOT IN ('ANALISTA','EMPLEADO') AND salario > 2000;
SELECT apellido, oficio, salario FROM emple WHERE oficio <> 'ANALISTA'
  AND oficio <> 'EMPLEADO' AND salario > 2000;
SELECT * FROM emple WHERE salario BETWEEN 2000 AND 3000;
SELECT apellido, salario, dept_no  FROM emple 
WHERE salario > 2000 AND (dept_no = 10 OR dept_no = 30);
SELECT apellido, salario, dept_no FROM emple
WHERE salario > 2000 AND dept_no IN (10, 30);
SELECT apellido, emp_no FROM emple WHERE salario NOT BETWEEN 1000 AND 2000;
SELECT lower(apellido) FROM emple;
SELECT concat(apellido, ' ', oficio) empleado_oficio FROM emple ORDER BY 1;
SELECT apellido, length(apellido) FROM emple ORDER BY length(apellido) DESC;
SELECT apellido, length(apellido) largo FROM emple ORDER BY 2 DESC;
SELECT DISTINCT year(fecha_alt) año FROM emple;
SELECT * FROM emple WHERE year(fecha_alt) = 1992;
SELECT * FROM emple WHERE monthname(fecha_alt) = 'February';
SELECT apellido, fecha_alt FROM emple WHERE month(fecha_alt) = 2;
SELECT apellido, greatest(salario, coalesce(comision, 0)) FROM emple;
SELECT apellido FROM emple WHERE apellido LIKE 'A%' AND year(fecha_alt) = 1990;
SELECT * FROM emple WHERE dept_no = 10 AND comision IS NULl;






