from django.urls import path
from . import user
from . import venue
from . import court

urlpatterns = [
        path('user/addUser',user.addUser,name='addUser'),
        path('user/getUser',user.getUser,name='getUser'),
        path('user/updateUser',user.updateUser,name='updateUser'),
        path('user/deleteUser',user.deleteUser,name='deleteUser'),
        path('user/getUserInfo',user.getUserInfo,name='getUserInfo'),
        path('user/getUserCollectedVenue',user.getUserCollectedVenue,name='getUserCollectedVenue'),
        path('user/getUserDiscountCard',user.getUserDiscountCard,name='getUserDiscountCard'),
        path('user/getOrderSite',user.getOrderSite,name='getOrderSite'),
        path('venue/getIndexVenue',venue.getIndexVenue,name='getIndexVenue'),
        path('venue/getCourtType',venue.getCourtType,name='getCourtType'),
        path('venue/filterCourtType',venue.filterCourtType,name='filterCourtType'),
        path('venue/getVenueDetail',venue.getVenueDetail,name='getVenueDetail'),
        path('court/getCourtDetail',court.getCourtDetail,name='getCourtDetail'),
]