# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
import glob
import os
from random import randint, sample
from SubTest.models import SubTestResult, RankRecord


def choose_images(request):
        tagcollection = [1,2,3]
        if request.method == 'POST':
                g = request.POST.get('img_group')
                orgTag = "org" + g
        return render(request,'choose_images.html',{'tag':tagcollection,'group':orgTag})

def show_image(request):
        global imgfiles
        posts = SubTestResult.objects.all()
        posts.orgName = []
        posts.candName = []
        path = 'E:/texture/totest/png/'
        g = ""
        tagcollection = [1,2,3]
        if request.method == 'GET':
                g = request.GET.get('img_group')
        elif request.method == 'POST':
                g = request.POST.get('section')
        if g != "":
                orgTag = "org" + g
                candTag = "cand" + g
                posts.orgName = []
                posts.candName = []
                for f in os.listdir(path):
                        if f.startswith(orgTag):
                                posts.orgName.append(f)
                        if f.startswith(candTag):
                                posts.candName.append(f)
                        candi_org = []
                for candi in posts.candName:
                        if candi[4] == posts.orgName[0][3]:
                                candi_org.append(candi)
                candi_index = range(0,len(candi_org))
                candinum = sample(candi_index,2)
                # print the collection of canidates
                print 'selected files'
                print posts.orgName
                print posts.candName[candinum[0]]
                print posts.candName[candinum[1]]
                imgfiles = [posts.orgName[0],posts.candName[candinum[0]],posts.candName[candinum[1]] ]
                
                if request.method == 'POST':
                        c = imgfiles
                        p = request.POST.getlist('answer[]')
                        
                        combo = [[c[0],p[0]],[c[1],p[1]],[c[2],p[2]]]
                        posts_rank = RankRecord(Record = combo)
##                       posts_rank.save()
        else:
                imgfiles = []
	return render(request,'display_images.html',{'tag':tagcollection,'ss':g,'images':imgfiles})
