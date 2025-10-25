"search.py"
from exct import utils, translator;


#Stores the index and the associated value name.
necessaryValuesMap:dict[int, str] = {
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

sideSearches:tuple[str] = (
	"bustSoftness",
	"bustWeight",
	"areolaSize"
);

numberOfValues = len(necessaryValuesMap) + len(sideSearches);



def allowed(value:float) -> bool:
	return (abs(value) <= utils.HIGHEST_ALLOWABLE_VALUE) and (abs(value) >= utils.LOWEST_ALLOWABLE_VALUE);


def getSliderValues(data:list[int], resultsDict:dict[str, int]) -> dict[str, int]:
	caIndex:int = utils.searchInList(data, 0xCA); #Start
	acIndex:int = utils.searchInList(data, 0xAC); #End
	relevantData:list[int] = data[caIndex:acIndex];
	numberOfValues:int = len(relevantData) // 5; #[4 bytes of data, 1 byte seperator] repeatedly.


	#Search through relevant data and find necessary values (in necessaryValuesMap.)
	for i in necessaryValuesMap.keys():
		if (i > numberOfValues): break; #Don't try to access extra bytes if less is found in the file.

		startIDX:int = i*5;
		endIDX:int = (i+1) * 5 - 1;
		bytesData:bytes = bytes(relevantData[startIDX:endIDX]);

		#Convert to a IEEE754 floating-point value.
		rawFloatValue:float = translator.bytesToFloat(bytesData);
		if (not allowed(rawFloatValue)): continue;

		#Clean and add to dataset.
		cleanedIntValue:int = int(round(rawFloatValue, 2) * 100.0);
		searchName:str = necessaryValuesMap[i];
		resultsDict[searchName] = cleanedIntValue;


	return resultsDict;





def getSideSearches(data:list[int], resultsDict:dict[str, int]) -> dict[str, int]:
	#Get alternative searches

	for search in sideSearches:
		#Clip data to just after the search
		searchInt:list[int] = utils.convertStringToIntList(search);
		index:int = utils.searchInList(data, searchInt);
		relevantData:list[int] = data[index:];

		#Clip data to be from seperator, +4 bytes.
		caIndex:int = utils.searchInList(data, [0xCA,]);
		floatBytes:list[int] = relevantData[caIndex:caIndex+4];

		#Convert to a IEEE754 floating-point value.
		rawFloatValue:float = translator.bytesToFloat(bytes(floatBytes));
		if (not allowed(rawFloatValue)): continue;

		#Clean and add to dataset.
		cleanedIntValue:int = int(round(rawFloatValue, 2) * 100.0);
		resultsDict[search] = cleanedIntValue;


	return resultsDict;
