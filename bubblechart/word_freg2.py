__author__ = 'Sophie'
import os

stopwords = []
stop_file = open("C:/Users/Sophie/Documents/DataViz/presentation/stopwords.txt", "r")
for word in stop_file:
    word = word.strip("\n")
    stopwords.append(word)

comment_dir = "C:/Users/Sophie/Documents/DataViz/presentation/data"
comment_data = {}
for file in os.listdir(comment_dir):
    print(file)
    comment_file = open('C:/Users/Sophie/Documents/DataViz/presentation/data/' + file, "r")
    # Initialize a counter for the lines
    line_number = 0
    # initialize a dict
    # Read each line one at a time
    i = 0
    for line in comment_file:
        i += 1
        # Increment line number
        line_number += 1
        # Split that string into a list, separate by commas
        comment_list = line.split(",")
        # No data until line 2, so start at line 2
        if line_number >= 2:
            videoID = comment_list[0].strip()
            comment = comment_list[1].strip()
            channelID = comment_list[2].strip()
            word_list = comment.split(" ")

            if videoID in comment_data:
                videoID_dict = comment_data[videoID]
                for word in word_list:
                    word = word.lower()
                    word = word.strip('",.!?*()$#@:/><')
                    if word != "" and word not in stopwords:
                        if word in videoID_dict:
                            videoID_dict[word] += 1
                        if word not in videoID_dict:
                            videoID_dict[word] = 1
            if videoID not in comment_data:
                comment_data[videoID] = {}
                videoID_dict = comment_data[videoID]
                for word in word_list:
                    word = word.lower()
                    word = word.strip('",.!?*()$#@')
                    if word != "" and word not in stopwords:
                        if word in videoID_dict:
                            videoID_dict[word] += 1
                        if word not in videoID_dict:
                            videoID_dict[word] = 1

videoID_counter = 1
toString = ""
for video in comment_data:
    print(videoID_counter)
    videoID_counter += 1
    comment_dict = comment_data[video]
    for word in comment_dict:
        if comment_dict[word] > 1:
            toString = toString + video + "," + word + "," + str(comment_dict[word]) + "\n"

print(toString)

myFile = open("word_frequency6.csv", "w")
header = "videoID,word,frequency\n"
myFile.write(header)
myFile.write(toString)
comment_file.close()
myFile.close()


