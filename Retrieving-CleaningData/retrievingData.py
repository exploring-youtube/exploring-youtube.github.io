# Sample Python code for user authorization

import os
import time
import csv

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

allChannels = {"JakePaul": ["user", "JakePaulProductions"]}
#                ,"LoganPaul":["channel","UCG8rbF3g2AMX70yOd8vqIZg"],
#                "JennaMarbles":["user","JennaMarbles"],
#                "ShaneDawson":["user","shane"],
#                "LizaKoshyToo": ["channel","UChoTvF02Cv74FF72OaJtTMA"],
#                "Superwoman":["user","IISuperwomanII"],
#                "DavidDobrik":["channel","UCmh5gdwCx6lN7gEC20leNVA"],
#                "KianAndJC": ["user","KianAndJc"],
#                "AceFamily":["channel","UCWwWOFsW68TqXE-HZLC3WIA"],
#                "RomanAtwoodVlogs":["user","RomanAtwoodVlogs"],
#                "Shaytards":["user","SHAYTARDS"],
#                "KYRsp33dy":["user","KYRSP33DY"],
#                "Fitz":["channel","UCtb8P4rf_1n8KS8eZk_lNNw"],
#                "Seananners":["user","SeaNanners"],
#                "Vanoss":["user","VanossGaming"],
#                "Hutch":["user","shaun0728"],
#                "JeffreeStar":["user","jeffreestar"],
#                "MannyMUA":["user","MannyMua733"],
#                "JamesCharles":["channel","UCucot-Zp428OwkyRm2I7v2Q"],
#                "JaclynHill":["user","Jaclynhill1"],
#                "LauraDIY":["user","LaurDIY"],
#                "BethanyMota":["user","Macbarbie07"],
#                "SafiyaNygaard":["channel","UCbAwSkqJ1W_Eg7wr3cp5BUA"],
#                "BuzzFeed":["user","BuzzFeedVideo"],
#                "Peta":["user","officialpeta"],
#                "FarmSanctuary":["user","farmsanctuary1"],
#                "MercyForAnimals":["user","mercyforanimals"],
#                "TheDodo":["user","TheDodoSite"]
#               }
channelVideos = {}
channelComments = {}
tryAgain = []

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def channels_list_by_username(service, **kwargs):
    results = service.channels().list(
        **kwargs
    ).execute()
    print("CHANNEL:")
    print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
          (results['items'][0]['id'],
           results['items'][0]['snippet']['title'],
           results['items'][0]['statistics']['viewCount']))

    channelTitle = results['items'][0]['snippet']['title']
    #print(results['items'][0])
    #print("# Videos:")
    #print(results['items'][0]['statistics']['videoCount'])
    numVideos = results['items'][0]['statistics']['videoCount']
    numSubscribers = results['items'][0]['statistics']['subscriberCount']
    #print(results['items'][0]['contentDetails'])
    #print(numVideos)

    #reutnring video id for 1st video
    return(numSubscribers,channelTitle, numVideos,results['items'][0]['contentDetails']['relatedPlaylists']['uploads'])

def playlist_items_list_by_playlist_id(numVideos,channelVideos, client, **kwargs):
  # See full sample for function
 # kwargs = remove_empty_kwargs(**kwargs)
    #print(numVideos)
    #print("PLAYLIST:")
    response = client.playlistItems().list(
      **kwargs
    ).execute()

    #print("Video Title:")
    #print(response["items"][0]['snippet']['title'])

    #print("Video ID:")
    #print(response["items"][0]['snippet']['resourceId']['videoId']) #['resourceId']['videoId'])
    #print("ALL:")
    print(response)


    #Bc max range is 50, only use 50 videos not numVideos
    for i in range(50):
        id = response['items'][i]['snippet']['resourceId']['videoId']
        title = response["items"][i]['snippet']['title']
        if id not in channelVideos:
            channelVideos[id]= title.encode('utf-8')
        else:
            print("already exists")
        #print(i)
    #print(channelVideos)
    #return(response["items"][0]['snippet']['resourceId']['videoId'])
    #print(response['nextPageToken'])
    return response['nextPageToken']

