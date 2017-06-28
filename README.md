# VPR Newscast

This is the code that produces the widget for VPR's [Latest Newscast](http://www.vpr.net/apps/newscast/).


## One-time setup work:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/latest-newscast.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Create a virtual environment for the app. `virtualenv venv`
1. Enter the virtual environment. `source venv/bin/activate`
1. Install the app requirements. `pip install -r requirements.txt`


## For regular updates, start here:

1. Change into the project directory. `cd latest-newscast`
1. Enter the virtual environment. `source venv/bin/activate`
1. To run locally, just hit a quick	`python app/index.py` and head to `127.0.0.1:5000`


## Pushing to production:

This project runs on a cron job in Webfaction. The cron is currently set to run every three minutes, pushing up to Amazon S3. To update the production code, SSH into our Webfaction server and update changes to the production code.


## Pym & Core Publisher:

We embed the latest newscast widget into Core Publisher using [Pym.js](http://blog.apps.npr.org/pym.js/).

Block Title: `Subscribe To The VPR News Podcast`
In the subheading field: `<div data-pym-src="http://www.vpr.net/apps/newscast/index.html"></div> <script type="text/javascript" src="//pym.nprapps.org/pym-loader.v1.min.js"></script>`
