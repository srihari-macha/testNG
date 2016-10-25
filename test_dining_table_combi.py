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


global table_price, window_before, window_after, total_price
class test_diningTable_combi(unittest.TestCase):


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
    def test_2_dining_table(self):
        driver = self.driver
        table = driver.find_element_by_xpath(".//*[@id='moreNav']/div[1]/ul/li/ul/li[1]/a")
        time.sleep(3)
        table.click()
        try:
            table_url = driver.current_url
            if table_url == "http://www.customfurnish.com/tables/":
                print "Dining table page opened..."
        except:
            print "ERR Dining table page not opened..."
            raise Exception
        time.sleep(2)

    @test
    def test_3_dining_table_comb(self):
        driver=self.driver

        try:

            shape_size=driver.find_elements_by_class_name("more-designs-image")
            #print "size of shape_size is:",len(shape_size)
            #print "\n\n"
            for i1 in range(1, len(shape_size)+1):  # 3
                shape_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
                shape_tab.click()

                shape_type = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i1)
                shape_type.click()
                shape_item_name=shape_type.text
                #print "shape is:",shape_item_name
                time.sleep(2)

                # list_size=driver.find_elements_by_css_selector("more-designs-image ")
                size_tab = driver.find_element_by_xpath(
                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                size_tab.click()
                time.sleep(2)

                list_size = driver.find_elements_by_class_name("more-designs-image")
                size = len(list_size)
                # print type(list_size)
                # print size

                for i2 in range(1, size + 1):
                    size_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
                    size_tab.click()
                    size_type = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i2)
                    driver.execute_script("arguments[0].click();", size_type)
                    size_item_name=size_type.text
                    #print "size is:",size_item_name
                    time.sleep(2)

                    leg_design=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]")
                    class_name=leg_design.get_attribute("class")

                    #print "class name is :",class_name
                    try:
                        if class_name=="ng-scope toolbar-option-disabled":
                            #print "leg design disabled!!!"
                            leg_design_item_name="None"

                            pedestal_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                            pedestal_tab.click()
                            pedestal_items_size = driver.find_elements_by_class_name("more-designs-image")
                            pedestal_size = len(pedestal_items_size)

                            for i4 in range(1, pedestal_size + 1):
                                pedestal_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                                pedestal_tab.click()
                                pedestal_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i4)
                                pedestal_item.click()
                                pedestal_design_item_name=pedestal_item.text
                                #print "Pedestal design:",pedestal_design_item_name

                                time.sleep(2)

                                top_material_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                top_material_tab.click()
                                top_material_size = driver.find_elements_by_class_name("more-designs-image")
                                top_size = len(top_material_size)

                                for i5 in range(1, top_size + 1):
                                    top_material_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                    top_material_tab.click()
                                    top_item = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i5)
                                    top_item.click()
                                    top_material_item_name=top_item.text
                                    #print "top material is:",top_material_item_name

                                    time.sleep(2)

                                    top_color_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                    top_color_tab.click()
                                    top_color_size = driver.find_elements_by_class_name("more-designs-image")
                                    color_size = len(top_color_size)

                                    for i6 in range(1, color_size + 1):
                                        top_color_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                        top_color_tab.click()
                                        color_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i6)
                                        driver.execute_script("arguments[0].click();", color_item)
                                        top_color_item_name=color_item.text
                                        #print "Top color is :",top_color_item_name

                                        time.sleep(2)

                                        leg_material_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                        leg_material_tab.click()
                                        leg_material_size = driver.find_elements_by_class_name("more-designs-image")
                                        material_size = len(leg_material_size)

                                        for i7 in range(1, material_size + 1):
                                            leg_material_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                            leg_material_tab.click()
                                            material_item = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                            material_item.click()
                                            leg_material_item_name=material_item.text
                                            #print "Leg material is:",leg_material_item_name

                                            time.sleep(2)

                                            leg_color_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                            leg_color_tab.click()
                                            leg_color_size = driver.find_elements_by_class_name("more-designs-image")
                                            new_color_size = len(leg_color_size)

                                            for i8 in range(1, new_color_size + 1):
                                                leg_color_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                leg_color_tab.click()
                                                leg_color_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                driver.execute_script("arguments[0].click();", leg_color_item)
                                                leg_color_item_name=leg_color_item.text
                                                #print "Leg color is:",leg_color_item_name
                                                time.sleep(2)


                        ped_design=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]")
                        class_name=ped_design.get_attribute("class")
                        #print "class name is:",class_name

                        if class_name=="ng-scope toolbar-option-disabled":
                            #print "\n\n"
                            #print "pedestal design is disabled..."
                            pedestal_design_item_name="None"
                            #print "i1 val is:", i1

                            # print "pedestal design disabled!!!"
                            leg_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                            leg_tab.click()
                            leg_items_size = driver.find_elements_by_class_name("more-designs-image")
                            leg_size = len(leg_items_size)

                            for i3 in range(1, leg_size + 1):
                                leg_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                                leg_tab.click()
                                leg_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i3)
                                driver.execute_script("arguments[0].click();", leg_item)
                                leg_design_item_name=leg_item.text
                                #print "Leg design is:",leg_design_item_name
                                time.sleep(2)

                                top_material_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                top_material_tab.click()
                                top_material_size = driver.find_elements_by_class_name("more-designs-image")
                                top_size = len(top_material_size)

                                for i5 in range(1, top_size + 1):
                                    top_material_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                    top_material_tab.click()
                                    top_item = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i5)
                                    top_item.click()
                                    top_material_item_name=top_item.text
                                    #print "Top material is:",top_material_item_name


                                    time.sleep(2)

                                    top_color_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                    top_color_tab.click()
                                    top_color_size = driver.find_elements_by_class_name("more-designs-image")
                                    color_size = len(top_color_size)

                                    for i6 in range(1, color_size + 1):
                                        top_color_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                        top_color_tab.click()
                                        color_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i6)
                                        driver.execute_script("arguments[0].click();", color_item)
                                        top_color_item_name=color_item.text
                                        #print "Top color is",top_color_item_name


                                        time.sleep(2)

                                        leg_material_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                        leg_material_tab.click()
                                        leg_material_size = driver.find_elements_by_class_name("more-designs-image")
                                        material_size = len(leg_material_size)

                                        for i7 in range(1, material_size + 1):
                                            leg_material_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                            leg_material_tab.click()
                                            material_item = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                            material_item.click()
                                            leg_material_item_name=material_item.text
                                            #print "leg material is:",leg_material_item_name

                                            time.sleep(2)

                                            leg_color_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                            leg_color_tab.click()
                                            leg_color_size = driver.find_elements_by_class_name("more-designs-image")
                                            new_color_size = len(leg_color_size)

                                            for i8 in range(1, new_color_size + 1):
                                                leg_color_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                leg_color_tab.click()
                                                leg_color_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                driver.execute_script("arguments[0].click();", leg_color_item)
                                                leg_color_item_name=leg_color_item.text
                                                #print "Leg color is:",leg_color_item_name

                                                time.sleep(2)
                                                leg_color_text = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                                #print "Leg color is", leg_color_text

                        ped_design = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]")
                        class_name = ped_design.get_attribute("class")
                        if class_name!="ng-scope toolbar-option-disabled":

                            leg_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                            leg_tab.click()
                            leg_items_size = driver.find_elements_by_class_name("more-designs-image")
                            leg_size = len(leg_items_size)

                            for i3 in range(1, leg_size + 1):
                                leg_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                                leg_tab.click()
                                leg_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i3)
                                driver.execute_script("arguments[0].click();", leg_item)
                                leg_design_item_name=leg_item.text
                                #print "Leg design is:",leg_design_item_name

                                time.sleep(2)

                                top_material_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                top_material_tab.click()
                                top_material_size = driver.find_elements_by_class_name("more-designs-image")
                                top_size = len(top_material_size)

                                pedestal_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                                pedestal_tab.click()
                                pedestal_items_size = driver.find_elements_by_class_name("more-designs-image")
                                pedestal_size = len(pedestal_items_size)

                                for i4 in range(1, pedestal_size + 1):
                                    pedestal_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                                    pedestal_tab.click()
                                    pedestal_item = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i4)
                                    pedestal_item.click()
                                    pedestal_design_item_name=pedestal_item.text
                                    #print "pedestal design is:",pedestal_design_item_name


                                    time.sleep(2)

                                    top_material_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                    top_material_tab.click()
                                    top_material_size = driver.find_elements_by_class_name("more-designs-image")
                                    top_size = len(top_material_size)

                                    for i5 in range(1, top_size + 1):
                                        top_material_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                                        top_material_tab.click()
                                        top_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i5)
                                        top_item.click()
                                        top_material_item_name=top_item.text
                                        #print "Top material is:",top_material_item_name


                                        time.sleep(2)

                                        top_color_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                        top_color_tab.click()
                                        top_color_size = driver.find_elements_by_class_name("more-designs-image")
                                        color_size = len(top_color_size)

                                        for i6 in range(1, color_size + 1):
                                            top_color_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                            top_color_tab.click()
                                            color_item = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i6)
                                            driver.execute_script("arguments[0].click();", color_item)
                                            top_color_item_name=color_item.text
                                            #print "Top color is:",top_color_item_name


                                            time.sleep(2)

                                            leg_material_tab = driver.find_element_by_xpath(
                                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                            leg_material_tab.click()
                                            leg_material_size = driver.find_elements_by_class_name("more-designs-image")
                                            material_size = len(leg_material_size)

                                            for i7 in range(1, material_size + 1):
                                                leg_material_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                                leg_material_tab.click()
                                                material_item = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i7)
                                                material_item.click()
                                                leg_material_item_name=material_item.text
                                                #print "Leg material is:",leg_material_item_name


                                                time.sleep(2)

                                                leg_color_tab = driver.find_element_by_xpath(
                                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                leg_color_tab.click()
                                                leg_color_size = driver.find_elements_by_class_name(
                                                    "more-designs-image")
                                                new_color_size = len(leg_color_size)

                                                for i8 in range(1, new_color_size + 1):
                                                    leg_color_tab = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                                    leg_color_tab.click()
                                                    leg_color_item = driver.find_element_by_xpath(
                                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i8)
                                                    driver.execute_script("arguments[0].click();", leg_color_item)
                                                    leg_color_item_name=leg_color_item.text
                                                    #print "Leg color is:",leg_color_item_name

                                                    time.sleep(2)


                    except Exception as e:
                        print " In exception in i1"


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
                pb.save("test_dining_table_combi.png", "png")
                print "Screenshot saved ."
            else:
                print "Unable to get the screenshot."
            print "Exception occured with this combination"
            print "Shape is:",shape_item_name
            print "size is:",size_item_name
            print "Leg Dsign is:",leg_design_item_name
            print "Pedestal Design is:",pedestal_design_item_name
            print "Top material is:",top_material_item_name
            print "Top color is:",top_color_item_name
            print "Leg material is:",leg_material_item_name
            print "Leg color is:",leg_color_item_name


            print e
            raise Exception


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()