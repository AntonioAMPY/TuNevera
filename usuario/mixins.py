from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class AuthRedirectMixins(object):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/twitter/')
		else:
			return super(AuthRedirectMixins, self).get(self, request, *args,**kwargs)

