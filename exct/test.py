import translator


filePath = "../CharacterCards/KoikatsuSun_F_20240410163006202_Tatsuya Yuki.png" #TMP.

startInt:list[int] = [ord(c) for c in "shapeValueBody"];


def searchInList(arr:list[any], search:any) -> int:
	for i, element in enumerate(arr):
		if (element == search[0]):
			found:bool = True;
			for o, c in enumerate(search):
				if (c != arr[i+o]):
					found = False;
					break;

			if found:
				return i + len(search);

	return -1;


data:list[int] = [];
found:bool = False;
with open(filePath, "rb") as pngFile:
	fileData:list[bytes] = pngFile.readlines();
	for line in fileData:
		ln = list(line);
		index = searchInList(ln, startInt);
		if ((index == -1) and not found): continue
		found = True;

		data.extend(ln);


searchInt:list[int] = [ord(c) for c in "bustWeight"];
index:int = searchInList(data, searchInt);
relevantData:list[int] = data[index:];

caIndex:int = searchInList(data, [0xCA,]);
floatBytes:list[int] = relevantData[caIndex:caIndex+4];

rawFloat:float = translator.bytesToFloat(bytes(floatBytes));
cleanFloat:int = int(round(rawFloat, 2) * 100.0);
print(cleanFloat)



