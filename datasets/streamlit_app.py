import streamlit as st
import requests
import json
from PIL import Image

st.set_page_config(page_title ='WanderLust', layout="wide", page_icon= '✈️')

st.image("https://iili.io/H906Las.md.png",width=300)
st.title('_Wandering_ what to do during your holiday?')
st.header('Select the top 5 categories you would like to do as part of an activity when you are travelling!')
st.markdown("By: Fung Xue Feng ([GitHub](https://github.com/FungXF))([Linkedin](https://www.linkedin.com/in/xue-feng-fung/))")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    accommodation = st.checkbox('Accommodation', help='Activites that include accommodation')
with col2:
    adventure = st.checkbox('Adventure', help='Ziplining, Rafting, Snowshoeing and more')
with col3:
    air_tour = st.checkbox('Air Tour', help='Tour in the Air with Guide')
with col4:
    beach = st.checkbox('Beach', help='Visiting a beach')
with col5:
    brew_dis_win = st.checkbox('Brewery/ Distillery/ Winery', help='Visiting Brewery/Distillery/Winery')


col6, col7, col8, col9, col10 = st.columns(5)
with col6:
    camping = st.checkbox('Camping', help='Activites that involves camping')
with col7:
    classes_and_workshops = st.checkbox('Classes and Workshop', help='Activities that involves an instructor')
with col8:
    entertainment = st.checkbox('Entertainment', help='Live Entertainment')
with col9:
    rental = st.checkbox('Equipment Rental', help='Only renting of equipment (snowboard, bicycle, boat, etc), no tours')
with col10:
    food = st.checkbox('Food Tour', help='Food Tour!')

    
col11, col12, col13, col14, col15 = st.columns(5)
with col11:
    hiking = st.checkbox('Hiking', help='Involves hiking') 
with col12:
    transport = st.checkbox('Includes Transport', help='Transport from A to B, includes passes and hop-on/off tours')  
with col13:
    island = st.checkbox('Island Hopping', help='Visiting an island')    
with col14:
    land_tour = st.checkbox('Land Tour', help='Tour in the Land with Guide')
with col15:
    city = st.checkbox('Located In City', help='Activities that takes place in the City')



col16, col17, col18, col19, col20 = st.columns(5)
with col16:
    nature = st.checkbox('Located In Nature', help='Activities that takes place in Nature/Mountain')
with col17:
    mountain_views = st.checkbox('Mountain Views',help='Having Mountain Views')
with col18:
    park = st.checkbox('Park', help='Visiting Parks and Gardens')
with col19:
    photography = st.checkbox('Photoshoot', help='Photography service is provided/included')
with col20:
    cruise = st.checkbox('River Cruise', help='E.g. River Cruise, Ferry to another island')


col21, col22,col23,col24,col25 = st.columns(5)
with col21:
    sea_tour = st.checkbox('Sea Tour', help='Tour in the Sea with Guide')    
with col22:
    sightseeing = st.checkbox('Sightseeing', help='Visting places of Interest')
with col23:
    experience = st.checkbox('Unique Experience', help='Experience an activity/do something "extra-ordinary"')
with col24:
    wildlife = st.checkbox('Wildlife Spotting', help ='Sealife spotting, Bird Watching, etc..')

    
if sightseeing:
    st.subheader('Activity needs to include Sightseeing:')
    sight = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="1")
else: 
    sight = 0
if land_tour:
    st.subheader('Activity needs to include Tour by Land:')
    land_t = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="2")
else: 
    land_t = 0
if air_tour:
    st.subheader('Activity needs to include Tour in Air:')
    air_t = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="3")
else: 
    air_t = 0
if sea_tour:
    st.subheader('Activity needs to include Tour of Sea:')
    sea_t = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="4")
else: 
    sea_t = 0
if park:
    st.subheader('Activity needs to include visiting Park/Garden:')
    parks = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="5")
else: 
    parks = 0
if city:
    st.subheader('Activity needs to be in the city:')
    in_city = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="6")
else: 
    in_city = 0
