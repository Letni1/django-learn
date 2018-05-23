# from django.urls import reverse, resolve
# from django.test import TestCase
# from ..views import home, board_topics, new_topic
# from ..models import Board, Topic, Post
# from django.contrib.auth.models import User
# from ..forms import NewTopicForm
#
#
# class BoardTest(TestCase):
#     def setUp(self):
#         Board.objects.create(name='Django', description='Django board.')
#
#     # def test_board_topics_view_success_status_code(self):
#     #     url = reverse('board_topics', kwargs={'pk': 1})
#     #     response = self.client.get(url)
#     #     self.assertEquals(response.status_code, 200)
#
#     def test_board_topics_not_found_status_code(self):
#         url = reverse('board_topics', kwargs={'pk': 99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)
#
#     def test_board_topics_url_resolves_board_topics_view(self):
#         view = resolve('/board/1/')
#         self.assertEquals(view.func.view_class, board_topics)
#
#
# class BoardTopicsTests(TestCase):
#     def test_board_topics_contains_navigation_link(self):
#         board_topic_url = reverse('board_topics', kwargs={'pk': 1})
#         homepage_url = reverse('home')
#         new_topic_url = reverse('new_topic', kwargs={'pk': 1})
#
#         response = self.client.get(board_topic_url)
#
#         self.assertContains(response, 'href="{0}"'.format(homepage_url))
#         self.assertContains(response, 'href="{0}"'.format(new_topic_url))
