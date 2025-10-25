"utils.py"
from itertools import chain


###Settings values###
#For the slider data;
LOWEST_ALLOWABLE_VALUE:float = 1.0e-5;
HIGHEST_ALLOWABLE_VALUE:float = 2.1;

#File reading;
DEFAULT_READ_FILEPATH:str = "CharacterCards/KoikatsuSun_F_20240410163006202_Tatsuya Yuki.png"; #TESTING ONLY
DATA_START_FLAG:str = "shapeValueBody";

#File writing [formatting/path];
WHITESPACE:int = 32;
DEFAULT_WRITE_FILEPATH:str = "result.txt";
###Settings values###



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



def writeToOutputFile(filePath:str, readValues:dict[str, int]) -> None:
	#Writes fileData to the relevant file.

	fileData:str = f"+-{'-'*WHITESPACE}-+------+\n";
	for (key, value) in readValues.items():
		if (key == "<SPACER>"):
			fileData += f"+-{'-'*WHITESPACE}-+------+\n";
		else:
			fileData += f"| {key}{(WHITESPACE-len(key))*' '} | {' ' if (value > 0) else ''}{'  ' if (abs(value) < 10) else (' ' if (abs(value) < 100) else '')}{value} |\n";
	fileData += f"+-{'-'*WHITESPACE}-+------+\n";


	with open(filePath, "w") as outFile:
		outFile.write(fileData);

	print(f"Successfully wrote data to: [{filePath}]");