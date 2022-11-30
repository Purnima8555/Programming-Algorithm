# Pattern Design:
#Writing the letters of my name:

# for row in range(6):
#     for column in range(5):
#         if((column==0) or (column==1) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==2) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==3) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==4) and (row!=0 and row!=3 and row!=4 and row!=5 and row!=6)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if ((column==0) and (row!=5) or (column==1) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4) or (column==2) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4) or (column==3) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4) or (column==4) and (row!=5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if ((column==0) or (column==1) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==2) and (row!=1 and row!=2 and row!=5 and row!=6) or (column==3) and (row!=1 and row!=2 and row!=4 and row!=6) or (column==4) and (row!=0 and row!=3 and row!=4 and row!=5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(6):
#         if ((column==0) or (column==1) and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5) or (column==2) and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5) or (column==3) and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5) or (column==4) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=5) or (column==5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(7):
#     for column in range(6):
#         if ((column==0) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==1) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==2) or (column==3) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==4) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if ((column==0) or (column==1) and (row!=0 and row!=2 and row!=3 and row!=3 and row!=4 and row!=5) or (column==2) and (row!=0 and row!=1 and row!=3 and row!=3 and row!=4 and row!=5) or (column==3) and (row!=0 and row!=2 and row!=3 and row!=3 and row!=4 and row!=5) or (column==4)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if((column==0) and (row!=0) or (column==1) and (row==0 or row==3) or (column==2) and (row==0 or row==3) or (column==3) and (row==0 or row==3) or (column==4) and (row!=0)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if ((column==0) or (column==1) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==2) and (row!=1 and row!=2 and row!=5 and row!=6) or (column==3) and (row!=1 and row!=2 and row!=4 and row!=6) or (column==4) and (row!=0 and row!=3 and row!=4 and row!=5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if((column==0) and (row!=0) or (column==1) and (row==0 or row==3) or (column==2) and (row==0 or row==3) or (column==3) and (row==0 or row==3) or (column==4) and (row!=0)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(6):
#         if ((column==0) or (column==1) and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5) or (column==2) and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5) or (column==3) and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5) or (column==4) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=5) or (column==5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# for row in range(6):
#     for column in range(5):
#         if((column==0) and (row!=0) or (column==1) and (row==0 or row==3) or (column==2) and (row==0 or row==3) or (column==3) and (row==0 or row==3) or (column==4) and (row!=0)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


# Writing name in patterns in one ROW:
# for row in range(7):
#     for column in range(70):
#         if((column==0) or (column==1) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==2) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==3) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==4) and (row!=0 and row!=3 and row!=4 and row!=5 and row!=6) or (column==5) and (row!=6) or (column==6) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==7) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==8) and (row!=6) or (column==9) or (column==10) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==11) and (row!=1 and row!=2 and row!=5 and row!=6) or (column==12) and (row!=1 and row!=2 and row!=4 and row!=6) or (column==13) and (row!=0 and row!=3 and row!=4 and row!=5) or (column==14) or (column==15) and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==16) and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5 and row!=6) or (column==17) and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==18) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=5 and row!=6) or (column==19) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=6) or (column==20) or (column==21) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==22) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==23) or (column==24) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==25) and (row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or (column==26) or (column==27) and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==28) and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5 and row!=6) or (column==29) and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==30) and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5 and row!=6) or (column==31) and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==32) or (column==33) and (row!=0) or (column==34) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==35) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==36) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==37) and (row!=0) or (column==38) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==39) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==40) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==41) or (column==42) and (row!=1 and row!=2 and row!=5 and row!=6) or (column==43) and (row!=1 and row!=2 and row!=4 and row!=6) or (column==44) and (row!=1 and row!=2 and row!=4 and row!=5) or (column==45) and (row!=0 and row!=3 and row!=4 and row!=5 and row!=6) or (column==46) and (row!=0) or (column==47) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==48) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==49) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==50) and (row!=0) or (column==51) or (column==52) and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6) or (column==53) and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5 and row!=6) or (column==54) and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==55) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=5 and row!=6) or (column==56) and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=6) or (column==57) or (column==58) and (row!=0) or (column==59) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==60) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==61) and (row!=1 and row!=2 and row!=4 and row!=5 and row!=6) or (column==62) and (row!=0)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()
