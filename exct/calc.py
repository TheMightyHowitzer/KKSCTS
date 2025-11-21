"calc.py"

import math as maths;
from collections.abc import Callable;
from exct import utils;






def getValueIfInMap(vMap:dict[str,int]|dict[str,float|None], key:str) -> int:
	#Returns value if in the map, else raises an error.
	if key in vMap:
		v:int|None = vMap[key];
		if (v is not None): return v;
	raise KeyError(f"Key [{key}] has no associated value.");



#Complex value functions;
def underBustCalc(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		variable_C29:float = getValueIfInMap(vMap, "Shoulder Width");
		variable_C30:float = getValueIfInMap(vMap, "Upper Torso Width");
		variable_C33:float = getValueIfInMap(vMap, "Hip Width");
		variable_D29:float = getValueIfInMap(vMap, "Shoulder Thickness");
		variable_D30:float = getValueIfInMap(vMap, "Upper Torso Thickness");

	except KeyError:
		print("Underbust Failed")
		return None; #Failed.
	L7 = 21.5
	O7 = 0.4
	Q7 = L7/(1+O7/3)
	L14 = 2869/3000 + 131/150000 * variable_C25
	L20 = (variable_C29*0.9+variable_C30*1.1)/2
	if 0<= L20 and L20 <= 100:
		P20 = L20/3 + L20**2 / 150
	else:
		P20 = L20
	L29 = Q7*L14*(1+P20/100*O7)
	M7 = 20.8/27.73
	N7 = L7*M7
	P7 = 0.9
	R7 = N7/(1+P7/3)
	M20 = (variable_D29*0.9+variable_D30*1.1)/2
	if 0<= M20 <= 100:
		Q20 = M20/3 + M20**2 / 150
	else:
		Q20 = M20
	M29 = R7*L14*(1+Q20/100*P7)
	uBust = (2*maths.pi*maths.sqrt(((L29/3)**2+(M29/3)**2)/2))+(L29+M29)*2/3

	return uBust;


def cupSize(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		print("Found Body Height")
		variable_C27:float = getValueIfInMap(vMap, "Breast Size");
		print("Found Breast Size")
		variable_D27:float = getValueIfInMap(vMap, "Breast Depth");
		print("Found Breast Depth")
		variable_E27:float = getValueIfInMap(vMap, "Breast Roundness");
		print("Found Breast Shape")
		variable_C29:float = getValueIfInMap(vMap, "Shoulder Width");
		print("Found Shoulder Width")
		variable_C30:float = getValueIfInMap(vMap, "Upper Torso Width");
		print("Found Upper Torso Width")
		variable_D29:float = getValueIfInMap(vMap, "Shoulder Thickness");
		print("Found Shoulder Thickness")
		variable_D30:float = getValueIfInMap(vMap, "Upper Torso Thickness");
		print("Found Upper Torso Thickness")

	except KeyError:
		print("Cup Failed")
		return None; #Failed.
	Q42 = 20.16
	L7 = 21.5
	K45 = 2*L7-Q42
	O7 = 0.4
	M45 = O7
	P45 = K45/(1+M45/3)
	L14 = 2869/3000 + 131/150000 * variable_C25
	L20 = (variable_C29*0.9+variable_C30*1.1)/2
	if 0<= L20 <= 100:
		P20 = L20/3 + L20**2 / 150
	else:
		P20 = L20
	print("Line 86 clear")
	N48 = P45*L14*(1+P20/100*M45)
	M7 = 20.8/27.73
	O45 = M7
	L45 = K45*O45
	P7 = 0.9
	N45 = P7
	Q45 = L45/(1+N45/3)
	M20 = (variable_D29*0.9+variable_D30*1.1)/2
	if 0<= M20 <= 100:
		Q20 = M20/3 + M20**2 / 150
	else:
		Q20 = M20
	print("Line 98 clear")
	O48 = Q45*L14*(1+Q20/100*N45)
	N52 = 10.5
	L49 = (450+variable_E27)/500
	G27 = 100
	O52 = 14/15+variable_C25*1/750
	M52 = variable_C27/50*N52*L49*G27/100*O52
	K49 = variable_D27/10000*30+0.85
	if variable_C27 > 50:
		L52 = (N52 * (2/3) * (1 + (variable_C27 - 50) / 25))*K49 * (G27 / 100) * O52
	else:
		L52 = (N52 * (2/3) * (variable_C27 / 50))*K49 * (G27 / 100) * O52
	print("Line 111 clear")
	K52 = (((M52/2)**2*(L52/3))*2/3*maths.pi) + ((M52/2)**2 * maths.pi * L52 * (2 / 3) / 3)
	cupSizeCalc = ((maths.sqrt(((maths.pi*N48*O48/9+N48*O48/9*5)+((pow(K52/2*3/maths.pi,1/3))**2*maths.pi))/maths.pi)*2*maths.pi)-(maths.sqrt((maths.pi*N48*O48/9+N48*O48/9*5)/maths.pi)*2*maths.pi))/2.54
	
	return cupSizeCalc;



def bustCalc(vMap:dict[str,int]) -> float|None:
	try:

		variable_D27:float = getValueIfInMap(vMap, "Breast Depth");

	except KeyError:
		print("Bust Failed")
		return None; #Failed.

	C14 = underBustCalc(vMap)
	F15 = cupSize(vMap)
	K49 = variable_D27/10000*30+0.85
	bust = C14+F15*2.54*K49

	return bust;



def waistCalc(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		print("Found Body Height")
		variable_C31:float = getValueIfInMap(vMap, "Lower Torso Width");
		print("Found Lower Torso Width")
		variable_C32:float = getValueIfInMap(vMap, "Upper Torso Width");
		print("Found Upper Torso Width")
		variable_E32:float = getValueIfInMap(vMap, "Belly Thickness");
		print("Found Belly Thickness")
		variable_C31:float = getValueIfInMap(vMap, "Lower Torso Width");
		print("Found Lower Torso Width")
		variable_C32:float = getValueIfInMap(vMap, "Waist Width");
		print("Found Waist Width")
		variable_E32:float = getValueIfInMap(vMap, "Belly Thickness");
		print("Found Belly Thickness")
		variable_D29:float = getValueIfInMap(vMap, "Shoulder Thickness");
		print("Found Shoulder Thickness")
		variable_D30:float = getValueIfInMap(vMap, "Upper Torso Thickness");
		print("Found Upper Torso Thickness")

	except KeyError:
		print("waist failed")
		return None; #Failed.
	L8 = 18.82
	O8 = 0.96
	Q8 = L8/(1+O8/3)
	L14 = 2869/3000 + 131/150000 * variable_C25
	L21 = (variable_C32*0.7+variable_C31*1.3)/2
	if 0 <= L21 <= 100:
		P21 = L21/3 + L21**2 / 150
	else:
		L21
	N15 = 1+variable_E32/1000
	L30 = Q8*L14*(1+P21/100*O8)*N15
	L7 = 21.5
	M7 = 20.8/27.73
	N7 = L7*M7
	P7 = 0.9
	R7 = N7/(1+P7/3)
	M20 = (variable_D29*0.9+variable_D30*1.1)/2
	if 0<= M20 <= 100:
		Q20 = M20/3 + M20**2 / 150
	else:
		Q20 = M20
	M30 = R7*L14*(1+Q20/100*P7)
	waistCirc = (2*maths.pi*maths.sqrt(((L30/3)**2+(M30/3)**2)/2))+(L30+M30)*2/3
	return waistCirc;




def hipsCalc(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		print("Found Body Height")
		variable_C33:float = getValueIfInMap(vMap, "Hip Width");
		print("Found Hip Width")
		variable_D33:float = getValueIfInMap(vMap, "Hip Thickness");
		print("Found Hip Thickness")
		variable_C34:float = getValueIfInMap(vMap, "Butt Size");
		print("Found Butt Size")
		variable_C35:float = getValueIfInMap(vMap, "Upper Thigh Width");
		print("Found Thigh Width")
		variable_D35:float = getValueIfInMap(vMap, "Upper Thigh Thickness");
		print("Found Thigh Thickness")

	except KeyError:
		print("hips Failed")
		return None; #Failed.

	O9 = 0.43
	L9 = 30.96
	Q9 = L9/(1+O9/3)
	if 0 <= variable_C33 and variable_C33 <= 100:
		P22 = variable_C33/3 + variable_C33**2 / 150
	else:
		P22 = variable_C33
	L14 = 2869/3000 + 131/150000 * variable_C25
	K24 = (variable_C35+variable_D35)/2
	L31 = Q9*(1+P22/100*O9)*L14*(1+K24/3000-1/60)
	M9 = 21.22/31.84
	N9 = L9*M9
	P9 = 0.46
	R9 = N9/(1+P9/3)
	if 0 <= variable_D33 and variable_D33 <= 100:
		Q22 = variable_D33/3 + variable_D33**2 / 150
	else:
		Q22 = variable_D33

	M31 = R9*(1+Q22/100*P9)*L14*(0.95+variable_C34/1000)*(0.975+K24/2000)
	hipCirc = (2*maths.pi*maths.sqrt(((L31/3)**2+(M31/3)**2)/2))+(L31+M31)*2/3

	return hipCirc;




def buxCalc(vMap:dict[str,int], prevValues:dict[str,float|None]) -> float|None:
	try:
		return 3000.0 * getValueIfInMap(prevValues, "Bust") * getValueIfInMap(prevValues, "Hips") * (1.15 ** (getValueIfInMap(prevValues, "Cup Size")/getValueIfInMap(prevValues, "Underbust")/getValueIfInMap(prevValues, "Height")/(getValueIfInMap(prevValues, "Waist") ** 1.5)));
	except KeyError:
		return None #Failed.



funcMap:dict[str,Callable|None] = {
	"Underbust":	underBustCalc,
	"Cup Size":		cupSize,
	"Bust":			bustCalc,
	"Waist":		waistCalc,
	"Hips":			hipsCalc,
	"Height":	 	(lambda vMap : 150.0 + (0.27 * getValueIfInMap(vMap, "Body Height"))),
};



def calculateValues(readValues:dict[str,int]) -> dict[str, float]:
	resultsDict:dict[str,float] = {key:func(readValues) for (key,func) in funcMap.items()};
	resultsDict["Bux"] = buxCalc(readValues, resultsDict);
	return resultsDict;