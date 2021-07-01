def make_album(singer,album,num=None):
	singer_album={'singer':singer.title(),'album':album.title()}
	if num:
		singer_album['num']=num
	return singer_album

while True:
	print('\nPls input singer and album:')
	print("(enter'q'quit)")

	singer=input('singer: ')
	if singer=='q':
		break

	album=input('album: ')
	if album=='q':
		break

	singer_album=make_album(singer,album)
	print(singer_album)

