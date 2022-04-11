-- INSERT 1000000 DUMMY DATA
insert into users (
	name, age, country)
select
	left(md5(i::text), 10),
	(floor(random() * 100 + 1)::int),
	left(md5(random()::text), 4)
from generate_series(1,1000000) s(i);
