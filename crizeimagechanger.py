# coding=utf-8
import dropbox #Dropobxのファイルをいじる
from PIL import Image #画像データの編集をする
import tempfile

#自分のdropboxアカウントと接続
accesskey=''
dbx = dropbox.Dropbox(accesskey)
dbx.users_get_current_account()
imagepath='/カメラアップロード'
#ファイル一覧を出力
for entry in dbx.files_list_folder(imagepath).entries:
    print(entry.name)
    if entry.name[-4:] == '.png':
        with tempfile.TemporaryDirectory() as dname:
            print(dname)
            dbx.files_download_to_file(dname,imagepath+'/'+entry.name)
