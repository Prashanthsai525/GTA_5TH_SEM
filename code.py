LOAD CSV WITH HEADERS FROM 'file:///movie.csv' 
AS row MERGE (m:movie {name: row.name, release_period: row.release_period, remake: row.remake, franchise: row.franchise, genre:row.genre, screens: toInteger(row.screens), revenue: toInteger(row.revenue), budget:toInteger(row.budget)});

CREATE CONSTRAINT ON (m:movie) ASSERT m.name IS UNIQUE;

LOAD CSV WITH HEADERS FROM 'file:///director_movie.csv' 
AS row MERGE (d:director {name: row.director}) MERGE (m:movie {name: row.movie}) MERGE (d)-[r:direct {new_director: row.new_director}]->(m);

LOAD CSV WITH HEADERS FROM 'file:///actor_movie.csv' 
AS row MERGE (a:actor {name: row.actor}) MERGE (m:movie {name: row.movie}) MERGE (a)-[r:act_in {new_actor: row.new_actor}]->(m);

CREATE CONSTRAINT ON (a:actor) ASSERT a.name IS UNIQUE;
CREATE CONSTRAINT ON (d:director) ASSERT d.name IS UNIQUE;