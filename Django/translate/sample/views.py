# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy as __


def index(request):
    msg = _('안녕하세요요요')

    # "구어"는 구분자 이다(아무거나 해도 됨)
    msg2 = __("구어", "안녕안녕")

    msg3 = f"{msg} {msg2}"
    return HttpResponse(msg3)

def sample(request):
    return render(request, 'sample/index.html')


# 언어 코드를 변경하는 뷰를 만들어 보기
# 1) url named group을 통해 language code 받기
from django.conf import settings


def trans1(request, code):
    # 지원하는 언어 코드 목록을 만듬
    languages = [language[0] for language in settings.LANGUAGES]
    # 기본 언어 설정 가져오기
    default_language = settings.LANGUAGE_CODE[:2]

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del (request.session[translation.LANGUAGE_SESSION_KEY])

    if code in languages and code != default_language:
        translation.activate(code)
        request.session[translation.LANGUAGE_SESSION_KEY] = code
    else:
        request.session[translation.LANGUAGE_SESSION_KEY] = default_language
        code = default_language

    return HttpResponse("Language Change to " + code)


# 2) 쿼리 스트링으로 language code 받기
def trans2(request):
    code = request.GET.get('code')
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del (request.session[translation.LANGUAGE_SESSION_KEY])
    translation.activate(code)

    request.session[translation.LANGUAGE_SESSION_KEY] = code


# 3) 언어별 설정 변경 뷰를 별도로 만들기
def trans_en(request):
    code = 'en'
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del (request.session[translation.LANGUAGE_SESSION_KEY])
    translation.activate(code)

    request.session[translation.LANGUAGE_SESSION_KEY] = code


def trans_ko(request):
    code = 'en'
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del (request.session[translation.LANGUAGE_SESSION_KEY])
    translation.activate(code)

    request.session[translation.LANGUAGE_SESSION_KEY] = code
