"search.py"

if (__name__ == "__main__"):
	#Ensures that debugging will import file with correct local path.
	import translator;
else:
	from exct import translator;



SEP_START:bytes	= b"\xca";
SEP_END:bytes	= b"\xad";


def findValue(characterData:bytes, valueName:str) -> float:
	#Finds valueName (case-insensitive)
	valueNameBytes:bytes = valueName.lower().encode("utf-8")

	#Make lowercase copy for searching
	dataLower:bytes = characterData.lower();
	print(valueNameBytes, type(dataLower), str(characterData).find(valueName))
	valueIndex:int = dataLower.find(valueNameBytes);
	if (valueIndex == -1):
		raise ValueError("Could not find " + valueName);

	#Slice from valueName's position
	clippedData:bytes = characterData[valueIndex:];

	#Find separators
	startIndex:int = clippedData.find(SEP_START);
	endIndex:int   = clippedData.find(SEP_END);
	print(startIndex, endIndex);

	if ((startIndex == -1) or (endIndex == -1)):
		raise ValueError("Separators not found");

	relevantBytes:bytes = clippedData[startIndex:endIndex+len(SEP_END)];
	print(relevantBytes)

	#Remove seperators
	relevantBytes = relevantBytes.replace(SEP_START, b"");
	relevantBytes = relevantBytes.replace(SEP_END, b"");
	print(relevantBytes);

	floatValue:float = translator.bytesToFloat(relevantBytes);	
	return floatValue;





if (__name__ == "__main__"):
	#Debugging; not used if file is imported.
	
	print(findValue(
		b'\x74\x61\x6c\x41\x6e\x67\x6c\x65\xca\x3f\x47\xd8\x5b\xb2\x48\x6f\x72\x69\x7a\x6f\x6e\x74\x61\x6c\x50\x6f\x73\x69\x74\x69\x6f\x6e\xca\x3e\xc9\x7f\x3a\xad\x56\x65\x72\x74\x69\x63\x61\x6c\x41\x6e\x67\x6c\x65\xca\x3f\x17\xf2\xca\xa5\x44\x65\x70\x74\x68\xca\x3e\xcb\x83\x0a\xa9\x52\x6f\x75\x6e',
		"HorizontalPosition"
	));