import click
import os
import imdb
from bs4 import BeautifulSoup
import requests
import struct

@click.command()
@click.option('-p','--path', default=None, help='Specify the path to the file or files.')
@click.option('-l','--language', default="english", help='Filter subtitles by language.')
@click.option('-f','--filesize', default=False, type=bool, help='Filter subtitles by file size.(in bytes)')
@click.option('-h','--hash', default=False, type=bool, help='Filter subtitles by hash.')
@click.option('-o','--output', default=None, help='Specify the output directory for subtitles.')
@click.option('-b','--batch', default=False, type=bool, help='Process subtitles in batch mode.')
def Download_Subtitle(path, language, filesize, hash, output, batch):
    db = imdb.IMDb()
    click.echo("\n\n")
    click.echo(click.style("Welcome to Subtitler", fg="white", bg="red"))
    p = os.path.realpath(os.path.curdir)

    if path is None:
        if not batch:
            path = p + "/ExampleVideo/Oppenheimer (2023).mp4"
        else:
            path = p + "/ExampleVideo/"

    if output is None:
        output = p + "/Output/"

    click.echo(click.style(f"\nReading Files From: {path}", fg="green"))
    subtitle_Id = []

    if not batch:
        if not path.endswith(".mp4"):
            path = path + ".mp4"
        if not os.path.exists(path):
            click.echo("Error No File Found: Check your file Directory it does not seem to exist!")
            return

        filehash, _filesize = hash_size_File_url(path)
        movie_name = os.path.basename(path).replace(".mp4", "")
        click.echo(
            click.style(
                f"\nGetting subtitles ready for \n Movie Name: {movie_name}\n Language: {language}\n Filesize: {_filesize}\n hash: {hash}",
                fg="yellow"
            )
        )
        print(click.style(f"Fetching Subtitles for {movie_name}!", fg="green"))
        m_id = db.search_movie(movie_name)[0].movieID
        link = f"https://www.opensubtitles.org/en/search/imdbid-{m_id}/sublanguageid-{language[:3]}"
        if filesize:
            link += f"/moviebytesize-{_filesize}"
        if hash:
            link += f"/moviehash-{filehash}"
        src = requests.get(link)

        if src.status_code != 200:
            print("Could Not Connect to the Website. Check your network!")
            return

        html = BeautifulSoup(src.text, "html.parser")

        try:
            k = html.find(id="search_results").find_all("tr")
        except AttributeError:
            click.echo(
                click.style(
                    f"No subtitles to fetch for\nMovie Name: {movie_name}\nLanguage: {language}\nFilesize: {_filesize}\nHash: {hash}",
                    fg="red"
                )
            )
            return

        click.echo(click.style("Subtitle Name:" + " " * 52 + "Date and time of upload:", bg="red"))
        num = 1
        for i in k:
            if i.has_attr("id") and "name" in i["id"]:
                s = i["id"].replace("name", "")
                m = i.find(id=f"main{s}")
                d = i.find("time")
                subtitle_Id.append(s)
                m_name = m.get_text().replace("Watch onlineDownload Subtitles Searcher", "").replace(m.find("a").get_text(), "").strip()
                m_name = m_name.ljust(50)
                num_display = f"{num})" if num >= 10 else f"{num} )"
                print(f"{num_display}{m_name}{' ' * 18}{d['title']}")
                num += 1

        s = int(input("\n\nEnter the serial number to download your subtitle: "))
        movie_name = movie_name.replace(".mp4", "")
        response = requests.get(f"https://www.opensubtitles.org/en/subtitleserve/sub/{subtitle_Id[s - 1]}")

        if response.status_code == 200:
            if not output.endswith("/"):
                output += "/"
            with open(f"{output}subtitle_{movie_name}.zip", 'wb') as file:
                file.write(response.content)
                click.echo(
                    click.style(
                        f"Downloaded in {output}subtitle{movie_name} successfully.",
                        fg="white",
                        bg="green"
                    )
                )
        else:
            click.echo(click.style("Failed to download the file.", fg="white", bg="red"))

    else:
        files = os.listdir(path)
        t_p = path
        for f in files:
            path = os.path.join(t_p, f)
            print(f)
            if not path.endswith(".mp4"):
                path = path + ".mp4"
            if not os.path.exists(path):
                click.echo("Error No File Found: Check your file Directory it does not seem to exist!")
                continue

            filehash, _filesize = hash_size_File_url(path)
            movie_name = os.path.basename(path).replace(".mp4", "")
            m_id = db.search_movie(movie_name)[0].movieID
            link = f"https://www.opensubtitles.org/en/search/imdbid-{m_id}/sublanguageid-{language[:3]}"
            if filesize:
                link += f"/moviebytesize-{_filesize}"
            if hash:
                link += f"/moviehash-{filehash}"
            src = requests.get(link)
            html = BeautifulSoup(src.text, "html.parser")

            try:
                k = html.find(id="search_results").find_all("tr")
                for i in k:
                    if i.has_attr("id") and "name" in i["id"]:
                        s = i["id"].replace("name", "")
                        subtitle_Id.append(s)
                movie_name = movie_name.replace(".mp4", "")
                response = requests.get(f"https://www.opensubtitles.org/en/subtitleserve/sub/{subtitle_Id[0]}")
                if response.status_code == 200:
                    if not output.endswith("/"):
                        output += "/"
                    with open(f"{output}subtitle_{movie_name}.zip", 'wb') as file:
                        file.write(response.content)
                    click.echo(
                        click.style(
                            f"Downloaded in {output}subtitle{movie_name} successfully.",
                            fg="white",
                            bg="green"
                        )
                    )
                else:
                    click.echo(click.style("Failed to download the file.", fg="white", bg="red"))
            except AttributeError:
                click.echo(
                    click.style(
                        f"No subtitles to fetch for\nMovie Name: {movie_name}\nLanguage: {language}\nFilesize: {_filesize}\nHash: {hash}",
                        fg="red"
                    )
                )

