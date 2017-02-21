#Math hasn't always been your best subject, and these programming
#symbols always trip you up! I mean, does ** mean Times, Times or To the
#power of? Luckily, you can create the function expression_out() to
#write out the expressions for you! These values will be stored in the
#preloaded dictionary OPERATORS just as shown above. But keep in mind:
#INVALID operators will be tested, to which you return "That's not an
#operator!" And all of the numbers will be <= 10! Isn't that nice!



d={
'+':'Plus ',
'-':   'Minus ',
'*':   'Times ',
'/':   'Divided By ',  
'**':  'To The Power Of ',
'=':   'Equals ',
'!=':  'Does Not Equal '
}
nu={
'1':'One',
'2':'Two',
'3':'Three',
'4':'Four',
'5':'Five',
'6':'Six',
'7':'Seven',
'8':'Eight',
'9':'Nine',
'10':'Ten'
}

def expression_out(exp):
    s=exp.split()
    if s[0] in nu and s[1] in d and s[2] in nu:
        return nu[s[0]] +" "+ d[s[1]] + nu[s[2]]
    return '''That's not an operator!'''
