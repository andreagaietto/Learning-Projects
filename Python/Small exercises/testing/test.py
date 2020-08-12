import unittest
from activities import eat, nap
#python name of file -v to run and see comments

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
                eat("broccoli", is_healthy=True),
                "I'm eating broccoli, because my body is a temple"
            )

    def test_eat_healthy_boolean(self):
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares")    

    def test_eat_unhealthy(self):
        """testing a thing"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO"
            )
    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I didn't mean to nap so long"
        )

if __name__ == "__main__":
    unittest.main()

#def test_laugh(self):
#   self.assertIn(laugh(), ('lol', 'haha', 'teehee'))
#checks that answer returned is in that tuple