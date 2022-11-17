
from flask import Flask, request
import os 
import pickle
import pandas as pd
import numpy as np
import random
from io import StringIO

api = Flask('ModelEndpoint')

attract = pickle.load(open('att_canada_ratesen.pkl','rb'))
attractions = pd.DataFrame(attract)

@api.route('/') 
def home(): 
    return {"message": "Hello!", "success": True}, 200

@api.route('/predict', methods = ['POST']) 
def recommend():
    profile = request.get_json(force=True)
    profile = pd.read_json(StringIO(profile), lines=True) 
    
    final_att_as_id = attractions.set_index(keys='name')
    final_att_as_id = pd.get_dummies(final_att_as_id, columns=['province','city_name'],drop_first=True)
    final_att_as_id.drop(labels=['attraction_id','location__lat', 'location__lng', 'attraction', 'price',
                                 'group_reviews','country','rating','description','duration','images'],axis=1, inplace= True)

    attract_categories = final_att_as_id.columns
    my_profile = pd.Series(data=np.zeros(len(attract_categories)), index=attract_categories) 

    my_profile['sightseeing'] = profile['sightseeing']
    my_profile['land tour'] = profile['land tour']
    my_profile['air tour'] = profile['air tour']
    my_profile['sea tour'] = profile['sea tour']
    my_profile['park'] = profile['park']
    my_profile['city'] = profile['city']
    my_profile['nature'] = profile['nature']
    my_profile['accommodation'] = profile['accommodation']
    my_profile['camping'] = profile['camping']
    my_profile['cruise'] = profile['cruise']
    my_profile['island'] = profile['island']
    my_profile['entertainment'] = profile['entertainment']
    my_profile['classes & workshops'] = profile['classes & workshops']
    my_profile['transport'] = profile['transport']
    my_profile['experience'] = profile['experience']
    my_profile['brewery/winery/distillery'] = profile['brewery/winery/distillery']
    my_profile['photography'] = profile['photography']
    my_profile['wildlife'] = profile['wildlife']
    my_profile['adventure'] = profile['adventure']
    my_profile['beach'] = profile['beach']
    my_profile['hiking'] = profile['hiking']
    my_profile['rental'] = profile['rental']
    my_profile['mountain views'] = profile['mountain views']
    my_profile['food'] = profile['food']

    recommendations = np.dot(final_att_as_id.values, my_profile.values)
    recommendations = pd.Series(recommendations, index=final_att_as_id.index)
    names = recommendations.sort_values(ascending=False).head(6).index
    names = names.tolist()  
    url = []
    for i in range(len(names)):
        url.append(attractions[attractions['name'] == names[i]]['attraction'].values[0]) 
    image = []
    for i in range(len(names)):
        image.append(attractions[attractions['name'] == names[i]]['images'].values[0])
    description = []
    for i in range(len(names)):
        description.append(attractions[attractions['name'] == names[i]]['description'].values[0])  
    
    return {'names': names, 'url': url, 'image': image, 'description': description}

@api.route('/random', methods = ['POST']) 
def random():
    # randomly = request.get_json(force=True)
    # randomly = pd.read_json(StringIO(randomly), lines=True) 
    import random
    random_choices = []
    for i in range(6):
        random_choices.append(random.choice(attractions['name'].values))
    url = []
    for i in range(len(random_choices)):
        url.append(attractions[attractions['name'] == random_choices[i]]['attraction'].values[0])
    image = []
    for i in range(len(random_choices)):
        image.append(attractions[attractions['name'] == random_choices[i]]['images'].values[0])
    description = []
    for i in range(len(random_choices)):
        description.append(attractions[attractions['name'] == random_choices[i]]['description'].values[0])
        
    return {'names': random_choices, 'url': url, 'image': image, 'description': description}

if __name__ == '__main__': 
    api.run(host='0.0.0.0', 
            debug=True, 
            port=int(os.environ.get("PORT", 8080))
           ) 
