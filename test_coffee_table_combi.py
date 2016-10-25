from selenium import webdriver
import time
import gtk.gdk
from proboscis import test
import unittest
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import itertools
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


global coffee_table_price, window_before, window_after, total_price
class test_custom_bed(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        cls.driver=webdriver.Firefox()
        driver=cls.driver
        driver.get("http://www.customfurnish.com/")
        print driver.title

    @test
    def test_1_home(self):
        driver=self.driver
        driver.maximize_window()
        time.sleep(10)
        close=driver.find_element_by_xpath(".//*[@id='SubscriptionModal']/a")
        close.click()
        home_url=driver.current_url
        if home_url=="http://www.customfurnish.com/":
            print "Home page opened..."
        else:
            print "ERR Home page not opened"
        time.sleep(5)

    @test
    def test_2_coffee_table(self):
        driver = self.driver
        coffee_table = driver.find_element_by_xpath(".//*[@id='moreNav']/div[1]/ul/li/ul/li[3]/a")
        time.sleep(3)
        coffee_table.click()
        try:
            coffee_table_url = driver.current_url
            if coffee_table_url == "http://www.customfurnish.com/coffee-tables/":
                print "Coffee table page opened..."
        except:
            print "ERR Coffee table page not opened..."
            raise Exception
        time.sleep(2)

    @test
    def test_3_coffee_table_comb(self):
        driver=self.driver
        count = 0
        action=ActionChains(driver)
        action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down("k").perform()

        size = driver.find_element_by_xpath(
            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
        size.click()
        size_items_size = driver.find_elements_by_class_name("more-designs-image")
        size_length = len(size_items_size)
        try:

            for i1 in range(1, size_length + 1):
                size_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
                size_tab.click()
                size_prop_name = size_tab.text
                print "prop name is:", size_prop_name
                size_items = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i1)
                size_items.click()
                size_item_name = size_items.text
                print "type name is :", size_item_name
                count += 1
                # print "count is:", count

                frame_material_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                frame_material_tab.click()
                frame_material_items = driver.find_elements_by_class_name("more-designs-image")
                size_frame_material = len(frame_material_items)
                for i2 in range(1, size_frame_material + 1):
                    frame_material_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                    frame_material_tab.click()
                    prop_name = frame_material_tab.text
                    print "property name is:", prop_name

                    frame_material_item = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i2)
                    frame_material_item.click()
                    frame_material_item_name = frame_material_item.text
                    print "item name is:", frame_material_item_name
                    count += 1
                    time.sleep(2)

                    frame_style_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                    frame_style_tab.click()
                    frame_style_items = driver.find_elements_by_class_name("more-designs-image")
                    style_size = len(frame_style_items)
                    # print "count is:", count

                    for i3 in range(1, style_size + 1):
                        frame_style_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                        frame_style_tab.click()
                        prop_name = frame_style_tab.text
                        count += 1
                        frame_style_item = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i3)
                        driver.execute_script("arguments[0].click();", frame_style_item)
                        frame_style_item_name = frame_style_item.text
                        count += 1
                        time.sleep(2)

                        top_material_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                        top_material_tab.click()
                        top_material_items = driver.find_elements_by_class_name("more-designs-image")
                        size_top_material = len(top_material_items)
                        # print "count is:", count

                        for i4 in range(1, size_top_material + 1):
                            top_material_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                            top_material_tab.click()
                            prop_name = top_material_tab.text
                            top_material_item = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i4)
                            top_material_item.click()
                            top_material_item_name = top_material_item.text
                            count += 1
                            time.sleep(2)

                            top_style_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                            top_style_tab.click()

                            top_style_items = driver.find_elements_by_class_name("more-designs-image")
                            size_top_style = len(top_style_items)
                            # print "count is:",count

                            for i5 in range(1, size_top_style + 1):
                                top_style_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                top_style_tab.click()
                                prop_name = top_style_tab.text

                                top_style_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i5)
                                top_style_item.click()
                                top_style_item_name = top_style_item.text
                                count += 1
                                time.sleep(2)
                                # print "count is:", count

                                drawer_style_text = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div/a[2]").text
                                if drawer_style_text != 'None':
                                    # print "Drawer style enabled ..."
                                    drawer_style_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                    drawer_style_tab.click()

                                    drawer_style_items = driver.find_elements_by_class_name("more-designs-image")
                                    size_drawer_style = len(drawer_style_items)

                                    for i6 in range(1, size_drawer_style + 1):
                                        drawer_style_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                        drawer_style_tab.click()
                                        prop_name = drawer_style_tab.text

                                        drawer_style_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i6)
                                        drawer_style_item.click()
                                        drawer_style_item_name = drawer_style_item.text
                                        print "drawer style item name is:", drawer_style_item_name
                                        count += 1
                                        time.sleep(2)
                                        # print "count is:", count

                                        drawer_fascia_text = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div/a[2]").text
                                        if drawer_fascia_text != 'None':
                                            # print "Drawer Fascia enabled..."
                                            drawer_fascia_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                            drawer_fascia_tab.click()
                                            prop_name = drawer_fascia_tab.text

                                            drawer_fascia_items = driver.find_elements_by_class_name(
                                                "more-designs-image")
                                            size_drawer_fascia = len(drawer_fascia_items)
                                            if size_drawer_fascia == 1:
                                                handle_style_item_name = "None"
                                                drawer_fascia_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li/img")
                                                drawer_fascia_item.click()
                                                item_name = drawer_fascia_item.text
                                                count += 1
                                                # print "count is:", count
                                            else:
                                                for i7 in range(1, size_drawer_fascia + 1):
                                                    drawer_fascia_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                                    drawer_fascia_tab.click()
                                                    prop_name = drawer_fascia_tab.text

                                                    drawer_fascia_item = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                                    drawer_fascia_item.click()
                                                    drawer_fascia_item_name = drawer_fascia_item.text
                                                    count += 1
                                                    time.sleep(2)

                                                    handle_style_text = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                                    if handle_style_text != 'None':
                                                        # print 'Handle style enabled'
                                                        handle_style_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                        handle_style_tab.click()

                                                        handle_style_items = driver.find_elements_by_class_name(
                                                            "more-designs-image")
                                                        size_handle_style = len(handle_style_items)

                                                        for i8 in range(1, size_handle_style + 1):
                                                            handle_style_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                            handle_style_tab.click()
                                                            prop_name = handle_style_tab.text

                                                            handle_style_item = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                            handle_style_item.click()
                                                            handle_style_item_name = handle_style_item.text
                                                            count += 1
                                                            time.sleep(2)
                                                            # print "count is:", count

                                                            frame_material_text = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
                                                            if frame_material_text != "Metal":
                                                                # print "Shelf material enabled.."
                                                                shelf_material_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                                shelf_material_tab.click()

                                                                shelf_material_items = driver.find_elements_by_class_name(
                                                                    "more-designs-image")
                                                                size_shelf_material = len(shelf_material_items)

                                                                for i9 in range(1, size_shelf_material + 1):
                                                                    shelf_material_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                                    shelf_material_tab.click()
                                                                    prop_name = shelf_material_tab.text

                                                                    shelf_material_item = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i9)
                                                                    shelf_material_item.click()
                                                                    shelf_material_item_name = shelf_material_item.text
                                                                    count += 1
                                                                    time.sleep(2)
                                                                    # print "count is:", count

                                                                    shelf_style_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div/a[2]").text
                                                                    if shelf_style_text != 'None':
                                                                        # print "shelf style enabled..."
                                                                        shelf_style_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                                        shelf_style_tab.click()

                                                                        shelf_style_items = driver.find_elements_by_class_name(
                                                                            "more-designs-image")
                                                                        size_shelf_items = len(shelf_style_items)

                                                                        for i10 in range(1, size_shelf_items + 1):
                                                                            shelf_style_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                                            shelf_style_tab.click()
                                                                            prop_name = shelf_style_tab.text

                                                                            shelf_style_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i10)
                                                                            shelf_style_item.click()
                                                                            shelf_style_item_name = shelf_style_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count

                                                                            leg_position_text = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div/a[2]").text
                                                                            if leg_position_text != 'None':
                                                                                # print "Leg position enabled..."
                                                                                leg_position_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                                leg_position_tab.click()

                                                                                leg_position_items = driver.find_elements_by_class_name(
                                                                                    "more-designs-image")
                                                                                size_leg_position = len(
                                                                                    leg_position_items)
                                                                                # print "count is:", count

                                                                                for i11 in range(1,
                                                                                                 size_leg_position + 1):
                                                                                    leg_position_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                                    leg_position_tab.click()
                                                                                    prop_name = leg_position_tab.text

                                                                                    leg_position_item = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i11)
                                                                                    leg_position_item.click()
                                                                                    leg_position_item_name = leg_position_item.text
                                                                                    count += 1
                                                                                    time.sleep(2)

                                                                                    frame_color_text = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                                                    if frame_color_text != "None":
                                                                                        # print "frame color enabled..."
                                                                                        frame_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                        frame_color_tab.click()

                                                                                        frame_color_items = driver.find_elements_by_class_name(
                                                                                            "more-designs-image")
                                                                                        size_frame_color = len(
                                                                                            frame_color_items)

                                                                                        for i12 in range(1,
                                                                                                         size_frame_color + 1):
                                                                                            frame_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                            frame_color_tab.click()
                                                                                            prop_name = frame_color_tab.text

                                                                                            frame_color_item = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                                            driver.execute_script(
                                                                                                "arguments[0].click();",
                                                                                                frame_color_item)
                                                                                            frame_color_item_name = frame_color_item.text
                                                                                            count += 1
                                                                                            time.sleep(2)
                                                                                            # print "count is:", count

                                                                                            top_color_text = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                                            if top_color_text != 'None':
                                                                                                # print "top color enabled..."
                                                                                                top_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                                top_color_tab.click()

                                                                                                top_color_items = driver.find_elements_by_class_name(
                                                                                                    'more-designs-image')
                                                                                                size_top_color = len(
                                                                                                    top_color_items)

                                                                                                for i13 in range(1,
                                                                                                                 size_top_color + 1):
                                                                                                    top_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                                    top_color_tab.click()
                                                                                                    prop_name = top_color_tab.text

                                                                                                    top_color_item = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                                    driver.execute_script(
                                                                                                        "arguments[0].click();",
                                                                                                        top_color_item)
                                                                                                    top_color_item_name = top_color_item.text
                                                                                                    count += 1
                                                                                                    time.sleep(2)
                                                                                                    # print "count is:", count

                                                                                                    handle_color_text = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                                    if handle_color_text != 'None':
                                                                                                        # print 'handle color is enabled...'
                                                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                        handle_color_tab.click()

                                                                                                        handle_color_items = driver.find_elements_by_class_name(
                                                                                                            "more-designs-image")
                                                                                                        size_handle_color = len(
                                                                                                            handle_color_items)

                                                                                                        for i14 in range(
                                                                                                                1,
                                                                                                                size_handle_color + 1):
                                                                                                            handle_color_tab = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                            handle_color_tab.click()
                                                                                                            prop_name = handle_color_tab.text
                                                                                                            count += 1
                                                                                                            handle_color_item = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                                            handle_color_item.click()
                                                                                                            handle_color_item_name = handle_color_item.text

                                                                                                            time.sleep(
                                                                                                                2)
                                                                                                            # print "count is:", count

                                                                                                            shelf_color_text = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                            if shelf_color_text != 'None':
                                                                                                                # print "shelf color tab enabled..."
                                                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                                shelf_color_tab.click()

                                                                                                                shelf_color_items = driver.find_elements_by_class_name(
                                                                                                                    "more-designs-image")
                                                                                                                size_shelf_color = len(
                                                                                                                    shelf_color_items)

                                                                                                                for i15 in range(
                                                                                                                        1,
                                                                                                                        size_shelf_color + 1):
                                                                                                                    shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                                    shelf_color_tab.click()
                                                                                                                    prop_name = shelf_color_tab.text

                                                                                                                    shelf_color_item = driver.find_element_by_xpath(
                                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                                    driver.execute_script(
                                                                                                                        "arguments[0].click();",
                                                                                                                        shelf_color_item)
                                                                                                                    shelf_color_item_name = shelf_color_item.text
                                                                                                                    count += 1
                                                                                                                    time.sleep(
                                                                                                                        2)
                                                                                                                    # print "count is:", count

                                                                                                            else:
                                                                                                                shelf_color_item_name = "None"

                                                                                                                # print "shelf color disabled!!!"

                                                                                                    else:
                                                                                                        handle_color_item_name = "None"
                                                                                                        # print "Handle color disabled!!!"
                                                                                                        shelf_color_text = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                        if shelf_color_text != 'None':
                                                                                                            # print "shelf color tab enabled..."
                                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                            shelf_color_tab.click()

                                                                                                            shelf_color_items = driver.find_elements_by_class_name(
                                                                                                                "more-designs-image")
                                                                                                            size_shelf_color = len(
                                                                                                                shelf_color_items)

                                                                                                            for i15 in range(
                                                                                                                    1,
                                                                                                                    size_shelf_color + 1):
                                                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                                shelf_color_tab.click()
                                                                                                                prop_name = shelf_color_tab.text
                                                                                                                shelf_color_item = driver.find_element_by_xpath(
                                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                                driver.execute_script(
                                                                                                                    "arguments[0].click();",
                                                                                                                    shelf_color_item)
                                                                                                                shelf_color_item_name = shelf_color_item.text
                                                                                                                count += 1
                                                                                                                time.sleep(
                                                                                                                    2)
                                                                                                                # print "count is:", count
                                                                                                        else:
                                                                                                            shelf_color_item_name = "None"

                                                                                                            # print "shelf color disabled!!!"


                                                                                            else:
                                                                                                top_color_item_name = "None"
                                                                                                # print "top color disabled!!!"
                                                                                                handle_color_text = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                                if handle_color_text != 'None':
                                                                                                    # print 'handle color is enabled...'
                                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                    handle_color_tab.click()

                                                                                                    handle_color_items = driver.find_elements_by_class_name(
                                                                                                        "more-designs-image")
                                                                                                    size_handle_color = len(
                                                                                                        handle_color_items)

                                                                                                    for i14 in range(1,
                                                                                                                     size_handle_color + 1):
                                                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                        handle_color_tab.click()
                                                                                                        prop_name = handle_color_tab.text

                                                                                                        handle_color_item = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                                        handle_color_item.click()
                                                                                                        handle_color_item_name = handle_color_item.text
                                                                                                        count += 1
                                                                                                        time.sleep(2)
                                                                                                        # print "count is:", count
                                                                                                else:
                                                                                                    handle_color_item_name = "None"
                                                                                                    # print "Handle color disabled!!!"
                                                                                                    shelf_color_text = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                    if shelf_color_text != 'None':
                                                                                                        # print "shelf color tab enabled..."
                                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                        shelf_color_tab.click()

                                                                                                        shelf_color_items = driver.find_elements_by_class_name(
                                                                                                            "more-designs-image")
                                                                                                        size_shelf_color = len(
                                                                                                            shelf_color_items)
                                                                                                        # print "count is:", count

                                                                                                        for i15 in range(
                                                                                                                1,
                                                                                                                size_shelf_color + 1):
                                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                            shelf_color_tab.click()
                                                                                                            prop_name = shelf_color_tab.text

                                                                                                            shelf_color_item = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                            driver.execute_script(
                                                                                                                "arguments[0].click();",
                                                                                                                shelf_color_item)
                                                                                                            shelf_color_item_name = shelf_style_item.text
                                                                                                            count += 1
                                                                                                            time.sleep(
                                                                                                                2)
                                                                                                            # print "count is:", count

                                                                                                    else:
                                                                                                        shelf_color_item_name = "None"
                                                                                                        pass
                                                                                                        # print "shelf color disabled!!!"


                                                                                    else:
                                                                                        frame_color_item_name = "None"
                                                                                        # print "frame color disabled!!!"
                                                                                        top_color_text = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                                        if top_color_text != 'None':
                                                                                            # print "top color enabled..."
                                                                                            top_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                            top_color_tab.click()

                                                                                            top_color_items = driver.find_elements_by_class_name(
                                                                                                'more-designs-image')
                                                                                            size_top_color = len(
                                                                                                top_color_items)

                                                                                            for i13 in range(1,
                                                                                                             size_top_color + 1):
                                                                                                top_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                                top_color_tab.click()
                                                                                                prop_name = top_color_tab.text

                                                                                                top_color_item = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                                driver.execute_script(
                                                                                                    "arguments[0].click();",
                                                                                                    top_color_item)
                                                                                                top_color_item_name = top_color_item.text
                                                                                                count += 1
                                                                                                time.sleep(2)
                                                                                                # print "count is:", count
                                                                                        else:
                                                                                            top_color_item_name = "None"
                                                                                            # print "top color disabled!!!"
                                                                                            handle_color_text = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                            if handle_color_text != 'None':
                                                                                                # print 'handle color is enabled...'
                                                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                handle_color_tab.click()

                                                                                                handle_color_items = driver.find_elements_by_class_name(
                                                                                                    "more-designs-image")
                                                                                                size_handle_color = len(
                                                                                                    handle_color_items)

                                                                                                for i14 in range(1,
                                                                                                                 size_handle_color + 1):
                                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                    handle_color_tab.click()
                                                                                                    prop_name = handle_color_tab.text

                                                                                                    handle_color_item = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                                    handle_color_item.click()
                                                                                                    handle_color_item_name = handle_color_item.text
                                                                                                    count += 1
                                                                                                    time.sleep(2)
                                                                                                    print "count is:", count
                                                                                            else:
                                                                                                handle_color_item_name = "None"
                                                                                                # print "Handle color disabled!!!"
                                                                                                shelf_color_text = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                if shelf_color_text != 'None':
                                                                                                    # print "shelf color tab enabled..."
                                                                                                    shelf_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                    shelf_color_tab.click()

                                                                                                    shelf_color_items = driver.find_elements_by_class_name(
                                                                                                        "more-designs-image")
                                                                                                    size_shelf_color = len(
                                                                                                        shelf_color_items)

                                                                                                    for i15 in range(1,
                                                                                                                     size_shelf_color + 1):
                                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                        shelf_color_tab.click()
                                                                                                        prop_name = shelf_color_tab.text

                                                                                                        shelf_color_item = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                        driver.execute_script(
                                                                                                            "arguments[0].click();",
                                                                                                            shelf_color_item)
                                                                                                        shelf_color_item_name = shelf_color_item.text
                                                                                                        count += 1
                                                                                                        time.sleep(2)
                                                                                                        # print "count is:", count

                                                                                                else:
                                                                                                    shelf_color_item_name = "None"


                                                                                                    # print "shelf color disabled!!!"

                                                                            else:
                                                                                leg_position_item_name = "None"
                                                                                # print("leg position disabled...")
                                                                                frame_color_text = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                                                if frame_color_text != "None":
                                                                                    # print "frame color enabled..."
                                                                                    frame_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                    frame_color_tab.click()

                                                                                    frame_color_items = driver.find_elements_by_class_name(
                                                                                        "more-designs-image")
                                                                                    size_frame_color = len(
                                                                                        frame_color_items)

                                                                                    for i12 in range(1,
                                                                                                     size_frame_color + 1):
                                                                                        frame_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                        frame_color_tab.click()
                                                                                        prop_name = frame_color_tab.text

                                                                                        frame_color_item = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                                        driver.execute_script(
                                                                                            "arguments[0].click();",
                                                                                            frame_color_item)
                                                                                        frame_color_item_name = frame_color_item.text
                                                                                        count += 1
                                                                                        time.sleep(2)
                                                                                        # print "count is:", count

                                                                                        top_color_text = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                                        if top_color_text != 'None':
                                                                                            # print "top color enabled..."
                                                                                            top_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                            top_color_tab.click()

                                                                                            top_color_items = driver.find_elements_by_class_name(
                                                                                                'more-designs-image')
                                                                                            size_top_color = len(
                                                                                                top_color_items)

                                                                                            for i13 in range(1,
                                                                                                             size_top_color + 1):
                                                                                                top_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                                top_color_tab.click()
                                                                                                prop_name = top_color_tab.text

                                                                                                top_color_item = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                                driver.execute_script(
                                                                                                    "arguments[0].click();",
                                                                                                    top_color_item)
                                                                                                top_color_item_name = top_color_item.text
                                                                                                count += 1
                                                                                                time.sleep(2)
                                                                                                # print "count is:", count

                                                                                                handle_color_text = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                                if handle_color_text != 'None':
                                                                                                    # print 'handle color is enabled...'
                                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                    handle_color_tab.click()

                                                                                                    handle_color_items = driver.find_elements_by_class_name(
                                                                                                        "more-designs-image")
                                                                                                    size_handle_color = len(
                                                                                                        handle_color_items)

                                                                                                    for i14 in range(1,
                                                                                                                     size_handle_color + 1):
                                                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                        handle_color_tab.click()
                                                                                                        prop_name = handle_color_tab.text
                                                                                                        count += 1
                                                                                                        handle_color_item = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                                        handle_color_item.click()
                                                                                                        handle_color_item_name = handle_color_item.text

                                                                                                        time.sleep(2)
                                                                                                        # print "count is:", count

                                                                                                        shelf_color_text = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                        if shelf_color_text != 'None':
                                                                                                            # print "shelf color tab enabled..."
                                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                            shelf_color_tab.click()

                                                                                                            shelf_color_items = driver.find_elements_by_class_name(
                                                                                                                "more-designs-image")
                                                                                                            size_shelf_color = len(
                                                                                                                shelf_color_items)

                                                                                                            for i15 in range(
                                                                                                                    1,
                                                                                                                    size_shelf_color + 1):
                                                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                                shelf_color_tab.click()
                                                                                                                prop_name = shelf_color_tab.text

                                                                                                                shelf_color_item = driver.find_element_by_xpath(
                                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                                driver.execute_script(
                                                                                                                    "arguments[0].click();",
                                                                                                                    shelf_color_item)
                                                                                                                shelf_color_item_name = shelf_color_item.text
                                                                                                                count += 1
                                                                                                                time.sleep(
                                                                                                                    2)
                                                                                                                # print "count is:", count

                                                                                                        else:
                                                                                                            shelf_color_item_name = "None"
                                                                                                            pass
                                                                                                            # print "shelf color disabled!!!"



                                                                                                else:
                                                                                                    handle_color_item_name = "None"
                                                                                                    # print "Handle color disabled..."
                                                                                                    shelf_color_text = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                    if shelf_color_text != 'None':
                                                                                                        # print "shelf color tab enabled..."
                                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                        shelf_color_tab.click()

                                                                                                        shelf_color_items = driver.find_elements_by_class_name(
                                                                                                            "more-designs-image")
                                                                                                        size_shelf_color = len(
                                                                                                            shelf_color_items)

                                                                                                        for i15 in range(
                                                                                                                1,
                                                                                                                size_shelf_color + 1):
                                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                            shelf_color_tab.click()
                                                                                                            prop_name = shelf_color_tab.text

                                                                                                            shelf_color_item = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                            driver.execute_script(
                                                                                                                "arguments[0].click();",
                                                                                                                shelf_color_item)
                                                                                                            shelf_color_item_name = shelf_color_item.text
                                                                                                            count += 1
                                                                                                            time.sleep(
                                                                                                                2)
                                                                                                            # print "count is:", count

                                                                                                    else:
                                                                                                        shelf_color_item_name = "None"
                                                                                                        pass
                                                                                                        # print "shelf color disabled!!!"




                                                                                        else:
                                                                                            top_color_item_name = "None"
                                                                                            # print "Top color disabled..."
                                                                                            handle_color_text = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                            if handle_color_text != 'None':
                                                                                                # print 'handle color is enabled...'
                                                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                handle_color_tab.click()

                                                                                                handle_color_items = driver.find_elements_by_class_name(
                                                                                                    "more-designs-image")
                                                                                                size_handle_color = len(
                                                                                                    handle_color_items)

                                                                                                for i14 in range(1,
                                                                                                                 size_handle_color + 1):
                                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                    handle_color_tab.click()
                                                                                                    prop_name = handle_color_tab.text
                                                                                                    count += 1
                                                                                                    handle_color_item = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                                    handle_color_item.click()
                                                                                                    handle_color_item_name = handle_color_item.text

                                                                                                    time.sleep(2)
                                                                                                    # print "count is:", count

                                                                                                    shelf_color_text = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                                    if shelf_color_text != 'None':
                                                                                                        # print "shelf color tab enabled..."
                                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                        shelf_color_tab.click()

                                                                                                        shelf_color_items = driver.find_elements_by_class_name(
                                                                                                            "more-designs-image")
                                                                                                        size_shelf_color = len(
                                                                                                            shelf_color_items)

                                                                                                        for i15 in range(
                                                                                                                1,
                                                                                                                size_shelf_color + 1):
                                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                            shelf_color_tab.click()
                                                                                                            prop_name = shelf_color_tab.text

                                                                                                            shelf_color_item = driver.find_element_by_xpath(
                                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                            driver.execute_script(
                                                                                                                "arguments[0].click();",
                                                                                                                shelf_color_item)
                                                                                                            shelf_color_item_name = shelf_color_item.text
                                                                                                            count += 1
                                                                                                            time.sleep(
                                                                                                                2)
                                                                                                            # print "count is:", count

                                                                                                    else:
                                                                                                        shelf_color_item_name = "None"

                                                                                                        # print "shelf color disabled!!!"


                                                                                else:
                                                                                    frame_color_item_name = "None"
                                                                                    # print "frame color disabled!!!"
                                                                                    top_color_text = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                                    if top_color_text != 'None':
                                                                                        # print "top color enabled..."
                                                                                        top_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                        top_color_tab.click()

                                                                                        top_color_items = driver.find_elements_by_class_name(
                                                                                            'more-designs-image')
                                                                                        size_top_color = len(
                                                                                            top_color_items)

                                                                                        for i13 in range(1,
                                                                                                         size_top_color + 1):
                                                                                            top_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                            top_color_tab.click()
                                                                                            prop_name = top_color_tab.text

                                                                                            top_color_item = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                            driver.execute_script(
                                                                                                "arguments[0].click();",
                                                                                                top_color_item)
                                                                                            top_color_item_name = top_color_item.text
                                                                                            count += 1
                                                                                            time.sleep(2)
                                                                                            # print "count is:", count
                                                                                    else:
                                                                                        top_color_item_name = "None"
                                                                                        # print "top color disabled!!!"
                                                                                        handle_color_text = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                        if handle_color_text != 'None':
                                                                                            # print 'handle color is enabled...'
                                                                                            handle_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                            handle_color_tab.click()

                                                                                            handle_color_items = driver.find_elements_by_class_name(
                                                                                                "more-designs-image")
                                                                                            size_handle_color = len(
                                                                                                handle_color_items)

                                                                                            for i14 in range(1,
                                                                                                             size_handle_color + 1):
                                                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                                handle_color_tab.click()
                                                                                                prop_name = handle_color_tab.text

                                                                                                handle_color_item = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                                handle_color_item.click()
                                                                                                handle_color_item_name = handle_color_item.text
                                                                                                count += 1
                                                                                                time.sleep(2)
                                                                                                print "count is:", count
                                                                                        else:
                                                                                            handle_color_item_name = "None"
                                                                                            # print "Handle color disabled!!!"
                                                                                            shelf_color_text = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                            if shelf_color_text != 'None':
                                                                                                # print "shelf color tab enabled..."
                                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                shelf_color_tab.click()

                                                                                                shelf_color_items = driver.find_elements_by_class_name(
                                                                                                    "more-designs-image")
                                                                                                size_shelf_color = len(
                                                                                                    shelf_color_items)

                                                                                                for i15 in range(1,
                                                                                                                 size_shelf_color + 1):
                                                                                                    shelf_color_tab = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                    shelf_color_tab.click()
                                                                                                    prop_name = shelf_color_tab.text

                                                                                                    shelf_color_item = driver.find_element_by_xpath(
                                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                    driver.execute_script(
                                                                                                        "arguments[0].click();",
                                                                                                        shelf_color_item)
                                                                                                    shelf_color_item_name = shelf_color_item.text
                                                                                                    count += 1
                                                                                                    time.sleep(2)
                                                                                                    # print "count is:", count

                                                                                            else:
                                                                                                shelf_color_item_name = "None"


                                                                                                # print "shelf color disabled!!!"




                                                                    else:
                                                                        shelf_style_item_name = "None"
                                                                        # print "shelf style disabled!!!"
                                                                        leg_position_text = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div/a[2]").text
                                                                        if leg_position_text != 'None':
                                                                            # print "Leg position enabled..."
                                                                            leg_position_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                            leg_position_tab.click()

                                                                            leg_position_items = driver.find_elements_by_class_name(
                                                                                "more-designs-image")
                                                                            size_leg_position = len(leg_position_items)

                                                                            for i11 in range(1, size_leg_position + 1):
                                                                                leg_position_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                                leg_position_tab.click()
                                                                                prop_name = leg_position_tab.text

                                                                                leg_position_item = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i11)
                                                                                leg_position_item.click()
                                                                                leg_position_item_name = leg_position_item.text
                                                                                count += 1
                                                                                time.sleep(2)
                                                                                # print "count is:", count
                                                                        else:
                                                                            leg_position_item_name = "None"
                                                                            # print "leg position disabled!!!"
                                                                            frame_color_text = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                                            if frame_color_text != "None":
                                                                                # print "frame color enabled..."
                                                                                frame_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                frame_color_tab.click()

                                                                                frame_color_items = driver.find_elements_by_class_name(
                                                                                    "more-designs-image")
                                                                                size_frame_color = len(
                                                                                    frame_color_items)

                                                                                for i12 in range(1,
                                                                                                 size_frame_color + 1):
                                                                                    frame_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                    frame_color_tab.click()
                                                                                    prop_name = frame_color_tab.text

                                                                                    frame_color_item = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                                    driver.execute_script(
                                                                                        "arguments[0].click();",
                                                                                        frame_color_item)
                                                                                    frame_color_item_name = frame_color_item.text
                                                                                    count += 1

                                                                                    time.sleep(2)
                                                                                    # print "count is:", count
                                                                            else:
                                                                                frame_color_item_name = "None"
                                                                                # print "frame color disabled!!!"
                                                                                top_color_text = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                                if top_color_text != 'None':
                                                                                    # print "top color enabled..."
                                                                                    top_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                    top_color_tab.click()

                                                                                    top_color_items = driver.find_elements_by_class_name(
                                                                                        'more-designs-image')
                                                                                    size_top_color = len(
                                                                                        top_color_items)

                                                                                    for i13 in range(1,
                                                                                                     size_top_color + 1):
                                                                                        top_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                        top_color_tab.click()
                                                                                        prop_name = top_color_tab.text

                                                                                        top_color_item = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                        driver.execute_script(
                                                                                            "arguments[0].click();",
                                                                                            top_color_item)
                                                                                        top_color_item_name = top_color_item.text
                                                                                        count += 1
                                                                                        time.sleep(2)
                                                                                        # print "count is:", count
                                                                                else:
                                                                                    top_color_item_name = "None"  # print "top color disabled!!!"
                                                                                    handle_color_text = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                    if handle_color_text != 'None':
                                                                                        # print 'handle color is enabled...'
                                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                        handle_color_tab.click()

                                                                                        handle_color_items = driver.find_elements_by_class_name(
                                                                                            "more-designs-image")
                                                                                        size_handle_color = len(
                                                                                            handle_color_items)

                                                                                        for i14 in range(1,
                                                                                                         size_handle_color + 1):
                                                                                            handle_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                            handle_color_tab.click()
                                                                                            prop_name = handle_color_tab.text

                                                                                            handle_color_item = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                            handle_color_item.click()
                                                                                            handle_color_item_name = handle_color_item.text
                                                                                            count += 1
                                                                                            time.sleep(2)
                                                                                            # print "count is:", count
                                                                                    else:
                                                                                        handle_color_item_name = "None"
                                                                                        # print "Handle color disabled!!!"
                                                                                        shelf_color_text = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                        if shelf_color_text != 'None':
                                                                                            # print "shelf color tab enabled..."
                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                            shelf_color_tab.click()

                                                                                            shelf_color_items = driver.find_elements_by_class_name(
                                                                                                "more-designs-image")
                                                                                            size_shelf_color = len(
                                                                                                shelf_color_items)

                                                                                            for i15 in range(1,
                                                                                                             size_shelf_color + 1):
                                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                                shelf_color_tab.click()
                                                                                                prop_name = shelf_color_tab.text

                                                                                                shelf_color_item = driver.find_element_by_xpath(
                                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                                driver.execute_script(
                                                                                                    "arguments[0].click();",
                                                                                                    shelf_color_item)
                                                                                                shelf_color_item_name = shelf_color_item.text
                                                                                                count += 1
                                                                                                time.sleep(2)
                                                                                                # print "count is:", count

                                                                                        else:
                                                                                            shelf_color_item_name = "None"
                                                                                            pass
                                                                                            # print "shelf color disabled!!!"




                                                            else:
                                                                shelf_material_item_name = "None"
                                                                # print "Shelf material disabled!!!"
                                                                shelf_style_text = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div/a[2]").text
                                                                if shelf_style_text != 'None':
                                                                    # print "shelf style enabled..."
                                                                    shelf_style_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                                    shelf_style_tab.click()

                                                                    shelf_style_items = driver.find_elements_by_class_name(
                                                                        "more-designs-image")
                                                                    size_shelf_items = len(shelf_style_items)

                                                                    for i10 in range(1, size_shelf_items + 1):
                                                                        shelf_style_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                                        shelf_style_tab.click()
                                                                        prop_name = shelf_style_tab.text

                                                                        shelf_style_item = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i10)
                                                                        shelf_style_item.click()
                                                                        shelf_style_item_name = shelf_style_item.text
                                                                        count += 1
                                                                        time.sleep(2)
                                                                        # print "count is:", count
                                                                else:
                                                                    shelf_style_item_name = "None"
                                                                    # print "shelf style disabled!!!"
                                                                    leg_position_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div/a[2]").text
                                                                    if leg_position_text != 'None':
                                                                        # print "Leg position enabled..."
                                                                        leg_position_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                        leg_position_tab.click()

                                                                        leg_position_items = driver.find_elements_by_class_name(
                                                                            "more-designs-image")
                                                                        size_leg_position = len(leg_position_items)

                                                                        for i11 in range(1, size_leg_position + 1):
                                                                            leg_position_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                            leg_position_tab.click()
                                                                            prop_name = leg_position_tab.text

                                                                            leg_position_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i11)
                                                                            leg_position_item.click()
                                                                            leg_position_item_name = leg_position_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count
                                                                    else:
                                                                        leg_position_item_name = "None"
                                                                        # print "leg position disabled!!!"
                                                                        frame_color_text = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                                        if frame_color_text != "None":
                                                                            # print "frame color enabled..."
                                                                            frame_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                            frame_color_tab.click()

                                                                            frame_color_items = driver.find_elements_by_class_name(
                                                                                "more-designs-image")
                                                                            size_frame_color = len(frame_color_items)

                                                                            for i12 in range(1, size_frame_color + 1):
                                                                                frame_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                                frame_color_tab.click()
                                                                                prop_name = frame_color_tab.text

                                                                                frame_color_item = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                                driver.execute_script(
                                                                                    "arguments[0].click();",
                                                                                    frame_color_item)
                                                                                frame_color_item_name = frame_color_item.text
                                                                                count += 1
                                                                                time.sleep(2)
                                                                                # print "count is:", count
                                                                        else:
                                                                            frame_color_item_name = "None"
                                                                            # print "frame color disabled!!!"
                                                                            top_color_text = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                            if top_color_text != 'None':
                                                                                # print "top color enabled..."
                                                                                top_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                top_color_tab.click()

                                                                                top_color_items = driver.find_elements_by_class_name(
                                                                                    'more-designs-image')
                                                                                size_top_color = len(top_color_items)

                                                                                for i13 in range(1, size_top_color + 1):
                                                                                    top_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                    top_color_tab.click()
                                                                                    prop_name = top_color_tab.text

                                                                                    top_color_item = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                    driver.execute_script(
                                                                                        "arguments[0].click();",
                                                                                        top_color_item)
                                                                                    top_color_item_name = top_color_item.text
                                                                                    count += 1
                                                                                    time.sleep(2)
                                                                                    # print "count is:", count
                                                                            else:
                                                                                top_color_item_name = "None"
                                                                                # print "top color disabled!!!"
                                                                                handle_color_text = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                                if handle_color_text != 'None':
                                                                                    # print 'handle color is enabled...'
                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                    handle_color_tab.click()

                                                                                    handle_color_items = driver.find_elements_by_class_name(
                                                                                        "more-designs-image")
                                                                                    size_handle_color = len(
                                                                                        handle_color_items)

                                                                                    for i14 in range(1,
                                                                                                     size_handle_color + 1):
                                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                        handle_color_tab.click()
                                                                                        prop_name = handle_color_tab.text

                                                                                        handle_color_item = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                        handle_color_item.click()
                                                                                        handle_color_item_name = handle_color_item.text
                                                                                        count += 1
                                                                                        time.sleep(2)
                                                                                        # print "count is:", count
                                                                                else:
                                                                                    handle_color_item_name = "None"
                                                                                    # print "Handle color disabled!!!"
                                                                                    shelf_color_text = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                    if shelf_color_text != 'None':
                                                                                        # print "shelf color tab enabled..."
                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                        shelf_color_tab.click()

                                                                                        shelf_color_items = driver.find_elements_by_class_name(
                                                                                            "more-designs-image")
                                                                                        size_shelf_color = len(
                                                                                            shelf_color_items)

                                                                                        for i15 in range(1,
                                                                                                         size_shelf_color + 1):
                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                            shelf_color_tab.click()
                                                                                            prop_name = shelf_color_tab.text

                                                                                            shelf_color_item = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                            driver.execute_script(
                                                                                                "arguments[0].click();",
                                                                                                shelf_color_item)
                                                                                            shelf_color_item_name = shelf_color_item.text
                                                                                            count += 1
                                                                                            time.sleep(2)
                                                                                            # print "count is:", count

                                                                                    else:
                                                                                        shelf_color_item_name = "None"
                                                                                        pass
                                                                                        # print "shelf color disabled!!!"


                                                    else:
                                                        handle_style_item_name = "None"
                                                        # print "Handle style disabled!!!"
                                                        frame_material_text = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
                                                        if frame_material_text != "Metal":
                                                            # print "Shelf material enabled.."
                                                            shelf_material_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                            shelf_material_tab.click()

                                                            shelf_material_items = driver.find_elements_by_class_name(
                                                                "more-designs-image")
                                                            size_shelf_material = len(shelf_material_items)

                                                            for i9 in range(1, size_shelf_material + 1):
                                                                shelf_material_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                                shelf_material_tab.click()
                                                                prop_name = shelf_material_tab.text

                                                                shelf_material_item = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i9)
                                                                shelf_material_item.click()
                                                                shelf_material_item_name = shelf_material_item.text
                                                                count += 1
                                                                time.sleep(2)
                                                                # print "count is:", count
                                                        else:
                                                            shelf_material_item_name = "None"
                                                            # print "shelf material disabled!!!"
                                                            shelf_style_text = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div/a[2]").text
                                                            if shelf_style_text != 'None':
                                                                # print "shelf style enabled..."
                                                                shelf_style_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                                shelf_style_tab.click()

                                                                shelf_style_items = driver.find_elements_by_class_name(
                                                                    "more-designs-image")
                                                                size_shelf_items = len(shelf_style_items)

                                                                for i10 in range(1, size_shelf_items + 1):
                                                                    shelf_style_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                                    shelf_style_tab.click()
                                                                    prop_name = shelf_style_tab.text

                                                                    shelf_style_item = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i10)
                                                                    shelf_style_item.click()
                                                                    shelf_style_item_name = shelf_style_item.text
                                                                    count += 1
                                                                    time.sleep(2)
                                                                    # print "count is:", count
                                                            else:
                                                                leg_position_item_name = "None"
                                                                # print "shelf syle disabled!!!"
                                                                leg_position_text = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div/a[2]").text
                                                                if leg_position_text != 'None':
                                                                    # print "Leg position enabled..."
                                                                    leg_position_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                    leg_position_tab.click()

                                                                    leg_position_items = driver.find_elements_by_class_name(
                                                                        "more-designs-image")
                                                                    size_leg_position = len(leg_position_items)

                                                                    for i11 in range(1, size_leg_position + 1):
                                                                        leg_position_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                        leg_position_tab.click()
                                                                        prop_name = leg_position_tab.text

                                                                        leg_position_item = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i11)
                                                                        leg_position_item.click()
                                                                        leg_position_item_name = leg_position_item.text
                                                                        count += 1
                                                                        time.sleep(2)
                                                                        # print "count is:", count
                                                                else:
                                                                    leg_position_item_name = "None"
                                                                    # print "leg position disabled!!!"
                                                                    frame_color_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                                    if frame_color_text != "None":
                                                                        # print "frame color enabled..."
                                                                        frame_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                        frame_color_tab.click()

                                                                        frame_color_items = driver.find_elements_by_class_name(
                                                                            "more-designs-image")
                                                                        size_frame_color = len(frame_color_items)

                                                                        for i12 in range(1, size_frame_color + 1):
                                                                            frame_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                            frame_color_tab.click()
                                                                            prop_name = frame_color_tab.text

                                                                            frame_color_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                            driver.execute_script(
                                                                                "arguments[0].click();",
                                                                                frame_color_item)
                                                                            frame_color_item_name = frame_color_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count
                                                                    else:
                                                                        frame_color_item_name = "None"
                                                                        # print "frame color disabled!!!"
                                                                        top_color_text = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                        if top_color_text != 'None':
                                                                            # print "top color enabled..."
                                                                            top_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                            top_color_tab.click()

                                                                            top_color_items = driver.find_elements_by_class_name(
                                                                                'more-designs-image')
                                                                            size_top_color = len(top_color_items)

                                                                            for i13 in range(1, size_top_color + 1):
                                                                                top_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                                top_color_tab.click()
                                                                                prop_name = top_color_tab.text

                                                                                top_color_item = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                                driver.execute_script(
                                                                                    "arguments[0].click();",
                                                                                    top_color_item)
                                                                                top_color_item_name = top_color_item.text
                                                                                count += 1
                                                                                time.sleep(2)
                                                                                # print "count is:", count
                                                                        else:
                                                                            top_color_item_name = "None"
                                                                            # print "top color disabled!!!"
                                                                            handle_color_text = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                            if handle_color_text != 'None':
                                                                                # print 'handle color is enabled...'
                                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                handle_color_tab.click()

                                                                                handle_color_items = driver.find_elements_by_class_name(
                                                                                    "more-designs-image")
                                                                                size_handle_color = len(
                                                                                    handle_color_items)

                                                                                for i14 in range(1,
                                                                                                 size_handle_color + 1):
                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                    handle_color_tab.click()
                                                                                    prop_name = handle_color_tab.text

                                                                                    count += 1
                                                                                    handle_color_item = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                    handle_color_item.click()
                                                                                    handle_color_item_name = handle_color_item.text
                                                                                    count += 1
                                                                                    time.sleep(2)
                                                                                    # print "count is:", count
                                                                            else:
                                                                                handle_color_item_name = "None"
                                                                                # print "Handle color disabled!!!"
                                                                                shelf_color_text = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                if shelf_color_text != 'None':
                                                                                    # print "shelf color tab enabled..."
                                                                                    shelf_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                    shelf_color_tab.click()

                                                                                    shelf_color_items = driver.find_elements_by_class_name(
                                                                                        "more-designs-image")
                                                                                    size_shelf_color = len(
                                                                                        shelf_color_items)

                                                                                    for i15 in range(1,
                                                                                                     size_shelf_color + 1):
                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                        shelf_color_tab.click()
                                                                                        prop_name = shelf_color_tab.text

                                                                                        shelf_color_item = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                        driver.execute_script(
                                                                                            "arguments[0].click();",
                                                                                            shelf_color_item)
                                                                                        shelf_color_item_name = shelf_color_item.text
                                                                                        count += 1
                                                                                        time.sleep(2)
                                                                                        # print "count is:", count

                                                                                else:
                                                                                    shelf_color_item_name = "None"
                                                                                    pass
                                                                                    # print "shelf color disabled!!!"

                                        else:
                                            drawer_fascia_item_name = "None"
                                            # print "Drawer fascia disabled!!!"
                                            handle_style_text = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                            if handle_style_text != 'None':
                                                # print 'Handle style enabled'
                                                handle_style_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                handle_style_tab.click()
                                                count += 1
                                                handle_style_items = driver.find_elements_by_class_name(
                                                    "more-designs-image")
                                                size_handle_style = len(handle_style_items)

                                                for i8 in range(1, size_handle_style + 1):
                                                    handle_style_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                    handle_style_tab.click()
                                                    prop_name = handle_style_tab.text

                                                    count += 1
                                                    handle_style_item = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                    handle_style_item.click()
                                                    handle_style_item_name = handle_style_item.text
                                                    count += 1
                                                    time.sleep(2)
                                                    # print "count is:", count
                                            else:
                                                handle_style_item_name = "None"
                                                # print "handle style disabled!!!"
                                                frame_material_text = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
                                                if frame_material_text != "Metal":
                                                    # print "Shelf material enabled.."
                                                    shelf_material_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                    shelf_material_tab.click()
                                                    count += 1
                                                    shelf_material_items = driver.find_elements_by_class_name(
                                                        "more-designs-image")
                                                    size_shelf_material = len(shelf_material_items)

                                                    for i9 in range(1, size_shelf_material + 1):
                                                        shelf_material_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                        shelf_material_tab.click()
                                                        prop_name = shelf_material_tab.text

                                                        count += 1
                                                        shelf_material_item = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i9)
                                                        shelf_material_item.click()
                                                        shelf_material_item_name = shelf_material_item.text
                                                        count += 1
                                                        time.sleep(2)
                                                        # print "count is:", count
                                                else:
                                                    shelf_material_item_name = "None"
                                                    # print "shelf material disabled!!!"
                                                    shelf_style_text = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div/a[2]").text
                                                    if shelf_style_text != 'None':
                                                        # print "shelf style enabled..."
                                                        shelf_style_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                        shelf_style_tab.click()
                                                        count += 1
                                                        shelf_style_items = driver.find_elements_by_class_name(
                                                            "more-designs-image")
                                                        size_shelf_items = len(shelf_style_items)

                                                        for i10 in range(1, size_shelf_items + 1):
                                                            shelf_style_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                            shelf_style_tab.click()
                                                            prop_name = shelf_style_tab.text

                                                            count += 1
                                                            shelf_style_item = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i10)
                                                            shelf_style_item.click()
                                                            shelf_style_item_name = shelf_style_item.text
                                                            count += 1
                                                            time.sleep(2)
                                                            # print "count is:", count
                                                    else:
                                                        shelf_style_item_name = "None"
                                                        # print "shelf syle disabled!!!"
                                                        leg_position_text = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div/a[2]").text
                                                        if leg_position_text != 'None':
                                                            # print "Leg position enabled..."
                                                            leg_position_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                            leg_position_tab.click()
                                                            count += 1
                                                            leg_position_items = driver.find_elements_by_class_name(
                                                                "more-designs-image")
                                                            size_leg_position = len(leg_position_items)

                                                            for i11 in range(1, size_leg_position + 1):
                                                                leg_position_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                leg_position_tab.click()
                                                                prop_name = leg_position_tab.text

                                                                count += 1
                                                                leg_position_item = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i11)
                                                                leg_position_item.click()
                                                                leg_position_item_name = leg_position_item.text
                                                                count += 1
                                                                time.sleep(2)
                                                                # print "count is:", count
                                                        else:
                                                            leg_position_item_name = "None"
                                                            # print "leg position disabled!!!"
                                                            frame_color_text = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                            if frame_color_text != "None":
                                                                # print "frame color enabled..."
                                                                frame_color_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                frame_color_tab.click()
                                                                count += 1
                                                                frame_color_items = driver.find_elements_by_class_name(
                                                                    "more-designs-image")
                                                                size_frame_color = len(frame_color_items)

                                                                for i12 in range(1, size_frame_color + 1):
                                                                    frame_color_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                    frame_color_tab.click()
                                                                    prop_name = frame_color_tab.text

                                                                    count += 1
                                                                    frame_color_item = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                    driver.execute_script("arguments[0].click();",
                                                                                          frame_color_item)
                                                                    frame_color_item_name = frame_color_item.text
                                                                    count += 1
                                                                    time.sleep(2)
                                                                    # print "count is:", count
                                                            else:
                                                                frame_color_item_name = "None"
                                                                # print "frame color disabled!!!"
                                                                top_color_text = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                if top_color_text != 'None':
                                                                    # print "top color enabled..."
                                                                    top_color_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                    top_color_tab.click()
                                                                    count += 1
                                                                    top_color_items = driver.find_elements_by_class_name(
                                                                        'more-designs-image')
                                                                    size_top_color = len(top_color_items)

                                                                    for i13 in range(1, size_top_color + 1):
                                                                        top_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                        top_color_tab.click()
                                                                        prop_name = top_color_tab.text
                                                                        count += 1
                                                                        top_color_item = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                        driver.execute_script("arguments[0].click();",
                                                                                              top_color_item)
                                                                        top_color_item_name = top_color_item.text
                                                                        count += 1
                                                                        time.sleep(2)
                                                                        # print "count is:", count
                                                                else:
                                                                    top_color_item_name = "None"
                                                                    # print "top color disabled!!!"
                                                                    handle_color_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                    if handle_color_text != 'None':
                                                                        # print 'handle color is enabled...'
                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                        handle_color_tab.click()
                                                                        count += 1
                                                                        handle_color_items = driver.find_elements_by_class_name(
                                                                            "more-designs-image")
                                                                        size_handle_color = len(
                                                                            handle_color_items)

                                                                        for i14 in range(1,
                                                                                         size_handle_color + 1):
                                                                            handle_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                            handle_color_tab.click()
                                                                            prop_name = handle_color_tab.text
                                                                            count += 1
                                                                            handle_color_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                            handle_color_item.click()
                                                                            handle_color_item_name = handle_color_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count
                                                                    else:
                                                                        handle_color_item_name = "None"
                                                                        # print "Handle color disabled!!!"
                                                                        shelf_color_text = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                        if shelf_color_text != 'None':
                                                                            # print "shelf color tab enabled..."
                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                            shelf_color_tab.click()
                                                                            count += 1
                                                                            shelf_color_items = driver.find_elements_by_class_name(
                                                                                "more-designs-image")
                                                                            size_shelf_color = len(
                                                                                shelf_color_items)

                                                                            for i15 in range(1,
                                                                                             size_shelf_color + 1):
                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                shelf_color_tab.click()
                                                                                prop_name = shelf_color_tab.text
                                                                                count += 1
                                                                                shelf_color_item = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                driver.execute_script(
                                                                                    "arguments[0].click();",
                                                                                    shelf_color_item)
                                                                                shelf_color_item_name = shelf_color_item.text
                                                                                count += 1
                                                                                time.sleep(2)
                                                                                # print "count is:", count

                                                                        else:
                                                                            shelf_color_item_name = "None"

                                                                            # print "shelf color disabled!!!"



                                else:
                                    drawer_style_item_name = "None"
                                    # print "Drawer style disabled!!!"
                                    drawer_fascia_text = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div/a[2]").text
                                    if drawer_fascia_text != 'None':
                                        # print "Drawer Fascia enabled..."
                                        drawer_fascia_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                        drawer_fascia_tab.click()
                                        count += 1
                                        drawer_fascia_items = driver.find_elements_by_class_name("more-designs-image")
                                        size_drawer_fascia = len(drawer_fascia_items)
                                        if size_drawer_fascia == 1:
                                            handle_style_item_name = None
                                            drawer_fascia_item = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li/img")
                                            drawer_fascia_item.click()
                                            count += 1
                                        else:
                                            for i7 in range(1, size_drawer_fascia + 1):
                                                drawer_fascia_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                                drawer_fascia_tab.click()
                                                prop_name = drawer_fascia_tab.text
                                                count += 1
                                                drawer_fascia_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                                drawer_fascia_item.click()
                                                drawer_fascia_item_name = drawer_fascia_item.text
                                                count += 1
                                                time.sleep(2)
                                                # print "count is:", count
                                    else:
                                        drawer_fascia_item_name = "None"
                                        # print "Drawer Fascia disabled!!!"
                                        handle_style_text = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                        if handle_style_text != 'None':
                                            # print 'Handle style enabled'
                                            handle_style_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                            handle_style_tab.click()
                                            count += 1
                                            handle_style_items = driver.find_elements_by_class_name(
                                                "more-designs-image")
                                            size_handle_style = len(handle_style_items)

                                            for i8 in range(1, size_handle_style + 1):
                                                handle_style_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                handle_style_tab.click()
                                                prop_name = handle_style_tab.text
                                                count += 1
                                                handle_style_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                handle_style_item.click()
                                                item_name = handle_style_item.text
                                                count += 1
                                                time.sleep(2)
                                                # print "count is:", count
                                        else:
                                            handle_style_item_name = "None"
                                            # print "Handle style disabled!!!"
                                            frame_material_text = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
                                            if frame_material_text != "Metal":
                                                # print "Shelf material enabled.."
                                                shelf_material_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                shelf_material_tab.click()
                                                count += 1
                                                shelf_material_items = driver.find_elements_by_class_name(
                                                    "more-designs-image")
                                                size_shelf_material = len(shelf_material_items)

                                                for i9 in range(1, size_shelf_material + 1):
                                                    shelf_material_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                    shelf_material_tab.click()
                                                    prop_name = shelf_material_tab.text
                                                    count += 1
                                                    shelf_material_item = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i9)
                                                    shelf_material_item.click()
                                                    item_name = shelf_material_item.text
                                                    count += 1
                                                    time.sleep(2)
                                                    # print "count is:", count
                                            else:
                                                shelf_material_item_name = "None"
                                                # print "Shelf material disabled!!!"
                                                shelf_style_text = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div/a[2]").text
                                                if shelf_style_text != 'None':
                                                    # print "shelf style enabled..."
                                                    shelf_style_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                    shelf_style_tab.click()
                                                    count += 1
                                                    shelf_style_items = driver.find_elements_by_class_name(
                                                        "more-designs-image")
                                                    size_shelf_items = len(shelf_style_items)

                                                    for i10 in range(1, size_shelf_items + 1):
                                                        shelf_style_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                        shelf_style_tab.click()
                                                        prop_name = shelf_style_tab.text

                                                        count += 1
                                                        shelf_style_item = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i10)
                                                        shelf_style_item.click()
                                                        item_name = shelf_style_item.text
                                                        count += 1
                                                        time.sleep(2)
                                                        print "count is:", count
                                                else:
                                                    shelf_style_item_name = 'None'
                                                    # print "shelf style disabled!!!"
                                                    leg_position_text = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div/a[2]").text
                                                    if leg_position_text != 'None':

                                                        # print "Leg position enabled..."
                                                        leg_position_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                        leg_position_tab.click()
                                                        count += 1
                                                        leg_position_items = driver.find_elements_by_class_name(
                                                            "more-designs-image")
                                                        size_leg_position = len(leg_position_items)

                                                        for i11 in range(1, size_leg_position + 1):
                                                            leg_position_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                            leg_position_tab.click()
                                                            prop_name = leg_position_tab.text

                                                            count += 1
                                                            leg_position_item = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i11)
                                                            leg_position_item.click()
                                                            leg_position_item_name = leg_position_item.text
                                                            count += 1
                                                            time.sleep(2)
                                                            # print "count is:", count

                                                            frame_color_text = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                            if frame_color_text != "None":
                                                                # print "frame color enabled..."
                                                                frame_color_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                frame_color_tab.click()
                                                                count += 1
                                                                frame_color_items = driver.find_elements_by_class_name(
                                                                    "more-designs-image")
                                                                size_frame_color = len(frame_color_items)

                                                                for i12 in range(1, size_frame_color + 1):
                                                                    frame_color_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                    frame_color_tab.click()
                                                                    prop_name = frame_color_tab.text
                                                                    count += 1
                                                                    frame_color_item = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                    driver.execute_script("arguments[0].click();",
                                                                                          frame_color_item)
                                                                    frame_color_item_name = frame_color_item.text
                                                                    count += 1
                                                                    time.sleep(2)
                                                                    # print "count is:", count

                                                                    top_color_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                    if top_color_text != 'None':
                                                                        # print "top color enabled..."
                                                                        top_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                        top_color_tab.click()
                                                                        count += 1
                                                                        top_color_items = driver.find_elements_by_class_name(
                                                                            'more-designs-image')
                                                                        size_top_color = len(top_color_items)

                                                                        for i13 in range(1, size_top_color + 1):
                                                                            top_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                            top_color_tab.click()
                                                                            prop_name = top_color_tab.text

                                                                            count += 1
                                                                            top_color_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                            driver.execute_script(
                                                                                "arguments[0].click();", top_color_item)
                                                                            top_color_item_name = top_color_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count

                                                                            handle_color_text = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                            if handle_color_text != 'None':
                                                                                # print 'handle color is enabled...'
                                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                handle_color_tab.click()
                                                                                count += 1
                                                                                handle_color_items = driver.find_elements_by_class_name(
                                                                                    "more-designs-image")
                                                                                size_handle_color = len(
                                                                                    handle_color_items)

                                                                                for i14 in range(1,
                                                                                                 size_handle_color + 1):
                                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                    handle_color_tab.click()
                                                                                    prop_name = handle_color_tab.text

                                                                                    count += 1
                                                                                    handle_color_item = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                    handle_color_item.click()
                                                                                    handle_color_item_name = handle_color_item.text
                                                                                    count += 1
                                                                                    time.sleep(2)
                                                                                    # print "count is:", count

                                                                                    shelf_color_text = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                    if shelf_color_text != 'None':
                                                                                        # print "shelf color tab enabled..."
                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                        shelf_color_tab.click()
                                                                                        count += 1
                                                                                        shelf_color_items = driver.find_elements_by_class_name(
                                                                                            "more-designs-image")
                                                                                        size_shelf_color = len(
                                                                                            shelf_color_items)

                                                                                        for i15 in range(1,
                                                                                                         size_shelf_color + 1):
                                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                            shelf_color_tab.click()
                                                                                            prop_name = shelf_color_tab.text

                                                                                            count += 1
                                                                                            shelf_color_item = driver.find_element_by_xpath(
                                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                            shelf_color_item.click()
                                                                                            shelf_color_item_name = shelf_color_item.text
                                                                                            count += 1
                                                                                            time.sleep(2)
                                                                                            # print "count is:", count

                                                                                    else:
                                                                                        shelf_color_item_name = "None"

                                                                                        # print "shelf color disabled!!!"



                                                                            else:
                                                                                handle_color_item_name = "None"
                                                                                # print "handle color disabled!!!"
                                                                                shelf_color_text = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                                if shelf_color_text != 'None':
                                                                                    # print "shelf color tab enabled..."
                                                                                    shelf_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                    shelf_color_tab.click()
                                                                                    count += 1
                                                                                    shelf_color_items = driver.find_elements_by_class_name(
                                                                                        "more-designs-image")
                                                                                    size_shelf_color = len(
                                                                                        shelf_color_items)

                                                                                    for i15 in range(1,
                                                                                                     size_shelf_color + 1):
                                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                        shelf_color_tab.click()
                                                                                        prop_name = shelf_color_tab.text

                                                                                        count += 1
                                                                                        shelf_color_item = driver.find_element_by_xpath(
                                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                        driver.execute_script(
                                                                                            "arguments[0].click();",
                                                                                            shelf_color_item)
                                                                                        item_name = shelf_color_item.text
                                                                                        count += 1
                                                                                        time.sleep(2)
                                                                                        # print "count is:", count

                                                                                else:
                                                                                    shelf_color_item_name = "None"

                                                                                    # print "shelf color disabled!!!"


                                                                    else:
                                                                        top_color_item_name = "None"
                                                                        # print "top color disabled!!!"
                                                                        handle_color_text = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                        if handle_color_text != 'None':
                                                                            # print 'handle color is enabled...'
                                                                            handle_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                            handle_color_tab.click()
                                                                            count += 1
                                                                            handle_color_items = driver.find_elements_by_class_name(
                                                                                "more-designs-image")
                                                                            size_handle_color = len(
                                                                                handle_color_items)

                                                                            for i14 in range(1,
                                                                                             size_handle_color + 1):
                                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                                handle_color_tab.click()
                                                                                prop_name = handle_color_tab.text
                                                                                count += 1
                                                                                handle_color_item = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                                handle_color_item.click()
                                                                                item_name = handle_color_item.text
                                                                                count += 1
                                                                                time.sleep(2)
                                                                                # print "count is:", count
                                                                        else:
                                                                            handle_color_item_name = "None"
                                                                            # print "Handle color disabled!!!"
                                                                            shelf_color_text = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                            if shelf_color_text != 'None':
                                                                                # print "shelf color tab enabled..."
                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                shelf_color_tab.click()
                                                                                count += 1
                                                                                shelf_color_items = driver.find_elements_by_class_name(
                                                                                    "more-designs-image")
                                                                                size_shelf_color = len(
                                                                                    shelf_color_items)

                                                                                for i15 in range(1,
                                                                                                 size_shelf_color + 1):
                                                                                    shelf_color_tab = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                    shelf_color_tab.click()
                                                                                    prop_name = shelf_color_tab.text
                                                                                    count += 1
                                                                                    shelf_color_item = driver.find_element_by_xpath(
                                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                    driver.execute_script(
                                                                                        "arguments[0].click();",
                                                                                        shelf_color_item)
                                                                                    item_name = shelf_color_item.text
                                                                                    count += 1
                                                                                    time.sleep(2)
                                                                                    # print "count is:", count

                                                                            else:
                                                                                shelf_color_item_name = "None"

                                                                                # print "shelf color disabled!!!"

                                                            else:
                                                                frame_color_item_name = "None"
                                                                # print "frame color disabled!!!"
                                                                top_color_text = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                                if top_color_text != 'None':
                                                                    # print "top color enabled..."
                                                                    top_color_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                    top_color_tab.click()
                                                                    count += 1
                                                                    top_color_items = driver.find_elements_by_class_name(
                                                                        'more-designs-image')
                                                                    size_top_color = len(top_color_items)

                                                                    for i13 in range(1, size_top_color + 1):
                                                                        top_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                        top_color_tab.click()
                                                                        prop_name = top_color_tab.text
                                                                        count += 1
                                                                        top_color_item = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                        driver.execute_script("arguments[0].click();",
                                                                                              top_color_item)
                                                                        item_name = top_color_item.text
                                                                        time.sleep(2)
                                                                        # print "count is:", count
                                                                else:
                                                                    top_color_item_name = "None"
                                                                    # print "top color disabled!!!"
                                                                    handle_color_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                    if handle_color_text != 'None':
                                                                        # print 'handle color is enabled...'
                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                        handle_color_tab.click()
                                                                        count += 1
                                                                        handle_color_items = driver.find_elements_by_class_name(
                                                                            "more-designs-image")
                                                                        size_handle_color = len(
                                                                            handle_color_items)

                                                                        for i14 in range(1,
                                                                                         size_handle_color + 1):
                                                                            handle_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                            handle_color_tab.click()
                                                                            prop_name = handle_color_tab.text
                                                                            count += 1
                                                                            handle_color_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                            handle_color_item.click()
                                                                            item_name = handle_color_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count
                                                                    else:
                                                                        handle_color_item_name = "None"
                                                                        # print "Handle color disabled!!!"
                                                                        shelf_color_text = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                        if shelf_color_text != 'None':
                                                                            # print "shelf color tab enabled..."
                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                            shelf_color_tab.click()
                                                                            count += 1
                                                                            shelf_color_items = driver.find_elements_by_class_name(
                                                                                "more-designs-image")
                                                                            size_shelf_color = len(
                                                                                shelf_color_items)

                                                                            for i15 in range(1,
                                                                                             size_shelf_color + 1):
                                                                                shelf_color_tab = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                                shelf_color_tab.click()
                                                                                prop_name = shelf_color_tab.text
                                                                                count += 1
                                                                                shelf_color_item = driver.find_element_by_xpath(
                                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                                driver.execute_script(
                                                                                    "arguments[0].click();",
                                                                                    shelf_color_item)
                                                                                item_name = shelf_color_item.text
                                                                                count += 1
                                                                                time.sleep(2)
                                                                                # print "count is:", count

                                                                        else:
                                                                            shelf_color_item_name = "None"



                                                    else:
                                                        leg_position_item_name = "None"
                                                        print "leg position disabled!!!"
                                                        frame_color_text = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div/a[2]").text
                                                        if frame_color_text != "None":
                                                            # print "frame color enabled..."
                                                            frame_color_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                            frame_color_tab.click()
                                                            count += 1
                                                            frame_color_items = driver.find_elements_by_class_name(
                                                                "more-designs-image")
                                                            size_frame_color = len(frame_color_items)

                                                            for i12 in range(1, size_frame_color + 1):
                                                                frame_color_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                frame_color_tab.click()
                                                                prop_name = frame_color_tab.text

                                                                count += 1
                                                                frame_color_item = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i12)
                                                                driver.execute_script("arguments[0].click();",
                                                                                      frame_color_item)
                                                                item_name = frame_color_item.text
                                                                count += 1
                                                                time.sleep(2)
                                                                # print "count is:", count
                                                        else:
                                                            frame_color_item_name = "None"
                                                            # print "frame color disabled!!!"
                                                            top_color_text = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div/a[2]").text
                                                            if top_color_text != 'None':
                                                                # print "top color enabled..."
                                                                top_color_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                top_color_tab.click()
                                                                count += 1
                                                                top_color_items = driver.find_elements_by_class_name(
                                                                    'more-designs-image')
                                                                size_top_color = len(top_color_items)

                                                                for i13 in range(1, size_top_color + 1):
                                                                    top_color_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[13]/div")
                                                                    top_color_tab.click()
                                                                    prop_name = top_color_tab.text
                                                                    count += 1
                                                                    top_color_item = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i13)
                                                                    driver.execute_script("arguments[0].click();",
                                                                                          top_color_item)
                                                                    item_name = top_color_item.text
                                                                    count += 1
                                                                    time.sleep(2)
                                                                    # print "count is:", count
                                                            else:
                                                                top_color_item_name = "None"
                                                                # print "top color disabled!!!"
                                                                handle_color_text = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div/a[2]").text
                                                                if handle_color_text != 'None':
                                                                    # print 'handle color is enabled...'
                                                                    handle_color_tab = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                    handle_color_tab.click()
                                                                    count += 1
                                                                    handle_color_items = driver.find_elements_by_class_name(
                                                                        "more-designs-image")
                                                                    size_handle_color = len(
                                                                        handle_color_items)
                                                                    # print "count is:", count

                                                                    for i14 in range(1,
                                                                                     size_handle_color + 1):
                                                                        handle_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[14]/div")
                                                                        handle_color_tab.click()
                                                                        prop_name = handle_color_tab.text

                                                                        count += 1
                                                                        handle_color_item = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                                                                        handle_color_item.click()
                                                                        item_name = handle_color_item.text
                                                                        count += 1
                                                                        time.sleep(2)
                                                                        # print "count is:", count
                                                                else:
                                                                    handle_color_item_name = "None"
                                                                    # print "Handle color disabled!!!"
                                                                    shelf_color_text = driver.find_element_by_xpath(
                                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div/a[2]").text
                                                                    if shelf_color_text != 'None':
                                                                        # print "shelf color tab enabled..."
                                                                        shelf_color_tab = driver.find_element_by_xpath(
                                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                        shelf_color_tab.click()
                                                                        count += 1
                                                                        shelf_color_items = driver.find_elements_by_class_name(
                                                                            "more-designs-image")
                                                                        size_shelf_color = len(
                                                                            shelf_color_items)

                                                                        for i15 in range(1,
                                                                                         size_shelf_color + 1):
                                                                            shelf_color_tab = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[15]/div")
                                                                            shelf_color_tab.click()
                                                                            prop_name = shelf_color_tab.text
                                                                            count += 1
                                                                            shelf_color_item = driver.find_element_by_xpath(
                                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                                                                            driver.execute_script(
                                                                                "arguments[0].click();",
                                                                                shelf_color_item)
                                                                            item_name = shelf_color_item.text
                                                                            count += 1
                                                                            time.sleep(2)
                                                                            # print "count is:", count

                                                                    else:
                                                                        shelf_color_item_name = "None"

                                                                        # print "shelf color disabled!!!"


        except Exception as e:
            print e
            action = ActionChains(driver)
            action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down("k").perform()
            time.sleep(1)
            w = gtk.gdk.get_default_root_window()
            sz = w.get_size()
            # print "The size of the window is %d x %d" % sz
            pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
            pb = pb.get_from_drawable(w, w.get_colormap(), 0, 0, 0, 0, sz[0], sz[1])
            if (pb != None):
                pb.save("test_coffee_table_combi.png", "png")
                print "Screenshot saved ."
            else:
                print "Unable to get the screenshot."



            #has_console_logs = any(map(lambda m: m.find('console log') >= 0, messages))
            #print('Success' if has_console_logs else 'Failure')


            #driver.get_screenshot_as_file("/home/cfit008/PycharmProjects/testNG/coffeetable_combinations.png")

            print "exeption raises when this combination clicked.."
            # print "property is:",prop_name
            # print "item is ",item_name

            print "Size item is:", size_item_name
            print "Frame material item is:", frame_material_item_name
            print "Frame style is:", frame_style_item_name
            print "Top material is:", top_material_item_name
            print "Top style is :", top_style_item_name
            print "Drawer style is:", drawer_style_item_name
            print "Drawer fascia is :", drawer_fascia_item_name
            print "Handle style is:", handle_style_item_name
            print "Shelf material is :", shelf_material_item_name
            print "Shelf style is:", shelf_style_item_name
            print "Leg Position is:", leg_position_item_name
            print "Frame color is:", frame_color_item_name
            print "Top color is:", top_color_item_name
            print "Handle color is:", handle_color_item_name
            print "Shelf color is:", shelf_color_item_name
            raise Exception

        print "final count is:", count

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()
