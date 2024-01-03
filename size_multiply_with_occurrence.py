'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t,z):
    substringArray=[]
    substringArrayForSecond=[]
    maxValues=[]
    #Write your alghoritm here.
    for i in range(len(t)):
        for j in range(len(t)-1-i):
            substringArray.append(t[i:len(t)-j])

    for i in range(len(z)):
        for j in range(len(z)-1-i):
            substringArrayForSecond.append(z[i:len(z)-j])

    for element in substringArray:
        counter=0
        for elementForSecond in substringArrayForSecond:
            if elementForSecond == element:
                counter=counter+1
        maxValues.append(counter*len(element))
    maxValue= max(maxValues)
    maxIndex= maxValues.index(maxValue)

    return "Substring is {}. Max value is {}".format(substringArray[maxIndex], maxValues[maxIndex])

if __name__ == '__main__':
    print(find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))