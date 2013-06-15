import vim
import uuid

callbacks = {}

class Callback(object):
    def __init__(self, method, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.method(*args, **kwargs)

def register(method, *args, **kwargs):
    """ Creates a new Callback, and maps it to a new UUID. """

    next_uuid = uuid.uuid1()
    callbacks[next_uuid] = Callback(method, *args, **kwargs)

def execute(needle, remove=False):
    for unique_id in callbacks:
        if str(unique_id) == str(needle):
            callback = callbacks[unique_id]
            callback()

            del callbacks[unique_id]
            return True

    return False
