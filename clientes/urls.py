
from django.urls import path

from .views import PersonList,PersonDetail,PersonCreate,PersonUpdate,PersonDelete
from .views import sorteio


urlpatterns = [

    path("person_list/",PersonList.as_view(),name='person_list_cbv'),
    path("person_detail/<int:pk>/",PersonDetail.as_view(),name='person_detail_cbv'),
    path("person_create/",PersonCreate.as_view(),name='person_create_cbv'),
    path("person_update/<int:pk>/", PersonUpdate.as_view(), name='person_update_cbv'),
    path("person_delete/<int:pk>/", PersonDelete.as_view(), name='person_delete_cbv'),
    path('sorteio/',sorteio,name='sorteio'),

]
