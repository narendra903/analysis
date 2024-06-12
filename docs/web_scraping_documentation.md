# Web Scraping Documentation

## Overview
This documentation explains the methods used to address various challenges encountered during the web scraping process for extracting laptop data using Selenium and Python.

## Key Challenges and Solutions

### 1. Handling the "Next" Button
**Problem:** The "Next" button was sometimes intercepted by other elements, causing `element click intercepted` errors.

**Solution:**
```python
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='list-bttnn' and contains(text(), 'Next')]"))
)
driver.execute_script("arguments[0].click();", next_button)
time.sleep(5)

### 2. Opening and Closing New Windows
**Problem:**  Extracting detailed data required opening new windows for each item.
**Solution:**
```python
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(link)
...
driver.close()
driver.switch_to.window(driver.window_handles[0])


### 3. Ensuring Checkbox is Selected


**Problem:**  Ensuring the "Available In Stores" checkbox was selected before scraping.

available_in_stores_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Available In Stores"]'))
)
if not available_in_stores_checkbox.is_selected():
    available_in_stores_checkbox.click()

### 4.Extracting Dynamic Content

**Problem:** Some elements were dynamically loaded, causing NoSuchElementException.

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".dynamic-element"))
)


Conclusion
This documentation provides an overview of the challenges encountered and the solutions implemented to handle web scraping using Selenium and Python effectively. By addressing these issues, we ensured reliable data extraction from the target website.

