import requests
api_key = 'AIzaSyDGe-kcOZNxvJ_q57JGIDZxxi82IQx0_0w'
test_url = 'https://developers.google.com'
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}& key= {api_key}'


res = requests.get(api_url)
if res.status_code == 200:
    data = res.json()
    cls_score = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
    print(cls_score)
else:
    print("Something went wrong")