
CREATE DATABASE sistemapos;
 CREATE USER 'sistema'@'localhost' IDENTIFIED BY '1234567';
 SELECT HOST, USER FROM USER;
 GRANT ALL PRIVILEGES ON sistemapos.* TO sistema@localhost;
 FLUSH PRIVILEGES;
 EXIT
 

CREATE TABLE distrito(
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50),
  PRIMARY KEY(id)
);

CREATE TABLE clientes (
   id INT NOT NULL AUTO_INCREMENT,
   nombre VARCHAR(150), 
   email VARCHAR(100), 
   direccion VARCHAR(150), 
   telefono VARCHAR(15), 
   celular VARCHAR(15), 
   dni CHAR(8), 
   distrito_id INT,
   PRIMARY KEY(id),
   FOREIGN KEY(distrito_id) REFERENCES distrito(id) ON DELETE RESTRICT ON UPDATE RESTRICT
 );