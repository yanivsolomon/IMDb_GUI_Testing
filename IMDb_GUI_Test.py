import time
from selenium import webdriver
import pytest
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# GUI tests for IMDb.com, contains the following tests:
# Logo Testing (size, href, location)
# Menu Testing (font family, color, bg color, size, fetch menu titles name)
# Buttons Testing (size, location, color,bg-color, button click and URL test)
# Main Colors Testing (header, body, headlines)
# Search Bar Testing (placeholder, size, b-g color, color)
# Slideshow Timer Testing (measure the time it takes for the image to change on the slideshow)


# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")


# Logo testing (size, href, location)
def test_logo(test_setup):
    driver.get("https://imdb.com")
    logo = driver.find_element_by_xpath("//a[@id='home_img_holder']")
    # Validating data
    assert logo.size == {'height': 32, 'width': 64}
    assert logo.get_attribute("href") == "https://www.imdb.com/?ref_=nv_home"
    assert logo.location == {'x': 108, 'y': 12}

# Menu testing (font family, color, bg color, size, fetch menu titles name)
def test_menu(test_setup):
    driver.get("https://imdb.com")
    # Menu font test
    menu = driver.find_element_by_xpath("//span[@class='ipc-responsive-button__text']")
    # Validating data
    assert menu.value_of_css_property("font-family") == "Roboto, Helvetica, Arial, sans-serif"
    assert menu.value_of_css_property("color") == "rgba(255, 255, 255, 1)"
    assert menu.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"
    assert menu.size == {'height': 18, 'width': 37}

    # Fetch menu titles test (fetch menus headers/titles)
    menu.click()
    time.sleep(1)
    itemtitle1 = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[1]/span/label/span[2]").text
    itemtitle2 = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[2]/div[1]/span/label/span[2]").text
    itemtitle3 = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[2]/div[2]/span/label/span[2]").text
    itemtitle4 = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[3]/span/label/span[2]").text
    itemtitle5 = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[4]/span/label/span[2]").text
    itemtitle6 = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[6]/span/label/span[2]").text

    assert itemtitle1 == "Movies"
    assert itemtitle2 == "TV Shows"
    assert itemtitle3 == "Watch"
    assert itemtitle4 == "Awards & Events"
    assert itemtitle5 == "Celebs"
    assert itemtitle6 == "Community"

# Buttons testing (size, location, color,bg-color, button click and URL test)
def test_buttons(test_setup):
    driver.get("https://imdb.com")
    # Scroll to the element
    driver.execute_script("window.scrollBy(0, 1000)")
    time.sleep(3)
    # First button testing:
    button_1 = driver.find_element_by_xpath("//span[normalize-space()='Sign in to IMDb']")
    assert button_1.size == {'height': 20, 'width': 100}
    assert button_1.location == {'x': 558, 'y': 1274}
    assert button_1.value_of_css_property("color") == "rgba(87, 153, 239, 1)"
    assert button_1.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"

    # Button click and url testing
    button_1.click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.imdb.com/registration/signin?ref_=hm_wls_signin"
    # Go back to main page and start of button 2
    driver.execute_script("window.history.go(-1)")
    # Button number 2
    # Scroll to the element
    driver.execute_script("window.scrollBy(0, 1500)")
    time.sleep(3)
    button_2 = driver.find_element_by_xpath("//span[normalize-space()='Watch Guide']")
    assert button_2.size == {'height': 20, 'width': 83}
    assert button_2.location == {'x': 189, 'y': 2528}
    assert button_2.value_of_css_property("color") == 'rgba(255, 255, 255, 1)'
    assert button_2.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"

    # Button click and url testing
    button_2.click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.imdb.com/what-to-watch/watch-guides/?ref_=hm_watch_wchgd"

    # Go back to main page and start of button 3
    driver.execute_script("window.history.go(-1)")
    # Button number 3
    # Scroll to the element
    driver.execute_script("window.scrollBy(0, -1300)")
    time.sleep(3)
    button_3 = driver.find_element_by_xpath("//span[normalize-space()='Most Popular']")
    assert button_3.size == {'height': 20, 'width': 88}
    assert button_3.location == {'x': 438, 'y': 1462}
    assert button_3.value_of_css_property("color") == 'rgba(255, 255, 255, 1)'
    assert button_3.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"

    # Button click and url testing
    time.sleep(2)
    button_3.click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.imdb.com/what-to-watch/popular/?ref_=hm_watch_pop"

    # Go back to main page and start of button 4
    driver.execute_script("window.history.go(-1)")
    time.sleep(2)
    # Button number 4
    # Scroll to the element (bottom of the screen)
    driver.execute_script("window.scrollBy(0, 9000)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 9000)")
    button_4 = driver.find_element_by_xpath("//span[normalize-space()='Sign in for more access']")
    assert button_4.size == {'height': 20, 'width': 155}
    assert button_4.location == {'x': 531, 'y': 4662}
    assert button_4.value_of_css_property("color") == 'rgba(0, 0, 0, 1)'
    assert button_4.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"

    # Button click and url testing
    time.sleep(2)
    button_4.click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.imdb.com/registration/signin?ref_=reg_ftr&u=%2F"


# Main colors testing (header, body, headlines)
def test_colors(test_setup):
    driver.get("https://imdb.com")
    # Header color
    header_element = driver.find_element_by_id("imdbHeader").value_of_css_property("background-color")
    assert header_element == "rgba(18, 18, 18, 1)"
    # Body color
    body_element = driver.find_element_by_tag_name("body").value_of_css_property("background-color")
    assert body_element == "rgba(0, 0, 0, 0)"
    # Footer color
    footer_element = driver.find_element_by_tag_name("footer").value_of_css_property("background-color")
    assert footer_element == "rgba(0, 0, 0, 1)"


# Search bar Testing (placeholder, size, b-g color, color)
def test_s_bar(test_setup):
    driver.get("https://imdb.com")
    search_bar = driver.find_element_by_xpath("//input[@id='suggestion-search']")
    # Validating data
    assert search_bar.get_attribute("placeholder") == "Search IMDb"
    assert search_bar.size == {'height': 31, 'width': 351}
    assert search_bar.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)"
    assert search_bar.value_of_css_property("color") == "rgba(0, 0, 0, 0.87)"


# Slideshow Timer Testing (measure the time it takes for the image to change on the slideshow)
def test_slideshow_timer(test_setup):
    # Navigate to IMDb
    driver.get("https://www.imdb.com")

    # Start the timer
    start_time = time.time()

    # Wait for the first slide to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div[2]/figure/div/div[2]/div[2]/div[2]"))
    )

    # Wait for the element to no longer be visible
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div[2]/figure/div/div[2]/div[2]/div[2]"))
    )

    # Stop the timer
    end_time = time.time()
    # Calculate the time taken for the second slide to be visible
    time_taken = end_time - start_time
    print(f"The slideshow changes image every: {time_taken} seconds.")