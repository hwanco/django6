from django.shortcuts import render
import googletrans
from googletrans import Translator

# Create your views here.
def index(request):
    text = request.GET.get("bftext","")
    bflang = request.GET.get("bflang","")
    aftlang = request.GET.get("aftlang","")

    translator = Translator()
    trans1 = translator.translate(text, src=bflang, dest=aftlang)

    content = {
        "trans":trans1.text,
        "text":text,
        "bflang":bflang,
        "aftlang":aftlang
    }
    return render(request, "trans/index.html", content)

def trans(request):
    context = {
        "ndict" : googletrans.LANGUAGES
        }
    if request.method == "POST":
        translator = Translator()
        b = request.POST.get("bf")
        f = request.POST.get("fr")
        t = request.POST.get("to")
        print(b,f,t)
        after = translator.translate(b, src=f, dest=t)
        print(after.text)
        context.update({
            "b" : b,
            "t" : t,
            "f" : f,
            "aft" : after.text
        })
    return render(request, "trans/trans.html", context)