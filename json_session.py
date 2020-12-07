import requests


def create_json_session(web_host, username, password, verify=True):
    session = requests.Session()
    # Start by getting supported versions from the base url...
    api_url = '%s/api/' % web_host
    r = session.get(api_url, verify=verify)
    print(api_url,r)
    # we get a list of versions
    versions = r.json()['data']
    # use most recent version...
    version = versions[-1]
    # get the 'base' url
    base_url = version['url:base']
    r = session.get(base_url)
    # which lists a bunch of urls as starting points
    urls = r.json()
    servers_url = urls['url:servers']
    login_url = urls['url:login']

    # To login we need to get CSRF token
    token_url = urls['url:token']
    token = session.get(token_url).json()['data']
    print('CSRF token', token)
    # We add this to our session header
    # Needed for all POST, PUT, DELETE requests
    session.headers.update({'X-CSRFToken': token,
                            'Referer': login_url})

    # List the servers available to connect to
    servers = session.get(servers_url).json()['data']

    SERVER_NAME = 'omero'
    servers = [s for s in servers if s['server'] == SERVER_NAME]
    if len(servers) < 1:
        raise Exception("Found no server called '%s'" % SERVER_NAME)
    server = servers[0]

    # Login with username, password and token
    payload = {'username': username,
               'password': password,
               # Using CSRFToken in header
               'server': server['id']}

    r = session.post(login_url, data=payload)
    login_rsp = r.json()
    assert r.status_code == 200
    assert login_rsp['success']
    
    # Can get our 'default' group

    return login_rsp, session, base_url


def retrieve_image(session, base_url, img_id, scale):
    from PIL import Image
    from io import BytesIO
    import numpy as np
    # just some magical code to get the correct address from the json api session and image id
    r = session.get(base_url)
    host = base_url.split("/api")[0]
    # which lists a bunch of urls as starting points
    urls = r.json()
    images_url = urls['url:images']
    single_image_url = images_url+str(img_id)+"/"
    thisjson = session.get(single_image_url).json()

    # calculate width to be requested based on metadata and the specified scale factor
    width = int(thisjson['data']['Pixels']['SizeX'])
    scaled = round(width/scale)
    img_address = host+"/webgateway/render_birds_eye_view/"+str(img_id)+"/"+str(scaled)+"/"
    jpeg = session.get(img_address, stream=True)

    if jpeg.status_code != 200:
        raise Exception("Received response {} with content: {}".format(jpeg.status_code, jpeg.content))

    # using PIL and BytesIO to open the request content as an image
    i = Image.open(BytesIO(jpeg.content))
    jpeg.close()
    return np.array(i)