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

    def was_expensive(self, budget):
        self.budget = budget
        if budget > 100000000:
            return True
        else:
            return False


Movie1 = Movie("Įdomus title", "Įdomusis", 150000000)
Movie2 = Movie("Kita dalis", "Įdomusis", 1)
print(Movie.was_expensive(Movie1, 150000000))
print(Movie.was_expensive(Movie2, 1))

