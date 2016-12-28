import imageio
import os
import subprocess
class Gif_Creator:
	
	def gnuplot_single_frame(self,array):
		data_file= open("sort1.dat","w")
		for count,elem in enumerate(array):
			data_file.write(str(count)+" "+str(elem)+"\n" )
		data_file.close()
		#os.system("gnuplot sort1png.gnu")
		p = subprocess.Popen(["gnuplot", "sort1png.gnu"])
		p.wait()
		return(imageio.imread("sort1.png"))
	def array_array_to_gif(self,array,filename):
		image_arr=[]
		for i in array:
			image_arr.append(self.gnuplot_single_frame(i))
		kwargs={"fps":"10"}
		imageio.mimsave(filename+".gif", image_arr,"GIF",**kwargs)
		print("utworzono plik animacja.gif, z liczba klatek:"+str(len(image_arr)))
		os.remove("sort1.png")
		os.remove("sort1.dat")
