Simple shell script which makes it easy to keep to use youtube-dl to sync 
youtube videos. Reccomended use is as a periodic script for cron to run, 
to keep stuff up to date. 

Usage: set up the youtube-dl.config file with the video or playlist you want, 
flags for youtube-dl to use, and the directory to put the result. 

Config Format: 
[url] [flags] [directory]
