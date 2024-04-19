import numpy as np
from scipy import interpolate

wl_list=[475.,500.]
# clear water absorption and scattering
# 475         0.0117    0.0034
# 500         0.0215    0.0029
print("water")
kd_w_list=[0.0117,0.0215]
kd_w = interpolate.interp1d(wl_list, kd_w_list, fill_value="extrapolate")
print(kd_w(490.))

# Diatoms absorption
# 475    0.0238   0.0213   0.0035   0.0020
# 500    0.0191   0.0173   0.0036   0.0020
kd_dia_list=[0.0238,0.0191]
kd_dia = interpolate.interp1d(wl_list, kd_dia_list, fill_value="extrapolate")
print("dia")
print(kd_dia(490.))

# Flagellates
# 475    0.0508   0.0242   0.0068   0.0071
# 500    0.0358   0.0171   0.0076   0.0071
print("fla")
kd_fla_list=[0.0508,0.0358]
kd_fla = interpolate.interp1d(wl_list, kd_fla_list, fill_value="extrapolate")
print(kd_fla(490.))

# Pico
# 450    0.1038   0.0265   0.0050   0.0039
# 475    0.0824   0.0158   0.0051   0.0039
print("Pic")
kd_pic_list=[0.1038,0.0824]
kd_pic = interpolate.interp1d(wl_list, kd_pic_list, fill_value="extrapolate")
print(kd_pic(490.))


# Dino
# 475    0.0290   0.0269   0.0007   0.0030
# 500    0.0224   0.0208   0.0007   0.0030
kd_din_list=[0.0290,0.0224]
kd_din = interpolate.interp1d(wl_list, kd_din_list, fill_value="extrapolate")
print("Din")
print(kd_din(490.))

# cdom absorption 
# 475  9.762151e-03  1.007317e-02  9.645327e-03
# 500  6.302918e-03  6.718569e-03  6.150132e-03
print("cdom")
kd_cdom_list=[9.762151e-03,6.302918e-03]
kd_cdom = interpolate.interp1d(wl_list, kd_cdom_list, fill_value="extrapolate")
print(kd_cdom(490.))

chl=0.02
cdom=0.2
kd_min=kd_w(490.) + kd_dia(490.) *chl/4. + kd_fla(490.) * chl/4. + kd_pic(490.) *  chl/4. + kd_din(490.) * chl/4. + kd_cdom(490.) *cdom

kd_min=kd_w(490.) + kd_dia(490.) *0. + kd_fla(490.) * 0. + kd_pic(490.) *  chl + kd_din(490.) * 0. + kd_cdom(490.) *cdom

print(kd_min)
