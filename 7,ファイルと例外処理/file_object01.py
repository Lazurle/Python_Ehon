# ファイルを扱うときには、ファイルそのものではなく
# ファイルを開いたときに得られるストリームオブジェクトというものを
# 使います。ストリームというものは「流れ」という意味で、この場合はデータの流れを
# 表しています。

## ◆ ファイルオブジェクト
#ファイル処理の基本と、読み書きに使われるファイルオブジェクトについて見ていく。

# ◆ ファイル
# プログラム上ではファイルは大きく２種
# ・テキストファイル（文字として読める）
# 例：Python(src), HTML etc.
# ・バイナリファイル（文字として読めない）
# 例：画像ファイル、音声ファイル。

# ◆ ファイル処理の基本
# open -> 読み書き（処理） -> close
# ファイルを扱うときは、ファイルそのものではなく、
# ストリームオブジェクトというものとファイルを紐づけて、
# そのオブジェクトを通してデータをやり取りします。
# 直に読み書きするのではなく、間に何かあるイメージ。
# 間にあるものが「ストリームオブジェクト」

# ◆ ファイルを開く
f = open('test.txt', 'r')
# f … ストリームオブジェクト
# 'test.txt' … ファイル名
# 'r' … 処理モード

## ◆ 処理モードの種類
# r -> 読み込み
# w -> 書き出し（新規作成）
# a -> 書き出し（追記）
# r+ -> 読み書き両用

# ◆ ファイルを閉じる
f.close()
