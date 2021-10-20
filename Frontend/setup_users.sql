create user web@localhost
	identified by 'BUIOSDBfOAJDOPASdjal334VBUIOV89GVuiv';

create table past_games
(
    id           int auto_increment,
    time_date    timestamp default CURRENT_TIMESTAMP null,
    player_count int       default -1                not null,
    match_length int                                 not null,
    winner_id    int                                 not null,
    win_method   varchar(100)                        not null,
    constraint past_games_id_uindex
        unique (id)
);

grant alter, create, delete, drop, insert, select, update on table past_games to web@localhost;

create table among_db.users
(
    id                int auto_increment           primary key,
    username          varchar(150)                 not null,
    hash              varchar(250)                 not null,
    email             varchar(250)                 null,
    phoneNumber       varchar(30)                  not null,
    `rank`            varchar(100)                 not null,
    constraint users_email_uindex
        unique (email),
    constraint users_username_uindex
        unique (username)
);

grant alter, create, delete, drop, insert, select, update on table users to web@localhost;
