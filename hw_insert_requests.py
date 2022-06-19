import psycopg2
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('postgresql://demo_netology:pass@localhost:5432/demo')
connection = engine.connect()

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_1 my', 3);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_2', 2);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_3', 1);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_4', 5);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_5', 3);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_6', 3);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_7', 5);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_8', 4);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_9', 5);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_10', 3);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_11', 2);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_12', 3);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_13', 6);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_14', 5);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration)
VALUES('track_15', 2);
""")

pprint(connection.execute(
"""
SELECT * FROM tracks;
""").fetchall())


connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_1', 2020);
""")
connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_2', 2022);
""")

connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_3', 2011);
""")

connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_4', 2019);
""")

connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_5', 2008);
""")

connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_6', 2015);
""")

connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_7', 2018);
""")

connection.execute(
"""
INSERT INTO collections(name, year_of_release)
VALUES('collection_8', 2013);
""")

pprint(connection.execute(
"""
SELECT * FROM collections;
""").fetchall())


connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_1', 2020);
""")

connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_2', 2022);
""")

connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_3', 2002);
""")

connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_4', 2005);
""")
connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_5', 2009);
""")

connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_6', 2018);
""")
#
connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_7', 2011);
""")
#
connection.execute(
"""
INSERT INTO albums(name, year_of_release)
VALUES('album_8', 2018);
""")
#
pprint(connection.execute(
"""
SELECT * FROM albums;
""").fetchall())


connection.execute(
"""
INSERT INTO artists(name)
VALUES('name_1 1');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('name_2');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('name_3');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('artist_4');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('artist_5');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('artist_6');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('artist_7');
""")

connection.execute(
"""
INSERT INTO artists(name)
VALUES('artist_8');
""")
#
pprint(connection.execute(
"""
SELECT * FROM artists;
""").fetchall())

connection.execute(
"""
INSERT INTO jenres(name)
VALUES('jenre_1');
""")

connection.execute(
"""
INSERT INTO jenres(name)
VALUES('jenre_2');
""")

connection.execute(
"""
INSERT INTO jenres(name)
VALUES('jenre_3');
""")

connection.execute(
"""
INSERT INTO jenres(name)
VALUES('jenre_4');
""")
#
connection.execute(
"""
INSERT INTO jenres(name)
VALUES('jenre_5');
""")

pprint(connection.execute(
"""
SELECT * FROM jenres;
""").fetchall())

print(connection.execute(
"""
SELECT * FROM jenres;
""").fetchall())

connection.execute(
"""
INSERT INTO trackcollection(track_id, collection_id)
VALUES(23, 1);
""")

connection.execute(
"""
INSERT INTO trackcollection(track_id, collection_id)
VALUES(24, 2);
""")

connection.execute(
"""
INSERT INTO trackcollection(track_id, collection_id)
VALUES(25, 3);
""")

pprint(connection.execute(
"""
SELECT * FROM trackcollection;
""").fetchall())

connection.execute(
"""
INSERT INTO albumartist(album_id, artist_id)
VALUES(1, 11);
""")

connection.execute(
"""
INSERT INTO albumartist(album_id, artist_id)
VALUES(2, 12);
""")

connection.execute(
"""
INSERT INTO albumartist(album_id, artist_id)
VALUES(3, 15);
""")

pprint(connection.execute(
"""
SELECT * FROM albumartist;
""").fetchall())