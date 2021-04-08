from django.shortcuts import render
from apiclient.discovery import build
import pafy,pickle
import time
from django.http import HttpResponse
import json
# Create your views here.
#API_KEY ="AIzaSyBK-LcrR8vEkWoqZitqORVz_UYhq5XMOME"
API_KEY = "AIzaSyDbz2YdQtO454p9U6MTM57kzMdK3kxU12k"
youtube=build('youtube','v3',developerKey=API_KEY)
def index(request):
    if request.method != 'POST':

        return render(request, 'index.html')
    else:
        query=request.POST['Music']
        req=youtube.search().list(q=query,part='snippet',type='video',videoCategoryId=10,maxResults=20)
        res=req.execute()
        query={
        'query':res['items']
        }

        return render(request,'index.html', query)



def music_now(request):
    new_list=[]
    new_dic={}
    videoid=request.GET['videoid']
    video = pafy.new(videoid)
    best = video.getbest()
    new_dic['title']=video.title
    new_dic['author']=video.author
    new_dic['img']=video.bigthumbhd
    new_dic['duration']=video.duration
    new_dic['views']=video.viewcount
    new_dic['playurl']=best.url
    new_dic['id']=video.videoid
    new_list.append(new_dic)

    context={
        'data_view':new_list,

        }
    print('video id music now',video)

    return HttpResponse(json.dumps(context))
# player=None
def music(request):

    videoid=request.GET['videoid']
    related_id=[videoid]
    new_list=[]
# get the related videos
    req=youtube.search().list(part='snippet',type='video',videoCategoryId=10,maxResults=20,relatedToVideoId=videoid)
    res=req.execute()
    for i in res['items']:
        related_id.append(i['id']['videoId'])

    # for 20 second late related views
    for j in related_id:
        new_dic={}
        try:
            video = pafy.new(j)
            best = video.getbest()
            new_dic['title']=video.title
            new_dic['author']=video.author
            new_dic['img']=video.bigthumbhd
            new_dic['duration']=video.duration
            new_dic['views']=video.viewcount
            new_dic['playurl']=best.url
            new_dic['id']=video.videoid
            new_list.append(new_dic)
        except OSError:
            continue
# end 20 second related views


        # playurl.append(best.url)
        # img.append(video.bigthumbhd)
        # durations.append(video.duration)
        # titles.append(video.title)
        # authors.append(video.author)

    context={
    'data_view':new_list,

    }

    return HttpResponse(json.dumps(context))
    # d=str(d)
    # return HttpResponse(video)
    # print(videoid,'video')

# def play_music(request, player_id):
#     player.play()
#     time.sleep(10)
#     player.stop()
#     return  render(request,'music_1.html',context)
