def findClosestValueInBst(tree, target, values=(float('inf'), float('inf'))):
    if tree == None:
		if len(values) != 0:
			return values[0]
		return None
	if target == tree.value:
		return target
	close = abs(tree.value - target)
	close_to = tree.value
	if close < values[1]:
		values = (close_to, close)
	if tree.left is None and tree.right is None:
		return values[0]
	if target >= tree.value:
		return findClosestValueInBst(tree.right, target, values)
	else:
		return findClosestValueInBst(tree.left, target, values)
    


