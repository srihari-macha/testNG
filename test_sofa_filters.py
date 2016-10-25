from selenium import webdriver
import time
from proboscis import test
import unittest
import HTMLTestRunner
import itertools
import gtk.gdk
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


global sofa_price, window_before, window_after, total_price
class test_sofa_filters(unittest.TestCase):


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
    def test_2_sofaFilters(self):
        driver = self.driver
        sofa = driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[5]/a")
        time.sleep(5)
        sofa.click()
        try:
            sofa_url = driver.current_url
            if sofa_url == "http://www.customfurnish.com/sofa":
                print "sofa page opened..."
        except:
            print "ERR sofa page not opened..."
        time.sleep(2)

    @test
    def test_3_sofaimg(self):
        driver = self.driver
        time.sleep(4)
        sofa_img = driver.find_element_by_xpath(
            ".//*[@id='variant-574e681348773c06df4b1310']/div/div[1]/a/div[2]/section/img")
        sofa_img.click()
        time.sleep(3)

    @test
    def test_4_filters(self):
        driver=self.driver

        color_tab = driver.find_element_by_xpath(".//*[@id='fabric_toolbar']/div[4]/div[1]")
        print "color tab type is:"
        print type(color_tab)
        #color_tab.click()
        time.sleep(1)


        try:
            color_filter = []
            for i in range(3, 13):
                color_filter.append(driver.find_element_by_xpath(
                    "html/body/div[1]/div[5]/div[2]/div[2]/div[2]/div[4]/div[1]/div/ul/li[%d]" % i))

            length_color = len(color_filter)
            #search = driver.find_element_by_xpath(".//*[@id='fabric_toolbar']/div[2]/div[2]/a/img")
            #search.click()
            time.sleep(2)

            print "length is :", length_color

            pattern_link=[]
            for j in range(3,7):
                pattern_link.append(driver.find_element_by_xpath("html/body/div[1]/div[5]/div[2]/div[2]/div[2]/div[4]/div[2]/div/ul/li[%d]" % j))

            length_pattern=len(pattern_link)
            print "length of pattern is:", length_pattern



            for l in range(1, length_color):
                print "iam in search"
                for i in itertools.combinations(color_filter, l):
                    color_tab = driver.find_element_by_xpath(".//*[@id='fabric_toolbar']/div[4]/div[1]")
                    color_tab.click()
                    # i[0].click()
                    # create_list.append(i[0])
                    de_select1 = driver.find_element_by_xpath(
                        "html/body/div[1]/div[5]/div[2]/div[2]/div[2]/div[4]/div[1]/div/ul/li[2]")
                    de_select1.click()
                    #time.sleep(1)
                    for j in range(0, l):
                        i[j].click()
                        color=i[j].text
                        #print "color is:",color
                    time.sleep(2)
                    #print "element clicked..."
                    search = driver.find_element_by_xpath(".//*[@id='fabric_toolbar']/div[2]/div[2]/a/img")
                    search.click()

                    for x in range(1, length_pattern):
                        for y in itertools.combinations(pattern_link, x):
                            pattern_tab=driver.find_element_by_xpath(".//*[@id='fabric_toolbar']/div[4]/div[2]")
                            pattern_tab.click()

                            de_select2=driver.find_element_by_xpath("html/body/div[1]/div[5]/div[2]/div[2]/div[2]/div[4]/div[2]/div/ul/li[2]")
                            de_select2.click()

                            for z in range(0,x):
                                y[z].click()
                                pattern=y[z].text
                                #print "pattern is :",pattern
                            time.sleep(2)
                            search = driver.find_element_by_xpath(".//*[@id='fabric_toolbar']/div[2]/div[2]/a/img")
                            search.click()
                            #print "\n"



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
                pb.save("test_sofa_filters.png", "png")
                print "Screenshot saved ."
            else:
                print "Unable to get the screenshot."

            print "Exception raised when..."
            print "color is:", color
            print "pattern is :", pattern
            print "\n"
            print e
            raise Exception




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()