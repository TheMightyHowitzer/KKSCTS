"kkscts.py"

import sys, os;
from pprint import pprint;
from exct import search;


#Stores the section and then each specific value to look for.
valuesToSearchFor:dict[str, tuple[str]] = {
	"General": (
		"Height", "Head Size",
	),

	"UpperBody": (
		"Neck Width", "Neck Thickness",	"Shoulder Width", "Shoulder Thickness", "Upper Torso Width",
		"Upper Torso Thickness", "Lower Torso Width", "Lower Torso Thickness",
	),

	"Chest": (
		"Breast Size", "Breast Vertical Position", "Breast Spacing", "Horizontal Position", "Vertical Angle",
		"Breast Depth",	"Breast Roundness", "Areaola Depth", "Nipple Thickness", "Nipple Depth", 
	),

	"LowerBody": (
		"Waist Position", "Belly Thickness", "Waist Width", "Waist Thickness", "Hip Width", "Hip Thickness",
		"Butt Size", "Butt Angle",
	),

	"Legs": (
		"Upper Thigh Width",  "Upper Thigh Thickness",  "Lower Thigh Width",  
	),

};

def getValues(characterData:bytes) -> dict[str, dict[str, float]]:
	resultsDict:dict[str, dict[str, float]] = {};
	for (sectionName, valueNames) in valuesToSearchFor.items():
		resultsDict[sectionName] = {};

		for valueName in valueNames:
			try:
				decodedValue:float = search.findValue(characterData, valueName);
				resultsDict[sectionName][valueName] = decodedValue;
			except ValueError:
				print(f"Could not find [{valueName}] in file.");

	return resultsDict;


def main() -> None:
	#filePath:str = f"CharacterCards/{input('Full name of the card to read [WITH .png]\n> ')}";
	filePath = "CharacterCards/KoikatsuSun_F_20240410163006202_Tatsuya Yuki.png" #TMP.

	data:bytes = b'';
	with open(filePath, "rb") as pngFile:
		fileData:list[bytes] = pngFile.readlines();
		for line in fileData:
			data += line;


	endOfImageData:int = str(data).find("IEND");
	characterData:bytes = bytes(str(data)[endOfImageData:], encoding="utf-8");
	

	valuesDict:dict[str, float] = getValues(characterData);

	pprint(valuesDict);




if (__name__ == "__main__"):
	main();