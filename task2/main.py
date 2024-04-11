from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from WikipediaMoviePage import WikipediaMoviePage

class TitanicPage(WikipediaMoviePage):
    def get_plot_summary(self):
        # Implementação específica para o Titanic, se necessário.
        pass



options = webdriver.ChromeOptions()
# Configurações adicionais aqui

# Especifique uma versão do ChromeDriver compatível
driver_version = '100.0.4896.20'
driver = webdriver.Chrome(ChromeDriverManager(version=driver_version).install(), options=options)


titanic_page = TitanicPage(driver, "https://pt.wikipedia.org/wiki/Titanic_(filme_de_1997)")
print(titanic_page.get_movie_title())