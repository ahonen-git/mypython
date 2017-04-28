#coding:utf-8


def rho(t,s,p):			# 水温、塩分、圧力から密度求める
	p=p*0.1						# dbarで入力した圧力をbarに変換する
	rhow=[999.842594,6.793952e-2,-9.095290e-3,1.001685e-4,-1.120083e-6,6.536332e-9]
	rhos=[0.824493,-4.0899e-3,7.6438e-5,-8.2467e-7,5.3875e-9,-5.72466e-3,1.0227e-4,-1.6546e-6,4.8314e-4]
	ww=[19652.21,148.4206,-2.327105,1.360477e-2,-5.155288e-5]
	ks=[54.6746,-0.603459,1.09987e-2,-6.1670e-5,7.944e-2,1.6483e-2,-5.3009e-4]
	kp=[3.239908,1.43713e-3,1.16092e-4,-5.77905e-7,2.2838e-3,-1.0981e-5,-1.6078e-6,1.91075e-4,8.50935e-5,-6.12293e-6,5.2787e-8,-9.9348e-7,2.0816e-8,9.1697e-10]
	pp0=[1.0,-1.0,-1.0,-1.0,4.1057e-9,-1.0]
	pp1=[3.6504e-4,8.3198e-5,-5.4065e-7,4.0274e-9]
	pp2=[1.7439e-5,-2.9778e-7]
	pp3=[8.9309e-7,-3.1628e-8,2.1987e-10]
	pp4=[-1.6056e-10,5.0484e-12]
	wrho=0.0
	for i in range(0,6):
		wrho=wrho*t+rhow[5-i]

	rhop= wrho + s * (rhos[0] + rhos[1] * t + rhos[2] * pow(t,2) + rhos[3] * pow(t,3) + rhos[4] * pow(t,4)) \
		  + pow(s,1.5) * (rhos[5] + rhos[6] * t + rhos[7]*pow(t,2)) \
		  + rhos[8] * pow(s,2)
	kw=0
	for i in range(0,5):
		kw=kw*t+ww[4-i]
	kst=kw + s*(ks[0]+ks[1]*t+ks[2]*pow(t,2)+ks[3]*pow(t,3)) \
		 + pow(s,1.5)*(ks[4]+ks[5]*t+ks[6]*pow(t,2))
	kstp = kst + p*(kp[0] + kp[1]*t + kp[2]*pow(t,2) + kp[3]*pow(t,3)) \
		   + p * s * (kp[4] + kp[5]*t + kp[6]*pow(t,2) ) \
		   + kp[7]* p * pow(s,1.5) \
		   + pow(p,2) * (kp[8] + kp[9]*t + kp[10]*pow(t,2)) \
		   + pow(p,2) * s * (kp[11] + kp[12]*t + kp[13]*pow(t,2))
	rho = rhop/(1. - p/kstp)
	return rho


def gamma(s,t,p):
	a=[ 3.5803e-05, 8.5258e-06,-6.8360e-08, 6.6228e-10]
	b=[ 1.8932e-06,-4.2393e-08]
	c=[ 1.8741e-08,-6.7795e-10, 8.7330e-12,-5.4481e-14]
	d=[-1.1351e-10, 2.7759e-12]
	e=[-4.6206e-13, 1.8676e-14,-2.1687e-16]
	gamma=a[0]+a[1]*t+a[2]*pow(t,2)+a[3]*pow(t,3)+(b[0]+b[1]*t)*(s-35.0) \
		   +(c[0]+c[1]*t+c[2]*pow(t,2)+c[3]*pow(t,3)+(d[0]+d[1]*t)*(s-35.0))*p \
		   +(e[0]+e[1]*t+e[2]*pow(t,2))*pow(p,2)
	return gamma
