from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import pandas as pd
import numpy as np
import pickle, json
# Create your views here.

similarity = pickle.load(open('./model/similarity.pkl','rb'))
details = pd.read_csv('./model/data/Cleaned_DF.csv')

def home(request):
    movie_name = details['title']
    
    context = {
        'movie_name' : movie_name    
    }
    
    return render(request, "home.html", context)

def search_results(request):
    if request.method == 'POST':
        name = request.POST.get('searchInput').strip()
        result = recommend(name) 
        print(result)   
        
        context = {
            'result' : result
        }      
        print(context)

        return JsonResponse(context)
    return HttpResponse('')

def recommend(movie):
    print('recommend '+movie)
    print(details['title'])

    movie_index = details[details['title'] == movie].index[0]
    print(movie_index)
    
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    for i in movies_list:
        print(details.iloc[i[0]].title)
        
    recommended_movies = [details.iloc[i[0]].title for i in movies_list]

    return recommended_movies