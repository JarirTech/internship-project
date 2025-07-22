from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class OffPlanPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_selector = (By.XPATH, '//span[text()="Off Plan"]')
        self.title_selector = (By.CSS_SELECTOR, '.product-title')  # Adjust selectors
        self.image_selector = (By.CSS_SELECTOR, '.product-image')  # Adjust selectors

    def click_off_plan(self):
        wait = WebDriverWait(self.driver, 10)

        off_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b"]/div[3]/a[2]/div[1]/div[2]')))
        off_plan.click()


    def click_off_plan_menu(self):
        self.driver.find_element(*self.menu_selector).click()
    def is_off_plan_page_loaded(self):
        try:
            self.driver.find_element(
                By.XPATH,
                '//button[@class="pb-5 text-sm transition-all border-b-2 whitespace-nowrap font-bold border-foreground"]'
            )
            return True
        except NoSuchElementException:
            raise AssertionError("Off Plan page did not load correctly — expected tab/button not found.")

    def all_products_have_title_and_image(self):
        try:
            product_items = self.driver.find_elements(By.CLASS_NAME, "product-card-class")
            assert product_items, " No product items were found on the page."

            for index, item in enumerate(product_items, start=1):
                try:
                    title = item.find_element(By.CLASS_NAME, "product-title-class")
                    image = item.find_element(By.TAG_NAME, "img")

                    assert title.text.strip() != "", f" Product {index} is missing a title."
                    assert image.get_attribute("src"), f" Product {index} is missing an image src."
                except Exception as e:
                    raise AssertionError(f" Error in product {index}: {str(e)}")
            return True
        except Exception as e:
            raise AssertionError(f" Failed while verifying all products: {str(e)}")


