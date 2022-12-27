import tweepy
import openai
import json

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAGxbkwEAAAAAnR1Ro4HFLhMp7R6hN%2BupXMvqjvs%3Dx0mx5GuD3iiMFsRjhDW37qROlRyFqPRtefVyE58Rb4LF1rB4WZ")

hashtag = "gpt3"
response = client.search_recent_tweets(query=hashtag, max_results=10)

for tweet in response.data:  

  openai.api_key = "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"
prompt = f"Haz un resumen de los ultimos 10 tweets con el hashtag '{hashtag}', no utilices acentos ni la letra ñ en el texto:"
model_engine = "text-davinci-003"
completion = openai.Completion.create(engine=model_engine, prompt=prompt, temperature=0.2, max_tokens=500, top_p=1, frequency_penalty=1, presence_penalty=1)
summary = completion

print(summary)
print(tweet.text);
 
  




from flask import Flask, render_template
app = Flask(name)

@app.route('/')
def home():
    return render_template('home.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

  #print(tweet.text);
  #
  # print(tweet.created_at)
  # print(tweet.user.screen_name)
  # print(tweet.user.name)
  # print(tweet.user.profile_image_url)
  # print(tweet.user.id)
  # print(tweet.user.location)
  # print(tweet.user.url)
  # print(tweet.user.description)
  # print(tweet.user.followers_count)
  # print(tweet.user.friends_count)
  
