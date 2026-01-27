class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        already_done = 0
        output_list = []
        values_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000 }
        for i in s:
            output_list.append(values_dict[i])
        for i in range(len(output_list)):
            if already_done == 1:
                already_done = 0
            elif i == (len(output_list)-1):
                output += output_list[i]
            elif output_list[i] >= output_list[i+1]:
                output+= output_list[i]
            else:
                output+= output_list[i+1] - output_list[i]
                already_done = 1
        return(output)

#Accepted Solution