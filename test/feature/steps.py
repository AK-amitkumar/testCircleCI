from lettuce import *

from lettuce_webdriver.util import AssertContextManager
import lettuce_webdriver.webdriver 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys

@before.all
def setup_browser():
	world.browser = webdriver.Chrome()

@step('I go to "(.*?)"')
def i_go_to_url(step, url):
	world.response = world.browser.get(url)


i_should_see_the_field_with_id
@step('I should see the field with id "([^"]*)"')
def i_should_see_the_field_with_id(step, field_d):
    with AssertContextManager(step):
        #text_field = world.browser.find_element_by_id(field_id)
		assert world.browser.find_element_by_id(field_id)