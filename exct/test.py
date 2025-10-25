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




caIndex:int = searchInList(data, [0xCA,]);
acIndex:int = searchInList(data, [0xAC,]);
relevantData:list[int] = data[caIndex:acIndex];
numValues:int = len(relevantData) // 5;


valueMap:dict[int, str] = {
	24: "Body Height",

	28: "Breast Size",

	33: "Breast Depth",
	34: "Breast Roundness",

	38: "Shoulder Width",
	39: "Shoulder Thickness",
	40: "Upper Torso Width",
	41: "Upper Torso Thickness",
	42: "Lower Torso Width",
	43: "Lower Torso Thickness",

	45: "Belly Thickness",
	46: "Waist Width",
	47: "Waist Thickness",
	48: "Hip Width",
	49: "Hip Thickness",
	50: "Butt Size",
	
	52: "Upper Thigh Width",
	53: "Upper Thigh Thickness"
};
fileData:str = "";



LOWEST_ALLOWABLE_VALUE:float = 1.0e-5;
HIGHEST_ALLOWABLE_VALUE:float = 2.1;
WHITESPACE:int = 32;
OUTPUT_FILE:str = "out.txt";



for i in range(numValues):
	if (i not in valueMap): continue;

	bytesData:bytes = bytes(relevantData[(i*5):((i+1)*5-1)]);
	rawFloatValue:float = translator.bytesToFloat(bytesData);
	if ((rawFloatValue > HIGHEST_ALLOWABLE_VALUE) or (abs(rawFloatValue) < LOWEST_ALLOWABLE_VALUE)): continue;

	cleanedFloatValue:int = int(round(rawFloatValue, 2) * 100.0);
	search:str = valueMap[i];
	fileData += (f"Search: {search}{(WHITESPACE-len(search))*' '}| Value: {cleanedFloatValue}\n");






searches:list[str] = {
	"bustSoftness",
	"bustWeight",
	"areolaSize"
};


for search in searches:
	searchInt:list[int] = [ord(c) for c in search];
	index:int = searchInList(data, searchInt);
	relevantData:list[int] = data[index:];

	caIndex:int = searchInList(data, [0xCA,]);
	floatBytes:list[int] = relevantData[caIndex:caIndex+4];

	rawFloat:float = translator.bytesToFloat(bytes(floatBytes));
	cleanFloat:int = int(round(rawFloat, 2) * 100.0);
	fileData += (f"Search: {search}{(WHITESPACE-len(search))*' '}| Value: {cleanFloat}\n");



with open(OUTPUT_FILE, "w") as outFile:
	outFile.write(fileData);



