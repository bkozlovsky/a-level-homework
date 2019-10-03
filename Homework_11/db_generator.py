from imdb import IMDb
import psycopg2

#connecting to the database

database = psycopg2.connect(dbname='movies_db', user='postgres', password='1q2q1q2q1q2q', host='localhost')

cursor = database.cursor()

#getting movies data
ia = IMDb()

top250 = ia.get_top250_movies()


def add_movies_to_db():

    mv_list = []
    id_num = 1

    for mv in top250[:10]:
        d ={}
        print('Getting movie #{} data...'.format(id_num))
        movie_data = ia.get_movie(mv.movieID)
        d['title'] = movie_data['title']
        d['year'] = movie_data['year']
        d['genres'] = '; '.join([g for g in movie_data['genres']])
        d['mv_cast'] = '; '.join([c['name'] for c in movie_data['cast']])
        d['directors'] = '; '.join([d['name'] for d in movie_data['directors']])
        d['runtimes'] = int(movie_data['runtimes'][0])
        d['languages'] = '; '.join([l for l in movie_data['languages']])
        d['plot'] = movie_data['plot'][0]
        mv_list.append(d)
        print('Movie #{} added successfully!\n'.format(id_num))
        id_num += 1

    it_id = 1

    for item in mv_list:
        print("Inserting movie {}...".format(it_id))
        sql_insert_query = """ INSERT INTO movies (title, year, genres, mv_cast, directors, runtimes, languages, plot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
        cursor.execute(sql_insert_query, (item['title'], item['year'], item['genres'], item['mv_cast'], item['directors'], item['runtimes'], item['languages'], item['plot']))
        print("Success!\n")
        it_id += 1
        
    print('Movies have been added to the database successfully!')

add_movies_to_db()

print("-------------------")

def add_actors_to_db():
    pindex_list = []
    for mv in top250[:2]:
        movie_data = ia.get_movie(mv.movieID)
        for c in movie_data['cast']:
            pindex_list.append(c.personID)
    
    print("Retrieved {} indexes\n".format(len(pindex_list)))

    cast_list = []

    print("Generating list of actors...")

    for p in pindex_list:
        d = {}
        person = ia.get_person(p)
        if 'name' and 'filmography' and 'mini biography' and 'birth date' in person.keys():
            if 'actor' in person['filmography'][0].keys():
                d['name'] = person['name']
                d['filmography'] = "; ".join([f['title'] for f in person['filmography'][0]['actor']])
                d['biography'] = person['mini biography'][0]
                d['birth_date'] = person['birth date']
                cast_list.append(d)

    it_id = 1

    for item in cast_list:
        print("Inserting actor {}...".format(it_id))
        sql_insert_query = """ INSERT INTO actors (name, filmography, biography, birth_date) VALUES (%s, %s, %s, %s) """
        cursor.execute(sql_insert_query, (item['name'], item['filmography'], item['biography'], item['birth_date']))
        print("Success!\n")
        it_id += 1
    
    print('Actors have been added to the database successfully!\n')

add_actors_to_db()

print("-------------------")

def add_directors_to_db():
    dindex_list = []
    for mv in top250[:25]:
        movie_data = ia.get_movie(mv.movieID)
        for c in movie_data['directors']:
            dindex_list.append(c.personID)
    
    print("Retrieved {} indexes\n".format(len(dindex_list)))

    print("Generating list of directors...")

    directors_list = []

    for dindex in dindex_list:
        d = {}
        person = ia.get_person(dindex)
        if 'name' and 'filmography' and 'mini biography' and 'birth date' in person.keys():
            if 'writer' in person['filmography'][0].keys():
                d['name'] = person['name']
                d['filmography'] = "; ".join([f['title'] for f in person['filmography'][0]['writer']])
                d['biography'] = person['mini biography'][0]
                d['birth_date'] = person['birth date']
                directors_list.append(d)
    
    it_id = 1

    for item in directors_list:
        print("Inserting director {}...".format(it_id))
        sql_insert_query = """ INSERT INTO directors (name, filmography, biography, birth_date) VALUES (%s, %s, %s, %s) """
        cursor.execute(sql_insert_query, (item['name'], item['filmography'], item['biography'], item['birth_date']))
        print("Success!\n")
        it_id += 1

    print('Directors have been added to the database successfully!\n')

add_directors_to_db()

print("Ready! Check the database.")

database.commit()
cursor.close()
database.close()

