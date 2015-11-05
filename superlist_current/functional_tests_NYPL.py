from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class testcase1_search(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.close()

	def test_search_org(self):
		self.browser.get('http://catalog.nypl.org/search')
		search_box = self.browser.find_element_by_name("searcharg")
		assert search_box != None
		search_box.send_keys('visualization')
		search_box.send_keys(Keys.ENTER)
		self.browser.implicitly_wait(3)
		#Browser should shows the results of visualization
		results = self.browser.find_elements_by_class_name("browseSearchtoolMessage")
		div = results[0]
		res = div.find_elements_by_tag_name("i")
		resCount = res[0].get_attribute('innerHTML')
		resCount = resCount[:-15]
		resCount = resCount.rstrip(" ")
		print("Results Count in http://catalog.nypl.org/search: " + resCount)


		self.browser.get('http://browse.nypl.org/iii/encore/?lang=eng')
		search_box = self.browser.find_element_by_id("searchString")
		assert search_box != None
		search_box.send_keys('visualization')
		search_box.send_keys(Keys.ENTER)
		self.browser.implicitly_wait(3)
		results1 = self.browser.find_elements_by_class_name("noResultsHideMessage")
		span = results1[0]
		resCount1 = span.get_attribute('innerHTML')
		print("Results Count in http://browse.nypl.org/iii/encore/?lang=eng: " + resCount1)
		assert resCount in resCount1
		print('=================Finish the test1!=================')


class testcase2_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase2: test if both websites can return correct result")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("software")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		result1 = driver.find_elements_by_class_name("browseSearchtoolMessage")
		div = result1[0]
		res1 = div.find_elements_by_tag_name("i")
		count1 = res1[0].get_attribute("innerHTML")
		count1 = count1[:-15]
		self.assertNotEqual(count1,'0')
	
		
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		searchBox = driver.find_element_by_id("searchString")
		searchBox.send_keys("software")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		result2 = driver.find_elements_by_class_name("noResultsHideMessage")
		div2 = result2[0]
		count2 = div2.get_attribute("innerHTML")
		self.assertNotEqual(count1,'0')
		print('=================Finish the test2!=================')

class testcase3_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase3: test if both websites can handle invalid keyword")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("!@__T")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		div1 = driver.find_element_by_id("rightSideCont")
		h2 = div1.find_element_by_tag_name("h2")
		result1 = h2.get_attribute("innerHTML")
		assert "NO" in result1
		assert "FOUND" in result1

		
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		searchBox = driver.find_element_by_id("searchString")
		searchBox.send_keys("!@__T")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		span2 = driver.find_element_by_class_name("noResultsMessage")
		result2 = span2.get_attribute("innerHTML")
		assert "No" in result2
		assert "found" in result2
		print('=================Finish the test3!=================')

class testcase4_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase4: test ISBN/ISSN search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'ISBN/ISSN'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("sass")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'ISBN/ISSN'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("978-3-16-148410-0")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tds = driver.find_elements_by_class_name("bibInfoData")
		td = tds[1]
		strong = td.find_element_by_tag_name("strong")
		result2 = strong.get_attribute("innerHTML")
		assert "Culturas ecuatorianas" in result2
		print("            test ISN: 978-3-16-148410-0, catelog.nypl.org result: " + result2)

		#search valid ISN in browse.nypl.org
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		searchBox = driver.find_element_by_id("searchString")
		searchBox.send_keys("978-3-16-148410-0")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		link = driver.find_element_by_id("recordDisplayLink2Component")
		result3 = link.get_attribute("innerHTML")
		assert "Culturas ecuatorianas" in result3
		print("            test ISN: 978-3-16-148410-0, browse.nypl.org result: " + result3)
		print('=================Finish the test4!=================')



class testcase5_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase6: test Call Number search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Call Number'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("sass")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Call Number'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("33433082849914")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tds = driver.find_elements_by_class_name("bibInfoData")
		td = tds[1]
		strong = td.find_element_by_tag_name("strong")
		result2 = strong.get_attribute("innerHTML")
		assert "La nuit" in result2
		print("            test Call Number: 33433082849914, catelog.nypl.org result: " + result2)

		#search valid ISN in browse.nypl.org
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		searchBox = driver.find_element_by_id("searchString")
		searchBox.send_keys("33433082849914")
		searchBox.send_keys(Keys.RETURN)
		link = driver.find_element_by_id("recordDisplayLink2Component")
		result3 = link.get_attribute("innerHTML")
		assert "La nuit" in result3
		print("            test Call Number: 33433082849914, browse.nypl.org result: " + result3)
		print('=================Finish the test5!=================')
		
class testcase6_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase6: test Author search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Author'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("!24444   *")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Author'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("Agatha Christie")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tds = driver.find_elements_by_class_name("browseHeaderData")
		result2 = tds[0].get_attribute("innerHTML")
		print("            test Author: Agatha Christie, catelog.nypl.org result: " + result2)

		#search valid ISN in browse.nypl.org
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		search_box = driver.find_element_by_id("searchString")
		assert search_box != None
		search_box.send_keys('Agatha Christie')
		search_box.send_keys(Keys.ENTER)
		driver.implicitly_wait(3)
		results1 = driver.find_elements_by_class_name("noResultsHideMessage")
		span = results1[0]
		resCount1 = span.get_attribute('innerHTML')
		print("Results Count in http://browse.nypl.org/iii/encore/?lang=eng: " + resCount1)
		self.assertNotEqual(result2,resCount1)
		print('Result count with Author: Agatha Christie are not the same!')
		print('=================Finish the test6!=================')	

class testcase7_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase7: test Title search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Title'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("!24444  @ *")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Title'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("world of warcraft")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tds = driver.find_elements_by_class_name("browseHeaderData")
		result2 = tds[0].get_attribute("innerHTML")
		print("            test Title: world of warcraft, catelog.nypl.org result: " + result2)

		#search valid ISN in browse.nypl.org
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		search_box = driver.find_element_by_id("searchString")
		assert search_box != None
		search_box.send_keys('world of warcraft')
		search_box.send_keys(Keys.ENTER)
		driver.implicitly_wait(3)
		results1 = driver.find_elements_by_class_name("noResultsHideMessage")
		span = results1[0]
		resCount1 = span.get_attribute('innerHTML')
		print("Results Count in http://browse.nypl.org/iii/encore/?lang=eng: " + resCount1)
		self.assertNotEqual(result2,resCount1)
		print('=================Finish the test7!=================')	

class testcase8_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase8: test Subject search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Subject'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("!24444  @ *")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Subject'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("world of warcraft")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tds = driver.find_elements_by_class_name("browseHeaderData")
		result2 = tds[0].get_attribute("innerHTML")
		print("            test Subject : world of warcraft, catelog.nypl.org result: " + result2)

		#search valid ISN in browse.nypl.org
		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		search_box = driver.find_element_by_id("searchString")
		assert search_box != None
		search_box.send_keys('world of warcraft')
		search_box.send_keys(Keys.ENTER)
		driver.implicitly_wait(3)
		results1 = driver.find_elements_by_class_name("noResultsHideMessage")
		span = results1[0]
		resCount1 = span.get_attribute('innerHTML')
		print("Results Count in http://browse.nypl.org/iii/encore/?lang=eng: " + resCount1)
		self.assertNotEqual(result2,resCount1)
		print('=================Finish the test8!=================')


class testcase9_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase9: test Genre search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Genre'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("!24444  @ *")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Genre'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("world of warcraft")
		searchBox.send_keys(Keys.RETURN)
		driver.implicitly_wait(3)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result
		print('=================Finish the test9!=================')

class testcase10_search(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	def tearDown(self):
		self.driver.close()
	
	def test_search_org(self):
		print("Testcase10: test Journal Title search with valid and invalid keywords")
		driver = self.driver
		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Genre'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search invalid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("!24444  @ *")
		searchBox.send_keys(Keys.RETURN)
		tr = driver.find_element_by_class_name("msg")
		td = tr.find_element_by_tag_name("td")
		result = td.get_attribute("innerHTML")
		assert "No" in result
		assert "found" in result

		driver.get("http://catalog.nypl.org/")
		el = driver.find_element_by_id("searchtype")
		label = 'Journal Title'
		for option in el.find_elements_by_tag_name("option"):
			if label in option.text:
				option.click()

		#search valid ISN
		searchBox = driver.find_element_by_name("searcharg")
		searchBox.send_keys("IEEE")
		searchBox.send_keys(Keys.RETURN)
		tds = driver.find_elements_by_class_name("browseHeaderData")
		result2 = tds[0].get_attribute("innerHTML")
		print("            test Journal Title : IEEE, catelog.nypl.org result: " + result2)


		driver.get("http://browse.nypl.org/iii/encore/?lang=eng")
		search_box = driver.find_element_by_id("searchString")
		assert search_box != None
		search_box.send_keys('IEEE')
		search_box.send_keys(Keys.ENTER)
		results1 = driver.find_elements_by_class_name("noResultsHideMessage")
		span = results1[0]
		resCount1 = span.get_attribute('innerHTML')
		print("Results Count in http://browse.nypl.org/iii/encore/?lang=eng: " + resCount1)
		self.assertNotEqual(result2,resCount1)	
		print('=================Finish the test10!=================')

if __name__ == '__main__':
	unittest.main(warnings= 'ignore')