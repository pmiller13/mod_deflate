# mod_deflate
Test Apache Performance of Caching + Compression
# Setup
1. Install Docker
2. Run 'docker pull httpd:2.4'
3. Run 'docker run  -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4' from the directory containing your HTML pages
  * Note that the directory containing your HTML needs 'chmod 775 ./html_dir'
4. Apache is now running in a docker container (kind of like a virtual machine)
* When you run a docker container, it gets assigned two unique identifiers, one is alphanumeric, the other is the bicomposition of two words
* Find these IDs by running 'docker ps' (maybe in another terminal)
5. To access your webpages, you need the IP address of your docker container running Apache
6. To get IP address run 'docker inspect name_or_id_of_your_container' and navigate to that IP
7. VOILA, this is stock configured Apache server


## Apache Compression w/ mod_deflate
[Past Report](http://www.webperformance.com/library/reports/moddeflate/)
[mod_flate Documentation](http://httpd.apache.org/docs/current/mod/mod_deflate.html)

### Compression Considerations
* By default, mod_deflate compresses before serving. For improved performance we can compress stuff prior

## Apache Caching
[Cache Documentation](https://httpd.apache.org/docs/2.4/caching.html)

## Project
1. Given 3 website designs: purely images, purely text, mixture
    * Need 3 different dummy website designs
    * Need 3 different Apache configuration files with options described below
2. Record page load times using default Apache configs
3. Record page load times with mod_deflate enabled
4. Record page loda times with mod_deflate enabled + pre-compressed
5. Record page load times with mod_deflate disabled
6. Mechanism to automate page load times
* Idea for automating this process:
  * Start a timer at the top of index.html
  * End the timer at the bottom of index.html
  * Embed this value somewhere on the page
  * Have a script that loads a page or set of pages many many times
  * Script will parse webpages for this timer value, eg: x = parse(webpage, "timer_val=XX.XX")
