"utils.py"
from itertools import chain


global DEBUG, QUIET;


###Settings values###
#For the slider data;
LOWEST_ALLOWABLE_VALUE:float = 1.0e-5;
HIGHEST_ALLOWABLE_VALUE:float = 2.1;

#File reading;
DEFAULT_READ_FILEPATH:str = "CharacterCards/KoikatsuSun_F_20250113120608760_Chitose Hana.png"; #TESTING ONLY
DATA_START_FLAG:str = "shapeValueBody";

#File writing [formatting/path];
WHITESPACE:int = 32;
DEFAULT_WRITE_FILEPATH:str = "result/result.txt";

#General
DEBUG:bool = True;  #Additional info for debug
QUIET:bool = False; #Entirely hides the UI
###Settings values###



###RATIOS###
MODEL_SIZE:float = 20.16;
UBUST_BASE_50_WIDTH:float = 21.5;
UBUST_W_SLIDER_RATIO:float = 0.4;
UBUST_D_SLIDER_RATIO:float = 0.9;
WAIST_BASE_50_WIDTH:float = 18.82;
WAIST_W_SLIDER_RATIO:float = 0.96;
WAIST_D_SLIDER_RATIO:float = 1.94;
HIP_D_SLIDER_RATIO:float = 0.46;
HIP_W_SLIDER_RATIO:float = 0.43;
HIP_BASE_50_WIDTH:float = 30.96;
BREAST_BASE_50:float = 10.5;

MUSCLEATURE_ESTIMATE:float = 3.1;
CUP_SIZE_TABLE:list[tuple[int]] = [
	(2.0, 12), #EU
	(2.5, 10)  #JP
];
CURRENT_SIZE_SYSTEM = 0; #EU ^
###RATIOS###



#Other;
def convertStringToIntList(text:str) -> list[int]:
	#Converts to the representation used for searchInList.
	return [ord(char) for char in text];
		







#Searching operations
def searchInList(arr:list[int], search:list[int]|int) -> int:
	#Finds some sequence of integers in a longer list of integers.
	#Uses very basic linear searching due to unorganised data.
	searchLST:list[int] = search if (type(search) == list) else [search,];

	for (mainIDX, element) in enumerate(arr):
		if (element == searchLST[0]):
			found:bool = True;

			#if (len(searchLST) == 0): break; #Confirmed found already.
			for subIDX, char in enumerate(searchLST):
				#Need to check following characters.
				if (char != arr[mainIDX+subIDX]):
					#Did not find char; sequence not found, keep searching.
					found = False;
					break;

			if found:
				#Return index after the flag.
				return mainIDX + len(searchLST);

	#Signal not found.
	return -1;








#File operations
def loadKKSFile(filePath:str) -> list[int]:
	#Load file and format as a list of integer values.
	startFlagInts:list[int] = convertStringToIntList(DATA_START_FLAG);

	fileData:list[bytes] = [];
	foundIndex:int = -1;
	with open(filePath, "rb") as pngFile:
		#Read bytes from file
		fileData = pngFile.readlines();

		for (lineIndex, line) in enumerate(fileData):
			#Convert line to be a list of integers
			ln:list[int] = list(line);

			#Check if line contains the start of data flag [Integer-list representation]
			index:int = searchInList(ln, startFlagInts);
			if (index == -1): continue; #Not found
			foundIndex = lineIndex;
			break;

	if (foundIndex == -1):
		raise IndexError("Could not find Koikatsu character data in file");

	return list(chain.from_iterable(
		[list(ln) for ln in fileData[foundIndex:]] #List comprehension method.
	));




#Order to write to file
writeOrder:tuple[str] = (
	"<SPACER>",
	"Bux", 		"Height",
	"Weight", 	"Underbust",
	"Cup Size", "Bust",
	"Waist", 	"Hips",
	"<SPACER>"
);

def writeToOutputFile(filePath:str, resultantValues:dict[str, float|str]) -> None:
	#Writes fileData to the relevant file.
	fileData:str = "";
	for key in writeOrder:
		if (key == "<SPACER>"):
			fileData += f"+-{'-'*WHITESPACE}-+------+\n";
			continue;

		value:float|str = resultantValues[key];
		if (type(value) == str):
			fileData += f"| {key}{(WHITESPACE-len(key))*' '} | {(WHITESPACE-len(value))*' '}{value} |\n";
		else:
			strValue:str = str(round(value,2));
			fileData += f"| {key}{(WHITESPACE-len(key))*' '} | {(WHITESPACE-len(strValue))*' '}{strValue} |\n";



	with open(filePath, "w") as outFile:
		outFile.write(fileData);

	print(f"Successfully wrote data to: [{filePath}]");
