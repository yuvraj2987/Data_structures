/*
 * Build Tree from In-Order and Pre-Order array List
 * idx       - 0 | 1  | 2 | 3 | 4 | 5  | 6 | 7  |
 * In -Order - 4 | 10 | 3 | 1 | 7 | 11 | 8 | 2  |
 * Pre-Order - 7 | 10 | 4 | 3 | 1 | 2  | 8 | 11 |
 * pre_idx = 0,1, 2, 3, 4, 5
 * in_start = 0
 * in_end = 7
 * bT(pre, in, 0, 7)
 * in.length = 8
 * pre.length = 8
 * root_elm = 7
 * nd -> 7
 * partition_idx = 4
 * nd.left = bT(pre, in, 0, 3)
 * nd.right = bT(pre, in, 5, 7)
 *
 * bT(pre, in, 0, 3)
 * in_start = 0
 * in_end = 3
 *root_elm = 10
  partition_idx = 1
  nd.left = bT(pre, in, 0, 0)
  nd.right = bT(pre, in, 2, 3)
 bT(pre, in, 0, 0)
 in_start = 0
 in_end = 0
 bT(pre, in, 2, 3)
 in_start = 2
 in_end = 3
 root_elm = 3
 partition_idx = 2
 nd.left = bT(pre, in, 2, 1) = null
 nd.right = bT(pre, in, 3, 3)
 root_elm = 1

 * */

public class BuildTree
{
    private static int pre_idx;
    public static Tree buildTree(int[] pre_order, int[] in_order)
    {
        if(pre_order == null || in_order == null) return null;

        if(pre_order.length != in_order_length) return null;

        Tree t = new Tree();
        pre_idx = 0;
        t.root = buildTree(pre_order, in_order, 0, in_order.length-1);
    
    }

    private static TreeNode buildTree(int[] pre, int[] in, int in_start, int in_end)
    {
        if (in_start > in_end) return null;

        if(in_start < 0 || in_end >= in.length) return null;

        if(pre_idx >= pre.length) return null; /*Unlikely*/

        int root_elm = pre[pre_idx++];//7, 10, 4, 3, 1
        TreeNode nd = new TreeNode(root_elm);
        if(in_start == in _end)
        {
            if(in[in_start] != root_elm)
                return null;
            else
                return nd;
        }
        int partition_idx = findElementIdx(in, root_elm, in_start, in_end);
        if(partition_idx < 0) return null; // Should throw exception?? This means 2 arrays do not represent the same tree

        nd.left  = buildTree(pre, in, in_start, partition_idx-1);
        nd.right = buildTree(pre, in, paratition_idx+1, in_end);
        return nd;
    }

}
