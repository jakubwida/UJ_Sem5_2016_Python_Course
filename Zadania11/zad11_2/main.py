from sorting_algorithms import Bubble_Sort
from number_list_generator import Number_List_Generator
from utils import Gif_Creator


NLG=Number_List_Generator()
array= NLG.random_list(15)
BS= Bubble_Sort(array)
print("praca w toku...")

out_arr=[]
while True:
	out=BS.step()
	if out!=None:
		out_arr.append(list(out))
	else:
		break



GC= Gif_Creator()
GC.array_array_to_gif(out_arr,"animacja")

