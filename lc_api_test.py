import requests
import sys
import json

def main():
    print("郵便番号を入力してください。")
    post_number = input()
    base_url = "http://zipcloud.ibsnet.co.jp/api/search"
    request = requests.get(base_url + "?zipcode=" + post_number)

    try:
        if sys.argv[1] == "json":
            print(request.text)
    except:
        parsed_obj = json.loads(request.text)
        print(parsed_obj["results"][0]["address1"] + parsed_obj["results"][0]["address2"] + parsed_obj["results"][0]["address3"])


if __name__ == '__main__':
    main()
