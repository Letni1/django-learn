from django.urls import reverse, resolve
from django.test import TestCase
from ..views import reply_topic
from ..models import Board, Topic, Post
from django.contrib.auth.models import User


class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all `reply_topic` view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='Letniland', description='Check')
        self.username = 'Check'
        self.password = 'check123'
        user = User.objects.create_user(username=self.username, email='check@gmail.com', password=self.password)
        self.topic = Topic.objects.create(subject='CHekc', board=self.board, starter=user)
        Post.objects.create(message='checking', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})

class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        topic_posts_url = '{url}?page=1#2'.format(url=url)
        self.assertRedirects(self.response, topic_posts_url)
