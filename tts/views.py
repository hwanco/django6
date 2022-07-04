from django.shortcuts import render
from gtts import gTTS

# Create your views here.
def tts(request):
    context = {}
    if request.method=="POST":
        b = request.POST.get("bf")
        t = request.POST.get("to")
        fn = request.POST.get("fname")
        tts = gTTS(text=b, lang=t)
        filename = f"media/tts/{fn}.mp3"
        tts.save(filename)
        context.update({
            "b":b,
            "t":t,
            "fn":fn
        })

    return render(request, "tts/tts.html", context)