# new_mypkg


# 実行方法
ロスコアを立ち上げる
 ```
roscore
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
 見る
 ```
rostopic echo /count_up
 ```
