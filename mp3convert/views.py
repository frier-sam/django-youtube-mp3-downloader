from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import youtube_dl
import os
from django.template.response import TemplateResponse

# download using optimal audio settings
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'ytmusic/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'restrictfilenames': False,
    'force':'ipv4',
    'ipv4':True}



@csrf_exempt
def main(request):
    return TemplateResponse(request, 'main.html', {'entries': 'all'})

@csrf_exempt
def convert(request):
    """This suggests a word based on the intial text , This for auto complete feature for just a word"""
    url = request.POST.get('url')
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])
    info_dict = ydl.extract_info(url, download=False)
    title = info_dict['title']
    file = open("ytmusic/{}.mp3".format(title), "rb").read()
    response=HttpResponse()
    response.write(file)
    response['Content-Type'] ='audio/mp3'
    response['Content-Length'] =os.path.getsize("ytmusic/{}.mp3".format(title) )
    response['Content-Disposition'] = 'attachment; filename={}.mp3'.format(title)
    response['mimetype'] = "audio/mpeg"
    os.remove("ytmusic/{}.mp3".format(title))
    return response#HttpResponse(file, mimetype="audio/mpeg")
