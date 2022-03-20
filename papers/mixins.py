from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages


class OrganisorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organisor:
            messages.info(self.request, "You have don't have access to this page go to contact page to request access ")
            return redirect("papers:index")
        return super().dispatch(request, *args, **kwargs)