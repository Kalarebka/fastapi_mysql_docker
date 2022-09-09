USE fastapi;

CREATE TABLE user(
    id INT AUTO_INCREMENT NOT NULL,
    username VARCHAR(64) UNIQUE NOT NULL,
    password VARCHAR(256) NOT NULL,
    email VARCHAR(128) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE post(
    id INT AUTO_INCREMENT,
    user_id INT,
    title VARCHAR(256) NOT NULL,
    content TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Sample data
insert into user (username, password, email) values ('Eryk', 'password', 'eryk@gmail.com');
insert into user (username, password, email) values ('Ika', 'password', 'ika@gmail.com');

insert into post (user_id, title, content) values (1, 'Post 1', 'Post 1 content');
insert into post (user_id, title, content) values (1, 'Post 2', 'Post 2 content');
insert into post (user_id, title, content) values (2, 'Post 3', 'Post 3 content');
insert into post (user_id, title, content) values (2, 'Post 4', 'Post 4 content');