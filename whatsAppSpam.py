from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import PyPDF2 as pdf


driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Open the pdf
# Make a pdf reader object
# Place the pdf in the same directory as this script
pdf_obj = open("PLACEHOLDER.pdf", "rb")
pdf_reader = pdf.PdfFileReader(pdf_obj)

# Count the total pages of the pdf file
total_pages = pdf_reader.numPages

count = 0
# Replace the target string with the name of the person you wanna spam
# Make sure their name exists in the "Chats" tab
target = '"PLACEHOLDER NAME"'

while count < total_pages:
    # Make a page object and point it to the current page
    page_obj = pdf_reader.getPage(count)
    # Get the text/Block of text from the page
    string = page_obj.extractText()

    # Logic to find the target's name in your "Chats" tab
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(ec.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()

    # Find the input dialogue box
    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = wait.until(ec.presence_of_element_located((
        By.XPATH, inp_xpath)))

    # And start spamming
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
    count += 1
