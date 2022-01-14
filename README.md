# mypkg

実行以降の経過時間表記をさせるROSリポジトリです。

実行方法は下で述べますが、分と秒を表示できます。

タイマーなどが狂った際に使えるかも？

# 開発環境:
Ubuntu20.04

Raspberry Pi 4

ROSをインストールした後実行してください。インストールがまだの方は以下のURLから簡単にインストールすることができます。

[千葉工業大学上田先生のリポジトリ](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)

インストールする前には一度 
 ```
 sudo apt update
 ```
 ```
 sudo apt upgrade
 ```
 をすることをおすすめします。怠ると壊れたパッケージがあるというエラーメッセージが表示され、catkinが入らず、apt install もできなくなる可能性があります。

# 使用機器等
### OS系統
・Ubuntu20.04LTS(PC)

・Raspberry Pi 4([Ubuntu20.04マイクロSD内蔵](https://onl.tw/a45isMj)Copyright (c) 2021 Ryuich Ueda)

・LANケーブル

# 実行
catkin_makeをいちいちうつのが面倒だったので.bashの仕様等の練習のため作成した。以下のコマンドを実行するとcatkin_makeしてくれる。
 ```
 ./catkin
 ```
## launchを使って立ち上げる
 ```
 roslaunch mypkg data.launch
 ```
以下実行しているタイマーを見ることができる。
 ```
 ./timer1.bash
 ```
 ```
 ./timer2.bash
 ```


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

https://youtu.be/OMmtrcRYW1M

# ライセンス
Copyright (c) 2021 Ryuich Ueda

Copyright (c) 2021 Hiroyuki Matsuda

ライセンスについて[LISENCE](https://github.com/hiro2001/mypkg/blob/main/LICENSE)をよく読んでからお使いください。
