from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from .apiviews import PollList, PollDetail,ChoiceList,CreateVote,PollViewSet,UserCreate,LoginView,UsersView,EventsView
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])



router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
router.register('all', UsersView, base_name='users')
router.register('events', EventsView, base_name='Events')
urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
      path(r'^', schema_view, name="docs"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
     path("login/", LoginView.as_view(), name="login"),
    # path("all/", UsersView.as_view(), name="ViewUsers"),
 


]
urlpatterns += router.urls
