create table public.xy_user
(
    id serial primary key,
    account varchar(255),
    nickname varchar(255),
    phone varchar(11),
    email varchar(255),
    avatar varchar(255),
    description varchar(255),
    gender int,
    create_time timestamp,
    update_time timestamp
);

comment on column xy_user.id is 'user id';
comment on column xy_user.account is 'user account';
comment on column xy_user.nickname is 'user nickname';
comment on column xy_user.phone is 'user phone';
comment on column xy_user.email is 'user email';
comment on column xy_user.avatar is 'user avatar';
comment on column xy_user.description is 'description';
comment on column xy_user.gender is 'gender';
comment on column xy_user.create_time is 'note create_time';
comment on column xy_user.update_time is 'note update_time';
