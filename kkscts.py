"kkscts.py"

import sys, os;
from pprint import pprint;
from exct import search;
from exct import calc;
from exct import utils;




def main() -> None:
	#Main program flow.
	inputFilePath:str = f"CharacterCards/{input('Full name of the card to read [WITHOUT .png extension]\n> ')}.png";
	if (len(inputFilePath) == 19): #User did not input any file; use default. (19 chars the user did not enter)
		inputFilePath = utils.DEFAULT_READ_FILEPATH;
	characterName:str = inputFilePath.replace("CharacterCards/KoikatsuSun_", "").replace(".png", "");
	outputFilePath:str = f"result/{characterName}.result.txt";


	#Load the file;
	data:list[int] = utils.loadKKSFile(inputFilePath);
	

	#Read values from data;
	readValues:dict[str, int] = {};
	readValues = search.getSliderValues(data, readValues); #From main chunk after data start flag

	readValues["<SPACER>"] = 0; #Adds space to the output for formatting.
	readValues = search.getSideSearches(data, readValues); #From the wider dataset


	#Print values
	numFound:int = search.numberOfFoundValues-1;
	print(f"Read [{numFound} of {search.numberOfValues}] values ({100.0*(numFound/search.numberOfValues):.2f}%)", end="");
	if (numFound < search.numberOfValues):
		print(" - Missing values defaulted to slider base values.");
	else:
		print(); #Newline.

	utils.WHITESPACE = max([len(key) for key in readValues.keys()]);


	#Calculate values;
	resultantValues:dict[str,float] = calc.calculateValues(readValues);


	#Debugging only
	if (utils.DEBUG):
		print();
		pprint(resultantValues);
		print();


	#Write to the file for the user;
	utils.writeToOutputFile(outputFilePath, resultantValues);





if (__name__ == "__main__"):
	main();