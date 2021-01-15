import preprocessor as p


class TweetUtils:
    def __init__(self):
        p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.RESERVED, p.OPT.SMILEY, p.OPT.NUMBER, p.OPT.HASHTAG)

    def clean_tweet(self, text):
        result = p.clean(text)
        return result
