from .base import TodoFunctionalTest
from selenium import webdriver

class DeleteItem(TodoFunctionalTest):
    def delete_item(self,todo_text):
        row = self.find_table_row(todo_text)
        self.browser.find_element_by_tag_name('a').click()

    def test_can_delete_items(self):
        #Edith saved items to her list
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Buy peacock feathers')
        self.enter_a_new_item('Buy milk')

        #Edith wants to delete item and clicked on the delete
        self.delete_item('Buy peacock feathers')

        #Edith saw that the list updated and the item goes away.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Buy milk', page_text)
        self.assertNotIn('Buy peacock feathers', page_text)
