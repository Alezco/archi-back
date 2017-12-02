USE archi;
DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS lists;

CREATE TABLE lists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);

CREATE TABLE cards (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    answer VARCHAR(256),
    question VARCHAR(256),
    date VARCHAR(256),
    listId INT,
    FOREIGN KEY cards(listId) REFERENCES lists(id)
);

INSERT INTO lists(name) VALUES("list1");
INSERT INTO lists(name) VALUES("list2");
INSERT INTO lists(name) VALUES("list3");
INSERT INTO lists(name) VALUES("list4");

INSERT INTO cards(answer, question, date, listId) VALUES("answer1", "question1", "date1", 1);
INSERT INTO cards(answer, question, date, listId) VALUES("answer2", "question2", "date2", 2);
INSERT INTO cards(answer, question, date, listId) VALUES("answer3", "question3", "date3", 1);
