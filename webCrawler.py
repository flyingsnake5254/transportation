import requests
from bs4 import BeautifulSoup


def getData(dataURL):
    returnData = requests.get(dataURL)
    returnData.encoding = returnData.apparent_encoding
    return returnData.text


def getSoup(dataURL):
    soup = BeautifulSoup(getData(dataURL), "html.parser")
    return soup


src = []
srcName = {}
# 高公局國道路況影像
freewayName = "國道一號,五楊高架,國道二號,國道三號,國三甲線,國道四號,國道五號,國道六號,國道八號,國道十號,高港高架"
expresswayName = "蘇花改,台61線,台62線,台64線,台66線,台68線,台72線,台74線,台76線,台78線,台82線,台84線,台86線,台88線"
provincialRoadName = "新北市,基隆市,桃園市,宜蘭縣,新竹縣,新竹市,苗栗縣,臺中市,花蓮縣,南投縣,彰化縣,雲林縣,嘉義縣,嘉義市,臺東縣,臺南市,屏東縣,高雄市"
taipeiName = "松山區,信義區,大安區,中山區,中正區,大同區,萬華區,文山區,南港區,內湖區,士林區,北投區"
newTaipeiName = "八里區,板橋區,淡水區,貢寮區,金山區,林口區,蘆洲區,坪林區,瑞芳區,三重區,三峽區,三芝區,深坑區,石碇區,樹林區,泰山區,土城區,萬里區,五股區,烏來區,新店區,新莊區,汐止區,鶯歌區,永和區,中和區"
taoyuanName = "八德區,大溪區,大園區,復興區,龜山區,龍潭區,蘆竹區,平鎮區,桃園區,新屋區,楊梅區,中壢區"
kaohsiungName = "大寮區,大社區,大樹區,鳳山區,岡山區,鼓山區,苓雅區,林園區,路竹區,美濃區,彌陀區,楠梓區,鳥松區,前金區,前鎮區,橋頭區,茄萣區,旗津區,旗山區,仁武區,三民區,小港區,新興區,燕巢區,鹽埕區,永安區,梓官區,左營區"
othersName = "基隆市,宜蘭縣,新竹市,新竹縣,台中市,彰化縣,南投縣,嘉義市,嘉義縣,台南市,屏東縣,馬祖"

freeway = freewayName.split(",")
expressway = expresswayName.split(",")
provincialRoad = provincialRoadName.split(",")
taipei = taipeiName.split(",")
newTaipei = newTaipeiName.split(",")
taoyuan = taoyuanName.split(",")
kaohsiun = kaohsiungName.split(",")
others = othersName.split(",")


for i in getSoup("https://tw.live/").select("div.cctv-menu ul li a"):
    if i.text in kaohsiun:
        print(i.text)
        lineName = []
        for j in getSoup(i["href"]).select("div.cctv-stack a span img"):
            lineName.append(j["alt"])

        index = 0
        for j in getSoup(i["href"]).select("div.cctv-stack a"):
            print("--------", lineName[index], ":", j["href"])
            # break #test
            src.append(j["href"])
            srcName[j["href"]] = lineName[index]
            index += 1

    #========若只需高雄道路相關資料，請將此行以「下」至下方註解指示處之間的CODE主解起來即可

    elif i.text in ["國道一號", "國道三號", "國道五號"]:
        print(i.text)
        # pass
        for j in getSoup(i["href"]).select("h5.card-title a"):
            print("----", j.text)

            lineName = []
            for k in getSoup(j["href"]).select("div.cctv-stack a span img"):
                lineName.append(k["alt"])

            index = 0
            for k in getSoup(j["href"]).select("div.cctv-stack a"):
                print("--------", lineName[index], ":", k["href"])

                src.append(k["href"])
                srcName[k["href"]] = lineName[index]
                index += 1

    elif i.text in ["五楊高架", "國道二號", "國三甲線", "國道四號", "國道六號", "國道八號", "國道十號", "高港高架"]:
        print(i.text)
        # pass
        lineName = []
        for j in getSoup(i["href"]).select("div.cctv-stack a span img"):
            lineName.append(j["alt"])

        index = 0
        for j in getSoup(i["href"]).select("div.cctv-stack a"):
            print("--------", lineName[index], ":", j["href"])

            src.append(j["href"])
            srcName[j["href"]] = lineName[index]
            index += 1
    elif i.text in expressway + provincialRoad + taipei + newTaipei + taoyuan + others:
        print(i.text)
        lineName = []
        for j in getSoup(i["href"]).select("div.cctv-stack a span img"):
            lineName.append(j["alt"])

        index = 0
        for j in getSoup(i["href"]).select("div.cctv-stack a"):
            print("--------", lineName[index], ":", j["href"])
            # break #test
            src.append(j["href"])
            srcName[j["href"]] = lineName[index]
            index += 1


    # ========若只需高雄道路相關資料，請將此行以「上」至下方註解指示處之間的CODE主解起來即可

# 於終端輸出所有CCTV網址
# print("============src==================")
# for i in src:
# 	print(i)

# 將所有CCTV網址匯出TXT
# 檔案位置
path = 'D:\\output.txt'
f = open(path, 'w')
for i in src:
    f.write(i + "\n")
f.close()
