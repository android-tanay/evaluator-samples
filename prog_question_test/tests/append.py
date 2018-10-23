# begin append code
##import inspect

class Counter(object):
    def __init__(self, fn):
        self.count = 0
        self.fn = fn

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.fn(*args, **kwargs)

    def get_count(self):
        return self.count
# end append code
