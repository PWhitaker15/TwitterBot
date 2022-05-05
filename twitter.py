from discord.ext import commands, tasks
import tweepy, time

token = '**************************************************'


bot = commands.Bot(command_prefix='!')

consumer_key = '******************'
consumer_secret = '**************************************************'
access_key = '**************************************************'
access_secret = '**************************************************'

client_id = '******************************'
client_secret = '******************************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


@bot.event
async def on_ready():
    social_check.start()
    print('bot active')


@tasks.loop(seconds=5)
async def social_check():
    oldTweet = []
    twitter = api.user_timeline(screen_name='USF_Esports', count=1, exclude_replies=True, include_retweets=False)
    for status in twitter:
        tweetID = status.id
    channel = bot.get_channel(***************)
    hist = await channel.history(limit=50).flatten()
    for msg in hist:
        oldTweet.append(msg.content)
    newTweet = f'https://twitter.com/USF_Esports/status/{tweetID}'
    if newTweet not in oldTweet:
        if newTweet not in oldTweet:
          await channel.send(f'https://twitter.com/USF_Esports/status/{tweetID}')


bot.run(token)
