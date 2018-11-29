
class ModelMixin:
    def to_dict(self):
        '''将 model 对象转化成 dict'''
        data = {}
        for field in self._meta.fields:
            name = field.attname
            value = getattr(self, name)
            data[name] = value
        return data
