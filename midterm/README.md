###Midterm Exam 2017

**Question 1**:
Use Enron data set to perform 3 analysis.

Analysis:
Enron Corporation was an American energy, commodities, and services company which On December 2 2001 filed for Chapter 11 protection, becoming the largest bankruptcy in U.S. history at that time. It  was later revealed that its reported financial condition was sustained by institutionalized, systematic, and creatively planned accounting fraud, known since as the Enron scandal.

**Analysis 1**

Analysing the inbox and sentbox of Founder of Enrorn "Jeffrey Skilling" for suspicious activities.In August 2001 Skilling resigned and sold almost $60 million in Enron shares.In 2006, Skilling was convicted of multiple federal felony charges, including insider trading, securities fraud, and making false statements to auditors.
> Key notes in analysis:
- Focusses onsSet of emails between January 2000 (period when stock price of Enron started to rise to a record high of US$90.75 per share) and August 2001 (when Jeffrey resigned as CEO of Enron).
- Retrieves the list of people who contacted Skilling frequently during the period on a monthly basis.
- Retrieves the list of pople who were contacted by Skilling on a monthly basis and identifies the most interacted individual. 

> Libraries
- nltk, os, glob, email, datetime, email.utils, time, datetime

Output
[Q1Analysis1Output.txt](https://github.com/praveen-sivadasan/Python/files/823082/Q1Analysis1Output.txt)

> Conclusion/Observations:
- During the period Skilling has frequently contacted(approx. 10 times) a private equity and venture capital firm based in New York. The email, eharris@insightpartners.com, belongs to Erica Harris of Insight Partners.


**Analysis 2**

Analysing the emails of enron employees for descrepencies with keywords "bankrupt", "fraud", "shutdown". Finding out the people who used these between below mentioned dates. Also analyse on which months theses word were used mostly.<br>
> Key notes in analysis:
- Start date of analysis is August 2001, Jeffrey Skilling resigned as CEO of Enron. 
- End date of analysis is December 2, 2001 - Enron files for Chapter 11 protection, becoming the largest bankruptcy in U.S. history.

Output
[Q1Analysis2Output.txt](https://github.com/praveen-sivadasan/Python/files/823087/Q1Analysis2Output.txt)

> Conclusion/Observations:
- Jeff Dasovich, Enron governmental affairs executive, and Steven Kean, Enron’s former chief of staff, seems to have used the word 'bankrupt' a lot in their sent emails.
- Was able to identify the months on which these keywords where used mostly, thereby leading way to further cut short the emails to focuss on.

**Analysis 3**

Analysing the communication between Enron employees and Arthur Andersen LLP, the accounting firm associated with Enron Corporation.<br>

U.S. Justice Department indicted Arthur Anderson in March 14, 2002 for obstruction of justice. Later in 2002, the firm voluntarily surrendered its licenses to practice as Certified Public Accountants in the United States after being found guilty of criminal charges relating to the firm's handling of the auditing of Enron.
> Key notes in analysis:
- Emails between January 2000 few months before Enron stocks sky rocketed and January 2002 when Enron ended partnership with the accounting firm, days after SEC widens its investigation to Arthur Anderson.
- Mapping employees to emails they have send with reference to Arthur Anderson.
- Identify top most months where Arthur Anderson was referred on emails.

> Libraries
- nltk, os, glob, email, datetime, re, email.utils, time, datetime

Output
[Q1Analysis3Output.txt](https://github.com/praveen-sivadasan/Python/files/823090/Q1Analysis3Output.txt)

> Conclusion/Observations:
- Arthur Anderson employees with emails randy.g.kruger.jr@arthuranderson.com, michael.abraham@us.arthuranderson.com, kimberly.r.scardino@us.arthuranderson.com where contacted frequently during the period.
- Identified Enron employees who have contacted Arthur Anderson more during or just before the crisis.
- In April-2001, 3 months before Jeffrey Skilling resigns as CEO and Kenneth Lay becomes CEO again, Arthur Anderson was most contacted.

**Question 2**:

Use NYT API to collect NYT data. Perform 3 analysis on the collected data.

**Analysis 1**

Finding the most disussed person under each sport category in New York Times between 2010 and 2016.
> Key notes in analysis:
- Using NYT Article Search API
- Using requests, configparser, os, sys, json, glob and pos_tag from nltk.tag
- Downloading and storing data in appropriate location
- Identifying athlete names using ProperNoun (NNP of post_tag) and ne_chunk of chunk.

> Libraries
- requests, configparser, os, sys, json, glob, nltk.tag

Output
[Q2Analysis1Output.txt](https://github.com/praveen-sivadasan/Python/files/823091/Q2Analysis1Output.txt)

> Conclusion/Observations:
- In sorted order sports are displayed with most discussed player names in descending order.
- Was able to identify the most frequently used names in the sports articles. For ex: Srilanka was the most discussed team in Cricket and Tiger Woods was the most discussed golf player.

**Analysis 2**

Finding the most discussed sports in New york Times between 2010 and 2016.
> Key notes in analysis:
- Using NYT Article Search API
- Using requests, configparser, os, sys, json, glob
- Downloading and storing data in appropriate location

> Libraries
- requests, configparser, os, sys, json, glob

Output
[Q2Analysis2Output.txt](https://github.com/praveen-sivadasan/Python/files/823096/Q2Analysis2Output.txt)

> Conclusion/Observations:
- Most discussed sports from sports articles published by NYTimes are displayed in descending order of their occurence.
- Soccer was the most discussed sport followed by College Basketball.

**Analysis 3**

2016 November is the month where US presidency election took place between Trump and Hilary. This analysis focus on the stand of NYTimes towards each contestants, by analysing the kind of articles published in their newspaper.

> Key notes in analysis:
- Conducting sentimental analyis on the articles published during the election month,November 2016
- Only considering articles focussing on a contestant directly
- Analysing on which months a contestant was favored by counting the frequency of neutral or positive articles.
- Graphical representation of results

> Libraries
- nltk, requests, configparser, os, sys, json, glob, datetime, time, email, matplotlib.pyplot,nltk.sentiment.vader

Output
[Q2Analysis3Output.txt](https://github.com/praveen-sivadasan/Python/files/823097/Q2Analysis3Output.txt)

![q2a3img](https://cloud.githubusercontent.com/assets/18182515/23638031/2eb81caa-02ad-11e7-8224-ae1a4055e750.png)

> Conclusion/Observations:
- Sentimental of article headlines gave a rough estimate of 150, published against Trump and 52 for Trump.
- Similarly for Hilarly there where only 30 articles published against her.
- Analysis also indicates that 22 of 30 articles against Hilary for the month of November where published between 1st November and 8th November (Election day US).

