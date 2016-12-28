# daily-title-stats
This repository contains the data file and python script used to perform some rudimentary analysis of the relationship between the titles and page views of Stanford Daily articles published in 2016.  Below is a summary of the results.

## Results Summary

We measured the correlation between certain aspects of article titles and their corresponding total page views.  It is important to keep in mind that correlation does not imply causation and so these results should not necessarily be interpreted as a "how to guide" on writing an article title that attracts attention.

Overall, no single aspect of a title correlated strongly with page views, but there were some slight relationships (outlined below) which may still be of interest.

## Title Length

Articles with titles that were longer in character length were slightly associated with lower page views (correlation: -0.042), and articles with titles that were longer in number of words were also associated with a lower page view count (correlation: -0.049).  This means that shorter articles with shorter titles, in both word count and character count, had slightly higher page views.  This result makes intuitive sense because a shorter title conveys a message faster and short titles are often more clever or interesting than a longer title, prompting readers to click on the article more frequently.

Interestingly enough, articles with titles that used longer words on average were slightly associated with higher page views (correlation: 0.021)

## Certain Characters in Title

### Colon

Articles that used one or more colons in the titles were slightly associated with higher page views (correlation: 0.047).

Articles with colon(s) in the title had 166 views on average and those without had 126 views on average.

### Comma

Articles that used one or more commas in the titles were slightly associated with lower page views (correlation: -0.030).

Articles with comma(s) in the title had 113 views on average and those without had 141 views on average.

### Exclamation Mark

Articles that used one or more exclamation marks in the titles were very slightly associated with lower page views (correlation: -0.007).

Articles with exclamation mark(s) in the title had 112 views on average and those without had 137 views on average.


## Further Analysis

Plenty additional anaylsis could be performed on this data, such as analyzing the tone of the words in the title and looking at the difference in these relationships when articles are broken into the specific sections of the Daily.