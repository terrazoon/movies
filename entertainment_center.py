import media
import fresh_tomatoes

#List of great Russian movies
how_i_ended_this_summer = media.Movie(
    "How I Ended This Summer",
    "A summer intern makes a terrible mistake in the arctic",
    "https://upload.wikimedia.org/wikipedia/en/6/66/How_I_Ended_This_Summer.jpg",
    "https://www.youtube.com/watch?v=45_2ZZlbirY")

cranes_are_flying = media.Movie(
    "Cranes Are Flying",
    "A woman survives World War 2",
    "https://images-na.ssl-images-amazon.com/images/I/41zzljJW80L.jpg",
    "https://www.youtube.com/watch?v=2e8QkVMM7j8")

brother = media.Movie(
    "Brother",
    "A young army veteran becomes a gangster in 1990s Russia",
    "http://www.imfdb.org/images/thumb/f/fc/Brat.JPG/300px-Brat.JPG",
    "https://www.youtube.com/watch?v=EfaTmDkVzGw")

letter_never_sent = media.Movie(
    "Letter Never Sent",
    "Geologist struggle to survive in Siberia",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/Letter_Never_Sent.jpg",
    "https://www.youtube.com/watch?v=dSloFAFCqY4&list=PLtjXDqqRka59iMhthGBnW6VrJ-uXiEmiC")

the_fool = media.Movie(
    "The Fool",
    "A janitor discovers an apartment building is about to collapse",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Fool_%282014_film%29.png",
    "https://www.youtube.com/watch?v=GXQZdN1L8bo")

solaris = media.Movie(
    "Solaris",
    "A psychologist on an alien planet gets more than he bargained for",
    "https://upload.wikimedia.org/wikipedia/en/5/54/Solyaris_ussr_poster.jpg",
    "https://www.youtube.com/watch?v=R4vSPEDxGic")

movies = [brother, cranes_are_flying, how_i_ended_this_summer, letter_never_sent, the_fool, solaris];

#Show the list in a browser
fresh_tomatoes.open_movies_page(movies);


