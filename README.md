# tsrewritebot
Python Twitterbot rewriting the earwormiest of Taylor Swift lyrics with NLTK.

[@tsrewrite](https://twitter.com/tsrewrite) is a Taylor Swift lyric rewriting Twitter Bot. It tweets rewritten song lyrics. A full explanation of how the bot selects words and builds new lyrics is [here](http://katieamazing.com/todo/).

These Python 2.7 scripts power @tsrewrite. The current deployment is complicated by the very large pre-trained model I use for similarity vectors. At present, I generate a large set of tweets locally, monthly, and upload them to PythonAnywhere's cloud where they are tweeted twice daily using Twython as a cron job.
