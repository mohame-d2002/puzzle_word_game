from django.urls import path
from .views import PlayGameView, LevelOneGameView, LevelTwoGameView, IncrementLevelView, LevelThreeGameView, LevelFourGameView, LevelFiveGameView, LevelSixGameView, RestartGamelView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('palygame', PlayGameView.as_view(), name='play'),
    path('levelone', LevelOneGameView.as_view(), name='level_one'),
    path('leveltwo', LevelTwoGameView.as_view(), name='level_two'),
    path('levelthree', LevelThreeGameView.as_view(), name='level_three'),
    path('levelfour', LevelFourGameView.as_view(), name='level_four'),
    path('levelfive', LevelFiveGameView.as_view(), name='level_five'),
    path('levelsix', LevelSixGameView.as_view(), name='level_six'),
    path("increment-level/", IncrementLevelView.as_view(), name="increment_level"),
    path("restart-level/", RestartGamelView.as_view(), name="restart_level"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)