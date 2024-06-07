import pytest
from selenium import webdriver
#from configuration import config as path
from Task_26.configuration import config as path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller


opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

imdb_url = "https://www.imdb.com/search/name/"

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(imdb_url)
    request.cls.driver = imdb_url

    yield driver
    # Teardown Chrome driver
    driver.quit()