if nature:
    st.subheader('Activity needs to include being in nature:')
    nat = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="7")
else: 
    nat = 0
if accommodation:
    st.subheader('Activity needs to include Accommodation:')
    accom = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="8")
else: 
    accom = 0
if camping:
    st.subheader('Activity needs to include Camping:')
    camp = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="9")
else: 
    camp = 0
if cruise:
    st.subheader('Activity needs to include Boat Tour:')
    crui = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="10")
else: 
    crui = 0
if island:
    st.subheader('Activity needs to include being on island:')
    islands = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="11")
else: 
    islands = 0
if entertainment:
    st.subheader('Activity needs to include entertainment:')
    enter = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="12")
else: 
    enter = 0
if classes_and_workshops:
    st.subheader('Activity needs to include classes and workshops:')
    class_work = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="13")
else: 
    class_work = 0
if transport:
    st.subheader('Activity needs to include Transport:')
    trans = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="14")
else: 
    trans = 0
if experience:
    st.subheader('Activity needs to include a unique experience:')
    exp = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="15")
else: 
    exp = 0
if brew_dis_win:
    st.subheader('Activity needs to include brewery/distillery/winery:')
    brewery_distillery_winery = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="16")
else: 
    brewery_distillery_winery = 0
if photography:
    st.subheader('Activity needs to include photoshoots:')
    photo = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="17")
else: 
    photo = 0
if wildlife:
    st.subheader('Activity needs to include observing wildlife:')
    wild = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="18")
else: 
    wild = 0
if adventure:
    st.subheader('Activity needs to be adventurous:')
    advent = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="19")
else: 
    advent = 0
if beach:
    st.subheader('Activity needs to include visting a beach:')
    beaches = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="20")
else: 
    beaches = 0
if hiking:
    st.subheader('Activity needs to include hiking:')
    hike = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="21")
else: 
    hike = 0
if rental:
    st.subheader('Renting of an equipment:')
    rentals = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="22")
else: 
    rentals = 0
if mountain_views:
    st.subheader('Having Mountain views:')
    mount_views = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="24")
else: 
    mount_views = 0
if food:
    st.subheader('Food Must be included in the activity:')
    foods = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="25")
else: 
    foods = 0

values = (sightseeing + land_tour + air_tour + sea_tour + park + city + nature + accommodation + 
          camping + cruise + island + entertainment + classes_and_workshops + transport + experience + 
          brew_dis_win + photography + wildlife + adventure + beach + hiking + rental + mountain_views + food)


submit = st.button('Show Recommendation')    

submit2 = st.button("Help me decide!")

    
# Randomizer if they cannot decide on the type of activites
if submit2:
    api_url = 'https://dsicapstone-l7bv2piloq-as.a.run.app'
    api_route = '/random'
    
    profile = {'empty':'empty'}
    response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
    output = response.json()
    names = output['names']
    url = output['url']
    image = output['image']
    description = output['description']    
    
    #display with the columns
    colrand1, colrand2, = st.columns(2)

    with colrand1:
        st.image((output['image'][0]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[0].split('_'))).title()}](%s)" % url[0])
        with st.expander("Read More"):
            st.markdown(f"{description[0]}")

    with colrand2:
        st.image((output['image'][1]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[1].split('_'))).title()}](%s)" % url[1])
        with st.expander("Read More"):
            st.markdown(f"{description[1]}")
        
    colrand3, colrand4 = st.columns(2)
    with colrand3:
        st.image((output['image'][2]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[2].split('_'))).title()}](%s)" % url[2])
        with st.expander("Read More"):
            st.markdown(f"{description[2]}")
        
    with colrand4:
        st.image((output['image'][3]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[3].split('_'))).title()}](%s)" % url[3])
        with st.expander("Read More"):
            st.markdown(f"{description[3]}")
        
    colrand5, colrand6 = st.columns(2)

    with colrand5:
        st.image((output['image'][4]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[4].split('_'))).title()}](%s)" % url[4])
        with st.expander("Read More"):
            st.markdown(f"{description[4]}")

    with colrand6:
        st.image((output['image'][5]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[5].split('_'))).title()}](%s)" % url[5])
        with st.expander("Read More"):
            st.markdown(f"{description[5]}")