def videos_list_by_id(client, **kwargs):
  # See full sample for function
  #kwargs = remove_empty_kwargs(**kwargs)
    #print(channelVideos)

    #print("VIDEOS:")
    response = client.videos().list(
        **kwargs
    ).execute()

    #print("ALL:")
    #print(response['items'][0]['statistics'])
    stats = ["NA","NA","NA","NA","NA"]
    try:
        #print("# Views:")
        numViews = response['items'][0]['statistics']['viewCount']
        #print(numViews)


        #print("# Comments:")
        numComments = response['items'][0]['statistics']['commentCount']
        #print(numComments)


        #print("# Favorites:")
        numFavs = response['items'][0]['statistics']['favoriteCount']
        #print(numFavs)

        #print("# Likes:")
        numLikes = response['items'][0]['statistics']['likeCount']
        #print(numLikes)


        #print("# Dislikes:")
        numDislikes = response['items'][0]['statistics']['dislikeCount']
        #print(numDislikes)

        #print("All0:")
        #print(response['items'][0])

        #print("Tags:")
        #print(response['items'][0]['snippet']['tags'])


        #print("Published:")
        dateAndTimeUploaded = response['items'][0]['snippet']['publishedAt']
        #print(dateAndTimeUploaded)

        #print("PageInfo:")
        #print(response['pageInfo'])

        stats = [numViews.encode('utf-8'),
                 numComments.encode('utf-8'),
                 numLikes.encode('utf-8'),
                 numDislikes.encode('utf-8'),
                 dateAndTimeUploaded.encode('utf-8')]
    except:
        print("no stats")
    return(stats)

    #print("ALL:")
    #print(response)

def comment_threads_list_by_video_id(client, **kwargs):
    # See full sample for function
    #kwargs = remove_empty_kwargs(**kwargs)

    response = client.commentThreads().list(
        **kwargs
    ).execute()

    #print("Comment:")
    #print(response['items'][0]['snippet']['topLevelComment'])
    # print("Text:")
    # print(response['items'][0]['snippet'])#s['topLevelComment']['snippet']['textOriginal'])
    comments = []
    for i in range(100):
        #print("Text:", i)
        #print(response['items'][i]['snippet'])  # s['topLevelComment']['snippet']['textOriginal'])
        text = response['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal']
        #print(text)
        text = text.strip('\n')
        text = text.strip('\t')
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        text = text.replace(',', ' ')
        comments.append(text)

    #print comments
    token = response['nextPageToken']
    return token, comments
    #print(response)

#def get_comments():

# def tryAgain(dict):
#     #gets comments per video in channelVideos dictionary
#     for videoID in dict:
#         #print(videoID)
#         try:
#             token, comments = comment_threads_list_by_video_id(service,
#                                             part='snippet,replies',
#                                             maxResults = 100,
#                                             videoId=videoID)
#             #time.sleep(1)
#             for i in range(9):
#                 #time.sleep(1)
#                 token, nextComments = comment_threads_list_by_video_id(service,
#                                                                 part='snippet,replies',
#                                                                 maxResults=100,
#                                                                 pageToken = token,
#                                                                 videoId=videoID)
#                 comments.extend(nextComments)
#                 #print(len(comments))
#         except:
#             print("stupid piece of shit still isn't working")
#             comments = []
#             if videoID not in tryAgain:
#                 tryAgain[videoID] = False
#             else:
#                 print("already exists in tryAgain")
#
#         time.sleep(1)
#         #adds comments to channelComments dictionary
#         if not comments:
#
#         if videoID not in channelComments:
#             print(videoID)
#             channelComments[videoID]= comments
#         else:
#             print("already exists in channelComments")
#     return dict

