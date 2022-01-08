#iada new_mypkg

# 開発環境:
Ubuntu20.04

Raspberry Pi 4
<span style="color: red; ">ラズパイ３だと動かないと思われるため注意。</span>

# 使用機器等
### OS系統
・Ubuntu20.04LTS(PC)

・Raspberry Pi 4([Ubuntu20.04マイクロSD内蔵](https://onl.tw/a45isMj)Copyright (c) 2021 Ryuich Ueda)

・LANケーブル

# 実行
## 実行方法(count.py)
ロスコアを立ち上げる
 ```
roscore &
 ```
 実行できるようにパーミッションを設定

 ```
chmod +x count.py
 ```
  ```
source ~/.bashrc
 ```
 実行
 ```
rosrun new_mypkg count.py
 ```
 ノードの確認（しなくてもよいが確認のために行う）
 ```
rosnode list
 ```
 トピックの確認(同じく確認のために行う)
 ```
rostopic list
 ```
 見る
 ```
rostopic echo /count_up
 ```

 -------------
## 実行方法(twice.py)
  ```
chmod +x twice.py
 ```
 ```
rosrun mypkg twice.py
 ```
## 実行（最終）
 ```
rosrun new_mypkg count.py
 ```
  ```
rostopic echo /twice
 ```

# ライセンス
Copyright (c) 2021 Ryuich Ueda
