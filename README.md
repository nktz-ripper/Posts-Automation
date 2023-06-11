# Posts-Automation
Scrapes news API, generate CSV, syncs to Google Tasks, and sends Headlines URLs to WhatsApp Number.

_Automation tool developed for my personal use, that might be useful for you._

_Very basic but so far it works._

# File index and contents
Google.py - Standard Google API python file
fetcher.py - Has the functions to getting headlines and basic parsing headlines JSON responses into arrays.
id_fetcher.py - I used it to get my Google Tasks List ID. You'd have to configure your Google Cloud APIs and oAuth before though.
scheduler.pyw - Python file that orchestrates everything. The .pyw makes it run "in the background".
tasklist_updater - Has the functions to update the Google Tasks List.


# Work in progress
Ideas?

a) Somehow get the headlines and automatically generate Social Media Posts (media design).

b) Somehow paraphrase the content of the scraped news to convert it to a social media post description.

c) Somehow post it automatically **as drafts** to Instagram, Facebook, LinkedIn, and others.


If any idea or suggestion to make that work pops to your mind, let me know in the DMs.
@advnakata
