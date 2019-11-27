For our week 1 progress, we currently have a web server that hosts a UI page through django.  The server runs on a raspberry pi that currently sits in
our apartment, so we can turn it on and off when we want to, and are able to ssh into it.  We did not have any significant issues, as Elijah
has experience with web servers, and we have decided to keep our UI page very simple.

We don't have any major concerns yet, but we still need to decide if we are going to measure the temperature through the water itself, or through the steam
when the water boils.  Measuring the water itself will make it very simple to tell when the water's boiling, but it presents more hazards since we'll be putting
sensors in direct proximity to water, and obviously water and photons don't get along.  The safest bet will be measuring a large temperature spike through the steam,
but that could present more inaccuracy than measuring the water directly.

Our next priorities are getting the sensor set up, and making that sensor communicate with the UI.
