from dataclasses import dataclass
from Weather_parse.settings import WEATHER_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS


@dataclass
class WeatherDay:
    date: str
    temperature: str
    weather_description: str


def parse_one_day(soup):
    date = soup.find("div", class_="city__main active")["data-id"]
    temperature = soup.find("div", class_="city__main-temp").text
    weather_description = soup.find("span", class_="city__main-image-icon")["data-tippy-content"]
    weather_description = " ".join(weather_description.split(" ")[2:])

    return WeatherDay(date, temperature, weather_description)


def parse_days():

    # Создание экземпляра WebDriver с опциями
    driver = webdriver.Chrome()

    driver.get(WEATHER_URL)

    all_days_date = []

    wrapper = driver.find_element(By.CSS_SELECTOR, "div.wrapper.city__week.fl-c")
    buttons = wrapper.find_elements(By.CSS_SELECTOR, "div.city__day.fl-col")
    for button in buttons:
        driver.execute_script("arguments[0].click();", button)
        page_source = driver.page_source
        soup = BS(page_source, "html.parser")
        all_days_date.append(parse_one_day(soup))

    # Закрытие браузера после использования
    driver.quit()

    return all_days_date


if __name__ == "__main__":
    parse_days()
