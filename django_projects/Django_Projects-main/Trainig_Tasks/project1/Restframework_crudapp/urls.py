from django.urls import path
#from .views import Create, Read, Update, Delete
from.views import create, read, update, delete
#from.views import BookList, BookDetails, BookDelete

urlpatterns = [
    # path('create', Create),
    # path('read', Read),
    # path('Update/<int:id>', Update),
    # path('Delete/<int:id>', Delete),
    # #path('gen', BookList.as_view()),
    #path('gen2/<int:pk>', BookDetails.as_view()),
    #path('gen3/<int:pk>', BookDelete.as_view()),
    path('genCreate', create.as_view()),
    path('genRead', read.as_view()),
    path('genUpdate/<int:id>', update.as_view()),
    path('genDelete/<int:pk>', delete.as_view()),
]
