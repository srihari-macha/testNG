from selenium import webdriver
import time
from proboscis import test
import unittest
import HTMLTestRunner
import gtk.gdk
import itertools
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


global window_before, window_after, total_price
class test_study_table_combi(unittest.TestCase):


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
    def test_2_study_table(self):
        driver = self.driver
        study_table = driver.find_element_by_xpath(".//*[@id='moreNav']/div[1]/ul/li/ul/li[5]/a")
        time.sleep(2)
        study_table.click()
        try:
            study_table_url = driver.current_url
            if study_table_url == "http://www.customfurnish.com/study-tables/":
                print "Study tables page opened..."
        except:
            print "ERR Study tables page not opened..."
            raise Exception
        time.sleep(2)

    @test
    def test_3_test_drawers_combi(self):
        driver = self.driver
        try:
            prop_list = driver.find_elements_by_class_name("canadel-tab-title")
            print "length of prop_list is:", len(prop_list)

            size_tab = driver.find_element_by_xpath(
                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
            size_tab.click()

            time.sleep(2)
            size_item = driver.find_element_by_xpath(
                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li")
            size_item.click()

            frame_material_tab = driver.find_element_by_xpath(
                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
            frame_material_tab.click()
            frame_material_list = driver.find_elements_by_class_name("more-designs-image")

            def looping():
                leg_position_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                leg_position_tab.click()
                leg_position_list = driver.find_elements_by_class_name("more-designs-image")
                for i14 in range(1, len(leg_position_list) + 1):
                    leg_position_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                    leg_position_tab.click()
                    time.sleep(2)
                    leg_position_item = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i14)
                    leg_position_item.click()
                    time.sleep(1)
                    frame_color_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                    frame_color_tab.click()
                    frame_color_list = driver.find_elements_by_class_name("more-designs-image")

                    for i15 in range(1, len(frame_color_list) + 1):
                        frame_color_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                        frame_color_tab.click()
                        time.sleep(2)
                        frame_color_item = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i15)
                        frame_color_item.click()
                        time.sleep(1)
                        top_color_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                        top_color_tab.click()
                        top_color_list = driver.find_elements_by_class_name("more-designs-image")

                        for i16 in range(1, len(top_color_list) + 1):
                            top_color_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                            top_color_tab.click()
                            time.sleep(2)
                            top_color_item = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i16)
                            top_color_item.click()
                            time.sleep(1)

                pass

            for i1 in range(1, len(frame_material_list) + 1):
                frame_material_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                frame_material_tab.click()
                time.sleep(2)
                frame_material_item = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i1)
                frame_material_item.click()
                time.sleep(1)

                frame_style_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                frame_style_tab.click()
                time.sleep(1)
                frame_style_list = driver.find_elements_by_class_name("more-designs-image")
                print "length of frame style is:", len(frame_style_list)

                for i2 in range(1, len(frame_style_list) - 3):
                    frame_style_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                    frame_style_tab.click()
                    time.sleep(2)
                    frame_style_item = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i2)
                    frame_style_item.click()
                    time.sleep(1)
                    top_material_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                    top_material_tab.click()
                    top_material_list = driver.find_elements_by_class_name("more-designs-image")

                    for i3 in range(1, len(top_material_list) + 1):
                        top_material_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                        top_material_tab.click()
                        time.sleep(2)
                        top_material_item = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i3)
                        top_material_item.click()
                        time.sleep(1)
                        top_material_name = top_material_item.text
                        print "top material is:", top_material_name
                        if top_material_name == "Toughened Glass":
                            top_style_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                            top_style_tab.click()
                            time.sleep(2)
                            top_style_item = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li")
                            top_style_item.click()
                            time.sleep(1)

                            frame_material_name = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
                            if frame_material_name == "Metal":
                                looping()

                            else:
                                looping()




                        else:
                            print "in else case"
                            top_style_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                            top_style_tab.click()
                            time.sleep(2)
                            top_style_list = driver.find_elements_by_class_name("more-designs-image")

                            for i4 in range(1, len(top_style_list) + 1):
                                top_style_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                top_style_tab.click()
                                time.sleep(2)
                                top_style_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i4)
                                top_style_item.click()
                                time.sleep(1)

                                print "in i4 in else case...."

                                # drawer_style_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                drawer_style_name = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div/a[2]").text
                                print "drawer style is :", drawer_style_name

                                if drawer_style_name != "None":
                                    drawer_style_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                    drawer_style_tab.click()
                                    drawer_style_list = driver.find_elements_by_class_name("more-designs-image")
                                    print "length of list is ", len(drawer_style_list)

                                    if len(drawer_style_list) == 1:
                                        drawer_style_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                        drawer_style_tab.click()
                                        time.sleep(2)
                                        drawer_style_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li")
                                        drawer_style_item.click()
                                        time.sleep(1)
                                        looping()


                                    else:
                                        drawer_style_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                        drawer_style_tab.click()
                                        time.sleep(2)
                                        drawer_style_list = driver.find_elements_by_class_name("more-designs-image")

                                        for i5 in range(2, len(drawer_style_list) + 1):
                                            drawer_style_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                            drawer_style_tab.click()
                                            time.sleep(2)
                                            drawer_style_item = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i5)
                                            drawer_style_item.click()
                                            time.sleep(1)
                                            drawer_fascia_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                            drawer_fascia_tab.click()
                                            time.sleep(1)
                                            drawer_fascia_list = driver.find_elements_by_class_name(
                                                "more-designs-image")

                                            for i6 in range(1, len(drawer_fascia_list) + 1):
                                                drawer_fascia_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                                drawer_fascia_tab.click()
                                                time.sleep(2)
                                                drawer_fascia_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i6)
                                                drawer_fascia_item.click()
                                                time.sleep(1)
                                                handle_style_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                handle_style_tab.click()
                                                time.sleep(1)
                                                handle_style_list = driver.find_elements_by_class_name(
                                                    "more-designs-image")

                                                for i7 in range(1, len(handle_style_list) + 1):
                                                    handle_style_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                    handle_style_tab.click()
                                                    time.sleep(2)
                                                    handle_style_item = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                                    handle_style_item.click()
                                                    time.sleep(1)

                                                    leg_position_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                    leg_position_tab.click()
                                                    leg_position_list = driver.find_elements_by_class_name(
                                                        "more-designs-image")
                                                    for i8 in range(1, len(leg_position_list) + 1):
                                                        leg_position_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                        leg_position_tab.click()
                                                        time.sleep(2)
                                                        leg_position_item = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                        leg_position_item.click()
                                                        time.sleep(1)
                                                        frame_color_tab = driver.find_element_by_xpath(
                                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                        frame_color_tab.click()
                                                        frame_color_list = driver.find_elements_by_class_name(
                                                            "more-designs-image")

                                                        for i9 in range(1, len(frame_color_list) + 1):
                                                            frame_color_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[10]/div")
                                                            frame_color_tab.click()
                                                            time.sleep(2)
                                                            frame_color_item = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i9)
                                                            frame_color_item.click()
                                                            time.sleep(1)
                                                            top_color_tab = driver.find_element_by_xpath(
                                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                            top_color_tab.click()
                                                            top_color_list = driver.find_elements_by_class_name(
                                                                "more-designs-image")

                                                            for i10 in range(1, len(top_color_list) + 1):
                                                                top_color_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[11]/div")
                                                                top_color_tab.click()
                                                                time.sleep(2)
                                                                top_color_item = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i10)
                                                                top_color_item.click()
                                                                time.sleep(1)

                                                                handle_color_tab = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[12]/div")
                                                                handle_color_tab.click()
                                                                time.sleep(1)
                                                                handle_color_item = driver.find_element_by_xpath(
                                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li")
                                                                handle_color_item.click()

                                else:
                                    looping()


        except Exception as e:
            print e
            action = ActionChains(driver)
            action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down("k").perform()
            time.sleep(1)
            driver.get_screenshot_as_file("/home/cfit008/PycharmProjects/testNG/test_study_tables_combi.png")
            raise Exception

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()
