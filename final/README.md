### Final Exam 2017 : California Crime Analysis(1980 - 2000)

For the detailed analysis of this topic I have resided to NYTimesAPI article search. The data has been retrieved abd stored as per the requirement. Along with this we will be using few datasets povided by Kaggle. 

**Analysis 1**:
Identify the state with highest crime record from 1980 to 2000. Also, identify the season when crime rate sky rockets in the state.

> Key notes in analysis:
The analysis revolves around basically two data sets provided by Kaggle along with NYTimes API. We follow the below procedure to get the result of our first analysis:  
- Analysis begins with identifying the state with max average crime rate from 1980 to 2000. A spectral helps us to identify that California is one of the states with high crime rate in US.
![murder_rate_states](https://cloud.githubusercontent.com/assets/18182515/25310269/d83a3350-27ae-11e7-9e8b-d9a4c54ab4d5.png)
Image : Spectral map of crime rate across US
Output
[Murder_rate_states.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- From the initial analysis of GlobalLandTemperaturesByState we reach the conclusion that during the months of Jun - Sep the average temperature is high around all states in United States.  
![maxaveragetemp](https://cloud.githubusercontent.com/assets/18182515/25310267/cf565fac-27ae-11e7-96b3-398d949f5154.png)  
Image : Average temperature around US in a fiscal calendar
Output
[Monthyly_avg_tmp.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- Now we do our analysis and try to obtain a data matrix of average weather around the calendar in United States from 1980 to 2000. A heatmap can be used to accurately visualize the temperature pattern across California.
![monthly_temp_1980_20](https://cloud.githubusercontent.com/assets/18182515/25310268/d29b6c20-27ae-11e7-8f8c-5347e499438b.png)
Image : HeatMap of average temperature across various months from 1980 to 2000.
Output
[Monthly_temp_1980_20.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)
- Similarly we create a heatmap to visually understand the crime pattern(if one exists) across California from 1980 to 2000.
![homicide_california](https://cloud.githubusercontent.com/assets/18182515/25310264/bc9c28e2-27ae-11e7-85f9-850c3cad32bf.png)
Image: HeatMap of crime across California
Output
[Homicide_california.csv](https://github.com/praveen-sivadasan/Python/blob/master/final/data/processed/Analysis_1/Homicide_california.csv)

> Conclusion/Observations: 
- Comparing the two heatmap we can conclude that during the period October to May from 1980 to 2000 the crime rate used to increase. Also we can infer from the heatmap of California that during 1988 to 1993 the crime rate was extremely high. We will further analyse on the crime in California during this time frame.

**Analysis 2**
Identifying the reasons for increased murder rate in California during June to Sept from 1988 to 1993.

> Key notes in analysis:
This analysis goes a bit in depth in identifying the type and mode by which crimes were being done during his period. We follow the below procedure to get the result of our first analysis:
- Aanlysing the average crime rate from 1988 to 1993 infers that thers has been a constant alleviation in the crime rate starting 1988. We will plot a line chart in identifying the pattern.
![murder_rate_cali_yearly](https://cloud.githubusercontent.com/assets/18182515/25310303/8a463742-27af-11e7-91ec-a3d624595137.png)
Image: Line chart of average crime rate across California
Output
[Murder_rate_Cali_yearly.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- Further analysing the type of crime being happening in California we can infer that 90% of crimes where Murder/Slaughter and the rest was accidental.
![crime_type_cali](https://cloud.githubusercontent.com/assets/18182515/25310305/8e56b348-27af-11e7-9a4d-f6b8c2faffea.png)
Image: Bar chart representing crime type in California
Output
[Crime_type_Cali.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- The homicide reports also help us in concentrate on the method of murder hapeening across California. By creating a pie chart using various weapons used to perform murder, it reveals that most murder weere conducted using handguns.
![cali_murder_weapons](https://cloud.githubusercontent.com/assets/18182515/25310306/938ec80a-27af-11e7-8a32-60cbd8321448.png)
Image: Pie chart to represent the weapons used while murdering
Output
[Cali_murder_weapons.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- We will now analyse the NYtimes articles released about California to identify reason for such sudden gruesome atmoshpehere. Initial analysis close to gun killing in California from the articles published from NYTimes, we try to create a grpah plot using lines. The graph indicated that most of the reason behind such crime was discrimantion or hate crime followed by frauds and drugs.
![cali_concerns_1988](https://cloud.githubusercontent.com/assets/18182515/25310302/88cb5f78-27af-11e7-903d-994b35b4c334.png)
Image: Boxed line chart
Output
[Cali_concerns_1988.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

> Conclusion/Observations:
- Hence we can colcude by saying that  in California at this period there was a large amount of discrimination followed by murder and capital punishments. The amount of hate crime was really high during this period along with very less or no gun control. This hence has led to a series of violent crimes in California using handguns.

**Analysis 3**
Intial analysis shows that a lot of hate crime and less/no gun control has led to a large scale of murder rate in California during 1989 to 1993. We will further analyse the characteristics of these crime perpetuators and the circumstances that led them to these crimes.

- We now try to understand the type of perpetrators by collecting the age group. We ue a bar graph to visualize the data and the results were mind blowing. Major crimes where done by people between the age of 18 to 21. This further hints us the influence of drugs or lack of education by which they tend to follow such cruelsome path.
![crime_perpetrator_cali_1988](https://cloud.githubusercontent.com/assets/18182515/25310332/65a8da42-27b0-11e7-8e5a-eeccc392d6b8.png)
Image: Bar graph to depict age vs crime rate
Output
[Crime_perpetrator_Cali_1988.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- Now we have to understand if the reasons we thought about have any infulence on all genders. Identifying the sex of the perpetrator using a pie chart it shows that most of the crimes were done by men and women's contribution were miniscual.

Image: Pie chart
Output
[Crime_perpetrator_Cali_sex_1988.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)
- Since during one of our previous analysis it was proved that discrimination was one of the major concerns during this particular period, we will try to group data according to race and attempts to make some sense out of it. We will use a simple line chart to visualise the data. The results show that black people were the most among early 20's people who used to perform crimes in California, hence our assumption of hate crime existing at California was right.  
![cali_crime_perpetrator_race_1988](https://cloud.githubusercontent.com/assets/18182515/25310333/65a999fa-27b0-11e7-9bac-bd5a6b98d793.png)
Image: Line chart
Output
[Cali_crime_perpetrator_race_1988.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)
- We can further strongify our conclusion by finding the race of the victims who were murdered by black people. We will use a Facet grid to estimate the amount of attack done by black on other races. The results shows that there used to be more internal conflicts among blacks followed by attack on white.
![race_wars_cali_1988](https://cloud.githubusercontent.com/assets/18182515/25310335/65aa3db0-27b0-11e7-9fbc-3d0574d9ea26.png)
Image: Facet grid
Output
[Race_wars_Cali_1988.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

> Conclusion/Observations:
- Hence we can conclude that most of the murders in California used to happen in California due to internal beefs among blacks and lack of education or drugs could be major factor in these.

**Extra Analysis**
Analysing the crime after 1995 with crime during 1988.

- Our intial analysis will be to identify rate at which crime was happening during 1990's by people of various ages. Our analysis using bar plot indicates that crime rate was plummed down after 1995. This could be because of various gun laws which was passed by the state inorder to prevent the gun usage.
![crime_comparison_1988_1995_by_age](https://cloud.githubusercontent.com/assets/18182515/25310369/e1a02cd6-27b0-11e7-9efd-3fd6df316ba9.png)
Image: Facet grid age vs crime rate
Output
[Crime_comparison_1988_1995_by_age.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- We can hence also comapre the amount of incidents happened after 1995 using guns. A plot using bars shows that a good amount of crime rate dropped during mid 90's.  
![crime_comparison_1988_1995_by_weapon](https://cloud.githubusercontent.com/assets/18182515/25310368/e19eff6e-27b0-11e7-93b9-4f288e28dd25.png)
Image: Facet grid weapon vs crima rate
Output
[Crime_comparison_1988_1995_by_weapon.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

- Analysing the data sets to verify if new gun regulations where introduced or not, which inturn led to a drop in gun use in California. We analyse the articles released during both the times and do a comparison. After using a bar graph it shows that eventhough the law and regulation were discussed almost at the same pace there was a tremendous increase in the discussion of referrendums and schooling and education in California.
![article_comparison_1988_1995](https://cloud.githubusercontent.com/assets/18182515/25310367/e19c4bd4-27b0-11e7-9ee8-68e8f26c70ae.png)
Image: Facet grid - rate at which newer topics were discussed
Output
[article_comparison_1988_1995.csv](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

> Conclusion/Observations:
- Hence we can conclude that by mid 90's there was a lot a discussion reagrding laws and regulations. Apart from that schooling and education was also widely discussed. This may have helped the society to help the people from early 20's to put their efforts in something useful towards the community rathe than involving in crimes like murder and drugs.



