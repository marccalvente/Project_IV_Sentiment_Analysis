# Project IV: Sentiment Analysis on whatsapp chat
---
<center>
<img src=images/whatsapp_banner.png alt=“shark_title” width=“400”/>
</center>

<br>

### Abstract

The goal of this project is to perform a sentiment analysis by using the nltk library on the messages of a whatsapp group chat.

This info will be loaded to a SQL database and will be accessible through an api.

<br>

#### Getting a file with the data
- First the whatsapp group chat has to be exported by opening the app on your phone, accessing the group info, and selecting Export chat.

<br>

#### Importing the data to a dataframe
- Getting_dataset_ready file imports the data to a pandas DataFrame using the whatstk library.
- Then it cleans the data deleting non chat rows and translates the chats to english so a better sentiment analysis can be performed and saves it in a .csv file.

** It took 6h to translate 37000 messages so be aware.

<br>

#### Performing sentiment analysis
- sentiment_analysis file imports the .csv file generated in the step above and performs the sentiment analysis for the text messages and for the emojis used.
- Then it prepares the data for being loaded to the MySQL database and loads it.

<br>

#### Consulting the info via API


| **Endpoint** | **Description** |
| --- | --- |
| /sql | Returns everything contained at the database |
| /sql/name/\<username> | Returns all the messages from a user |
| /sql/date/\<date> | Returns all the messages from a date (YYYY-MM_DD format) |
| /sql/messages_score | Returns the sentiment score of the messages grouped by user |
| /sql/emojis_score | Returns the sentiment score of the emojis grouped by user |
| /insertrow | Inserts a new row in the chats table from the database |

The scores range from -1 to 1, with -1 being the most negative and 1 the most poitive possible values.