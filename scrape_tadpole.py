import json
import requests

TADPOLES_URL = 'https://www.tadpoles.com/remote/v1/obj_attachment'
FOLDER = 'images/'
INPUT_FILE = 'www.tadpoles.com.har'


def download_image(obj, key):
    headers = {
        'authority': 'www.tadpoles.com',
        'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
        'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'image',
        'referer': 'https://www.tadpoles.com/parents',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'YOUR_COOKIE'
    }

    params = (
        ('obj', obj),
        ('key', key)
    )

    response = requests.get(TADPOLES_URL, headers=headers, params=params)
    return response


def main(sub_folder):
    with open(FOLDER + sub_folder + '/' + INPUT_FILE) as f:
        img_count = 0;
        data = json.load(f)
        for entry in data['log']['entries']:
            url = entry['request']['url']
            if "obj_attachment" in url:
                # get the params
                clean_url = url.split('?')[1]
                print(clean_url)
                for queryParam in entry['request']['queryString']:
                    if queryParam['name'] == 'obj':
                        obj = queryParam['value']
                    if queryParam['name'] == 'key':
                        key = queryParam['value']

                response_headers = entry['response']['headers']
                for header in response_headers:
                    if header['name'] == 'content-type':
                        media_type = header['value']
                        break
                if media_type == 'image/png':
                    media_extension = '.mp4'
                else:
                    media_extension = '.jpg'
                response = download_image(obj, key)
                if response.status_code == 200:
                    img_name = FOLDER + sub_folder + '/img' + '_' + str(img_count) + media_extension
                    with open(img_name, 'wb') as handler:
                        handler.write(response.content)
                        img_count += 1


if __name__ == '__main__':
    months = [
        'aug-2018',
        'jul-2018',
        'jun-2018',
        'may-2018',
        'apr-2018',
        'mar-2018',
        'feb-2018',
        'jan-2018',
        'dec-2017',
        'nov-2017',
        'oct-2017',
        'sep-2017',
        'aug-2017',
        'jul-2017',
        'jun-2017',
        'may-2017',
        'apr-2017',
        'mar-2017',
        'feb-2017',
        'jan-2017',
        'dec-2016',
        'nov-2016',
        'oct-2016',
        'sep-2016',
        'aug-2016',
        'jul-2016',
        'jun-2016',
        'may-2016',
        'apr-2016',
        'mar-2016',
        'feb-2016',
        'jan-2016',
        'dec-2015',
        'nov-2015',
        'oct-2015',
        'sep-2015',
        'aug-2015'
    ]
    for month in months:
        main(month)
