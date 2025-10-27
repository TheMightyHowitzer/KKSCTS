"calc.py"

import math as maths;
from collections.abc import Callable;
import utils;






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

	except KeyError:
		return None; #Failed.

	avgC:float = (variable_C29*0.9 + variable_C30*1.1)/2.0;
	avgD:float = (variable_D29*0.9 + variable_D30*1.1)/2.0;

	termC:float = (avgC/3.0 + avgC**2 / 150.0) if (0.0 <= avgC <= 100.0) else avgC;
	termD:float = (avgD/3.0 + avgD**2 / 150.0) if (0.0 <= avgD <= 100.0) else avgD;


	A:float = utils.UBUST_BASE_50_WIDTH / (1.0 + utils.UBUST_W_SLIDER_RATIO / 3.0) * (2869.0/3000.0);
	B:float = (131.0/150000.0) * variable_C25 * (1.0 + termC / 100.0 * utils.UBUST_W_SLIDER_RATIO) / 3.0;
	subTermA = A + B;

	C:float = utils.UBUST_BASE_50_WIDTH * 20.8 / 27.73 / (1.0 + utils.UBUST_D_SLIDER_RATIO / 3.0) * (2869.0/3000.0);
	D:float = (131.0/150000.0) * variable_C25 * (1.0 + termD / 100.0 * utils.UBUST_D_SLIDER_RATIO) / 3.0;
	subTermB = C + D;

	sqrtTerm:float = maths.sqrt((subTermA**2 + subTermB**2)/2.0);
	addTerm:float = subTermA + subTermB;

	return (2.0 * maths.pi * sqrtTerm + (addTerm * (2.0/3.0)));


