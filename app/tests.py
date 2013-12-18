from django.test import TestCase
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from app.models import Articles
from datetime import datetime


class ArticleModelTest(TestCase):

    def test_creating_a_new_article(self):
        article = Articles(title="This is title", body="This is body", slug="this is slug", created=datetime.now())
        article.save()

        articles_in_database = Articles.objects.all()
        self.assertEqual(len(articles_in_database), 1)
        only_article_in_database = articles_in_database[0]
        self.assertEqual(only_article_in_database, article)

        self.assertEqual(only_article_in_database.title, "This is title")
        self.assertEqual(only_article_in_database.body, "This is body")

    def test_admin_url_test(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)


class ArticleAdminTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)
        super().setUpClass()

        User.objects.create_superuser(username='admin', email='admin@gmail.com', password='admin')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_can_create_new_articles(self):
        self.browser.get(self.live_server_url + '/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.submit()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        article_links = self.browser.find_elements_by_link_text('Articless')
        self.assertEqual(len(article_links), 1)

        self.browser.get(self.live_server_url + '/admin/app/articles/add')
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('This is New Title Post')

        body_field = self.browser.find_element_by_name('body')
        body_field.send_keys('This is body')
        body_field.send_keys(Keys.ENTER)

    def test_for_index_view(self):
        self.browser.get(self.live_server_url + '/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Articles', body.text)