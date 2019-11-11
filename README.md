# backend

API:

/songs/
Json of all available songs, some info about them, including the id.

/song/<id>
returns a zip file containing the song's information.
  
TODO:
Implement database that contains the primary key, song metadata, and zip file as a blob in db.
