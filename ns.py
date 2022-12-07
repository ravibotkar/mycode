from nslookup import Nslookup
import os

def multilineinput():
    print("Please paste your multi-line input.\n"
          "To end, press ctrl+d on Linux/Mac, ctrl+z on Windows")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return lines


iplist = multilineinput()

print(iplist)

def main(ip):
    resp = os.system("nslookup "+ ip)
    #print(resp)
    return resp

for l in iplist:
    main(l)

#if __name__ == "__main__":
#main()
