# TwinkerBot

https://youtu.be/W4SHebbPJD8

# Required libraries

  - Python 3
  - Tensorflow 1.0.0
  - numpy
  - tweepy

# Instructions

    -Download the twitter pre-trained model, and dropt the files inside to the corresponding folder on /ckpt/twitter. Confirm the override of the 'checkpoint' file. https://drive.google.com/file/d/0B9ZysvmClMHZME5PVk9aekhQM1U/view?usp=sharing
    -Do the same for the cornell pre-trained model, and drop it on /ckpt/cornell: https://drive.google.com/file/d/0B9ZysvmClMHZQVQ3ZEJHa09ZWE0/view?usp=sharing.
    
    - If you desire to continue the training, just run CornellTraining.py or twitter_training.py depending on which model you want (Check the git repository for the updated link of the data).
    
    -If you want to test withouth twitter, you can use chatlog.py for twitter data set and cornellchatlog.py, the output of the first one will be on testtraining.txt and for the second one on CornellTraining.txt
    
    -Finally if you want to chat with the bot on twitter just run Playground.py. It will ask for a data model, just input cornell or twitter
    
    
