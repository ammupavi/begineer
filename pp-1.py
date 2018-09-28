count = {}
for s in check_string:
  if count.has_key(s):
    count[s] += 1
  else:
    count[s] = 1
