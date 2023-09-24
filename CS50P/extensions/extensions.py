
def main():
    file = input("File name: ")
    ext = file.strip().split(".")[-1].lower()
    #print(ext)
    match ext:
        case "gif":
            print("image/gif")
        case "jpeg":
            print("image/jpeg")
        case "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

if __name__ == "__main__":
    main()    

