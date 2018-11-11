import urllib
def read_text():
    quotes = open("/home/nidhi/Desktop/eval.c")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)

def check_profanity(contents):
    connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q=" + contents)
    output = connection.read()
    connection.close()
    #print(output)
    if "true" in output:
        print("Profanity alert!!")
    elif "false" in output:
        print("The document has no curse words!")
    else:
        print("Couldn't Scan.Try again!")


read_text()
