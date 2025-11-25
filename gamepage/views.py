from django.views.generic import TemplateView

# Create your views here.
    


class LevelOneGameView(TemplateView):
    template_name = 'level_one.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context
    


class LevelTwoGameView(TemplateView):
    template_name = 'level_two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context


class LevelThreeGameView(TemplateView):
    template_name = 'level_three.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context


class LevelFourGameView(TemplateView):
    template_name = 'level_four.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context

class LevelFiveGameView(TemplateView):
    template_name = 'level_five.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context


class LevelSixGameView(TemplateView):
    template_name = 'level_six.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context


from django.views.generic import TemplateView
from .models import UserProgress
from django.shortcuts import redirect

class PlayGameView(TemplateView):
    template_name = 'playegame.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current user's level progress
        try:
            progress = UserProgress.objects.get(user=self.request.user)
            context['level'] = progress.level_progress
        except UserProgress.DoesNotExist:
            context['level'] = 1  # default if no progress yet
        return context

from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProgress

class IncrementLevelView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        progress, created = UserProgress.objects.get_or_create(user=user)
        progress.level_progress += 1
        progress.save()
        return JsonResponse({
            "status": "success",
            "new_level": progress.level_progress
        })

    def get(self, request, *args, **kwargs):
        # Optionally handle GET if someone accesses the URL directly
        return JsonResponse({"status": "error", "message": "POST only"}, status=400)
    

class RestartGamelView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        progress, created = UserProgress.objects.get_or_create(user=user)
        progress.level_progress = 1
        progress.save()
        return redirect('play')

    def get(self, request, *args, **kwargs):
        # Optionally handle GET if someone accesses the URL directly
        return JsonResponse({"status": "error", "message": "POST only"}, status=400)