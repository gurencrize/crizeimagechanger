# coding=utf-8
import dropbox #Dropobxのファイルをいじる
from PIL import Image #画像データの編集をする
import os

#自分のdropboxアカウントと接続
accesskey=
dbx = dropbox.Dropbox(accesskey)
dbx.users_get_current_account()
imagepath='\\カメラアップロード'
dropboxpath=os.path.expanduser('~')
print(dropboxpath)
#ファイル一覧を出力
for entry in dbx.files_list_folder(imagepath).entries:
    print(entry.name)
    #拡張子がpngかどうか調べる
    if entry.name[-4:] == '.png':
        #画像をjpg形式に変換
        img = Image.open(dropboxpath+imagepath+'/'+entry.name)
        upload = dropboxpath+imagepath+'\\'+entry.name[:-4]+'.jpg'
        img.save(upload,'jpg')
