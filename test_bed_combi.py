from selenium import webdriver
import gtk.gdk
import time
from proboscis import test
import unittest
import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global bed_table_price, window_before, window_after, total_price
class test_bed(unittest.TestCase):


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
        time.sleep(3)

    @test
    def test_2_bed(self):
        driver = self.driver
        bed = driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[6]/a")
        time.sleep(2)
        bed.click()
        try:
            bed_url = driver.current_url
            if bed_url == "http://www.customfurnish.com/beds-online/":
                print "Beds page opened..."
        except:
            print "ERR Beds page not opened..."
            raise Exception
        time.sleep(2)

    @test
    def test_3_bed_combinations(self):
        driver = self.driver
        try:
            #action = ActionChains(driver)
            #action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down("k").perform()

            beds_prop = []
            beds_prop.append(driver.find_elements_by_class_name("canadel-tab-title"))
            # print "beds prop is:",beds_prop
            # list_prop=[]
            # for i in range(1,10):
            #    list_prop.append(driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[%d]/div" % i))
            category_tab = driver.find_element_by_xpath(
                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
            category_tab.click()
            list_prop = driver.find_elements_by_class_name("more-designs-image")

            for i1 in range(1, len(list_prop) + 1):
                category_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
                category_tab.click()
                print "property name is:",category_tab.text
                time.sleep(2)
                category_items = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i1)
                category_items.click()
                print "item name is:",category_items.text
                time.sleep(2)
                size_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                size_tab.click()
                time.sleep(1)
                length_size = driver.find_elements_by_class_name("more-designs-image")
                for i2 in range(1, len(length_size) + 1):
                    size_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                    size_tab.click()
                    print "property name is:",size_tab.text
                    time.sleep(2)
                    size_item = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i2)
                    size_item.click()
                    print "Item name is:",size_item.text
                    time.sleep(2)
                    head_board_style_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                    head_board_style_tab.click()
                    time.sleep(1)
                    length_head_board_style = driver.find_elements_by_class_name("more-designs-image")

                    for i3 in range(1, len(length_head_board_style) +1):
                        head_board_style_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                        head_board_style_tab.click()
                        print "property name is:",head_board_style_tab.text
                        head_board_style_item = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i3)
                        driver.execute_script("arguments[0].click();", head_board_style_item)
                        print "item name is:",head_board_style_item.text
                        time.sleep(2)
                        foot_board_style_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                        foot_board_style_tab.click()
                        time.sleep(1)
                        length_foot_board_style = driver.find_elements_by_class_name("more-designs-image")

                        for i4 in range(1, len(length_foot_board_style) + 1):
                            foot_board_style_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                            foot_board_style_tab.click()
                            print "property name is:",foot_board_style_tab.text
                            time.sleep(1)
                            foot_board_style_item = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i4)
                            foot_board_style_item.click()
                            print "item name is:",foot_board_style_item.text
                            time.sleep(2)
                            storage_style_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                            storage_style_tab.click()
                            time.sleep(1)
                            length_storage_style = driver.find_elements_by_class_name("more-designs-image")

                            for i5 in range(1, len(length_storage_style) + 1):
                                storage_style_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                storage_style_tab.click()
                                print "property name is:",storage_style_tab.text
                                time.sleep(1)
                                storage_style_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i5)
                                storage_style_item.click()
                                print "item name is:",storage_style_item.text
                                time.sleep(2)
                                head_board_material_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                head_board_material_tab.click()
                                time.sleep(1)
                                length_head_board_material = driver.find_elements_by_class_name("more-designs-image")

                                for i6 in range(1, len(length_head_board_material) + 1):
                                    head_board_material_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                    head_board_material_tab.click()
                                    print "property name is:",head_board_material_tab.text
                                    time.sleep(1)
                                    head_board_material_item = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i6)
                                    head_board_material_item.click()
                                    print "item name is:",head_board_material_item.text
                                    time.sleep(2)
                                    head_board_color_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                    head_board_color_tab.click()
                                    time.sleep(1)
                                    length_head_board_color = driver.find_elements_by_class_name("more-designs-image")

                                    for i7 in range(1, len(length_head_board_color) +1):
                                        head_board_color_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                        head_board_color_tab.click()
                                        print "property name is:",head_board_color_tab.text
                                        time.sleep(1)
                                        head_board_color_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                        driver.execute_script("arguments[0].click();", head_board_color_item)
                                        print "item name is:",head_board_color_item.text
                                        time.sleep(2)
                                        frame_material_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                        frame_material_tab.click()
                                        time.sleep(1)
                                        length_frame_material = driver.find_elements_by_class_name("more-designs-image")

                                        for i8 in range(1, len(length_frame_material)+1):
                                            frame_material_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                            frame_material_tab.click()
                                            print "property name is:",frame_material_tab.text
                                            time.sleep(1)
                                            frame_material_item = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                            frame_material_item.click()
                                            print "item name is:",frame_material_item.text
                                            time.sleep(1)
                                            frame_color_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                            frame_color_tab.click()
                                            time.sleep(1)
                                            length_frame_color = driver.find_elements_by_class_name(
                                                "more-designs-image")
                                            print "frame color length is:", len(length_frame_color)

                                            for i9 in range(1, len(length_frame_color) +1):
                                                frame_color_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[9]/div")
                                                frame_color_tab.click()
                                                print "property name is:",frame_color_tab.text
                                                time.sleep(1)
                                                frame_color_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i9)
                                                driver.execute_script("arguments[0].click();", frame_color_item)
                                                print "item name is:", frame_color_item.text
                                                time.sleep(2)


        except Exception as e:
            action = ActionChains(driver)
            action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down("k").perform()
            print "Exception occured with this combination."
            print e
            time.sleep(1)
            w = gtk.gdk.get_default_root_window()
            sz = w.get_size()
            #print "The size of the window is %d x %d" % sz
            pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
            pb = pb.get_from_drawable(w, w.get_colormap(), 0, 0, 0, 0, sz[0], sz[1])
            if (pb != None):
                pb.save("test_bed_combi.png", "png")
                print "Screenshot saved ."
            else:
                print "Unable to get the screenshot."
            raise Exception


    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass


if __name__ == '__main__':
    HTMLTestRunner.main()



