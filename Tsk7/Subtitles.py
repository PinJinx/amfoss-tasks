import click
import os
import imdb
from bs4 import BeautifulSoup
import requests


@click.command()
@click.option('--path', default = None, help='Specify the path to the file or files.')
@click.option('--language', default="english", help='Filter subtitles by language.')
@click.option('--filesize', default=None, type=int, help='Filter subtitles by file size.(in bytes)')
@click.option('--hash', default=None, help='Filter subtitles by hash.')
@click.option('--output', default=None, help='Specify the output directory for subtitles.')
@click.option('--batch', default=False,type=bool, help='Process subtitles in batch mode.')




def Download_Subtitle(path,language,filesize,hash,output,batch):
    db = imdb.IMDb()
    click.echo("\n\n")
    click.echo(click.style("Welcome to Subtitler",fg="white",bg="red"))
    p = os.path.realpath(os.path.curdir)
    if(path == None):
        if not batch:
            path = p+"/ExampleVideo/Oppenheimer (2023).mp4"
        else:
            path = p+"/ExampleVideo/"
    if(output == None):
        output = p+"/Output/"
    
    click.echo(click.style("\nReading Files From :"+path,fg="green"))
    subtitle_Id=[]
    if(not batch):
        if not path.endswith(".mp4"):
            path = path + ".mp4"
        if not os.path.exists(path):
            click.echo("Error No File Found: Check your file Directory it doesnot seem to exist!")
            return
        movie_name = path.split("/")[-1]
        movie_name = movie_name.replace(".mp4","")

        click.echo(click.style("\nGetting subtitles ready for \n Movie Name:"+movie_name+"\n Language:"+language+"\n Filesize:"+str(filesize)+"\n hash:"+str(hash),fg="yellow"))

        print(click.style("Fetching Subtitles for "+movie_name+"!",fg="green"))
        m_id = db.search_movie(movie_name)[0].movieID
        if(filesize != None):
            src = requests.get("https://www.opensubtitles.org/en/search/imdbid-"+m_id+"/sublanguageid-"+language[:3]+"/moviebytesize-"+str(filesize))
        else:
            src = requests.get("https://www.opensubtitles.org/en/search/imdbid-"+m_id+"/sublanguageid-"+language[:3])
        if src.status_code != 200:
            print("Could Not Connect to the Website. Check your network!")
        html = BeautifulSoup(src.text,"html.parser")
        k = html.find(id="search_results").find_all("tr")

        click.echo(click.style("Subtitle Name:"+" "*52+"Date and time of upload:",bg = "red"))
        num = 1
        for i in k:
            if i.has_attr("id"):
                if "name" in i["id"]:
                    s = str(i["id"]).replace("name","")
                    m = i.find(id = "main"+s)
                    d = i.find("time")
                    subtitle_Id.append(s)
                    m_name = m.get_text().replace("Watch onlineDownload Subtitles Searcher","")
                    m_name = m_name.replace(m.find("a").get_text(),"")
                    m_name = m_name.replace("\n","")
                    while (len(m_name) < 50):
                        m_name += " "
                    if(num < 10):
                        print(str(num)+" )",end="")
                    else:
                        print(str(num)+")",end="")
                    print(m_name," "*18,end="")
                    print(d["title"])
                    num+=1
        s = int(input("\n"*2 + "Enter the serial number to dowload your subtitle:"))
        movie_name=movie_name.replace(".mp4","")
        response = requests.get("https://www.opensubtitles.org/en/subtitleserve/sub/"+subtitle_Id[s-1])
        if response.status_code == 200:
            if(not output.endswith("/")):
                output+="/"
            with open(output+"subtitle_"+movie_name+".zip", 'wb') as file:
                file.write(response.content)
                click.echo(click.style("Downloaded in "+output+"subtitle"+movie_name+" successfully.",fg="white",bg="green"))
        else:
            click.echo(click.style("Failed to download the file.",fg="white",bg="red"))

    else:
        files = os.listdir(path)
        t_p = path
        for f in files:
            path = t_p
            path+=f
            print(f)
            if not path.endswith(".mp4"):
                path = path + ".mp4"
            if not os.path.exists(path):
                click.echo("Error No File Found: Check your file Directory it doesnot seem to exist!")
                return
            movie_name = path.split("/")[-1]
            movie_name = movie_name.replace(".mp4","")
            m_id = db.search_movie(movie_name)[0].movieID
            if(filesize != None):
                src = requests.get("https://www.opensubtitles.org/en/search/imdbid-"+m_id+"/sublanguageid-"+language[:3]+"/moviebytesize-"+str(filesize))
            else:
                src = requests.get("https://www.opensubtitles.org/en/search/imdbid-"+m_id+"/sublanguageid-"+language[:3])
            html = BeautifulSoup(src.text,"html.parser")
            k = html.find(id="search_results").find_all("tr")
            for i in k:
                if i.has_attr("id"):
                    if "name" in i["id"]:
                        s = str(i["id"]).replace("name","")
                        subtitle_Id.append(s)
            movie_name=movie_name.replace(".mp4","")
            response = requests.get("https://www.opensubtitles.org/en/subtitleserve/sub/"+subtitle_Id[0])
            if response.status_code == 200:
                if(not output.endswith("/")):
                    output+="/"
                with open(output+"subtitle_"+movie_name+".zip", 'wb') as file:
                    file.write(response.content)
                click.echo(click.style("Downloaded in "+output+"subtitle"+movie_name+" successfully.",fg="white",bg="green"))
            else:
                click.echo(click.style("Failed to download the file.",fg="white",bg="red"))
                




        
        





if __name__ == "__main__":
    Download_Subtitle()