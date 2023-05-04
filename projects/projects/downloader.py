from pytube import YouTube


def get(field):
    link = input(f"Enter the {field}: ")
    return link


def download(link, path=""):
    if path != "":
        YouTube(link).streams.get_highest_resolution().download(path)
    else:
        YouTube(link).streams.get_highest_resolution().download()


def main():
    link = get("link")
    path = get("path")
    download(link, path)


if (__name__ == "__main__"):
    main()
