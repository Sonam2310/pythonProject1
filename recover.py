@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":

        driver = webdriver.Chrome(executable_path='C:\\Users\\rajiv\\chromedriver.exe')
        driver.implicitly_wait(5)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='C:\\Users\\rajiv\\geckodriver.exe')
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()

    request.cls.driver = driver
   # yield
    #driver.close()