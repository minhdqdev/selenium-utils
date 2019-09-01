'''
This file define some functions working with selenium's driver.

Author: minhdq99hp

'''
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def scroll_until_exists(driver, elem_ids, time_out=None):
    '''
    Args:
        elem_ids (List): contain ids of the elements we want to check whether if they exist.

    '''
    if time_out is None:
        time_out = 120 # seconds

    start = time.time()

    while True:
        print('scrolling...')
        actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN)
        actions.send_keys(Keys.CONTROL, Keys.END)
        actions.perform()

        # time.sleep(0.5)

        # exit condition
        found = False
        for elem_id in elem_ids:
            try:
                driver.find_element_by_id(elem_id)
                found = True
                break
            except NoSuchElementException:
                continue

        if found:
            break

        # check time out
        if time.time() - start >= time_out:
            break
