# Capstone - Travel Recommender (WanderLust)

## Notebook 1 of 4
- Notebook 1: Introduction, Scraping
- Notebook 2: Combining Datasets, Data Cleaning, EDA and Base Model
- Notebook 3: NLP (Sentiment Analysis), Feature Engineering + EDA + Model(With Feature Engineering) Conclusion + Recommendations
- Notebook 4: Google Cloud + Streamlit

## Executive Summary
### Introduction & Background
Tourism is defined as when people travel and stay in places outside of their usual environment for less than one consecutive year for leisure, business, health, or other reasons. [link](https://www.statista.com/topics/962/global-tourism/#dossierContents__outerWrapper). Globally it is made up 10 percent of global GDP in 2019 and was worth almost $9 trillion. [link](https://www.mckinsey.com/industries/travel-logistics-and-infrastructure/our-insights/reimagining-the-9-trillion-tourism-economy-what-will-it-take)

With post-covid times settling in, more people are looking into leisure travel and finding things to do overseas to fill up their itinerary. But, with the overwhelming amount of information available online and so many options available, the process of finding something one prefer to do can be a hassle. 

Popular travel websites in recent times, such as (e.g. [Tripadvisor.com](https://www.tripadvisor.com/), [Expedia.com](https://www.expedia.com/) and [Booking.com](https://www.booking.com/attractions/index.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaMkBiAEBmAExuAEXyAEP2AED6AEB-AECiAIBqAIDuAL_3MGbBsACAdICJGQ2NDZlYjljLTJiNDEtNGM5Yi05NDExLTQzNzIyYmE5MjFiMtgCBOACAQ&sid=0bd894e0a09fa5a41d0d1005be44fb09)) prioritise country location as an input before recommending the activities.

Research has shown that 97% of the travel consumers are influenced by customer post-experience reviews when it comes to making a purchase decision. Hence, we decided to incorporate reviews and ratings by unique individuals on the activity on the modelling system. Sentiment analysis was done using a pretrained model from Hugging Face [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment). The result was that the more positive the activity is received, plus matching to the degree of the genre the user is interested in, the more likely it would be recommended. 

What’s interesting is that this might include activities that user might not have specifically tried before. For example, the user might not know Snowshoeing, however the same user who likes adventure and nature and has rated it high in interest may be recommended Snowshoeing as an activity. The Travel Recommendation System not only would be a useful tool especially for those that focus on activity research over location when it comes to travelling, but also can be a trusted source since it is based on analysing past reviews.

### Problem Statement
- Popular travel websites in recent times, such as (e.g. [Tripadvisor.com](https://www.tripadvisor.com/), [Expedia.com](https://www.expedia.com/) and [Booking.com](https://www.booking.com/attractions/index.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaMkBiAEBmAExuAEXyAEP2AED6AEB-AECiAIBqAIDuAL_3MGbBsACAdICJGQ2NDZlYjljLTJiNDEtNGM5Yi05NDExLTQzNzIyYmE5MjFiMtgCBOACAQ&sid=0bd894e0a09fa5a41d0d1005be44fb09)) prioritise country location as an input before recommending the activities. However, that assumes that everyone has already decided on the country they are planning to go to. What if the person, or user, has not decided where to go, or prefers to choose based on their hobby or interest? 

- That’s where the Travel Recommender System comes in. It pulls out a list of 6 things that a user is likely to enjoy, based on what they like to do when they travel and how important it is to do a genre of activity when overseas. 

### Project Goals
1. To achieve accurate recommendations based on user’s selection of categories of activities they would like to do, especially for new users (cold start issue)
2. Incorporate sentiment analysis of reviews to modelling - feature engineering

# Scraping
- Some of the information that were not in the dataset includes
1. Description of the activity
2. Duration of the activity
3. URL of images
- The scraping file is saved as 'durationdescriptionimages.csv' and will be added to the other datasets in Notebook 2.

## Notebook 2 of 4
- Notebook 1: Introduction, Scraping
- **Notebook 2: Combining Datasets, Data Cleaning, EDA and Base Model**
- Notebook 3: NLP (Sentiment Analysis), Feature Engineering + EDA + Model(With Feature Engineering) Conclusion + Recommendations
- Notebook 4: Google Cloud + Streamlit

### Datasets
- The datasets were obtained from [here](https://github.com/sachinnpraburaj/Intelligent-Travel-Recommendation-System)
- Additional information that were not available in the dataset were scrapped from Tripadvisor website using Selenium
- As per the dataset, the focus will be on Canada Tripadvisor
- List of datasets that were imported for this project 
1. `attractions_details_batch1.csv`
2. `attractions_details_batch1.csv`
3. `attractions_cat.csv`
4. `attractions_reviews_batch1_1.csv`
5. `attractions_reviews_batch1_2.csv`
6. `attractions_reviews_batch1_3.csv`
7. `attractions_reviews_batch1_4.csv`
8. `attractions_reviews_batch1_5.csv`
9. `attractions_reviews_batch1_6.csv`
10. `attractions_reviews_batch1_7.csv`
11. `attractions_reviews_batch2_1.csv`
12. `attractions_reviews_batch2_2.csv`
13. `attractions_reviews_batch2_3.csv`
14. `attractions_reviews_batch2_4.csv`
15. `attractions_reviews_batch2_5.csv`
16. `attractions_reviews_batch2_6.csv`

| Dataset | Description |
|---|---|
| attractions_details.csv | attraction_id, name, country, province, city, location, location__lat, location__lng, price and rating|
| attractions_cat.csv | attraction_id, attraction, category|
| attractions_review.csv | attraction_id, rating, review, review_date, user|

## Import Data and Merging all the csv files 
- `attractions`, `reviews`, `categories` + Data Cleaning
- Activites that were not within country 'Canada' and 'United States' were dropped since the focus is on Canada or trips that will visit Canada 
- Only trips that would involve going to or from Canada will be kept.
- 'att_w_review' dataframe was exported to excel for re-labelling of all attraction/activities's categories.

# Importing the `final_data_text_data`
1. Since the `att_w_review` dataframe's categories that was pre-labelled did not give a good representative of the activity. Thus, each activity was relabelled manually to give a true representation of the activity.
2. Below is the categories of the activity and its description. (Each activity can have multiple category, e.g. A person takes the river cruise in Niagara falls and the tour brings the person to winery: `Land Tour`, `Sightseeing`, `Winery`, `Cruise`)
3. During manual labelling of each activities, the activities that does not involve being in Canada were dropped. (e.g. [Horse Riding in Florida - Webster](https://www.tripadvisor.ca/AttractionProductReview-g34721-d16661532-Mustang_horse_rescue_volunteer_experience_Full_Day-Webster_Florida.html)) - Filtering of outliers
- Below are the types of category that an activity can be labelled with.

|Category|Description|
|----|----|
|sightseeing|visting places of interest|
|land tour|guide - land|
|air tour|guide - air|
|sea tour|guide - sea|
|airlandsea tour|includes a combination of air, land, and sea guide|
|airsea tour|includes a combination of air and sea guide|
|airland tour|includes a combination of air and land guide|
|landsea tour|includes a combination of sea and land guide|
|park|gardens, park|
|city|anything that happens in a city|
|nature|anything that happens out of the city in a mountainy area |
|accommodation|if they include hotels/dorms|
|camping|if they sleep in a tent|
|cruise boat| (whale watching), river cruise, ferry to another island|
|island|anything that is an island on its own|
|entertainment|live entertainment (excluding live commentary)/watching or hearing somethng|
|classes & workshops|anything that has a teacher/instructor|
|transport|a vehicle to transport people from A-B, include passes and hopon/hop off tours|
|experience|when they get to experience an activity/do something "extra-ordinary"|
|activities|engaging in an activity|
|mountain views|where you can see mountain (visbile)|
|food|food tours|
|alcohol|if alcohol is provided or available for purchase|
|brewery|if they visit a brewery|
|distillery|if they visit a distillery|
|winery|if they visit a winery|
|photography|as long as photography service is provided|
|wildlife|wild animals (not including the possibility of a bird flying)|
|adventure|risky/scary activities|
|beach|if they are visiting a beach|
|hiking|if they are going on a trail/hiking a mountain/snowshoeing|
|rental|if they are renting something|

**Summary for final_att_data**
1. `final_att_data` was merged with `duration_description_image`
2. `final_att_data` dropped the rows that were not related to Canada (either orginate travel from Canada or travelling to Canada)
3. 'combined_feat' column has the combined categories of each activities then dummified.
4. Since the prices are missing and the dataset values outdataed, the columns will be dropped.
5. Since the coordinates are missing, will use the columns of `province` and `city_name` instead. Thus, `location__lat` and `location__lng` will be dropped.

- Observaions: Overall ratings have a left skewed distribution
- Activities are mainly centered around larger cities/province

## Refinement of Categories

1. For `airland tour`= 13, `airlandsea tour`= 17, `airsea tour`= 15, `landsea tour`= 125, since their total count is low and is represented by their individual taggings (i.e. `land tour`, `sea tour`, `air tour`), thus they will be dropped from the category.
2. For `winery`= 175, `brewery`= 57, `distillery`= 21, these will be combined together to form a single category called `brewery/winery/distillery` since these activities have some similarity between them and their count is not that large.
3. `Activities` and `Alcohol` are generic category, thus these shall be removed.

- The final categories that were used in the dataset `final_att_data` are as per the table below.
|Category|Description|
|----|----|
|Accommodation|Activites that include accommodation|
|Adventure|Ziplining, Rafting, Snowshoeing and more|
|Air Tour|Tour in the Air with Guide|
|Beach|Visiting a Beach|
|Brewery/ Distillery/Winery|Visiting Brewery/Distillery/Winery|
|Camping|Activites that involves camping|
|Classes & Workshops|Activities that involves an instructor|
|Entertainment|Live entertainment (excluding live commentary)/watching or hearing somethng|
|Equipment Rental|Only renting of equipment (snowboard, bicycle, boat, etc), no tours|
|Food|Food Tours|
|Hiking|Involves Hiking|
|Includes Transport|Transport from A to B, includes passes and hop-on/off tours|
|Island Hopping|Visiting an island|
|Land Tour|Tour in the Land with Guide|
|Located In City|Activities that takes place in the City|
|Located in Nature|Activities that takes place in Nature/Mountain|
|Mountain Views|Having Mountain Views|
|Park|Visiting Parks and Gardens|
|Photoshoot|Photography service is provided/included
|River Cruise| E.g. River cruise, ferry to another island|
|Sea Tour|Tour in the Sea with Guide|
|Sightseeing|Visting places of Interest|
|Unique Experience|Experience an activity/do something "extra-ordinary"|
|Wildlife Spotting|Sealife spotting, Bird Watching, etc..|


- Through the count of categories of all activities:
- Most of the activites are land tour and sightseeing
- There is almost equal distribution between city activities and nature activities

## Survey Response
- Based on a survey response of 16 people, approximately 11 got a good recommendation. 
- Thus, this concludes that the base model has a good performance in recommending activities based on user preferences on the different types of categories that is being chosen.

# Cold-start (New User)
- The issue with recommender system is the new user/ coldstart issue is that since it does not have record of user preference, it is unable to recommend to what user likes.
- In order to tackle this issue, during the user's interaction with the recommender system, it would request the user to indicate their preference before recommending the activities.

- The Base Model recommendation of activities were based on similarity value based on computing the user's profile and the activities categories.
- However, just based on activities categories alone on a recommender is not sufficient as user ratings and reviews were not looked into.
- Thus, Notebook 3 will look into the user review (through using pre-trained NLP model) and evaluate based on sentiment analysis.

## Notebook 3 of 4
- Notebook 1: Introduction, Scraping
- Notebook 2: Combining Datasets, Data Cleaning, EDA and Base Model
- **Notebook 3: NLP (Sentiment Analysis), Feature Engineering + EDA + Model(With Feature Engineering) Conclusion + Recommendations**
- Notebook 4: Google Cloud + Streamlit

## Sentiment Analysis on the user review
1. The rational to look into the user reviews in particular the Sentiment Analysis to get a sense of the customer's feelings. This is especially important for companies because one of the basic lessons that all companies should follow is that success lies in the hands of their customers. Understanding how those customers feel about your product or service is essential to financial survival and prosperity. [Link](https://www.repustate.com/blog/product-review-sentiment-analysis/)
2. Below are a few reasons why consumers writes a review [Link](https://business.trustpilot.com/reviews/learn-from-customers/why-do-people-write-reviews-what-our-research-revealed)
- Venting frustrations if the experience was negative
- Praising and helping the company if the experience was positive
- Having a need to express oneself and feel empowered in doing so
- Wanting to be recognized or acknowledged for having certain knowledge/taste
- Feeling part of a community and wanting to give back
3. 75% of people trust a business after seeing a positive review
4. 95% of shoppers read the reviews posted on business reviews before making a purchase.
5. 97% of consumers report that the customer reviews they read influence their purchasing decision. [Link](https://websitebuilder.org/blog/online-review-statistics/)
- Thus, user review actually plays an important role for attractions/activities. 
- However, rather than displaying the reviews as text for user to read (as it could be quite time consuming to comb through tens of reviews for each activities), sentiment analysis will be formed as part of Feature Engineering to incorporate with the model thus providing attractions/activities with good ratings and reviews.
4. For TripAdvisor website, it is not possible to rate and activity without writing a review.   
   Thus, those without reviews will not have any ratings as well.
   
**Observation:**
- There are 13610 for 804 activities, the remaining activites does not have a review.
- Since there are only less than 1% of reviews that contains emojis, the regex used on the reviews will only extract text out to reduce noise.

## Hugging Face Transformer: [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
1. Why chose this model: Since Twitter has a mixture of noisy text and formal text
2. This transformer is able to perform the following 
- Emotion Recognition
- Sentiment Analysis
3. From the analysis, it is able to produce 3 output (Positive, Neutral and Negative) sentiments.

**Observation:**
- Additional verification of the Hugging Face Model was done off the code notebook and found that the model has good performance to analyse the sentiment analysis. Thus, the assigned probability for each review was used in the Feature Engineering.

## Feature Engineering - Rating X Sentiment
- Activities that have cosine similarity with other activities are not enough to justify to customers of this recommendation system. 
- Since this recommender system aims to provides the best experience with their favourite types of activities.
- Based on the checks on the ratings of each review does not have similar score as sentiments, a new feature combines both the rating and sentiment to account for any discrepancy. (E.g. Someone might give a 5.0 review since they are very happy with the activity but still has some comments on areas of improvement which through the sentiment analysis might provide a neutral sentiment) (Thus, this would have a 1.0 on sentiment analysis score)

|User Ratings| Sentiment Score|
|---|---|
|Range from 1 to 5| Positive = 2, Neutral = 1 Negative = 0.5|

E.g. Highest score = 10 (e.g. rating = 5, sentiment score = 5)  
E.g. Lowest score = 0.5 (e.g. rating = 1, sentiment score = 0.5)

**Observation**
- The rating, sentiment analysis, rating*sentiment value are heavily left-skewed.
- The mean of all reviews of all Activities are centered around between 9 to 10.
- The median of all reviews all Activities are centered around 10.
- Impute the median 'rating_senti' value to the attractions without any reviews
- Perform a minmax scaler on the column `rating_senti`

- The attraction similarity values between this model and the base model looks largely similar.  
- This is because  a large number of activities do not have ratings and reviews yet. Given the left-skewed distribution, the median value of ratings was imputed to activities without user ratings. This results in most of the attractions having a rating of (9.794), hence there is not much of a significant difference between the attraction similarity values between the models.  However, overtime with more reviews added to the database, the results would differ more.
- A second survey was conducted across 15 person which saw 12 people having a good recommendation. This is an 11.25% increase in the performance.

- In Notebook 4: The pickle file `att_canada_ratesen.pkl` will be the model that is being deployed on streamlit.

## Notebook 4 of 4
- Notebook 1: Introduction, Scraping
- Notebook 2: Combining Datasets, Data Cleaning, EDA and Base Model
- Notebook 3: NLP (Sentiment Analysis), Feature Engineering + EDA + Model(With Feature Engineering) Conclusion + Recommendations
- **Notebook 4: Google Cloud + Streamlit**

## Conclusion
- Even without selecting which country to plan to go, the Travel Recommender System is able recommend a list of things that a user is likely to enjoy, based on what (5 things) they like to do when they travel and how important it is to do a genre of activity when overseas. 
- Through conducting the survey to test the 1st model, it is able to correctly recommend approximately 11 of 16 times.
- On the 2nd model testing, it is able to correctly recommend 12 of 15 times which is 11.25% increase in the performance.
- However, this is still based on a small scale testing which can be further expanded to get a true reading of the performance of the recommender model.

## Project Goals
1. To achieve accurate recommendations based on user’s selection of categories of activities they would like to do, especially for new users (cold start issue)
2. Incorporate sentiment analysis of reviews to modelling - feature engineering
- Both are achieved through the model with feature engineering and deployment through Streamlit
- By adding reviews as part of the model, it incorporates the reviews as part of the feature of the activities, thus ensuring that only those with good reviews and rating are recommended.

## Modelling (Rating X Sentiment)
1. Feature Engineering: Rating * Sentiments 
- Sentiments: The chosen pre-trained NLP Model cardiffnlp/twitter-roberta-base-sentiment has taken into account of the user sentiments based on their reviews which has been mapped with 0.5 for Negative, 1 for Neutral and 2 for Positive.
- The idea of having this feature is incorporate within the model and eliminate the need for user to read on reviews to make sure that the recommended activity is a highly rated & reviewed activity.
2. Despite this model having quite similar recommendations with the base model, overtime with more reviews added to the database, the results would differ more. Since a large number of activities do not have ratings and reviews yet. Given the left-skewed distribution, the median value of ratings was imputed to activities without user ratings. This results in most of the attractions having a rating of (9.794), hence there is not much of a significant difference between the attraction similarity values between the models.

## Limitations:
- As the user reviews and ratings have been more established, usage of other hybrid model that would be able to filter out attractions/activities that has been lowly rated.
- Ability to filter by Months (Since some activities are bound by Seasons, e.g. winter activities)
- Ability to set a budget 
- Adding in other attributes to have a more inclusive recommender (E.g. Accessibility Feature such as Wheelchair, Family)

## Recommendations/ Future Works
- To scale the recommender geographically across the World.
- To expand the recommender to existing users.
- To add in User-based recommendation with implicit data and reviews of all attractions
- Expand to an itinerary planner with selected activities which would recommend place to stay and restaurants based on each day's itinerary