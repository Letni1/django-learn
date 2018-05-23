from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase
from ..models import Board, Post, Topic
from ..views import topic_posts


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='letniland', description='check123')
        user = User.objects.create_user(username='Checki', email='check@gmail.com', password='check123')
        topic = Topic.objects.create(subject='Hello checking', board=board, starter=user)
        Post.objects.create(message='Checking message', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def teset_view_function(self):
        view = resolve('/boards/1/topics/1')
        self.assertEquals(view.func.view_class, PostListView)
