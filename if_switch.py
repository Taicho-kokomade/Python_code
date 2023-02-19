rank = "甲"
if rank == "甲":
  print("大変良いです")
elif rank == "乙":
  print("良いです")
elif rank == "丙":
  print("頑張りましょう")
else:
  print("???")

arank = "甲" #上記と同じ式
msg = {
  "甲": "大変良いです",
  "乙": "良いです",
  "丙": "頑張りましょう"
}
# キーの有無を確認
if arank in msg:
  print(msg[arank])
else:
  print("???")

