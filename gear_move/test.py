# start = posx(574.07, 149.69, 340.0, 0.0,-180.0, 0.0)
# set_digital_output(2,ON)
# set_digital_output(1,OFF)

# mwait(1)

# # 초기 위치로 이동 및 gripper 설정

# #a = get_current_posx()[0]
# a = start

# force_ext = get_tool_force(DR_BASE)
# tp_popup("{}".format(force_ext))

# amovel(-100, 15, 15)

# while 1:
#     # if force_ext[2] <= 30:
#     #     # a[2] = a[2] - 1
#     #     # movel(a, 50, 50)
    
#     # else:
#     #     tp_popup("Ground Detected")   
#     #     a[2] = a[2] + 15
#     #     set_digital_output(2,OFF)
#     #     set_digital_output(1,ON)
#     #     mwait(1)
#     #     break

#     if force_ext[2] > 30 :
#         stop(DR_SSTOP)
#         a[2] += 15
#         movel(a, 50, 50)
#         set_digital_output(2,OFF)
#         set_digital_output(1,ON)
#         mwait(1)
#         break


# movel(start, 50, 50)

# s2 = posx(276.04, 149.69, 340.0, 0.0,-180.0, 0.0)
# movel(s2, 50, 50)

# a = get_current_posx()[0]

# while 1:
#     if force_ext[2] <= 30:
#         a[2] = a[2] - 1
#         movel(a, 50, 50)

#     else:
#         tp_popup("Ground Detected")   
#         a[2] = a[2] + 15
#         set_digital_output(2,ON)
#         set_digital_output(1,OFF)
#         mwait(1)
#         break
