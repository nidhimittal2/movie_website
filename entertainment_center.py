import fresh_tomatoes
import media

forrest = media.Movie("Forrest Gump","The story depicts several decades in the life of Forrest Gump (Hanks), a slow-witted but kind-hearted man from Alabama who witnesses several defining historical events in the 20th century in the United States.",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                      "https://www.youtube.com/watch?v=uPIEn0M8su0")
bful_mind = media.Movie("A Beautiful Mind","A Beautiful Mind is a 2001 American biographical drama film based on the life of John Nash, a Nobel Laureate in Economics.",
                       "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                       "https://www.youtube.com/watch?v=9wZM7CQY130")

hangover = media.Movie("The Hangover","The Hangover is a 2009 American comedy film.",
                       "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                       "https://www.youtube.com/watch?v=TZc39afdeXU")
theory = media.Movie("The Theory of everything","This is based on the life of great scientist,STEPHAN HAWKING",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/The_Theory_of_Everything_%282014%29.jpg",
                        "https://www.youtube.com/watch?v=Salz7uGp72c")

due = media.Movie("Due date"," The film follows a man (Robert Downey Jr.) who must get across the country to Los Angeles in time for the birth of his child and is forced to road-trip with an aspiring actor.",
                  "https://upload.wikimedia.org/wikipedia/en/5/53/Due_Date_Poster.jpg",
                  "https://www.youtube.com/watch?v=Hd_aN0LAgMo")
movies = [forrest,bful_mind,hangover,theory,due]
fresh_tomatoes.open_movies_page(movies)
