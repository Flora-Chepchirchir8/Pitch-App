import unittest
from app.models import Comments


class CommentsTest(unittest.TestCase):

    def setUp(self):
       self.new_comment = Comments(id=1, user_id = 2, comment = 'cross buns',pitches_id = '5',date_posted='2022-05-08')

    def test_comment_variables(self):

       self.assertEquals(self.new_comment.comment,'cross buns')
       self.assertEquals(self.new_comment.date_posted,'2022-05-08')
       self.assertEquals(self.new_comment.user_id, 2)
      

    def test_save_comment(self):

        self.assertTrue(len(Comments.query.all())>0)