from django.urls import path,include
from rest_framework.routers import DefaultRouter
from cooperative import views

router=DefaultRouter()
router.register('farmers', views.FarmerViewSet, basename='farmers' )
router.register('porters', views.PorterViewSet, basename='porters')
router.register('collection', views.MilkCollectionViewSet, basename='collection')
router.register('notice',views.NoticeViewSet, basename='notice')

urlpatterns=[
    path('feedback/',views.ViewFeedback.as_view()),
    path('',include(router.urls))
]