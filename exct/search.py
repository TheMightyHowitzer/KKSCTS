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

defaultValues:dict[str,int] = {
	"Body Height": 30,

	"Breast Size": 43,

	"Breast Depth": 40,
	"Breast Roundness": 62,

	"Shoulder Width": 30,
	"Shoulder Thickness": 13,
	"Upper Torso Width": 15,
	"Upper Torso Thickness": 81,
	"Lower Torso Width": 44,
	"Lower Torso Thickness": 42,

	"Belly Thickness": 9,
	"Waist Width": 15,
	"Waist Thickness": 69,
	"Hip Width": 0,
	"Hip Thickness": 37,
	"Butt Size": 68,

	"Upper Thigh Width": 63,
	"Upper Thigh Thickness": 62
};

sideSearches:tuple[str] = (
	"bustSoftness",
	"bustWeight",
	"areolaSize"
);



global numberOfValues, numberOfFoundValues;
numberOfValues = len(necessaryValuesMap) + len(sideSearches);
numberOfFoundValues = 0;



def allowed(value:float) -> bool:
	return (abs(value) <= utils.HIGHEST_ALLOWABLE_VALUE) and (abs(value) >= utils.LOWEST_ALLOWABLE_VALUE);


def getSliderValues(data:list[int], resultsDict:dict[str, int]) -> dict[str, int]:
	global numberOfValues, numberOfFoundValues;

	caIndex:int = utils.searchInList(data, 0xCA); #Start
	acIndex:int = utils.searchInList(data, 0xAC); #End
	relevantData:list[int] = data[caIndex:acIndex];
	numberOfValues = len(relevantData) // 5; #[4 bytes of data, 1 byte seperator] repeatedly.


	#Search through relevant data and find necessary values (in necessaryValuesMap.)
	for i in necessaryValuesMap.keys():
		#print(i, "search for: ", end="")
		#if (i > numberOfValues): print("broke"); break; #Don't try to access extra bytes if less is found in the file.
		#else: print()

		startIDX:int = i*5;
		endIDX:int = (i+1) * 5 - 1;
		bytesData:bytes = bytes(relevantData[startIDX:endIDX]);

		#Convert to a IEEE754 floating-point value.
		rawFloatValue:float = translator.bytesToFloat(bytesData);
		
		searchName:str = necessaryValuesMap[i];
		cleanedIntValue:int = 0;
		if (not allowed(rawFloatValue)):
			cleanedIntValue = defaultValues[searchName];
		else:
			#Clean and add to dataset.
			cleanedIntValue = int(round(rawFloatValue, 2) * 100.0);
			numberOfFoundValues += 1;

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
