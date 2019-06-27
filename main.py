import module_calc
import module_time
import module_str

value_type = input('enter type: ')
print(value_type)
allowed_types = ['num', 'str', 'date','exit']
exit = {'q', 'quit', 'e', 'exit'}
if value_type in allowed_types:
    print('ok')
else:
    print('not in allowed_types')

if value_type == "num":
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    module_calc.run_calc()
elif value_type == "str":
    print(module_str.str_func())
elif value_type == "date":
    print(module_time.time_now())
    print(module_time.cal_now())
else:
    value_type = "exit"
    print("goodbye")
