import time

from numpy.ma.bench import timer


class A:
    """
    This is documentation for class A.
    
    """
    def __init__(self, num_elem):
        self.attr1 = list(range(num_elem))

    def foo(self):
        print('foo', self.name, self)

    def benchmark(func):
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs)
            end = time.time()
            print('[*] Execution time: {} secs.'.format(end - start))
            return return_value
        return wrapper


class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = (time.time() - self.start) * 1000
        print(self.message.format(elapsed_time))


class lazy_object:

    reset = 0

    def __init__(self, callable, *args, **kw):
        self.__dict__['callable'] = callable
        self.__dict__['args'] = args
        self.__dict__['kw'] = kw
        self.__dict__['obj'] = None

    def initObj(self):
        if self.obj is None:
            self.__dict__['obj'] = self.callable(*self.args, **self.kw)

    def __getattr__(self, name):
        self.initObj()
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        if name == 'reset' and value == 1:
            self.__dict__['obj'] = None
        else:
            self.initObj()
            setattr(self.obj, name, value)

    def __len__(self):
        self.initObj()
        return getattr(self.obj)

    def __getitem__(self, idx):
        self.initObj()
        return self.obj[idx]

a = lazy_object(A, num_elem=10**8)

with timer('Elapsed: {}ms'):
    type(a.attr1)

with timer('Elapsed: {}ms'):
    type(a.attr1)

a.reset = 1

with timer('Elapsed: {}ms'):
    type(a.attr1)
