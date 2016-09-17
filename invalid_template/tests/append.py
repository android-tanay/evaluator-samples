# begin append code
##import inspect
def count_keywords(keyword, funct):
    count = 0
    try:
        s = inspect.getsourcelines(funct)[0]
        for e in s:
            if keyword in e:
                count += 1
    except:
        pass
    return count

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
