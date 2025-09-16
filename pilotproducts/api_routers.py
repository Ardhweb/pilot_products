from rest_framework.routers import DefaultRouter
from core.api.views import LetterDesignViewSet

router = DefaultRouter()
router.register(r'core/coverletter', LetterDesignViewSet,basename='letterdesign')


