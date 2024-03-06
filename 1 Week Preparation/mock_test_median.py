# Find the median given an array of elements
import statistics as st

def getMedian(arr):
    median = st.median(arr)
    print(median)


arr = [0,1,2,3,4,5,6]
getMedian(arr)