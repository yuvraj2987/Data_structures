


public static int getMedian(int[] arr1, int[] arr2)
{
    if(arr1 == null || arr2 == null) return Interger.MinValue;

    return getMedian(arr1, arr2, 0, arr1.length-1, 0, arr2.length-1);
}


private static int getMedian(int[] arr1, int[] arr2, int start1, int end1, int start2, int end2)
{
    if(start1 > end1 || start2 > end2) return Integer.MinValue;

    if(start1 < 0 || end1 >= arr1.length || start2 < 0 || end2 >= arr2.length)
        return Integer.MinValue;
    
    if(start1 == end1 && start2 == end2)
        /*when there is single element on both side of the array*/
    {
        int median = (arr1[start1] + arr2[start2])/2;
        return median;
    }

    if(end1 - start1 == 1 || end2 - start2 == 1)
    {
        int median = Math.Max(arr1[start1], arr2[start2]) + Math.Min(arr1[end1], arr2[end2]) / 2;
        return median;
    }
    int arr1_median_idx = start1+(end1-start1)/2;
    int arr2_median_idx = start2+(end2-start2)/2;

    median1 = arr1[arr1_median_idx];
    median2 = arr2[arr2_median_idx];
    if (median1 == median2) return median1;

    if(median1 > median2)
    {
        return getMedian(arr1, arr2, start1, arr1_median_idx, arr2_median_idx, end2);
    }
    else
        return getMedian(arr1, arr2, arr1_median_idx, end1, start2, arr2_median_idx);

}
