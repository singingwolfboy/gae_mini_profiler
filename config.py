from google.appengine.api import users


# Customize should_profile to return true whenever a request should be profiled.
# This function will be run once per request, so make sure its contents are fast.
class ProfilerConfigProduction(object):
    @staticmethod
    def should_profile(environ):
        user = users.get_current_user()
        return user and user.email().endswith("@cloudlock.com")


class ProfilerConfigDevelopment(object):
    @staticmethod
    def should_profile(environ):
        return users.is_current_user_admin()
