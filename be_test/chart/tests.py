from django.test import Client, TestCase


class SimpleChartTest(TestCase):
    def test_simple1(self):
        c = Client()
        rep = c.post('/chart/simple', {'data': '1 2'})
        with open('chart/test1.png', 'rb') as f:
            data = b''.join(rep.streaming_content)
            self.assertEqual(data, f.read())
