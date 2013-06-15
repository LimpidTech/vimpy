class AutoInstance(type):
    def __new__(mcs, name, bases, dict):
        new_type = type.__new__(mcs, name, bases, dict)

        if getattr(new_type, 'auto_instance', True):
            new_type()

        return new_type
