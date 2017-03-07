###Midterm Exam 2017

**Question 1**:
Use Enron data set to perform 3 analysis.

Analysis:
Enron Corporation was an American energy, commodities, and services company which On December 2 2001 filed for Chapter 11 protection, becoming the largest bankruptcy in U.S. history at that time. It  was later revealed that its reported financial condition was sustained by institutionalized, systematic, and creatively planned accounting fraud, known since as the Enron scandal.

**Analysis 1**

Analysing the inbox and sentbox of Founder of Enrorn "Jeffrey Skilling" for suspicious activities.In August 2001 Skilling resigned and sold almost $60 million in Enron shares.In 2006, Skilling was convicted of multiple federal felony charges, including insider trading, securities fraud, and making false statements to auditors.
> The analysis focusses on
- Set of emails between January 2000 (period when stock price of Enron started to rise to a record high of US$90.75 per share) and August 2001 (when Jeffrey resigned as CEO of Enron).
- Retrieves the list of people who contacted Skilling frequently during the period.
- Retrieves the list of pople who were contacted by Skilling and iedntifies the most interacted individual. 

Output
[Q1Analysis1Output.txt](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

> Conclusion:

**Analysis 2**

Analysing the emails of enron employees for descrepencies with keywords "bankrupt", "fraud", "shutdown". Finding out the people who used these between below mentioned dates. Also analyse on which months theses word were used mostly.<br>
>Key notes:<br>
- Start date of analysis is August 2001, Jeffrey Skilling resigned as CEO of Enron. 
- End date of analysis is December 2, 2001 - Enron files for Chapter 11 protection, becoming the largest bankruptcy in U.S. history.

Output
[Q1Analysis2Output.txt](https://github.com/praveen-sivadasan/Python/files/823087/Q1Analysis2Output.txt)

>Conclusion: Analysis helps in:
- Identifying the Enron employees who used these critical keywords frequently.
- Understanding on which months which keywords where used, thereby providing hints to any kind of conspiracy present during the period.

**Analysis 3**

Analysing the communication between Enron employees and Arthur Andersen LLP, the accounting firm associated with Enron Corporation.<br>

U.S. Justice Department indicted Arthur Anderson in March 14, 2002 for obstruction of justice. Later in 2002, the firm voluntarily surrendered its licenses to practice as Certified Public Accountants in the United States after being found guilty of criminal charges relating to the firm's handling of the auditing of Enron.

> The analysis focusses on
- Emails between January 2000 few months before Enron stocks sky rocketed and January 2002 when Enron ended partnership with the accounting firm, days after SEC widens its investigation to Arthur Anderson.
- Mapping employees to emails they have send with reference to Arthur Anderson.
- Identify top most months where Arthur Anderson was referred on emails.

Output
[Q1Analysis3Output.txt](https://github.com/praveen-sivadasan/Python/files/823090/Q1Analysis3Output.txt)

> Conclusion: Analysis helps in:
- Identifying Enron emails who have contacted Arthur Anderson more during or just before the crisis.


**Question 2**:

Use NYT API to collect NYT data. Perform 3 analysis on the collected data.

**Analysis 1**

Finding the most disussed person under each sport category in New York Times between 2010 and 2016.

>Key notes:
- Using NYT Article Search API
- Using requests, configparser, os, sys, json, glob and pos_tag from nltk.tag

Output
[Q2Analysis1Output.txt](https://github.com/praveen-sivadasan/Python/files/823091/Q2Analysis1Output.txt)

**Analysis 2**

Finding the most discussed sports in New york Times between 2010 and 2016.

>Key notes:
- Using NYT Article Search API
- Using requests, configparser, os, sys, json, glob

Output
[Q2Analysis2Output.txt](https://github.com/praveen-sivadasan/Python/files/823096/Q2Analysis2Output.txt)

**Analysis 3**

2016 November is the month where US presidency election took place between Trump and Hilary. This analysis focus on the stand of NYTimes towards each contestants, by analysing the kind of articles published in their newspaper.

>Key notes:
- Conducting sentimental analyis on the articles published during the election month,November 2016
- Only considering articles focussing on a contestant directly
- Analysing on which months a contestant was favored by counting the frequency of neutral or positive articles.
- Graphical representation of results
- Used following nltk, requests, configparser, os, sys, json, glob, datetime, time, email, matplotlib.pyplot,nltk.sentiment.vader

Output
[Q2Analysis3Output.txt](https://github.com/praveen-sivadasan/Python/files/823097/Q2Analysis3Output.txt)

![q2a3img](https://cloud.githubusercontent.com/assets/18182515/23638031/2eb81caa-02ad-11e7-8224-ae1a4055e750.png)

