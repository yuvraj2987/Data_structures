# SubTree Problem
## CCIR - 4.8

Two very large binary trees. T1 and T2. T1 has million of nodes. T2 has hundreds of nodes.
The alternative solution in CCIR call subTree and treeMatch methods recursively. 
They claim ln(n)+ lg(m) space complexity. Which is confusing. 
Consider very unbalanced tree. Then to subTree to return False it has to go till n-m depth. 

So I am writing an answer using BFS.
At any time queue will have at max 3 elements.
