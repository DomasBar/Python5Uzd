# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.


class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = int(budget)

    def __repr__(self):
        return f"{self.title}, {self.director}, {self.budget}"

    def was_expensive(self):
            return(print(self.budget >100000000))


movie1 = Movie("Įdomus title", "Įdomusis", 150000000)
movie2 = Movie("Kita dalis", "Įdomusis", 1)
movie1.was_expensive()
movie2.was_expensive()


