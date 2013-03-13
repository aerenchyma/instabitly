##**instabitly**

... is a command-line script in Python to import any links you've saved in [Instapaper](http://www.instapaper.com) to [bit.ly](http://www.bitly.com). 

It assumes you have an account on both sites and have saved a bunch of links in Instapaper that you now want saved in your bit.ly account, either for access to bit.ly stats and APIs with respect to the links, for shortened URLs, for searching without paying money*, or any other reason -- why else would you be running this?

It's heavily commented for those who want to know exactly how it works, in particular if you're new to Python/programming. 

It's also a recent development because this was functionality I wanted, so it'll later be prettier and full of More Options. See _**TODOS**_, below.

*<small>Instapaper does not allow you to search links you've saved without a subscription. This costs money and requires you to be able to pay via PayPal/by card online. However, it costs only $3/3 months, so effectively $1/month, and is worth it if the service is valuable to you. It's awesome software and I thoroughly support [supporting it](http://www.instapaper.com/subscription)! That said, I wanted this for other reasons. And thus.</small>

##**requirements**

To run this script as-is, you must have a file ```secure_info_instabitly.py``` in the same directory as the script, which need contain only one line:

```oauth_token = "yourbitlyoauthtokengoeshere"```

You can acquire an oauth token for the bit.ly APIs [here](https://bitly.com/a/oauth_apps) (again, assuming you have a _bit.ly_ account), and find their API documentation (which is awesome) [here](http://dev.bitly.com/links.html).

**Dependencies:**
[requests](http://docs.python-requests.org/en/latest/)
[mechanize](https://pypi.python.org/pypi/mechanize/)

both can be installed with ```pip```.


Otherwise, you just need Python and command-line access.

##**to run**

```cd``` to the directory you've saved this script in and run:

```python
python instapaper_to_bitly.py
```

Type in the appropriate things when prompted. There you go!


##**options**

Save your Instapaper email and password, if it is insecure enough that you don't mind saving it in plain text on your computer (or hell, encrypt it, I guess...) and save it in your ```secure_info_instabitly.py``` file. 

Comment out the lines:

```python
username = raw_input("Input the email address for your Instapaper account.\n")
password = getpass.getpass("Input your Instapaper password.\n")
```

and replace them with

```python
username = sib.username
password = sib.password
```

or whatever you've made the variables be. (Let me know if this is confusing. Really!)


If you want to see the links you're saving in the console, uncomment the line ```#print "Just saved: ", link```. Probably not worth it, but hey.

##**TODOS and things**

* Neater and more comprehensive error checking 
(it's currently really messy)
* General cleanup (see above)
* More options 

**n.b.** 
_this script currently cycles through all of your most recent 2000 (or fewer, if you don't have 2000) links saved in Instapaper. This may change in future, but updates TBA._

_it's not the fastest thing in the_ whole world, _but it doesn't take too long and for the moment that's okay._

##**license**

This script is licensed under the [MIT license](http://opensource.org/licenses/MIT):

**The MIT License (MIT)**

Copyright (c) 2013 [aerenchyma](http://github.com/aerenchyma)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
