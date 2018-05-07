class Mapper(object):
    @staticmethod
    def map(enum, value):
        result = None
        for enum_value in enum:
            if Mapper._normalize(value) == Mapper._normalize(enum_value.value):
                result = enum_value
        return result

    @staticmethod
    def _normalize(value: str):
        return value.lower().replace(" ", "")
