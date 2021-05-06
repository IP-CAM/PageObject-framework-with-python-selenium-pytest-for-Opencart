import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="Choose browser: Chrome or Firefox")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        print("\n\nStart Chrome browser for test...")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\n\nStart Firefox browser for test...')
        browser = webdriver.Firefox()
    elif browser_name == 'ie':
        print('\n\nStart Ie browser for test...')
        browser = webdriver.Ie()
    else:
        print(f'Browser "{browser_name}" is not supported by this test! Chrome, Firefox or Ie only!')
    yield browser
    print('\nQuit browser...')
    browser.quit()
