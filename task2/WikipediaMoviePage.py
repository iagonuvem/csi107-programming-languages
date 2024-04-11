
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaMoviePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 10)

    def get_movie_title(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "firstHeading"))).text

    def get_genre(self):
        genre_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//th[text()='Gênero']/following-sibling::td")))
        return genre_element.text.split("\n")

    def get_plot_summary(self):
        # Aqui você precisará identificar um seletor que capture o primeiro parágrafo do enredo. Pode variar.
        pass

    def get_cast(self):
        # Similar ao método get_genre, mas localizando o elenco.
        pass

    def get_music(self):
        # Localizar a informação de música.
        pass

    def get_awards(self):
        # Localizar a informação de prêmios.
        pass

    def get_release_date(self):
        # Localizar a data de lançamento.
        pass
