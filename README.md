### Python script to download all images from  tadpole
- Unfortunately the tadpoles app does not provide a bulk download option and you need to manually download each image one by one.
- I used google sign in and not email id based sign in when I setup the account, couldn't find any bulk downloaders for that.
- Once all photos are downloaded you can sync them to your cloud, amazon photos in my case.

## Setup
This script is very trivial and you do need to perform some manual steps. Some of these steps can be automated but I didnt want tpo spend any more time on this :smile:

1. Create an images/ folder and all the corresponding month folders using the month-year format. ex: jan-2018
2. Login to the app and click on the jan-2018 folder, inspect the Network tab in Developer tools.
3. Right-click on any obj_attachment endpoint, Copy > Copy as Curl
4. Paste the curl command on the terminal to make sure this works, redirect output to test.jpg and verify that you get an image.
```bash
curl ..... > test.jpg
open test.jpg
```
5. Now we need the headers from the curl command. For that use https://curl.trillworks.com/ and get the corresponding headers.
6. Copy the headers and replace the headers in the scrape_tadpole.py script
7. Finally you will need to copy the HAR files into the image folders. This needs to be done for each month and is kinda painful. It can be automated but shouldn't take you more than 30 mins. Make sure to _clear the log_ before each reading and also _disable cache_
- Create folders under images/
```bash
mkdir jan-2017 feb-2017 mar-2017 apr-2017 may-2017 jun-2017 jul-2017 aug-2017 sep-2017 oct-2017 nov-2017 dec-2017

```
- Click on the tadpoles site on the folder like jan-2018, make sure to hit the Clear button before you save the HAR file.
- Click on the download button, a downarrow with underscore. This will export the HAR file and make sure you save it to the corresponding folder under images/
8. Update the months in the month list in main.

## Run the script
```bash
python scrape_tadpole.py
```