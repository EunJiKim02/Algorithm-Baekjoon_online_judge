stack = []
while(True):
  #종료조건 넣기
  sentence = input()
  if(sentence == '.'):
    break
  for i in sentence:
      if(i == '.'):
        break
      elif(i == '[' or i=='('):
        stack.append(i)
      elif(len(stack) == 0 and (i == ']'or i ==')')):
        stack.append('e')
        break
      elif(i == ']'):
        if stack[len(stack)-1] != '[':
          break
        else:
          stack.pop()
      elif(i == ')'):
        if stack[len(stack)-1] != '(':
          break
        else:
          stack.pop()
        
  if(len(stack) == 0):
      print('yes')
  else:
      print('no')
  
  stack.clear()
