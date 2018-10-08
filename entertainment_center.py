import fresh_tomatoes
import media

#Creating 6 Movie Instances
the_line_king = media.Movie("The Lion King",
            "https://2.bp.blogspot.com/-P2SFpV1S1m8/W67Uw-UkftI/AAAAAAAAAP4/l8RawY_CYcQIFVW_sHVyuR3ms367LBquACLcBGAs/s1600/The_lion_king_poster%25281%2529.jpg",
            "https://www.youtube.com/watch?v=_ujGv5dhGfk")

a_beautiful_mind = media.Movie("A Beautiful Mind",
            "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
            "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

the_matrix = media.Movie("The Matrix",
            "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
            "https://www.youtube.com/watch?v=m8e-FF8MsqU")

source_code = media.Movie("Source Code",
            "https://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg",
            "https://www.youtube.com/watch?v=mnJegNyAb1w")

warrior = media.Movie("Warrior",
            "https://2.bp.blogspot.com/-QmYTWOEwPH0/W67R8MbwKxI/AAAAAAAAAPY/57oEXbDYxtcC0zCUGh1K1eDp7RYLDn0FgCLcBGAs/s1600/warrior_poster.jpg",
            "https://www.youtube.com/watch?v=kY7HcUACs58&t=8s")

transporter_2 = media.Movie("Transporter 2",
            "https://upload.wikimedia.org/wikipedia/en/e/eb/The_Transporter_2_poster.jpg",
            "https://www.youtube.com/watch?v=sYJ5LDoWRT4")

#Creating a list of movies needed as input to the website
movies = [the_line_king,a_beautiful_mind,the_matrix,source_code,warrior,transporter_2]
fresh_tomatoes.open_movies_page(movies)