if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()

    for channelStr in allChannels:
        #Replace with channel's user or channel ID
        lst = allChannels[channelStr]
        idStr = lst[1]
        start = lst[0]

        #if you're using CHANNELID use this code
        #returns the channel's title and total number of videos
        if start == "channel":
            numSubscribers,channelTitle, numVideos,uploadsID = channels_list_by_username(service,
                                part='snippet,contentDetails,statistics',
                                id= idStr)

        #if you're using USDERID use this code
        #returns the channel's title and total number of videos
        if start == "user":
            numSubscribers,channelTitle, numVideos,uploadsID = channels_list_by_username(service,
                                part='snippet,contentDetails,statistics',
                                forUsername= idStr)

        #adds the channel's videos' ID to a dictionary (max 50 videos)
        #returns nextPageToken to get videos past the maxed number
        token = playlist_items_list_by_playlist_id(numVideos, channelVideos, service,
                                           part='snippet,contentDetails',
                                           maxResults= 50,
                                           playlistId= uploadsID)

        #run again w/ pageToken to retrieve 150 more videos
        n = 1
        if numVideos < 200:
            n=3
        for i in range(n):
            #print("a")
            token = playlist_items_list_by_playlist_id(numVideos, channelVideos, service,
                                               part='snippet,contentDetails',
                                               maxResults= 50,
                                               pageToken = token,
                                               playlistId= uploadsID)

        #returns stats for all videos in the channelVideos dictionary
        for videoID in channelVideos:
            #print(videoID)
            #print(channelVideos[videoID])
            #stats list includes # views, # likes, # dislikes, date video was uploaded
            stats = videos_list_by_id(service,
                          part='snippet,contentDetails,statistics',
                          id= videoID)
            #print("here")
            vidTitle = channelVideos[videoID].replace(',', ' ')
            #adding video title, video ID and channel title to stats list
            stats.append(vidTitle)
            stats.append(idStr)
            stats.append(channelTitle)
            stats.append(numSubscribers)
            #updates dictionary value to stats list
            channelVideos[videoID] = stats

        #writes video stats to CSV
        #header: videoId (key), views, commmets, likes, dislikes, dateUploaded, videoTitle, channelId, channelName
        fileStr  = channelStr + ".csv"
        with open(fileStr, 'w') as file:
            file.write('videoId,views,comments,likes,dislikes,dateUploaded,videoTitle,channelId,channelName,subscribers')
            file.write('\n')
            for videoID in channelVideos:
                #ignores any videos whose title was giving an error due to emojis or other characters not in ASCII
                try:
                    row = videoID + "," + ",".join(channelVideos[videoID])
                    file.write(row)
                    file.write('\n')
                except:
                    print("there was a problem")
                #print(row)
        #time.sleep(1)
        #channelVideos = {}




    #tryAgain = {}
    #gets comments per video in channelVideos dictionary
        #print(channelVideos)
        for videoID in channelVideos:
            #print(videoID)
           # try:
                #print("yaass")
                token, comments = comment_threads_list_by_video_id(service,
                                                part='snippet,replies',
                                                maxResults = 100,
                                                videoId=videoID)
                #time.sleep(1)
                #for i in range(9):
                    #time.sleep(1)
                token, nextComments = comment_threads_list_by_video_id(service,
                                                                    part='snippet,replies',
                                                                    maxResults=100,
                                                                    pageToken = token,
                                                                    videoId=videoID)
                comments.extend(nextComments)
                #print(comments)
                    #print(len(comments))
            # except:
            #     print("stupid piece of shit still isn't working")
            #     comments = []
            #     if videoID not in tryAgain:
            #         tryAgain[videoID] = False
            #     else:
            #         print("already exists in tryAgain")

                time.sleep(1)
            #adds comments to channelComments dictionary
                if videoID not in channelComments:
                    print(videoID)
                    channelComments[videoID]= comments
                else:
                    print("already exists in channelComments")
        #print(channelComments)
        #writes out all comments into CSV file
        #header: videoID (key), comment, channelId, channelName
        cmmtfileStr = channelStr + "Comments.csv"
       # print(cmmtfileStr)
        with open(cmmtfileStr, 'w') as file:
            file.write('videoId,comment,channelId,channelName')
            file.write('\n')
            for videoID in channelVideos:
                commentList = channelComments[videoID]
                for comment in commentList:
                    try:
                        row = videoID + "," + comment.strip() + ","  + channelTitle + "," + idStr
                        file.write(row)
                        file.write('\n')
                    except:
                        print("there was a problem")

        channelVideos = {}
        channelComments = {}