def temp_file():
    import tempfile
    file = tempfile.NamedTemporaryFile()
    filename = file.name
    return filename

def is_local(_str):
    from urllib.parse import urlparse
    if os.path.exists(_str):
        return True
    elif urlparse(_str).scheme in ['', 'file']:
        return True
    return False

def hash_size_File_url(filepath):
    # https://trac.opensubtitles.org/projects/opensubtitles/wiki/HashSourceCodes
    # filehash = filesize + 64bit sum of the first and last 64k of the file
    name = filepath
    if is_local(filepath):
        local_file = True
    else:
        local_file = False

    if not local_file:
        f = None
        url = name
        response = requests.head(url)
        filesize = int(response.headers['content-length'])

        if filesize < __64k * 2:
            try:
                filesize = int(str(response.headers['content-range']).split('/')[1])
            except:
                pass

        first_64kb = temp_file()
        last_64kb = temp_file()

        headers = {"Range": f"bytes=0-{__64k - 1}"}
        r = requests.get(url, headers=headers)
        with open(first_64kb, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        if filesize > 0:
            headers = {"Range": f"bytes={filesize - __64k}-{filesize - 1}"}
        else:
            f.close()
            os.remove(first_64kb)
            return "SizeError", 0

        try:
            r = requests.get(url, headers=headers)
            with open(last_64kb, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        except:
            f.close()
            if os.path.exists(last_64kb):
                os.remove(last_64kb)
            if os.path.exists(first_64kb):
                os.remove(first_64kb)
            return 'IOError', 0
        f = open(first_64kb, 'rb')

    try:
        longlongformat = '<q'  # little-endian long long
        bytesize = struct.calcsize(longlongformat)

        if local_file:
            f = open(name, "rb")
            filesize = os.path.getsize(name)
        hash = filesize

        if filesize < __64k * 2:
            f.close()
            if not local_file:
                os.remove(last_64kb)
                os.remove(first_64kb)
            return "SizeError", 0

        range_value = __64k // __byte_size

        for _ in range(range_value):
            buffer = f.read(bytesize)
            (l_value,) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash &= 0xFFFFFFFFFFFFFFFF  # to remain as 64bit number

        if local_file:
            f.seek(max(0, filesize - __64k), 0)
        else:
            f.close()
            f = open(last_64kb, 'rb')

        for _ in range(range_value):
            buffer = f.read(bytesize)
            (l_value,) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash &= 0xFFFFFFFFFFFFFFFF

        f.close()
        if not local_file:
            os.remove(last_64kb)
            os.remove(first_64kb)
        returnedhash = f"{hash:016x}"
        return returnedhash, filesize

    except IOError:
        if not local_file:
            os.remove(last_64kb)
            os.remove(first_64kb)
        return 'IOError', 0

if __name__ == "__main__":
    __64k = 65536
    __longlong_format_char = 'q'
    __byte_size = struct.calcsize(__longlong_format_char)
    Download_Subtitle()
