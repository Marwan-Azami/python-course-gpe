var_notes = [ 19, 20, 12, 15, 0, 9]

var_c20 = (20 in var_notes and # True
           19 in var_notes and  # True
           1 in var_notes or not # false
            11 in var_notes      # True
           )     # True
# True * True * False + True
print(var_c20)
                      # True                            or      # False
res1 = var_notes[0] >= 10 or (var_notes[len(var_notes)-1] >= 10 and var_notes[3] % 2 ==0 )
                        # True                               and    False
res2 = (var_notes[0] >= 10 or var_notes[len(var_notes)-1] >= 10) and var_notes[3] % 2 ==0

print(res1)
print(res2)
