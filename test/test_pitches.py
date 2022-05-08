import unittest
from app.models import  Pitches 

class PitchesTest(unittest.TestCase):

    def test_save_pitch(self):
        self.assertTrue(len(Pitches.query.all())>0)



 