# After selecting the 5 categories of activites, the recommender would then pull out the top 6 recommended activites
if submit:
    if values != 5:
        st.error("**Choose exactly 5 options!**")
        
    else:
        profile = {'sightseeing': sight, 'land tour': land_t, 'air tour': air_t, 'sea tour': sea_t,
           'park': parks, 'city': in_city, 'nature': nat, 'accommodation': accom,
           'camping': camp, 'cruise': crui, 'island': islands, 'entertainment': enter, 
           'classes & workshops': class_work, 'transport': trans, 'experience': exp, 
           'brewery/winery/distillery': brewery_distillery_winery, 'photography': photo,
           'wildlife': wild, 'adventure': advent, 'beach': beaches, 'hiking': hike, 
           'rental': rentals, 'mountain views': mount_views, 'food': foods}
                                                        
        api_url = 'https://dsicapstone-l7bv2piloq-as.a.run.app'
        api_route = '/predict'

        response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) 
        output = response.json()
        names = output['names']
        url = output['url']
        image = output['image']
        description = output['description']
        
        #display with the columns
        colres1, colres2, = st.columns(2)
        with colres1:
            st.image((image[0]), use_column_width='always')
            st.markdown(f"[{(' '.join(names[0].split('_'))).title()}](%s)" % url[0])
            with st.expander("Read More"):
                st.markdown(f"{description[0]}")

        with colres2:
            st.image((image[1]), use_column_width='always')
            st.markdown(f"[{(' '.join(names[1].split('_'))).title()}](%s)" % url[1])
            with st.expander("Read More"):
                st.markdown(f"{description[1]}")
        
        colres3, colres4 = st.columns(2)
        with colres3:
            st.image((image[2]), use_column_width='always')
            st.markdown(f"[{(' '.join(names[2].split('_'))).title()}](%s)" % url[2])
            with st.expander("Read More"):
                st.markdown(f"{description[2]}")
        
        with colres4:
            st.image((image[3]), use_column_width='always')
            st.markdown(f"[{(' '.join(names[3].split('_'))).title()}](%s)" % url[3])
            with st.expander("Read More"):            
                st.markdown(f"{description[3]}")
        
        colres5, colres6 = st.columns(2)
        with colres5:
            st.image((image[4]), use_column_width='always')
            st.markdown(f"[{(' '.join(names[4].split('_'))).title()}](%s)" % url[4])
            with st.expander("Read More"):
                st.markdown(f"{description[4]}")

        with colres6:
            st.image((image[5]), use_column_width='always')
            st.markdown(f"[{(' '.join(names[5].split('_'))).title()}](%s)" % url[5])
            with st.expander("Read More"):
                st.markdown(f"{description[5]}")

# Changing the background and words styling and colours 
# Background-colour changes background colour
# svg.icon: the question mark
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
         background-color: #F0FFFF;
         }}
         svg.icon {{
             stroke: rgb(49, 51, 63);
         }}
         h3 {{
             font-size: 28px;
             font-weight: bold;
             color:#5A5A5A;  
         }}
         h1, h2  {{
             color:#5A5A5A;
         }}
         .css-1offfwp p, .css-1fv8s86.e16nr0p34 p {{
             font-size: 20px;
             font-weight: bold;
             color:#5A5A5A;         
         }}
         .css-81oif8, .css-k3w14i {{
             font-size: 17px;
             font-weight: bold;
             color:#5A5A5A;
         }}
         .css-1djdyxw, .css-1djdyxw {{
             font-weight: bold;
             color:#5A5A5A;            
         }}
         .css-1h6yrjv p {{
             color: #5A5A5A;
             background-color:white;
         }}
         .st-co, .st-cp {{
             color: #5A5A5A;
         }}
         .st-da, .st-cx {{ border-color: black;}}
         </style>
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
