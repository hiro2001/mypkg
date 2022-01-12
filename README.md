# timer mypkg

実行以降の経過時間表記をさせるリポジトリです。

実行方法は下で述べますが、分と秒を表示できます。

タイマーなどが狂った際に使えるかも？

# 開発環境:
Ubuntu20.04

Raspberry Pi 4

# 使用機器等
### OS系統
・Ubuntu20.04LTS(PC)

・Raspberry Pi 4([Ubuntu20.04マイクロSD内蔵](https://onl.tw/a45isMj)Copyright (c) 2021 Ryuich Ueda)

・LANケーブル

# 実行
## 実行方法(count.py)
scriptsに入っておく
 ```
 cd scripts
 ```

ロスコアを立ち上げる
 ```
roscore &
 ```
 ```
chmod +x count.py
 ```
  ```
source ~/.bashrc
 ```
 実行
 ```
rosrun mypkg count.py
 ```
 ノードの確認（しなくてもよいが確認のために行う）
 ```
rosnode list
 ```
 トピックの確認(同じく確認のために行う)
 ```
rostopic list
 ```
 経過秒数のみを見る
 ```
rostopic echo /second_up
 ```
## 実行方法(min.py)
  ```
chmod +x min.py
 ```
  ```
source ~/.bashrc
 ```
 二回目以降は下のコマンドだけで良い。
 ```
rosrun mypkg min.py
 ```

## 実行方法(time.py)
  ```
chmod +x time.py
 ```
  ```
source ~/.bashrc
 ```
 二回目以降は下のコマンドだけで良い。
 ```
rosrun mypkg time.py
 ```
## 実行（最終）
 秒表示
 ```
rostopic echo /timer1
 ```
 分表示
  ```
rostopic echo /timer2
 ```
# デモ動画


# ライセンス
Copyright (c) 2021 Ryuich Ueda

Copyright (c) 2021 Hiroyuki Matsuda

ライセンスについて[LISENCE](https://github.com/hiro2001/mypkg/blob/main/LICENSE)をよく読んでからお使いください。
