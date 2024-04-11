from selenium import webdriver
from WikipediaMoviePage import WikipediaMoviePage

class TitanicPage(WikipediaMoviePage):
    def get_plot_summary(self):
        # Implementação específica para o Titanic, se necessário.
        pass

driver = webdriver.Chrome()  # Ajuste conforme seu navegador e webdriver.
titanic_page = TitanicPage(driver, "https://pt.wikipedia.org/wiki/Titanic_(filme_de_1997)")
print(titanic_page.get_movie_title())