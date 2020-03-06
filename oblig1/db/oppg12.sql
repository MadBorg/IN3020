-- this is an example

DROP TABLE IF EXISTS StudioList, SceneInventory, R, S;

CREATE TABLE StudioList (
    StudioID varchar(255),
    inventory varchar(255)
);

CREATE TABLE SceneInventory(
    sceneID varchar(255),
    inventory varchar(255)
);

CREATE TABLE R(
    a varchar(10),
    b int
);

CREATE TABLE S(
    a varchar(10)
);

INSERT INTO StudioList(StudioID, inventory )
VALUES 
    ('StID0001', 'table'),
	('StID0001', 'chair'),
	('StID0002', 'pen'),
	('StID0003', 'book'),
	('StID0004', 'sword'),
	('StID0004', 'candle'),
	('StID0005', 'greenRoom'),
	('StID0005', 'magicMirror'),
	('StID0005', 'magicWell');

INSERT INTO SceneInventory(sceneID, inventory)
VALUES 
    ('ScID0001', 'magicMirror'),
	('ScId0002', 'sword'),
	('ScId0001', 'greenRoom'),
	('ScId0003', 'book'),
	('ScId0001', 'magicWell'),
	('ScId0003', 'pen'),
	('ScId0002', 'candle');

INSERT INTO R(a,b)
VALUES
    ('a',1),
    ('d',2),
    ('c',1),
    ('a',3),
    ('a',2),
    ('C',1);

INSERT INTO S(a)
VALUES
    ('a'),
    ('b'),   
    ('c');


