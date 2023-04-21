drop table if exists public.xy_note;
create table public.xy_note
(
    id serial primary key,
    title varchar(255) default 'Untitled',
    subtitle varchar(255) default '',
    content text default '',
    category int default -1,
    tags varchar[] default '{}',
    format int,
    create_time timestamp default now(),
    update_time timestamp default now(),
    user_id int,
    pv int default 0,
    uv int default 0,
    likes integer[] default '{}'
);

comment on column xy_note.id is 'note id';
comment on column xy_note.title is 'note title';
comment on column xy_note.subtitle is 'note subtitle';
comment on column xy_note.content is 'latest note content';
comment on column xy_note.category is '-1: default';
comment on column xy_note.tags is 'note tags';
comment on column xy_note.format is '1:markdown 2:rich text';
comment on column xy_note.create_time is 'note create_time';
comment on column xy_note.update_time is 'note update_time';
comment on column xy_note.user_id is 'creator';
comment on column xy_note.pv is 'page view';
comment on column xy_note.uv is 'user view';
comment on column xy_note.likes is 'list of user who likes this note';
