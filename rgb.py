def red(r,g,b): # red,green,blue
    threshold= max(r,g,b)
    return (
        threshold > 8 # for neglecting black
        and r == threshold # r should be greater then g and b   
        and g < threshold*0.5 # g will be less
        and b < threshold*0.5 # b will be less
    )
color_db = [[255,0,0], [254,100,100], [128, 45, 24], [255, 245, 221]]
for i in color_db:
    if(i== [255,0,0]):
        print(i,"is red")
    elif(red(i[0],i[1],i[2])== True):
        print(i,"is a shade of red")
