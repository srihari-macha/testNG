from selenium import webdriver
import time
from proboscis import test
import unittest
import HTMLTestRunner
import gtk.gdk
from selenium.webdriver.common.action_chains import ActionChains
import itertools
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


global chairs_price, window_before, window_after, total_price
class test_diningChairs_combi(unittest.TestCase):


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
    def test_2_chairs(self):
        driver = self.driver
        chairs = driver.find_element_by_xpath(".//*[@id='moreNav']/div[1]/ul/li/ul/li[2]/a")
        time.sleep(3)
        chairs.click()
        try:
            chairs_url = driver.current_url
            if chairs_url == "http://www.customfurnish.com/chairs/":
                print "Chairs page opened..."
        except:
            print "ERR chairs page not opened..."
        time.sleep(2)

    @test
    def test_3_dining_chairs_comb(self):
        driver = self.driver

        try:
            for i in range(1,24):
                frame_style = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
                frame_style.click()
                time.sleep(2)
                frame_style_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" %i)
                #frame_style_item.click()
                driver.execute_script("arguments[0].click();",frame_style_item)
                frame_style_item_name=frame_style_item.text
                time.sleep(2)

                for j in range(1,4):
                    frame_material=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                    frame_material.click()
                    time.sleep(2)
                    frame_material_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" %j)
                    frame_material_item.click()
                    frame_material_item_name=frame_material_item.text
                    time.sleep(2)

                    for k in range(1,13):
                        frame_color=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                        frame_color.click()
                        time.sleep(2)
                        frame_color_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" %k)
                        #frame_color_item.click()
                        driver.execute_script("arguments[0].click();", frame_color_item)
                        frame_color_item_name=frame_color_item.text
                        time.sleep(2)

                        for l in range(1,59):
                            fabric=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                            fabric.click()
                            time.sleep(2)
                            fabric_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" %l)
                            #fabric.click()
                            driver.execute_script("arguments[0].click();", fabric_item)
                            fabric_item_name=fabric_item.text
                            time.sleep(2)

        except Exception as e:
            action = ActionChains(driver)
            action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down("k").perform()
            time.sleep(1)
            w = gtk.gdk.get_default_root_window()
            sz = w.get_size()
            # print "The size of the window is %d x %d" % sz
            pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
            pb = pb.get_from_drawable(w, w.get_colormap(), 0, 0, 0, 0, sz[0], sz[1])
            if (pb != None):
                pb.save("test_dining_chairs_combi.png", "png")
                print "Screenshot saved ."
            else:
                print "Unable to get the screenshot."

            print " Exception occured with this combination..."
            print "Frame style is:",frame_style_item_name
            print "Frame material is:",frame_material_item_name
            print "Frame color is:",frame_color_item_name
            print "fabric is:",fabric_item_name
            print e
            raise Exception

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()

