from urllib import parse, request
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_item(total_sf: int,
                    stories_above: int,
                    stories_below: int,
                    ssystem: str,
                    ddlEcoRegion: str,
                    ddlExisting: str,
                    ddlNewType: str,
                    land_disturbed: int,
                    land_installed: int,
                    agree_terms: str = "agrees",
                    submit: str = 'Calculate'):
    parameters = {
    'total_sf': total_sf,
    'stories_above': stories_above,
    'stories_below': stories_below,
    'ssystem': ssystem,
    'ddlEcoRegion': ddlEcoRegion,
    'ddlExisting': ddlExisting,
    'ddlNewType': ddlNewType,
    'land_disturbed': land_disturbed,
    'land_installed': land_installed,
    'agree_terms': agree_terms,
    'submit':submit
    }

    data = parse.urlencode(parameters).encode()
    req = request.Request(r'http://www.buildcarbonneutral.org/calculated.php', data=data)
    resp = request.urlopen(req)
    # read the content from the request
    content = resp.read()
    soup = BeautifulSoup(content, "html.parser")
    calc_data = soup.find_all(class_="calc_result")[0].get_text()
    return calc_data
