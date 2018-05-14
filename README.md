# exploring-youtube.github.io
#videos

Exploring YouTube Data by Jen Cruz-Hernandez and Sophie Fuller
CS360 Data Visualization Final Project

Link to presentation slides: https://docs.google.com/presentation/d/1VVzOKCK65eRaR5Nf6ztUaMBrlGkjfgHRGLo965wO50A/edit?usp=sharing

Link to website: https://exploring-youtube.github.io/

All D3 and HTML are in index.html.  It is commented with different functions for handling all of our visualizations.

The Python code written to retrieve data from the YouTube API is in a folder labeled Retrieving-CleaningData

The folder labeled data has all the data we need to make the visualizations.  Comment data and individual channel data are in their own folders and word files are held in there too. 

The links to all the thumbnails and an early version of the buttons are in a folder called thumbnails.

In a folder labeled docs are early versions of our index.html files and the code needed to generate it.

The code for producing the line chart is in a folder called linechart.

The Python code for generating word frequencies and the code for making a bubble chart which was later integrated into index.html are in a folder called bubblechart

Using our website:
Click on a YouTuber to view their videos on the YouTube logo. Their videos will be colored red. If a video was posted before the policy change, it will be light grey and, if it was posted after the change, it will be dark grey. Once that video is clicked on, some stats for that video will appear. Above the button will be the YouTuber's channel name, number of subscribers, and number of views.  Clicking on the name will send you to their channel.

Once a channel is selected, the line chart updates with the number of views over time of that channel's 100 most recent videos. A vertical dark grey line denotes the policy change in relation to their views. If a video is selected, a thumnail of their video and like/dislikes, number of views, and number of comments appears. Clicking on the thumbnail will link you to this video on YouTube. 

Below that will be a bubble chart of the 200 most recent comments. If the word frequency is greater than 1, that word will appear in its own circle, sized according to the frequency. There is a simple tooltip when a word is hovered over. 
