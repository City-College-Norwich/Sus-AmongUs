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

create user web@localhost
	identified by 'BUIOSDBfOAJDOPASdjal334VBUIOV89GVuiv';

grant alter, create, delete, drop, insert, select, update on table past_games to web@localhost;
