when the user write a new post and add it into posts by using E -addpost command
The program would inform the user the keywords in the post that can be transcludes
in my program there are four keywords that can be transcluded:
@weather, @temperature from the OpenWeather.py
@album, @lastfm from the LastFM.py

program would ask user whether to transclude these keywords or not
when user said yes,
it would send request to the OpenWeather API used the api key with my account 67fcab5c53747315abd0075d15383708 and the zipcode 92697 to get the weather and temperature now in Irvine
and it would replace the @weather and @temperature in the post if it exists with message from OpenWeather

Also, it would do the same thing with LastFM
the @album and @lastfm would be replaced by the album name and the singer name

And then it would ask whether to send the transcluded post to the server
if user said yes, it would send to the server.

And there are two unittest that test two transclude function