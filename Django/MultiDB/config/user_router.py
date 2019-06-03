from django.conf import settings

class UserRouter:
    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'user':
            return 'user'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'user':
            return 'user'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = settings.DATABASES.key()
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True