#!/bin/python3
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to the ChromeDriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a ChromeDriver service object
chrome_service = Service(executable_path=chromedriver_path)

# Start the ChromeDriver service
chrome_service.start()

# Set the path to the Chrome binary
chrome_binary_path = '/usr/bin/google-chrome-stable'

# Set up the driver with the path to the Chrome binary and the ChromeDriver service object
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.binary_location = chrome_binary_path
chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
chrome_driver.set_window_size(1024, 768)
# Navigate to the website
try:  
   url=os.environ["url"]
except KeyError: 
   print("Please set the environment variable url")
   print("url=https://cooks-api.themeatstick.com/app-webapi?RecipeKey=a036bc707fd06193594964 ./scraper.py")
   sys.exit(1)
chrome_driver.get(url)
import time
time.sleep(5)




# Find the canvas element
#canvas_xpath="/html/body/div[@class='d-none d-sm-block container']/div[@class='row']/div[@class='col d-flex flex-column']/div[@class='row pt-3 flex-fill']/div[@id='chartContainer2']/div[1]/canvas"
canvas_xpath="/html/body/div[2]/div/div[2]/div[2]/div/div[1]/canvas"
canvas = chrome_driver.find_elements(By.XPATH, canvas_xpath)[0]

# Get the size and location of the canvas
# Calculate the start and end points of the slide
canvas_location = canvas.location
canvas_size = canvas.size
print("canvassize",canvas.size, "canvas loc",canvas_location)





location = canvas.location
size = canvas.size

# calculate the bounds of the element
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# print the bounds of the element
print(f"Bounds: ({left}, {top}, {right}, {bottom})")










start_x = 190
start_y = 1

end_x = 250
end_y = start_y
print("Startx",start_x,"start_y",start_y)
# Create an ActionChains object and move the mouse to the start position
actions = ActionChains(chrome_driver)
actions.move_to_element_with_offset(canvas, start_x, start_y)
duration = 1  # duration of the sliding motion in seconds
steps = 30  # number of steps for the sliding motion
x_step = (end_x-start_x)/steps
y_step = 0
print("Stepping: ",x_step,y_step)
# Generate a sliding motion by gradually moving the mouse to the end position
# Find the paragraph tag with the current-temp and internal-temp classes
tempxPath = "/html/body/div[@class='d-none d-sm-block container']/div[@class='row']/div[@class='col d-flex flex-column']/div[@class='row pt-4']/div[@class='col ps-3']/div[@class='row pt-3']/div[@class='col-3 internal-temp-block']/div[@class='row'][2]/p[@class='current-temp internal-temp']"
ambxPath = "/html/body/div[@class='d-none d-sm-block container']/div[@class='row']/div[@class='col d-flex flex-column']/div[@class='row pt-4']/div[@class='col ps-3']/div[@class='row pt-3']/div[@class='col-3 ambient-temp-block']/div[@class='row'][2]/p[@class='current-temp ambient-temp']"
elpxPath = "/html/body/div[@class='d-none d-sm-block container']/div[@class='row']/div[@class='col d-flex flex-column']/div[@class='row pt-4']/div[@class='col ps-3']/div[@class='row'][2]/div[@class='col-6']/p[@class='current-time']"
battxPath ="/html/body/div[@class='d-none d-sm-block container']/div[@class='row']/div[@class='col d-flex flex-column']/div[@class='row pt-4']/div[@class='col ps-3']/div[@class='row align-items-center']/div[@class='col-auto']/img[@class='col-auto battery']"
print("Elapsed temperature:", chrome_driver.find_element(By.XPATH, elpxPath).text)

for i in range(steps):
    #print("Step:",i,"currentx",start_x+(i*x_step))
    actions.move_by_offset(x_step, y_step).perform()
    time.sleep(duration / steps)
    temp_par = chrome_driver.find_element(By.XPATH, tempxPath)
    temp_amb = chrome_driver.find_element(By.XPATH, ambxPath)
    # Get the text content of the paragraph tag
    temp_text = temp_par.text
    print("Time:",chrome_driver.find_element(By.XPATH, elpxPath).text,"Temperature:", temp_text, " Ambient temp", temp_amb.text)

actions.release().perform()
time.sleep(1)

temp_par = chrome_driver.find_element(By.XPATH, tempxPath)
temp_amb = chrome_driver.find_element(By.XPATH, ambxPath)
batt_perc = chrome_driver.find_element(By.XPATH, battxPath)
img_url = batt_perc.get_attribute('src')


import re

text = img_url
pattern = "Battery(\d+)"

match = re.search(pattern, text)
if match:
    bPerc = match.group(1)
else:
    bPerc="missing"


print("Battery:",bPerc,"%")

# Get the text content of the paragraph tag
temp_text = temp_par.text
print("Current temperature:", temp_text, " Ambient temp", temp_amb.text)

# Quit the driver and stop the ChromeDriver service
chrome_driver.quit()
chrome_service.stop()

