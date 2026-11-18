FOR EACH ROW
set NEW.name=ifnull(new.name,concat('user_', uuid()));

insert into users(name, email, password)
values('-', 'test@email.com', '1234');

select * from users;


CREATE DATABASE IF NOT EXISTS flask_auth;
USE flask_auth;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(64) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL
);

INSERT INTO users (user_name, user_password)
VALUES ('Vladimir Putin', '123456789');
