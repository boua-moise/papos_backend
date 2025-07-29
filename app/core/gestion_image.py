from pathlib import Path
from fastapi import File, UploadFile

from upyloadthing import UTApi, UTApiOptions

api = UTApi(UTApiOptions(token="eyJhcGlLZXkiOiJza19saXZlX2ZiMzZmMjllY2VlMmRmMzFkZWQ4MWQ2YjIxMmIxMzk2M2RmMzZiMThhMDc5Y2I5M2Q0OTNiZGIwN2I0OGUzMGQiLCJhcHBJZCI6InkxdjYwM3g1YTYiLCJyZWdpb25zIjpbInNlYTEiXX0="))

DIRECTORY = Path().cwd() / "static"
DIRECTORY.mkdir(parents=True, exist_ok=True)
def register_image(image):
    url = ""
    with open(image, "rb") as f:
        result = api.upload_files(f)
    for el in result:
        url = el.url
    return url

async def save_image_local(image:UploadFile):

    data = await image.read()

    image_path = DIRECTORY / image.filename

    image_path.write_bytes(data)

    url = register_image(image_path)

    image_path

    response = {
    "success" : 1,
    "file": {
        "url" : url
        }
    }

    return response

