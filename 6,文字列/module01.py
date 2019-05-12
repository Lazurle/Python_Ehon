# ◆ モジュール

# ◆ モジュールのインポート
# これまでたびたび登場してきたimportはほかの
# Pythonスクリプトファイルを読み込む命令です。
# 読み込まれるファイルことをモジュールといいます。
import re # re.pyというスクリプトファイルを読み込んでいる。「.py」は いらない
          # re.pyファイルはPythonのインストールフォルダのlibフォルダの中にある。
s = 'Learn Python, Shiori'
mobj = re.match('Le', s)
# あらかじめ用意されている様々な便利な機能を手軽に利用できます。

## モジュールファイルはカレントフォルダや、libフォルダに置かれている必要があります。
## モジュールの探索先のパスを得るには次の様なコードを書きます。
import sys
# print( sys.path )
# パス（場所）が出てくる

# ◆ モジュールの作成
# モジュールは誰でも作ることが可能。
# スクリプトファイルと同じフォルダに「mymodule.py」
# というファイルを作って、これをインポートするには次のようにします。
import mymodule
mymodule.myFunc()
# result -> 野獣先輩

# ◆ 別名を下記のようにつけることも可能。
import mymodule as yaju
yaju.myFunc()
# result -> 野獣先輩

# ◆ 関数のインポート
# 次のようにfromを使って特定のメソッドだけをインポートすることも可
from mymodule import myFunc
myFunc()
# result -> 野獣先輩

# ◆ フォルダ階層の指定
from mod.mod1 import mymodule1
mymodule1.myFunc()

### パッケージ
# カレントフォルダ\mod\mod1.py, mod2.py, __init__.py
# とある場合「__init__.py」に
from . import mod1
from . import mod2
#と記述し、カレントフォルダにあるソースファイルでは、次の様に指定してimport文を記述
import mod
# これを実行すると自動的に「__init__.py」が実行されて、
# 「mod1.py」「mod2.py」がインポートされ、これらのファイルの中のメソッドや変数を
# 利用することが可能
