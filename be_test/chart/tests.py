from django.test import Client, TestCase
from chart import errors


class SimpleChartTest(TestCase):
    def test_simple1(self):
        c = Client()
        rep = c.post('/chart/simple', {'data': '5 1.3 4 1.0 3.5', 'width': '3', 'height': '2'})
        with open('chart/test1.png', 'rb') as f:
            data = b''.join(rep.streaming_content)
            self.assertEqual(data, f.read())

    def test_simple_insufficient_args(self):
        c = Client()
        rep = c.post('/chart/simple')
        self.assertJSONEqual(rep.content.decode(), errors.INSUFFICIENT_ARGS)

    def test_simple_invalid_size(self):
        c = Client()
        rep1 = c.post('/chart/simple', {'data': '1 2 3 4     5.5', 'width': -1})
        rep2 = c.post('/chart/simple', {'data': '1 3 2 4', 'width': 'what?'})
        self.assertJSONEqual(rep1.content.decode(), errors.INVALID_SIZE)
        self.assertJSONEqual(rep2.content.decode(), errors.INVALID_SIZE)

    def test_simple_invalid_data(self):
        c = Client()
        rep1 = c.post('/chart/simple', {'data': '      '})
        rep2 = c.post('/chart/simple', {'data': 'a b c'})
        self.assertJSONEqual(rep1.content.decode(), errors.INVALID_DATA)
        self.assertJSONEqual(rep2.content.decode(), errors.INVALID_DATA)
