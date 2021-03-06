from selenium import webdriver
from .base import TodoFunctionalTest

class NewVisitorTest(TodoFunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get(self.live_server_url)

        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        self.enter_a_new_item('Buy peacock feathers')
        edith_list_url = self.browser.current_url

        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('Buy peacock feathers')

        self.enter_a_new_item('Use peacock feathers to make a fly')

        self.check_for_row_in_list_table('Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make a fly')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        ##TODO - Fix this test, when we have real user accounts 
        page_text = self.browser.find_element_by_tag_name('body').text

        # self.assertNotIn('Buy peacock feathers', page_text)
        # self.assertNotIn('make a fly', page_text)

        self.enter_a_new_item('Buy milk')
        francis_list_url = self.browser.current_url

        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