def cupSize(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		variable_C27:float = getValueIfInMap(vMap, "Breast Roundness");
		variable_E27:float = getValueIfInMap(vMap, "Breast Shape");
		variable_C29:float = getValueIfInMap(vMap, "Shoulder Width");
		variable_C30:float = getValueIfInMap(vMap, "Upper Torso Width");

	except KeyError:
		return None; #Failed.


	avgC:float = (variable_C29*0.9 + variable_C30*1.1) / 2.0;

	# Conditional term
	termC:float = (avgC/3.0 + avgC**2 / 150.0) if (0.0 <= avgC <= 100.0) else avgC;

	componentA:float = maths.pi*2.0*utils.UBUST_BASE_50_WIDTH - utils.MODEL_SIZE/(1.0 + utils.UBUST_W_SLIDER_RATIO/3.0)*(2869.0/3000.0) + (131.0/150000.0) * variable_C25 * (1.0 + termC / 100.0 * utils.UBUST_W_SLIDER_RATIO) * 20.8 / 27.73 / 9.0;
	componentB:float = componentA * 5 + 2*utils.UBUST_BASE_50_WIDTH;
	termMult:float = (utils.BREAST_BASE_50 * (2.0/3.0) * (1.0 + (variable_C27-50.0)/25.0)) if (variable_C27 > 50.0) else (utils.BREAST_BASE_50 * (2.0/3.0) * variable_C27 / 50.0);

	subTermA:float = ((variable_C27/50.0 * utils.BREAST_BASE_50 * (450.0 + variable_E27)/500.0 * variable_MULT/100.0 * 14.0/15.0 + variable_C25/1500.0)**2 * (termMult * variable_D27 / 10000.0 * 30.0 + 0.85 * variable_MULT / 100.0 * (14.0/15.0) + variable_C25 / 1500.0) * (2.0/3.0) * maths.pi);
	subTermB:float = ((variable_C27/50.0 * utils.BREAST_BASE_50 * (450.0 + variable_E27)/500.0 * variable_MULT/100.0 * 14.0/15.0 + variable_C25/1500.0)**2 * maths.pi * (termMult * variable_D27 / 10000.0 * 30.0 + 0.85 * variable_MULT / 100.0 * 14.0/15.0 + variable_C25 / 1500.0)  * (2.0/3.0)/3.0 / 2.0 * 3.0 / maths.pi)**(1.0/3.0);

	termPower:float = (subTermA + subTermB)**2 * maths.pi;

	return maths.floor(((maths.sqrt(component1 + component2) + termPower*2.0*maths.pi - maths.sqrt(component1 + component2)*2*maths.pi)/2.54));




def bustCalc(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		variable_C33:float = getValueIfInMap(vMap, "Hip Width");
		variable_D33:float = getValueIfInMap(vMap, "Hip Thickness");
		variable_C34:float = getValueIfInMap(vMap, "Butt Size");
		variable_C35:float = getValueIfInMap(vMap, "Thigh Width");
		variable_D35:float = getValueIfInMap(vMap, "Thigh Thickness");

	except KeyError:
		return None; #Failed.


	C33Term:float = (variable_C33/3.0 + variable_C33**2 / 150.0) if (0.0 <= variable_C33 <= 100.0) else variable_C33;
	D33Term:float = (variable_D33/3.0 + variable_D33**2 / 150.0) if (0.0 <= variable_D33 <= 100.0) else variable_D33;

	A:float = variable_L9 / (1.0 + utils.HIP_W_SLIDER_RATIO / 3.0) * (1.0 + C33Term / 100.0 * utils.HIP_W_SLIDER_RATIO) * (2869.0/3000.0);
	B:float = (131.0/150000.0) * variable_C25 * (1.0 + (variable_C35 + variable_D35)/2.0/3000.0 - (1.0/60.0));
	subTermA:float = A + B;

	C:float = variable_L9 * (21.22/31.84) / (1.0 + utils.HIP_D_SLIDER_RATIO / 3.0) * (1.0 + D33Term / 100.0 * utils.HIP_D_SLIDER_RATIO) * (2869.0/3000.0);
	D:float = (131.0/150000.0) * variable_C25 * (0.95 + variable_C34 / 1000.0) * (0.975 + (variable_C35 + variable_D35)/2.0/2000.0);
	subTermB:float = C + D;

	sqrtTerm:float = maths.sqrt((subTermA** + subTermB**2)*0.5);
	addTerm:float = subTermA + subTermB;

	return (2.0 * maths.pi() * sqrtTerm) + (addTerm * (2.0/3.0));



def waistCalc(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		variable_C31:float = getValueIfInMap(vMap, "Lower Torso Width");
		variable_D31:float = getValueIfInMap(vMap, "Lower Torso Thickness");
		variable_C32:float = getValueIfInMap(vMap, "Upper Torso Width");
		variable_D32:float = getValueIfInMap(vMap, "Upper Torso Thickness");
		variable_E32:float = getValueIfInMap(vMap, "Belly Thickness");

	except KeyError:
		return None; #Failed.


	avgC:float = (variable_C32*0.7 + variable_C31*1.3)/2.0;
	avgD:float = (variable_D32*0.7 + variable_D31*1.3)/2.0;

	termC:float = (avgC/3.0 + avgC**2 / 150.0) if (0.0 <= avgC <= 100.0) else avgC;
	termD:float = (avgD/3.0 + avgD**2 / 150.0) if (0.0 <= avgD <= 100.0) else avgD;

	subTermA:float = utils.WAIST_BASE_50_WIDTH / (1.0 + utils.WAIST_W_SLIDER_RATIO/3) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (1.0 + termC / 100.0 * utils.WAIST_W_SLIDER_RATIO) * 1.0 + variable_E32 / 1000.0 / 3.0;
	subTermB:float = utils.WAIST_BASE_50_WIDTH * 17.22 / 21.0 / 1.05 / (1.0 + utils.WAIST_D_SLIDER_RATIO / 3.0) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (1.0 + termD / 100.0 * utils.WAIST_D_SLIDER_RATIO) * 1.0 + variable_E32 / 300.0 / 3.0;

	sqrtTerm:float = maths.sqrt((subTermA**2 + subTermB**2)/2.0);
	addTerm:float = utils.WAIST_BASE_50_WIDTH / (1.0 + utils.WAIST_W_SLIDER_RATIO/3) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (1.0 + term_C / 100.0 * utils.WAIST_W_SLIDER_RATIO) * 1.0 + variable_E32 / 1000.0 + utils.WAIST_BASE_50_WIDTH * 17.22 / 21.0 / 1.05 / (1.0 + utils.WAIST_D_SLIDER_RATIO / 3.0) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (1.0 + term_D / 100.0 * utils.WAIST_D_SLIDER_RATIO) * 1.0 + variable_E32 / 300.0;


	return (2.0 * maths.pi * sqrtTerm + addTerm * (2.0 / 3.0));




def hipsCalc(vMap:dict[str,int]) -> float|None:
	try:
		variable_C25:float = getValueIfInMap(vMap, "Body Height");
		variable_C33:float = getValueIfInMap(vMap, "Hip Width");
		variable_D33:float = getValueIfInMap(vMap, "Hip Thickness");
		variable_C34:float = getValueIfInMap(vMap, "Butt Size");
		variable_C35:float = getValueIfInMap(vMap, "Thigh Width");
		variable_D35:float = getValueIfInMap(vMap, "Thigh Thickness");

	except KeyError:
		return None; #Failed.


	termC:float = (variable_C33/3.0 + variable_C33**2 / 150.0) if (0.0 <= variable_C33 <= 100.0) else variable_C33;
	termD:float = (variable_D33/3.0 + variable_D33**2 / 150.0) if (0.0 <= variable_D33 <= 100.0) else variable_D33;
	
	subterm1:float = utils.HIP_BASE_50_WIDTH / (1.0 + utils.HIP_W_SLIDER_RATIO/3.0) * (1.0 + termC / 100.0 * utils.HIP_W_SLIDER_RATIO) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (1.0 + (variable_C35 + variable_D35)/2.0/3000.0 - 1.0/60.0) / 3.0;
	subterm2:float = utils.HIP_BASE_50_WIDTH * 21.22 / 31.84 / (1.0 + utils.HIP_D_SLIDER_RATIO / 3.0) * (1.0 + termD / 100.0 * utils.HIP_D_SLIDER_RATIO) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (0.95 + variable_C34 / 1000.0) * (0.975 + (variable_C35 + variable_D35)/2.0/2000.0) / 3.0;

	sqrtTerm:float = maths.sqrt(subterm1**2 + subterm2**2)/2.0
	addTerm:float = utils.HIP_BASE_50_WIDTH / (1.0 + utils.HIP_W_SLIDER_RATIO/3.0) * (1.0 + termC / 100.0 * utils.HIP_W_SLIDER_RATIO) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (1.0 + (variable_C35 + variable_D35)/2.0/3000.0 - 1.0/60.0) + utils.HIP_BASE_50_WIDTH * 21.22 / 31.84 / (1.0 + utils.HIP_D_SLIDER_RATIO / 3.0) * (1.0 + termD / 100.0 * utils.HIP_D_SLIDER_RATIO) * 2869.0 / 3000.0 + 131.0 / 150000.0 * variable_C25 * (0.95 + variable_C34 / 1000.0) * (0.975 + (variable_C35 + variable_D35)/2.0/2000.0);

	return (2.0 * maths.pi * sqrtTerm + addTerm * 2.0 / 3.0);




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
	"Bux":			buxCalc
};



def calculateValues(readValues:dict[str,int]) -> dict[str, float]:
	resultsDict:dict[str,float] = {key:func(readValues) for (key,func) in funcMap.items()};
	resultsDict["Bux"] = buxCalc(readValues, resultsDict);
	return resultsDict;