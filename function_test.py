from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3);

	#def tearDown(self):
		#self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])


	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
        # to check out its homepag
		self.browser.get('http://www.advanced-online.com/custom/build_frameset_for_dotNetEntry.asp?company=HAB&dNTC=HAB6&pway=Password&wide=1')
		# She notices the page title and header mention to-do lists
		iframe = self.browser.find_element_by_tag_name("iframe")
		src = iframe.get_attribute("src")
		#self.browser.get(src)
		self.browser.switch_to_frame(iframe)
		framesets = self.browser.find_elements_by_tag_name("frameset")
		n = 0
		newframe = None
		for item in framesets:
			if n == 1:
				newframe = item
				break
			n = n + 1
		assert newframe != None
		frames = newframe.find_elements_by_tag_name("frame")

		n = 0
		target_frame = None
		for item in frames:
			if n == 0:
				target_frame = item
				break;
		assert target_frame != None
		self.browser.switch_to_frame(target_frame)
		#self.browser.switch_to_default_content()
		#originframesets = self.browser.find_elements_by_tag_name("frameset")
		#src = target_frame.get_attribute("src")
		#self.browser.get(src)

		#self.browser.switch_to_frame(iframe)
		#frameset = self.browser.find_element_by_tag_name("frameset")
		#newframe = frameset.find_element_by_tag_name("framset")
		#target_frame = newframe.find_element_by_tag_name("frameset")

		#frame = self.browser.find_element_by_tag_name("frame")

		#self.browser.switch_to_frame(frame)
		#frameset = self.browser.find_element_by_tag_name("framest")
		#frame = frameset.find_element_by_tag_name("frame")
		search_box = self.browser.find_element_by_id("Text1")
		assert search_box != None
		self.browser.implicitly_wait(4)
		search_box.send_keys("aa@bb.com")
		search_box.send_keys(Keys.RETURN)
		self.browser.switch_to_default_content()
		iframe = self.browser.find_element_by_tag_name("iframe")
		assert iframe != None
		self.browser.switch_to_frame(iframe)
		framesets = self.browser.find_elements_by_tag_name("frameset")
		assert framesets != None
		n = 0
		newframe = None
		for item in framesets:
			if n == 1:
				newframe = item
				break
			n = n + 1
		assert newframe != None
		frames = newframe.find_elements_by_tag_name("frame")




		


		

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings= 'ignore')