create table crappers
(
  name   varchar not null,
  number int     not null
);

create table shits
(
  crapper    int      not null
    constraint shits_crappers_number_fk
    references crappers (number),
  time_taken datetime not null
);



INSERT INTO crappers (name, number) VALUES ('FAIRY', 0);
INSERT INTO crappers (name, number) VALUES ('AIRWICK', 1);
INSERT INTO crappers (name, number) VALUES ('NESCAFE', 2);
INSERT INTO crappers (name, number) VALUES ('ARIEL', 3);
INSERT INTO crappers (name, number) VALUES ('FINISH', 4);

