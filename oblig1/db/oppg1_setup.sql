DROP TABLE IF EXISTS OnStagePersonnel, StageManager;

-- Setup
CREATE TABLE OnStagePersonnel  (
    ospID SERIAL PRIMARY KEY,
    name varchar(255),
    lastname varchar(255)
);

CREATE TABLE StageManager (
    ospID int REFERENCES OnStagePersonnel(ospID),
    smID int,
    function text,
    PRIMARY KEY (ospID, smID)
);

-- DATA

INSERT INTO OnStagePersonnel (name, lastname)
VALUES
    ('Jhon', 'Doe'),
    ('William', 'Smith'),
    ('James', 'Williams'),
    ('Charles', 'Brown'),
    ('George', 'Garcia'),
    ('Frank', 'Martinez');

INSERT INTO StageManager (ospID, smID, function)
VALUES
    (1, 1, 'rehearsals'), 
    (2, 2, 'coordinating'), 
    (3, 3, 'communicating'), 
    (4, 1, 'rehearsals'),
    (5, 2, 'coordinating'),
    (6, 3, 'communicating');

