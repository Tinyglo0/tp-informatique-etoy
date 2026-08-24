# --------- PYODIDE:env --------- #
year = ['1896', '1900', '1904', '1908', '1912', '1920', '1924', '1924', '1928', '1928', '1932', '1932', '1936', '1936', '1948', '1948', '1952', '1952', '1956', '1956', '1956', '1960', '1960', '1964', '1964', '1968', '1968', '1972', '1972', '1976', '1976', '1980', '1980', '1984', '1984', '1988', '1988', '1992', '1992', '1994', '1996', '1998', '2000', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016', '2018', '2021', '2022', '2024', '2026', '2028', '2030', '2032', '2034']
city = ['Athens', 'Paris', 'St. Louis', 'London', 'Stockholm', 'Antwerp', 'Chamonix', 'Paris', 'St. Moritz', 'Amsterdam', 'Lake Placid', 'Los Angeles', 'Garmisch-Partenkirchen', 'Berlin', 'St. Moritz', 'London', 'Oslo', 'Helsinki', "Cortina d'Ampezzo", 'Melbourne', 'Stockholm', 'Squaw Valley', 'Rome', 'Innsbruck', 'Tokyo', 'Grenoble', 'Mexico City', 'Sapporo', 'Munich', 'Innsbruck', 'Montreal', 'Lake Placid', 'Moscow', 'Sarajevo', 'Los Angeles', 'Calgary', 'Seoul', 'Albertville', 'Barcelona', 'Lillehammer', 'Atlanta', 'Nagano', 'Sydney', 'Salt Lake City', 'Athens', 'Turin', 'Beijing', 'Vancouver', 'London', 'Sochi', 'Rio de Janeiro', 'Pyeongchang', 'Tokyo', 'Beijing', 'Paris', "Milan–Cortina d'Ampezzo", 'Los Angeles', 'French Alps', 'Brisbane', 'Salt Lake City']
country = ['Greece', 'France', 'United States', 'United Kingdom', 'Sweden', 'Belgium', 'France', 'France', '\xa0Switzerland', 'Netherlands', 'United States', 'United States', 'Germany', 'Germany', '\xa0Switzerland', 'United Kingdom', 'Norway', 'Finland', 'Italy', 'Australia', 'Sweden', 'United States', 'Italy', 'Austria', 'Japan', 'France', 'Mexico', 'Japan', 'West Germany', 'Austria', 'Canada', 'United States', 'Soviet Union', 'Yugoslavia', 'United States', 'Canada', 'South Korea', 'France', 'Spain', 'Norway', 'United States', 'Japan', 'Australia', 'United States', 'Greece', 'Italy', 'China', 'Canada', 'United Kingdom', 'Russia', 'Brazil', 'South Korea', 'Japan', 'China', 'France', 'Italy', 'United States', 'France', 'Australia', 'United States']
season = ['Summer', 'Summer', 'Summer', 'Summer', 'Summer', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter']
# --------- PYODIDE:code --------- #
# 1. Créez une liste 'villes_hiver' contenant toutes les villes qui ont organisé les jeux en hiver (Winter).
villes_hiver = []

# --------- PYODIDE:corr --------- #
villes_hiver = []
for i in range(len(season)):
    if season[i] == "Winter":
        villes_hiver.append(city[i])

# --------- PYODIDE:secrets --------- #
assert len(villes_hiver) == 22, "Le nombre de villes n'est pas correct."
assert villes_hiver[0] == "Chamonix", "La première ville n'est pas correcte."
assert "Winter" not in villes_hiver, "La liste ne doit contenir que les noms des villes."
