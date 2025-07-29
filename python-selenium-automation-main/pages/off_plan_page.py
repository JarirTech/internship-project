from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OffPlanPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        # XPaths and class names may vary slightly in mobile DOM — confirm by inspecting mobile version
        self.menu_selector = (By.XPATH, '//span[text()="Off Plan"]')
        self.off_plan_xpath = (By.XPATH, '//div[@class="menu-text" and text()="Off-plan"]')

    def click_off_plan(self):
        try:
            # Wait for element and scroll into view for mobile
            element = self.wait.until(EC.presence_of_element_located(self.off_plan_xpath))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Try standard click
            try:
                clickable = self.wait.until(EC.element_to_be_clickable(self.off_plan_xpath))
                clickable.click()
            except Exception:
                # Fallback: JS click (mobile tap simulation)
                self.driver.execute_script("arguments[0].click();", element)

        except TimeoutException:
            self.driver.save_screenshot("off_plan_click_error_mobile.png")
            raise AssertionError("❌ Off-plan menu item not found or not clickable on mobile.")

    def click_off_plan_menu(self):
        try:
            menu_item = self.wait.until(EC.element_to_be_clickable(self.menu_selector))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", menu_item)
            menu_item.click()
        except Exception as e:
            raise AssertionError(f"❌ Failed to click Off Plan menu on mobile: {e}")

    def is_off_plan_page_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located((
                By.XPATH,
                '//button[@class="pb-5 text-sm transition-all border-b-2 whitespace-nowrap font-bold border-foreground"]'
            )))
            return True
        except TimeoutException:
            raise AssertionError("❌ Off Plan page did not load correctly on mobile — expected tab/button not found.")

    def all_products_have_title_and_image(self):
        try:
            product_items = self.driver.find_elements(By.CLASS_NAME, "product-card-class")
            assert product_items, "⚠️ No product items were found on the mobile page."

            for index, item in enumerate(product_items, start=1):
                try:
                    title = item.find_element(By.CLASS_NAME, "product-title-class")
                    image = item.find_element(By.TAG_NAME, "img")

                    assert title.text.strip() != "", f"⚠️ Product {index} is missing a title."
                    assert image.get_attribute("src"), f"⚠️ Product {index} is missing an image src."
                except Exception as e:
                    raise AssertionError(f"❌ Error in product {index}: {str(e)}")
            return True
        except Exception as e:
            raise AssertionError(f"❌ Failed while verifying all products on mobile: {str(e)}")
