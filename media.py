import webbrowser

class Movie():
  """This class contains information for a movies (title,
     storyline, poster url, and trailer url)"""
  
  def __init__(self, movie_title, movie_storyline, poster_url, trailer_url):
      self.title = movie_title
      self.storyline = movie_storyline
      self.poster_image_url = poster_url
      self.trailer_youtube_url = trailer_url

  def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)
