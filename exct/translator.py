"translator.py"

def bytesToFloat(byteData:bytes) -> float:
	#Reinterpret;
	iRep:int = int.from_bytes(byteData, byteorder="big");
	
	#Unpack all 32 bits;
	signBit:bool = bool(iRep >> 31); 		#First bit. (1 is negative, 0 is positive.)
	exponentB:int = (iRep >> 23) & 0xFF;	#Next 8 bits. (127-biased.)
	mantissaU:int = iRep & 0x7FFFFF; 		#Lowest 23 bits. (value of 1.XX but omitting the 1 and only storing the XX)

	#Add normalized 1.
	mantissaU |= 0x800000;

	#Ironically, make it a float for processing.
	mantissaF:float = float(mantissaU) / 8388608; #"Rightshift" by 23, to make it 1.XX
	exponentI:int = exponentB - 127; #Undo the exponent bias.
	power:float = 2 ** exponentI;

	floatValue:float = mantissaF * power;
	if (signBit): #Is negative.
		floatValue *= -1;
	return floatValue;





if (__name__ == "__main__"):
	#Debugging; not used if file is imported.
	
	#0x3F23D70A → 0.64
	print(bytesToFloat(b'\x3F\x23\xD7\x0A'));
	#Prints "0.6399999856948853"