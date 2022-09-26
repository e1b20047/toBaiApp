from ctypes import resize
import cv2
import tkinter as tk
import re
import numpy as np
from tkinter import filedialog
from PIL import Image
import tkinterdnd2 as tk2


buttonColor='#7777FF'
resizePicture_y=80
window_width=400
window_height=300

register=[]#ここに変換する画像のパスを登録
def isNumber(self,S):
    if(re.match(re.compile('0+'))):#0は除外
        return False
    if(re.match(re.compile('[0-9]+'),S)):#数値のみで構成された文字列の場合True
        return True
    return False

#ボタン入力時イベント

def getFilePathToFileDialog():
    filenames=filedialog.askopenfilenames(
    title="画像ファイルを開く",
    filetypes=[("image file",".bmp .png .jpg .jpeg .gif")],
    initialdir=""
    )
    return filenames

def dialogButtonClick():
	filenames=getFilePathToFileDialog()
	resistPath(filenames)
	printPicture()
	#createBigPicture(filenames)
 
def decideButtonClick():
    printPath()
    createBigPicture(register)
    return


def getPictureToPath(path):
	
	return 


def createBigPicture(filenames):
	num=entry.get()#フォームから値を取得
	if((num.isdecimal())):#正しい入力値ならばそのまま
		bairitu=int(num)
	else:#正しくない入力値ならば終了
		print("入力値が不正です")
		return
	for filename in filenames:#取得した配列全体を見る
		buf=np.fromfile(filename,np.uint8)
	
		dotPoint=len(filename)
		dotPoint=filename.rfind('.')#後ろからドットの位置を探す(拡張子とファイル名の分岐点を見つける)
		
		newFileName=filename[:dotPoint]+"_"+str(num)+"bai"+filename[dotPoint:]	
		image = np.asarray(Image.open(filename).convert("RGBA"), dtype=np.uint8)
		#img = cv2.imread(filename)#ダイアログで取得したパスから画像読み出し
		img=cv2.imdecode(buf,cv2.IMREAD_UNCHANGED)
		img2=image.repeat(bairitu, axis=0).repeat(bairitu, axis=1)#bairitu倍化
	#print(img2.shape)
		Image.fromarray(img2).save(newFileName)
	#cv2.imwrite(newFileName2,img3) #なんかできない
		print("output:"+newFileName)

#window作成
root = tk2.Tk()
# ウインドウのサイズ指定

root.geometry(str(window_width)+"x"+str(window_height))
root.configure(bg='#8888FF')

#入力フォーム
entry=tk.Entry(root,width=3,validate="key",font=('',40),bg=buttonColor)
entry.insert(0,10)#初期値に10を置く
entry.place(x=10,y=10)
label1=tk.Label(text="倍にする",font=('',30),bg='#8888FF')
label1.place(x=100,y=20)

#画像表示キャンバス
canvas=tk.Canvas(bg='#7777E0',width=window_width,height=window_height/2)
canvas.place(x=0,y=window_height/2)


def resistPath(filenames):
    for filename in filenames:
        register.append(filename)
    print(register)
    return

def printPath():
    for filename in register:
        print(filename)

def printPicture():
	count=0
	for filename in register:
		if(count>=5):return
		image = np.asarray(Image.open(filename).convert("RGBA"), dtype=np.uint8)
		image = Image.open(filename)
		
		
		resizePicture_x=resizePicture_y
		photo=image.resize((resizePicture_x,resizePicture_y))
		photo=tk.PhotoImage(photo)
		canvas.create_image(10+count*80,10,image=photo)
		count+=1
	return


#ダイアログ表示ボタン
dialogButton=tk.Button(root,text='画像を選択',command=dialogButtonClick,height=1,width=10,bg=buttonColor)
dialogButton.place(x=10,y=80)

#変換開始ボタン
decideButton=tk.Button(root,text='画像変換開始',command=decideButtonClick,height=1,width=10,bg=buttonColor)
decideButton.place(x=100,y=80)


# ウインドウ状態の維持
root.mainloop()
