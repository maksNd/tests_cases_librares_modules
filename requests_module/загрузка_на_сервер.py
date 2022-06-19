import requests

picture_fo_upload = r'picture_for_upload.jpeg'
link_for_upload = r'https://httpbin.org/post'

with open(picture_fo_upload, 'rb') as file:
    requests.post(link_for_upload, data=picture_fo_upload)
