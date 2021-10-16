def isMonotonic(array):
    # Write your code here.
    if not array:
		return True
	ctr_p = 0
	ctr_n = 0
	ctr_e = 0
	last = array[0]
	for cur in array[1:]:
		if ctr_p > 0 and ctr_n > 0:
			return False
		if cur > last:
			ctr_p += 1
		elif cur < last:
			ctr_n += 1
		else:
			ctr_e += 1
		
		last = cur
	if len(array)-1 == ctr_p or len(array)-1 == ctr_n or ctr_e == len(array)-1 or ctr_p + ctr_e == len(array)-1 or ctr_n + ctr_e == len(array)-1:
		return True
	return False

