DROP DATABASE IF EXISTS exercicios_complexos;
CREATE DATABASE exercicios_complexos;
USE exercicios_complexos;

CREATE TABLE produtos (
    id_produto INT,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    valor DECIMAL (10,2),
    estoque INT
);

INSERT INTO produtos (id_produto, nome_produto, categoria, Valor, estoque) VALUES
(1, 'Notebook Pro', 'Eletrônicos', 4500.00, 5),
(2, 'Mouse Gamer', 'Periféricos', 150.00, 50),
(3, 'Teclado Mecânico', 'Periféricos', 350.00, 20),
(4, 'Monitor 4K', 'Eletrônicos', 2800.00, 12),
(5, 'Cadeira Office', 'Mobília', 1200.00, 8),
(6, 'Webcam HD', 'Periféricos', 400.00, 15),
(7, 'Mesa Stand-up', 'Mobília', 2500.00, 3);

--EX01:
SELECT * FROM produtos WHERE valor > 300 AND valor < 1500;
--EX02:
SELECT * FROM produtos WHERE categoria = 'eletrônicos' AND estoque > 10;
--EX03:
SELECT * FROM produtos WHERE categoria = 'periféricos' OR valor < 200;
-- EX04:
SELECT nome_produto, valor FROM produtos ORDER BY DESC;
-- EX05:
SELECT * FROM produtos ORDER BY estoque ASC LIMIT 2;

