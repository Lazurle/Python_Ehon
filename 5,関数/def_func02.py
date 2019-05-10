def calc(calctype, a, b, c):
    if calctype == '和':
        x = a + b + c
        s = '{}+{}+{}={}'.format(a, b, c, x)
    elif calctype == '積':
        x = a * b * c
        s = '{}+{}+{}={}'.format(a, b, c, x)
    else:
        x = 'ナニコレ???'
        s = x
    return calctype + ':' + s
a = 1
b = 2
c = 3
result_01 = calc('和', a, b, c)
result_02 = calc('積', a, b, c)
result_03 = calc('２４歳、惑星です。', a, b, c)

print(result_01,'\n', result_02,'\n', result_03, sep='')

# 和:1+2+3=6
# 積:1+2+3=6
# ２４歳、惑星です。:ナニコレ???
