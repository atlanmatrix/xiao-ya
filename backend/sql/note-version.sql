create table public.xy_note_version
(
    id serial primary key,
    note_id int,
    title varchar(255),
    subtitle varchar(255),
    content text,
    category int,
    tags varchar[],
    create_time timestamp default now(),
    user_id int not null
);

comment on column xy_note_version.id is 'note version id';
comment on column xy_note_version.note_id is 'related note id';
comment on column xy_note_version.title is 'note title';
comment on column xy_note_version.subtitle is 'note subtitle';
comment on column xy_note_version.content is 'latest note content';
comment on column xy_note_version.category is 'note category';
comment on column xy_note_version.tags is 'note tags';
comment on column xy_note_version.create_time is 'note create_time';
comment on column xy_note_version.user_id is 'creator';
