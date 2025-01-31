from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def faq_list(request):
    lang_code = request.query_params.get('lang', 'en')
    
    faqs = FAQ.objects.all()
    translated_faqs = []
    
    for faq in faqs:
        translated_faq = {
            'question': faq.get_translated_question(lang_code),
            'answer': faq.get_translated_answer(lang_code),
        }
        translated_faqs.append(translated_faq)
    
    return Response(translated_faqs)
