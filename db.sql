DROP DATABASE IF EXISTS fruit_ninja;
CREATE DATABASE fruit_ninja;
USE fruit_ninja;

CREATE TABLE highscores (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30)
    score INT
);

