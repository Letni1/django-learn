from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home, board_topics, new_topic, BoardListView
from ..models import Board, Topic, Post
from django.contrib.auth.models import User
from ..forms import NewTopicForm


class HomeTest(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board")
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topic_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topic_url))

    # def test_board_topics_view_link_back_to_home(self):
    #     board_topic_url = reverse('board_topics', kwargs={'pk': 1})
    #     response = self.client.get(board_topic_url)
    #     homeurl = reverse('home')
    #     self.assertContains(self.response, 'href="{0}"'.format(homeurl))
