# from django.core import mail
# from django.urls import reverse, resolve
# from django.test import TestCase
# from django.contrib.auth.models import User
#
#
# class PasswordResetMailTests(TestCase):
#     def setUp(self):
#         User.objects.create_user(username='Max', email='check@check.com', password='check123')
#         self.response = self.client.post(reverse('password_reset'), {'email': 'check@check.com'})
#         self.email = mail.outbox[0]
#
#     def test_email_subject(self):
#         self.assertEquals('[Letniland] Please reset your password', self.email.subject)
#
#     def test_email_body(self):
#         context = self.response.context
#         token = context.get('token')
#         uid = context.get('uid')
#         password_reset_token_url = reverse('password_reset_confirm', kwargs={
#             'uidb64': uid,
#             'token': token
#                 })
#         self.assertIn(password_reset_token_url, self.email.body)
#         self.assertIn('Max', self.email.body)
#         self.assertIn('check@check.com', self.email.body)
#
#     def test_email_to(self):
#         self.assertEqual(['check@check.com'], self.email.to)
