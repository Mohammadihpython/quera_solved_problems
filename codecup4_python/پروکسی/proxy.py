class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_method = None
        self.method_calls = {}

    def __getattr__(self, name):
        if not hasattr(self._obj, name):
            raise Exception("No Such Method")
        self.last_method = name
        self.method_calls.setdefault(name, 0)
        self.method_calls[name] += 1
        return getattr(self._obj, name)

    def last_invoked_method(self):
        if self.last_method is not None:
            return self.last_method
        else:
            raise Exception("No Method Is Invoked")

    def count_of_calls(self, method_name):
        if method_name in self.method_calls:
            return self.method_calls[f"{method_name}"]
        else:
            return 0

    def was_called(self, method_name):
        return method_name in self.method_calls


class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on
