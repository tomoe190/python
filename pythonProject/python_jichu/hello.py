class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)

    def test(self):
        a = 1
        while True:
            a += 1
            yield a




