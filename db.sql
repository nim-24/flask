FOR EACH ROW
set NEW.name=ifnull(new.name,concat('user_', uuid()));

insert into users(name, email, password)
values('-', 'test@email.com', '1234');

select * from users;
