def arithmetic_arranger(problems, option = False):
  
  tam_problems = len(problems)
  if tam_problems > 5:
    return "Error: Too many problems."


  results = []
  operaciones = []

  for problema in problems:
    problema = problema.split()
    operaciones.append(problema)
    if not ((problema[1] == "+") or (problema[1] == "-")):
      return "Error: Operator must be '+' or '-'."
    else:
      try:
        if problema[1] == "+":
          results.append(str(int(problema[0]) + int(problema[2])))
        else:
          results.append(str(int(problema[0]) - int(problema[2])))
      except ValueError:
        return "Error: Numbers must only contain digits."
    if not (len(problema[0]) <= 4 and len(problema[2]) <= 4):
      return "Error: Numbers cannot be more than four digits."


  no_up = ''
  no_down = ''
  down_dash = ''
  data = ''
  
  for count, problema in enumerate(operaciones):
    aux = 0
    if count < tam_problems - 1:
      if len(problema[0]) > len(problema[2]):
        aux = len(no_up)
        no_up += '  ' + problema[0] + '    '
        no_down += problema[1] + (' '*(len(problema[0]) - len(problema[2]) + 1)) + problema[2] + '    '
        aux = len(no_up) - aux
      else:
        aux = len(no_up)
        no_up += ' ' + (' '*(len(problema[2]) - len(problema[0]) + 1)) + problema[0] + '    '
        no_down += problema[1] + ' ' + problema[2] + '    '
        aux = len(no_up) - aux
      if option:
        data += (' '*(aux - 4 - len(results[count]))) + results[count] + '    '
      down_dash += ('-'*(aux - 4)) + (' ' * 4)
    else:
      if len(problema[0]) > len(problema[2]):
        no_up += '  ' + problema[0]
        aux = len(no_down)
        no_down += problema[1] + (' '*(len(problema[0]) - len(problema[2]) + 1)) + problema[2]
        aux = len(no_down) - aux
      else:
        no_up += ' ' + (' '*(len(problema[2]) - len(problema[0]) + 1)) + problema[0]
        aux = len(no_down)
        no_down += problema[1] + ' ' + problema[2]
        aux = len(no_down) - aux
      if option:
        data += (' '*(aux - len(results[count]))) + results[count]
      down_dash += ('-'*(aux))
  
  if option:
    return no_up + '\n' + no_down + '\n' + down_dash + '\n' + data
  else:
    return no_up + '\n' + no_down + '\n' + down_dash