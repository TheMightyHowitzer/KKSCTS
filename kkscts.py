"kkscts.py"

import sys, os, argparse;
import re as regex;
from pprint import pprint;
from exct import search;
from exct import calc;
from exct import utils;


def setupCLIargs() -> argparse.Namespace:
	parser:argparse.ArgumentParser = argparse.ArgumentParser(
		prog="KKSCTS", #Program name
		description="Parses Koikatsu-Sunshine character PNG files into a readable character sheet." #Description
	);

	#Arguments;
	parser.add_argument("-f", "--file", help="The name of the card to use, within the subfolder 'CharacterCards/'", type=str); #Filename
	parser.add_argument("-v", "--verbose", help="Debugging/Verbose output", type=bool); #Verbosity
	parser.add_argument("-q", "--quiet", help="Disables the UI entirely.", type=bool); #UI-hide

	#Read arguments into values;
	return parser.parse_args();



def main(fileName:str) -> None:
	#Main program flow.

	#Handle filename.
	inputFilePath:str = "";
	characterName:str = "";
	if (len(fileName) == 0): #User did not input any file; use default.
		userInput:str = input('Full name of the card to read [WITHOUT .png extension]\n> ');
		if (len(userInput) == 0):
			inputFilePath = f"CharacterCards/{utils.DEFAULT_READ_FILEPATH}";
			characterName = utils.DEFAULT_READ_FILEPATH.replace("KoikatsuSun_", "").replace(".png", "");
		else:
			inputFilePath = f"CharacterCards/{userInput}.png";
			characterName = userInput.replace("KoikatsuSun_", "").replace(".png", "");

	else:
		inputFilePath = f"CharacterCards/{fileName}.png";
		characterName = fileName.replace("KoikatsuSun_", "").replace(".png", "");
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
	args:argparse.Namespace = setupCLIargs();

	fileName:str = f"{args.file}" if (args.file is not None) else "";
	fileName = regex.sub(r'(?i)\.png', '', fileName);

	utils.DEBUG = utils.DEBUG or (args.verbose is not None);
	utils.QUIET = args.quiet is not None;

	main(fileName);