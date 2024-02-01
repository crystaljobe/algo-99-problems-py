#write a program that can print the song "99 Bottles of Beer"
#make sure to change "bottles" to "bottle" at the correct time

def bottle_song(num):
	#print 99 to 0 using a loop/or other
	for x in reversed(range(num + 1)) :
		if x > 2 :
			print(f"{x} bottles of beer on the wall, {x} bottles of beer. \n Take one down and pass it around, {x-1} bottles of beer on the wall.")
		elif x == 2 :
			print(f"{x} bottles of beer on the wall, {x} bottles of beer. \n Take one down and pass it around, {x-1} bottle of beer on the wall.")
		elif x == 1 :
			print(f"{x} bottle of beer on the wall, {1} bottle of beer. \n Take one down and pass it around, no more bottles of beer on the wall. \n No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall.")
bottle_song(1)

####kldjsfalkfdajalskdfjdfls
#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down and pass it around, 98 bottles of beer on the wall.
# ....
# Take one down and pass it around, 1 bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.