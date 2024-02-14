CREATE DATABASE cole;
USE cole;
CREATE TABLE alumnos(
  expediente INTEGER PRIMARY KEY,
  nombre VARCHAR(100),
  localidad VARCHAR(50),
  fecha_nac DATE,
  direccion VARCHAR(50),
  curso INTEGER,
  nivel VARCHAR(45),
  faltas INTEGER
);

INSERT INTO alumnos VALUES
 (123456,'Juan Miguel Soler Bakero','Murcia','1995-10-10','Gran Via, 2,4A',1,'ESO',15),
 (654321,'Laura Gomez Fernandez','Lorca','1994-05-10','Junterrones ,10,5B',2,'ESO',25),
 (765432,'Beatriz Martinez Hernandez','Murcia','1993-05-05','Plaza Mayor,6,3B',3,'ESO',5),
 (987654,'Diego Martin Llorente','Alhama de Murcia','1990-06-03','Diego de la cierva,5,7A',1,'BACHILLER',34),
 (445544,'Juan Francisco Cano Riquelme','Murcia','1992-07-01','Plaza de Belluga,3,4A',4,'ESO',13),
 (223322,'Raquel Riquelme Rubio','Lorca','1990-11-23','San Juan,14,3B',1,'BACHILLER',7),
 (9988877,'Cristina Sanchez Bermejo','Murcia','1995-03-19','Torre de Romo,7',1,'ESO',1),
 (334455,'Pedro Jesus Rodriguez Soler','Alhama de Murcia','1994-03-10','Camino de Badel,4',2,'ESO',11),
 (334400,'Javier Ramanez Rodriguez','Murcia','1993-05-27','Gran Via, 4,3A',3,'ESO',0),
 (993322,'Gema Rubio Colero','Lorca','1992-09-09','Plaza Fuensanta,5,7A',1,'BACHILLER',19),
 (554411,'Joaquin Hernandez Gonzales','Lorca','1991-12-12','Junterrones4,5A',2,'BACHILLER',14)
 ;
 
SELECT * FROM alumnos;
SELECT nombre,localidad,fecha_nac FROM alumnos;
SELECT * FROM alumnos WHERE localidad = 'Lorca';
SELECT * FROM alumnos WHERE localidad IN ('Lorca','Alhama de Murcia');
SELECT * FROM alumnos WHERE localidad = 'Alhama de Murcia' AND curso = 1 AND nivel = 'ESO';
SELECT * FROM alumnos WHERE localidad = 'Lorca' AND curso = 2 AND nivel = 'BACHILLER' AND faltas >10;
SELECT * FROM alumnos WHERE localidad = 'Murcia' ORDER BY nombre;
SELECT * FROM alumnos ORDER BY nivel,curso;
SELECT * FROM alumnos WHERE faltas > 10 AND curso IN (1,2);
SELECT * FROM alumnos WHERE faltas <10 AND curso IN (3,4) AND localidad = 'Murcia';
SELECT DISTINCT curso FROM alumnos;
SELECT * FROM alumnos WHERE faltas != 10 AND curso = 1 AND nivel = 'ESO';
SELECT * FROM alumnos WHERE nombre LIKE 'B%';
SELECT * FROM alumnos WHERE localidad = 'Murcia' AND nombre LIKE '%o';
SELECT * FROM alumnos WHERE curso = 1 AND nivel = 'ESO' and NOMBRE like '%u%';
SELECT * FROM alumnos WHERE faltas = NULL;
SELECT * FROM alumnos WHERE faltas BETWEEN 10 AND 20 ORDER BY nombre;
SELECT * FROM alumnos WHERE faltas BETWEEN 10 AND 20 AND localidad = 'Murcia' AND curso = 1 AND nivel = 'ESO';
SELECT * FROM alumnos WHERE faltas < 10 AND faltas >20;
SELECT * FROM alumnos WHERE YEAR(fecha_nac) = 1993 OR YEAR(fecha_nac) = 1994;
SELECT * FROM alumnos WHERE curso IN (1,2);
SELECT * FROM alumnos WHERE curso IN (3,4) AND localidad = 'Murcia';
SELECT * FROM alumnos WHERE nivel NOT IN ('ESO') ORDER BY curso DESC, nombre DESC;
SELECT * FROM alumnos WHERE curso IN (1,2) AND nivel != 'BACHILLER' ORDER BY nombre;
SELECT * FROM alumnos WHERE nombre LIKE 'j%' AND faltas>10 AND nivel != 'BACHILLER'
ORDER BY curso, nombre;
SELECT expediente,nombre,curso,nivel FROM alumnos WHERE nivel != 'BACHILLER' ORDER BY curso,nivel,nombre DESC;
SELECT upper(nombre) FROM alumnos WHERE localidad = 'Murcia';
SELECT upper(nombre), lower(localidad) FROM alumnos ORDER BY localidad;
SELECT concat(nombre ,' ',localidad) alumno_localidad, REPLACE (nivel, 'BACHILLER','BACHILLERATO') nivel2 FROM alumnos;
SELECT nombre,length(nombre) FROM alumnos;
SELECT nombre,YEAR(fecha_nac) año,monthname(fecha_nac)mes FROM alumnos;
SELECT nombre, 2024-(YEAR(fecha_nac)) edad FROM alumnos;














