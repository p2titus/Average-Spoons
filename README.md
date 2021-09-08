# Average Spoons finder!
Ever had a problem where you've no idea where the optimal spoons between you and
a group of buddies is? Well look no further! Simply input postcodes of you and
your buddies and this program will show you details of the average spoons!

## Requirements
	Python 3.9 or later
	A Google Maps API key (if using the default methods)

## Installation and setup
Note this repo does not have a PyPi package. There is no particular intention to make one either.
All required packages can be found in the `requirements.txt`

You will need to add the Maps API key at locationservices/keys.json. The file should be formatted as follows:

	{
	  "google_key": {
	    "key": [key goes here]
	  }
	}

After, simply create a list of address objects from averager.py. Then run `find_closest_spoons` in main

Happy hunting :)
