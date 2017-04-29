# Scraping HackerNews Top Articles

Parse HackerNews articles and get the info on these articles.

## What this script does

It's a quick demo of Scrapy - it parses HackerNews homepage and lists links, titles for these links and votes.

## To do

- Save items to the database via item pipelines
- Add a second crawler which will pull pages metadata

## How to use it

You can setup Vagrant environment by running `vagrant up`

SSH into the box with `vagrant ssh`

To setup all dependencies run the following commands:

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6 python3.6-dev virtualenv
virtualenv -p python3.6 /home/vagrant/.hn_scrapy
source /home/vagrant/.hn_scrapy/bin/activate
cd /srv/hn_scrapy
pip install -r deploy/requirements.txt
```

The next time you SSH don't forget to active python environment by running `source /home/vagrant/.hn_scrapy/bin/activate`

You can run the script by running `python scraper.py` inside `/srv/hn_scrapy/hn_scrapy` directory.

## Debugging

If you want to modify the script and try to crawl different website Scrapy has a great debug interface which can be activated by running `scrapy shell https://news.ycombinator.com`. This command will load ipython so you could explore the resource in an interactive way.
