"""
Auto-generated from VB Button1 handlers. Do not edit by hand.
"""
import math
from .vbcommon import (vbval, vdiv, vbint, vbs, vbcstr, cv, cv2, cv3, cv4,
                      tank, tank2, tann, rt, vasin, vacos, vsqrt)
def gen_Kako_Cal_1(self):
    aL = vbval(self.txt('TextBox2'))
    bL = vbval(self.txt('TextBox3'))
    cL = vbval(self.txt('TextBox4'))
    AD = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = 'A=' + cv(vdiv(vasin(vdiv(aL, bL)) * 180, math.pi))
    self.a(TMP)
    TMP = 'C=' + cv(vdiv(vacos(vdiv(aL, bL)) * 180, math.pi))
    self.a(TMP)
    TMP = ('c=' + cv(vsqrt(((bL + aL) * (bL - aL)))))
    self.a(TMP)
    TMP = ('cx2=' + cv((vsqrt(((bL + aL) * (bL - aL))) * 2)))
    self.a(TMP)


def gen_Kako_Cal_1_ac(self):
    aL = vbval(self.txt('TextBox2'))
    cL = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    TMP = 'A=' + cv(vdiv(math.atan(vdiv(aL, cL)) * 180, math.pi))
    self.a(TMP)
    TMP = 'C=' + cv(90 - vdiv(math.atan(vdiv(aL, cL)) * 180, math.pi))
    self.a(TMP)
    TMP = ('b=' + cv(vsqrt(aL * aL + cL * cL)))
    self.a(TMP)


def gen_Kako_Cal_1_bc(self):
    bL = vbval(self.txt('TextBox3'))
    cL = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    aL = vsqrt(bL * bL - cL * cL)
    TMP = 'A=' + cv(vdiv(math.atan(vdiv(aL, cL)) * 180, math.pi))
    self.a(TMP)
    TMP = 'C=' + cv(90 - vdiv(math.atan(vdiv(aL, cL)) * 180, math.pi))
    self.a(TMP)
    TMP = ('a=' + cv(aL))
    self.a(TMP)
    TMP = ('ax2=' + cv(aL * 2))
    self.a(TMP)


def gen_Kako_Cal_1_Aa(self):
    aL = vbval(self.txt('TextBox2'))
    AD = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = ('C=' + cv(90 - AD))
    self.a(TMP)
    TMP = 'b=' + cv(vdiv(aL, math.sin(vdiv(AD, 180) * math.pi)))
    self.a(TMP)
    TMP = 'c=' + cv(vdiv(aL, math.tan(vdiv(AD, 180) * math.pi)))
    self.a(TMP)
    TMP = 'cx2=' + cv(vdiv(aL, math.tan(vdiv(AD, 180) * math.pi)) * 2)
    self.a(TMP)


def gen_Kako_Cal_1_Ab(self):
    bL = vbval(self.txt('TextBox3'))
    AD = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = ('C=' + cv(90 - AD))
    self.a(TMP)
    TMP = 'a=' + cv(bL * math.sin(vdiv(AD, 180) * math.pi))
    self.a(TMP)
    TMP = 'c=' + cv(bL * math.cos(vdiv(AD, 180) * math.pi))
    self.a(TMP)
    TMP = 'ax2=' + cv(bL * math.sin(vdiv(AD, 180) * math.pi) * 2)
    self.a(TMP)
    TMP = 'cx2=' + cv(bL * math.cos(vdiv(AD, 180) * math.pi) * 2)
    self.a(TMP)


def gen_Kako_Cal_1_Ac(self):
    cL = vbval(self.txt('TextBox4'))
    AD = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = ('C=' + cv(90 - AD))
    self.a(TMP)
    TMP = 'a=' + cv(cL * math.tan(vdiv(AD, 180) * math.pi))
    self.a(TMP)
    TMP = 'b=' + cv(vdiv(cL, math.cos(vdiv(AD, 180) * math.pi)))
    self.a(TMP)
    TMP = 'ax2=' + cv(cL * math.tan(vdiv(AD, 180) * math.pi) * 2)
    self.a(TMP)


def gen_Kako_Cal_2(self):
    R1 = vbval(self.txt('TextBox2'))
    D1 = vbval(self.txt('TextBox3'))
    RTV = rt(D1, R1)
    TMP = ''
    self.set_out('')
    TMP = ('A=' + cv(RTV.A))
    self.a(TMP)
    TMP = ('B=' + cv(RTV.B))
    self.a(TMP)
    TMP = ('C=' + cv(RTV.C))
    self.a(TMP)
    TMP = ('A+C=' + cv((RTV.A + RTV.C)))
    self.a(TMP)
    TMP = ('(A+C)x2=' + cv(((RTV.A + RTV.C) * 2)))
    self.a(TMP)
    TMP = ('Bx2=' + cv((RTV.B * 2)))
    self.a(TMP)


def gen_Kako_Cal_3(self):
    R1 = vbval(self.txt('TextBox2'))
    R2 = vbval(self.txt('TextBox3'))
    AL = vbval(self.txt('TextBox4'))
    Sa = (AL - R2)
    Sb = (R1 - R2)
    D1 = vdiv(vasin(vdiv(Sa, Sb)) * 180, math.pi)
    Ba = R1 * math.sin(vdiv(D1, 180) * math.pi)
    Bb = R1 - R1 * math.cos(vdiv(D1, 180) * math.pi)
    Ec = (R2 - (AL - Ba))
    Bc = vsqrt(((R2 * R2) - (Ec * Ec)))
    TMP = ''
    self.set_out('')
    TMP = ('a=' + cv(Ba))
    self.a(TMP)
    TMP = ('b=' + cv(Bb))
    self.a(TMP)
    TMP = ('c=' + cv(Bc))
    self.a(TMP)
    TMP = ('ax2=' + cv((Ba * 2)))
    self.a(TMP)
    TMP = ('b+c=' + cv((Bb + Bc)))
    self.a(TMP)
    TMP = ('(b+c)x2=' + cv(((Bb + Bc) * 2)))
    self.a(TMP)


def gen_Kako_Cal_4(self):
    R1 = vbval(self.txt('TextBox2'))
    R2 = vbval(self.txt('TextBox3'))
    AL = vbval(self.txt('TextBox4'))
    Sa = (AL + R2)
    Sb = (R1 + R2)
    D1 = vdiv(vasin(vdiv(Sa, Sb)) * 180, math.pi)
    Bc = R1 * math.cos(vdiv(D1, 180) * math.pi)
    Bb = Sb * math.cos(vdiv(D1, 180) * math.pi) - Bc
    Ba = R1 * math.sin(vdiv(D1, 180) * math.pi)
    TMP = ''
    self.set_out('')
    TMP = ('a=' + cv(Ba))
    self.a(TMP)
    TMP = ('b=' + cv(Bb))
    self.a(TMP)
    TMP = ('c=' + cv(Bc))
    self.a(TMP)
    TMP = ('ax2=' + cv((Ba * 2)))
    self.a(TMP)
    TMP = ('R1+c=' + cv((R1 + Bc)))
    self.a(TMP)
    TMP = ('R1+c+b=' + cv(((R1 + Bc) + Bb)))
    self.a(TMP)


def gen_Kako_Cal_5(self):
    KakouChou = vbval(self.txt('TextBox2'))
    if (KakouChou == 0):
        self.msgbox('加工長が入力されていません。')
        return
    ZairyouTanka = vbval(self.txt('TextBox3'))
    KakouSuu = vbval(self.txt('TextBox4'))
    KakouJikan = vbval(self.txt('TextBox5'))
    ZairyouChou = vbval(self.txt('ComboBox1'))
    if (ZairyouChou == 0):
        self.msgbox('材料長が入力されていません。')
        return
    if (self.cbindex('ComboBox3') == (-1)):
        self.msgbox('材種が選択されていません。')
        return
    Hijyuu = 0
    if (self.cbindex('ComboBox3') == 0):
        Hijyuu = 0.793
    elif (self.cbindex('ComboBox3') == 1):
        Hijyuu = 0.273
    elif (self.cbindex('ComboBox3') == 2):
        Hijyuu = 0.85
    elif (self.cbindex('ComboBox3') == 3):
        Hijyuu = 0.89
    elif (self.cbindex('ComboBox3') == 4):
        Hijyuu = 0.785
    ZairyouKei = vbval(self.txt('ComboBox2'))
    if (ZairyouKei == 0):
        self.msgbox('材料径が入力されていません。')
        return
    Kosuu_Hon = vbint(vdiv(ZairyouChou - 300, KakouChou))
    SeihinChou_Zanzai = vdiv(ZairyouChou, Kosuu_Hon)
    Tanjyuu = vdiv(vdiv(ZairyouKei, 10) * ZairyouKei, 10) * SeihinChou_Zanzai * Hijyuu * 0.7854
    Tanka = 0
    if (ZairyouTanka != 0): Tanka = vdiv(ZairyouTanka, 1000) * Tanjyuu
    SouJyuuryou = 0
    if (KakouSuu != 0): SouJyuuryou = (Tanjyuu * KakouSuu)
    SouKakaku = 0
    if ((KakouSuu != 0) and (Tanka != 0)): SouKakaku = (Tanka * KakouSuu)
    ZaiHonJyu = 0
    if (SouJyuuryou != 0): ZaiHonJyu = vdiv(SouJyuuryou, vdiv(vdiv(ZairyouKei, 10) * ZairyouKei, 10) * ZairyouChou * Hijyuu * 0.7854)
    HonDay = 0
    if ((KakouJikan != 0) and (Kosuu_Hon != 0)): HonDay = vdiv(vdiv(3600, KakouJikan) * 24, Kosuu_Hon)
    NisSsuu = 0
    if ((ZaiHonJyu != 0) and (HonDay != 0)): NisSsuu = vdiv(ZaiHonJyu, HonDay)
    TMP = ''
    self.set_out('')
    TMP = (('個数／本 = ' + str(Kosuu_Hon).replace(' ', '')) + '個')
    self.a(TMP)
    TMP = (('残材込み加工長 = ' + cv2(SeihinChou_Zanzai)) + 'mm')
    self.a(TMP)
    TMP = (('単重 = ' + cv2(Tanjyuu)) + 'ｇ')
    self.a(TMP)
    TMP = (('単価 = ' + cv2(Tanka)) + '円')
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = (('必要重量 = ' + cv3(SouJyuuryou)) + 'g')
    self.a(TMP)
    TMP = (('必要本数 = ' + cv3(ZaiHonJyu)) + '本')
    self.a(TMP)
    TMP = (('必要経費 = ' + cv3(SouKakaku)) + '円')
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = (('使用本数／日 = ' + cv4(HonDay)) + '本')
    self.a(TMP)
    TMP = (('必要日数 = ' + cv4(NisSsuu)) + '日')
    self.a(TMP)


def gen_Kako_Cal_6(self):
    MMin = vbval(self.txt('TextBox2'))
    if (MMin == 0):
        self.msgbox('周速が入力されていません。')
        return
    Kei = vbval(self.txt('TextBox3'))
    if (Kei == 0):
        self.msgbox('径寸法が入力されていません。')
        return
    TMP = ''
    self.set_out('')
    TMP = '回転数（Ｓ） = ' + cv(vdiv(MMin * 1000, Kei * math.pi))
    self.a(TMP)


def gen_Kako_Cal_7(self):
    Yama = vbval(self.txt('TextBox2'))
    Tani = vbval(self.txt('TextBox3'))
    Yoyu = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    TMP = ('基準位置から刃先まで = ' + cv(tank((Yama + Yoyu), Tani, 30)))
    self.a(TMP)


def gen_Kako_Cal_8(self):
    R1 = vbval(self.txt('TextBox2'))
    Z1 = vbval(self.txt('TextBox3'))
    Zai = vbval(self.txt('TextBox4'))
    aL = (R1 - Z1)
    bL = R1
    TMP = ''
    self.set_out('')
    TMP = ('A=' + cv((R1 - vsqrt(((bL + aL) * (bL - aL))))))
    self.a(TMP)
    TMP = ('接触する径=' + cv(((Zai + (R1 * 2)) - ((R1 - vsqrt(((bL + aL) * (bL - aL)))) * 2))))
    self.a(TMP)


def gen_Kako_Cal_9(self):
    R1 = vbval(self.txt('TextBox2'))
    X1 = vbval(self.txt('TextBox3'))
    bL = R1
    cL = vdiv(X1, 2)
    aL = vsqrt(((bL * bL) - (cL * cL)))
    TMP = ''
    self.set_out('')
    TMP = ('A=' + cv((aL * 2)))
    self.a(TMP)


def gen_Kako_Cross_1(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Z2 = vbval(self.txt('TextBox9'))
    Shift = vbval(self.txt('TextBox10'))
    Yoyu = vbval(self.txt('TextBox11'))
    if (Mill == 0): Mill = 1
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    Times = Z2
    TA = 0
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Y' + cv(Zai + 1) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2)) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    Times = Z2
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2))
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    TMP = 'G0 X0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_10(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = (vbval(self.txt('TextBox6')) * 2)
    Z1 = vbval(self.txt('TextBox7'))
    Shift = vbval(self.txt('TextBox8'))
    Torishiro = (vbval(self.txt('TextBox9')) * 2)
    Safe = (vbval(self.txt('TextBox10')) * 2)
    if (Torishiro == 0): Torishiro = 1
    Ichi = (Zai + 1)
    L = X1
    StepCount = vbint(vdiv(X1, Torishiro))
    Amari = (L - (StepCount * Torishiro))
    Ex = (Ichi + 1)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T800'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = ((((('G0 X0' + ' Y') + cv((Zai + 1))) + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T8')
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    for I in range(1, StepCount + 1):
        if ((Ex - Safe) < Ichi):
            TMP = (('G1 Y' + cv((Ex + Safe))) + ' F0.2')
            self.a(TMP)
        TMP = (('G1 Y' + cv((Zai - (I * Torishiro)))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G0 Y' + cv(Ichi))
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        Ex = (Zai - (I * Torishiro))
    if (Amari != 0):
        TMP = (('G1 Y' + cv(((Zai - (StepCount * Torishiro)) + Safe))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 Y' + cv((Zai - L))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G0 Y' + cv(Ichi))
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_11(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    C1 = vbval(self.txt('TextBox6'))
    Ana = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Shift = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T700'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = ((((('G0 X' + cv((Zai + 1))) + ' Y0') + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T7')
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = (('G1 X' + cv((Zai + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((Zai - (Ana + (C1 * 2))))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_12(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = (vbval(self.txt('TextBox6')) * 2)
    Z1 = vbval(self.txt('TextBox7'))
    Shift = vbval(self.txt('TextBox8'))
    Torishiro = (vbval(self.txt('TextBox9')) * 2)
    Safe = (vbval(self.txt('TextBox10')) * 2)
    if (Torishiro == 0): Torishiro = 1
    Ichi = (Zai + 1)
    L = X1
    StepCount = vbint(vdiv(X1, Torishiro))
    Amari = (L - (StepCount * Torishiro))
    Ex = (Ichi + 1)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T800'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = ((((('G0 X' + cv((Zai + 1))) + ' Y0') + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T8')
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    for I in range(1, StepCount + 1):
        if ((Ex - Safe) < Ichi):
            TMP = (('G1 X' + cv((Ex + Safe))) + ' F0.2')
            self.a(TMP)
        TMP = (('G1 X' + cv((Zai - (I * Torishiro)))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G0 X' + cv(Ichi))
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        Ex = (Zai - (I * Torishiro))
    if (Amari != 0):
        TMP = (('G1 X' + cv(((Zai - (StepCount * Torishiro)) + Safe))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 X' + cv((Zai - L))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G0 X' + cv(Ichi))
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_13(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = (vbval(self.txt('TextBox6')) * 2)
    Z1 = vbval(self.txt('TextBox7'))
    Shift = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T900'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = ((((('G0 X0' + ' Y') + cv((Zai + 1))) + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T9')
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = '(M38)'
    self.a(TMP)
    TMP = '(G4 U0.2)'
    self.a(TMP)
    TMP = (((((((('G384 V' + cv(((X1 + 1) * (-1)))) + F) + ' (G784 V') + cv(((X1 + 1) * (-1)))) + F) + ' M36 S') + S) + ')')
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_14(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = (vbval(self.txt('TextBox6')) * 2)
    Z1 = vbval(self.txt('TextBox7'))
    Shift = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T900'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ((((('G0 X' + cv((Zai + 1))) + ' Y0') + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T9')
    self.a(TMP)
    TMP = 'M8'
    self.a(TMP)
    TMP = 'G0 C0'
    self.a(TMP)
    TMP = 'M7'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (((('G784 U' + cv(((X1 + 1) * (-1)))) + F) + ' M36 S') + S)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = 'M9'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_15(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = (vbval(self.txt('TextBox6')) * 2)
    Z1 = vbval(self.txt('TextBox7'))
    Shift = vbval(self.txt('TextBox8'))
    Torishiro = (vbval(self.txt('TextBox9')) * 2)
    if (Torishiro == 0): Torishiro = 1
    Ichi = (Zai + 1)
    L = X1
    StepCount = vbint(vdiv(X1, Torishiro))
    Amari = (L - (StepCount * Torishiro))
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T800'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ((((('G0 X0' + ' Y') + cv((Zai + 1))) + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T8')
    self.a(TMP)
    TMP = 'M8'
    self.a(TMP)
    TMP = 'G0 C0'
    self.a(TMP)
    TMP = 'M7'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    for I in range(1, StepCount + 1):
        TMP = (('G88 Y' + cv((Zai - (I * Torishiro)))) + F)
        self.a(TMP)
    if (Amari != 0):
        TMP = (('G88 Y' + cv((Zai - L))) + F)
        self.a(TMP)
    TMP = 'G80'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = 'M9'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_16(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = (vbval(self.txt('TextBox6')) * 2)
    Z1 = vbval(self.txt('TextBox7'))
    Shift = vbval(self.txt('TextBox8'))
    Torishiro = (vbval(self.txt('TextBox9')) * 2)
    if (Torishiro == 0): Torishiro = 1
    Ichi = (Zai + 1)
    L = X1
    StepCount = vbint(vdiv(X1, Torishiro))
    Amari = (L - (StepCount * Torishiro))
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T800'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ((((('G0 X' + cv((Zai + 1))) + ' Y0') + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T8')
    self.a(TMP)
    TMP = 'M8'
    self.a(TMP)
    TMP = 'G0 C0'
    self.a(TMP)
    TMP = 'M7'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    for I in range(1, StepCount + 1):
        TMP = (('G88 X' + cv((Zai - (I * Torishiro)))) + F)
        self.a(TMP)
    if (Amari != 0):
        TMP = (('G88 X' + cv((Zai - L))) + F)
        self.a(TMP)
    TMP = 'G80'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = 'M9'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_2(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Shift = vbval(self.txt('TextBox9'))
    Yoyu = vbval(self.txt('TextBox10'))
    if (Mill == 0): Mill = 1
    Z2 = 0
    if (Z1 >= (Mill - Yoyu)):
        Z2 = (Z1 + Yoyu)
        Z1 = (Yoyu * (-1))
    else:
        Z2 = Mill
        Z1 = (Z1 - Mill)
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    Times = Z2
    TA = 0
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Y' + cv(Zai + 1) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2)) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    Times = Z2
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2))
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 Y' + cv(X1))
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 Y' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    TMP = 'G0 X0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_3(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Shift = vbval(self.txt('TextBox9'))
    if (Mill == 0): Mill = 1
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X0' + ' Y' + cv(Zai + 1) + ' Z' + cv(Shift - vdiv(Mill, 2) - 1) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z' + cv(Shift - vdiv(Mill, 2) - 0.2) + ' F0.2'
    self.a(TMP)
    TMP = 'G1 Z' + cv(Z1 + Shift + Tanmen - vdiv(Mill, 2)) + F
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 X' + cv((Ichi + 1))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 X0' + ' Z' + cv(Shift - vdiv(Mill, 2) - 1)
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z' + cv(Shift - vdiv(Mill, 2) - 0.2) + ' F0.2'
    self.a(TMP)
    TMP = 'G1 Z' + cv(Z1 + Shift + Tanmen - vdiv(Mill, 2)) + F
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 X' + cv((Ichi + 1))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'G0 X0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_4(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Z2 = vbval(self.txt('TextBox9'))
    Shift = vbval(self.txt('TextBox10'))
    if (Mill == 0): Mill = 1
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Y' + cv(Zai + 1) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2)) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    if (Z2 > Mill):
        TMP = ('G1 X0' + F)
        self.a(TMP)
        TMP = 'G1 Z' + cv(Z1 + Z2 + Shift + Tanmen - vdiv(Mill, 2)) + F
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 X' + cv((Ichi + 1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
        self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2))
    self.a(TMP)
    TMP = ('G0 Y' + cv(X1))
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    if (Z2 > Mill):
        TMP = ('G1 X0' + F)
        self.a(TMP)
        TMP = 'G1 Z' + cv(Z1 + Z2 + Shift + Tanmen - vdiv(Mill, 2)) + F
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 X' + cv((Ichi + 1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(((Ichi * (-1)) - 1))) + F)
        self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'G0 X0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_5(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Z2 = vbval(self.txt('TextBox9'))
    Shift = vbval(self.txt('TextBox10'))
    Yoyu = vbval(self.txt('TextBox11'))
    if (Mill == 0): Mill = 1
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    Times = Z2
    TA = 0
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1) + ' Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2)) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    Times = Z2
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2))
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    TMP = 'G0 Y0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_6(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Shift = vbval(self.txt('TextBox9'))
    Yoyu = vbval(self.txt('TextBox10'))
    if (Mill == 0): Mill = 1
    Z2 = 0
    if (Z1 >= (Mill - Yoyu)):
        Z2 = (Z1 + Yoyu)
        Z1 = (Yoyu * (-1))
    else:
        Z2 = Mill
        Z1 = (Z1 - Mill)
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    Times = Z2
    TA = 0
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1) + ' Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2)) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    Times = Z2
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2))
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    Times -= Mill
    TA = 0
    while True:
        if (Times <= 0): break
        if (((Times - Mill) >= 0) and ((Mill - Yoyu) > 0)):
            TA = ((TA + Mill) - Yoyu)
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = (Times - (Mill - Yoyu))
        else:
            TA += Times
            TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2) + TA)
            self.a(TMP)
            TMP = ('G0 X' + cv(X1))
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
            self.a(TMP)
            TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
            self.a(TMP)
            TMP = ('G0 X' + cv((Zai + 1)))
            self.a(TMP)
            Times = 0
    TMP = 'G0 Y0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_7(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Shift = vbval(self.txt('TextBox9'))
    if (Mill == 0): Mill = 1
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1) + ' Y0' + ' Z' + cv(Shift - vdiv(Mill, 2) - 1) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z' + cv(Shift - vdiv(Mill, 2) - 0.2) + ' F0.2'
    self.a(TMP)
    TMP = 'G1 Z' + cv(Z1 + Shift + Tanmen - vdiv(Mill, 2)) + F
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 Y' + cv((Ichi + 1))) + F)
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 Y0' + ' Z' + cv(Shift - vdiv(Mill, 2) - 1)
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z' + cv(Shift - vdiv(Mill, 2) - 0.2) + ' F0.2'
    self.a(TMP)
    TMP = 'G1 Z' + cv(Z1 + Shift + Tanmen - vdiv(Mill, 2)) + F
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 Y' + cv((Ichi + 1))) + F)
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'G0 X0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_8(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Mill = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    X1 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Z2 = vbval(self.txt('TextBox9'))
    Shift = vbval(self.txt('TextBox10'))
    if (Mill == 0): Mill = 1
    bL = vdiv(Zai, 2)
    cL = vdiv(X1, 2)
    Ichi = (vsqrt(((bL * bL) - (cL * cL))) * 2)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = (((('T600(MILL D=' + cv(Mill)) + ' DanmenHaba=') + cv(Ichi)) + ')')
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = 'G0 X' + cv(Zai + 1) + ' Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2)) + ' T6'
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    if (Z2 > Mill):
        TMP = ('G1 Y0' + F)
        self.a(TMP)
        TMP = 'G1 Z' + cv(Z1 + Z2 + Shift + Tanmen - vdiv(Mill, 2)) + F
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 Y' + cv((Ichi + 1))) + F)
        self.a(TMP)
        TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
        self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = '(M6)'
    self.a(TMP)
    TMP = 'M57(G0 C180.0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = 'G0 Y' + cv(Zai + 1 + Mill) + ' Z' + cv(Z1 + Shift + Tanmen + vdiv(Mill, 2))
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi + 1) + Mill))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
    self.a(TMP)
    if (Z2 > Mill):
        TMP = ('G1 Y0' + F)
        self.a(TMP)
        TMP = 'G1 Z' + cv(Z1 + Z2 + Shift + Tanmen - vdiv(Mill, 2)) + F
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 Y' + cv((Ichi + 1))) + F)
        self.a(TMP)
        TMP = (('G1 Y' + cv(((Ichi * (-1)) - 1))) + F)
        self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'G0 Y0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cross_9(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Zai = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    C1 = vbval(self.txt('TextBox6'))
    Ana = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Shift = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = 'M5'
    self.a(TMP)
    TMP = 'T700'
    self.a(TMP)
    TMP = 'G101'
    self.a(TMP)
    TMP = ('M36 S' + S)
    self.a(TMP)
    TMP = ((((('G0 X0' + ' Y') + cv((Zai + 1))) + ' Z') + cv(((Z1 + Shift) + Tanmen))) + ' T7')
    self.a(TMP)
    TMP = '(M8)'
    self.a(TMP)
    TMP = 'M50(G0 C0)'
    self.a(TMP)
    TMP = '(M7)'
    self.a(TMP)
    TMP = (('G1 Y' + cv((Zai + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 Y' + cv((Zai - (Ana + (C1 * 2))))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = ('G0 Y' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)
    TMP = 'M38'
    self.a(TMP)
    TMP = '(M9)'
    self.a(TMP)
    TMP = 'M59'
    self.a(TMP)


def gen_Kako_Cut_1(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Shift = vbval(self.txt('TextBox5'))
    Zai = vbval(self.txt('TextBox6'))
    L = vbval(self.txt('TextBox7'))
    Tanmen = vbval(self.txt('TextBox8'))
    Ana = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((Zai + 1))) + ' Z') + cv((((KHaba + Shift) + L) + Tanmen))) + ' T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((Zai + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((Ana - 0.4))) + F)
    self.a(TMP)
    TMP = 'G1 X-1.7 F0.02'
    self.a(TMP)


def gen_Kako_Drill_1(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Ichi = vbval(self.txt('TextBox4'))
    Clear = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T1100'
    self.a(TMP)
    TMP = (('G0 Z' + cv(Ichi)) + ' T11')
    self.a(TMP)
    TMP = 'G1 Z' + cv(vdiv(X1, 2) + Tanmen + Clear) + F
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Drill_2(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Ichi = vbval(self.txt('TextBox4'))
    Clear = vbval(self.txt('TextBox5'))
    Safe = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    KakoCho = vbval(self.txt('TextBox8'))
    Torishiro = vbval(self.txt('TextBox9'))
    if (Torishiro == 0): Torishiro = 1
    L = ((KakoCho + Clear) + Tanmen)
    StepCount = vbint(vdiv(L, Torishiro))
    Amari = (L - (StepCount * Torishiro))
    Ex = (Ichi + Clear)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T1200'
    self.a(TMP)
    TMP = (('G0 Z' + cv(Ichi)) + ' T12')
    self.a(TMP)
    for I in range(1, StepCount + 1):
        if ((Ex - Safe) > Ichi):
            TMP = (('G1 Z' + cv((Ex - Safe))) + ' F0.2')
            self.a(TMP)
        TMP = (('G1 Z' + cv(((I * Torishiro) + Ichi))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G0 Z' + cv(Ichi))
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        Ex = ((I * Torishiro) + Ichi)
    if (Amari != 0):
        TMP = (('G1 Z' + cv((((StepCount * Torishiro) - Safe) + Ichi))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 Z' + cv((L + Ichi))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G0 Z' + cv(Ichi))
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Drill_3(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Ichi = vbval(self.txt('TextBox4'))
    Clear = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    KakoCho = vbval(self.txt('TextBox7'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T1200'
    self.a(TMP)
    TMP = (('G0 Z' + cv(Ichi)) + ' T12')
    self.a(TMP)
    TMP = (('G1 Z' + cv((((Ichi + Tanmen) + Clear) + KakoCho))) + F)
    self.a(TMP)
    TMP = '(G4 U0.2)'
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Drill_4(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Ichi = vbval(self.txt('TextBox4'))
    Clear = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    KakoCho = vbval(self.txt('TextBox7'))
    TapW = ((Tanmen + Clear) + KakoCho)
    TMP = ''
    self.set_out('')
    TMP = 'G25'
    self.a(TMP)
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T1300'
    self.a(TMP)
    TMP = (('G0 Z' + cv(Ichi)) + ' T13')
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = '(TAP - CASE 1)'
    self.a(TMP)
    TMP = (('G184 W' + cv(TapW)) + F)
    self.a(TMP)
    TMP = 'G4 U0.5'
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = '(RIDGID TAP - CASE 2)'
    self.a(TMP)
    TMP = 'G99 M5'
    self.a(TMP)
    TMP = ('M29 S' + S)
    self.a(TMP)
    TMP = (('G84 W' + cv(TapW)) + F)
    self.a(TMP)
    TMP = 'G80'
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = '(TAP - CASE 3)'
    self.a(TMP)
    TMP = ((('G1 W' + cv(TapW)) + F) + ' M87')
    self.a(TMP)
    TMP = 'G4 U0.5'
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = '(TAP - CASE 4)'
    self.a(TMP)
    TMP = (('G32 W' + cv(TapW)) + F)
    self.a(TMP)
    TMP = ((('G32 W' + cv(((TapW + 2) * (-1)))) + F) + ' M4')
    self.a(TMP)
    TMP = 'G4 U0.5'
    self.a(TMP)
    TMP = ''
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Drill_5(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    Ichi = vbval(self.txt('TextBox4'))
    Clear = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    Kakocho = vbval(self.txt('TextBox7'))
    Torishiro = vbval(self.txt('TextBox8'))
    if (Torishiro == 0): Torishiro = 1
    L = ((Kakocho + Clear) + Tanmen)
    StepCount = vbint(vdiv(L, Torishiro))
    Amari = (L - (StepCount * Torishiro))
    TMP = ''
    self.set_out('')
    TMP = 'T1300'
    self.a(TMP)
    TMP = (('G0 Z' + cv(Ichi)) + ' T13')
    self.a(TMP)
    TMP = 'G25'
    self.a(TMP)
    TMP = 'G99 M5'
    self.a(TMP)
    TMP = ('M29 S' + S)
    self.a(TMP)
    for I in range(1, StepCount + 1):
        TMP = (('G84 Z' + cv(((I * Torishiro) + Ichi))) + F)
        self.a(TMP)
    if (Amari != 0):
        TMP = (('G84 Z' + cv((L + Ichi))) + F)
        self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_1(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv(((X1 - (C1 * 2)) - 0.4)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv(C1)) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(Z1)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (C2 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' Z') + cv(((Z1 + C2) + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_10(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(Tanmen)) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G1 X-0.3' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 - (tann(((Z1 + 0.2) + Tanmen), D1) * 2))))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R1)).B * 2)))) + ' Z') + cv(((Z1 - (rt(D1, R1)).C) + Tanmen))) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv(X1)) + ' Z') + cv(((Z1 + (rt(D1, R1)).A) + Tanmen))) + ' R') + cv(R1)) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ')')
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_11(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(Tanmen)) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G1 X-0.3' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)) - 0.8)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ('G1 Z0.05' + F)
    self.a(TMP)
    TMP = ((((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + ' Z') + cv(Tanmen)) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' Z') + cv(((rt((90 - D1), R1)).B + Tanmen))) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_12(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    Tanmen = vbval(self.txt('TextBox11'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(Tanmen)) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G1 X-0.3' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)) - 0.8)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ('G1 Z0.05' + F)
    self.a(TMP)
    TMP = ((((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + ' Z') + cv(Tanmen)) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' Z') + cv(((rt((90 - D1), R1)).B + Tanmen))) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R2)).B * 2)))) + ' Z') + cv(((Z1 - (rt(D1, R2)).C) + Tanmen))) + F) + ' (B=') + cv((rt(D1, R2)).B)) + ' C=') + cv((rt(D1, R2)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv(X1)) + ' Z') + cv(((Z1 + (rt(D1, R2)).A) + Tanmen))) + ' R') + cv(R2)) + F) + ' (A=') + cv((rt(D1, R2)).A)) + ')')
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_13(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    Tanmen = vbval(self.txt('TextBox9'))
    AnaKei = vbval(self.txt('TextBox10'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((AnaKei - 0.4)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(Tanmen)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (tann(Z1, D1) * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_14(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    AnaKei = vbval(self.txt('TextBox11'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((AnaKei - 0.4)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(Tanmen)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (tann(Z1, D1) * 2)))) + F)
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R1)).B * 2)))) + ' Z') + cv(((Z1 - (rt(D1, R1)).C) + Tanmen))) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv(X1)) + ' Z') + cv(((Z1 + (rt(D1, R1)).A) + Tanmen))) + ' R') + cv(R1)) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ')')
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_15(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    AnaKei = vbval(self.txt('TextBox11'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((AnaKei - 0.4)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(Tanmen)) + F)
    self.a(TMP)
    TMP = ((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' Z') + cv(((rt((90 - D1), R1)).B + Tanmen))) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_16(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    Tanmen = vbval(self.txt('TextBox11'))
    AnaKei = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((AnaKei - 0.4)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(Tanmen)) + F)
    self.a(TMP)
    TMP = ((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' Z') + cv(((rt((90 - D1), R1)).B + Tanmen))) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R2)).B * 2)))) + ' Z') + cv(((Z1 - (rt(D1, R2)).C) + Tanmen))) + F) + ' (B=') + cv((rt(D1, R2)).B)) + ' C=') + cv((rt(D1, R2)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv(X1)) + ' Z') + cv(((Z1 + (rt(D1, R2)).A) + Tanmen))) + ' R') + cv(R2)) + F) + ' (A=') + cv((rt(D1, R2)).A)) + ')')
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_17(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    D1 = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (tann(Z1, D1) * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' W') + cv(Z1)) + F)
    self.a(TMP)


def gen_Kako_Maebiki_18(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    D1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = ((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' W') + cv((rt((90 - D1), R1)).B)) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((('G1 X' + cv(X1)) + ' W') + cv((Z1 - (rt((90 - D1), R1)).B))) + F) + '(B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_19(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    D1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    R2 = vbval(self.txt('TextBox7'))
    TMP = ''
    self.set_out('')
    TMP = ((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' W') + cv((rt((90 - D1), R1)).B)) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv((X1 - ((rt(D1, R2)).B * 2)))) + ' W') + cv(((Z1 - (rt(D1, R2)).C) - (rt((90 - D1), R1)).B))) + F) + ' (B=') + cv((rt(D1, R2)).B)) + ' C=') + cv((rt(D1, R2)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(X1)) + ' W') + cv(((rt(D1, R2)).A + (rt(D1, R2)).C))) + ' R') + cv(R2)) + F) + ' (A=') + cv((rt(D1, R2)).A)) + ' C=') + cv((rt(D1, R2)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_2(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    Tanmen = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(Tanmen)) + ' T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G1 X-0.3' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((((X1 - (C1 * 2)) - 0.4) - (Tanmen * 2))))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((C1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (C2 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' Z') + cv((((Z1 + C2) + 0.2) + Tanmen))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_20(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    D1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (tann(Z1, D1) * 2)))) + F)
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R1)).B * 2)))) + ' W') + cv((Z1 - (rt(D1, R1)).C))) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(X1)) + ' W') + cv(((rt(D1, R1)).A + (rt(D1, R1)).C))) + ' R') + cv(R1)) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_21(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    D1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = ((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' W') + cv((rt((90 - D1), R1)).B)) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((('G1 X' + cv((X1 + 0.4))) + ' W') + cv(((Z1 - (rt((90 - D1), R1)).B) + tank2(0.4, D1)))) + F) + '(B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_22(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    D1 = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (tann(Z1, D1) * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + 0.4))) + ' W') + cv((Z1 + tank2(0.4, D1)))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_23(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    C1 = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' W') + cv(C1)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((Z1 - C1))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_24(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    R1 = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X1)) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((Z1 - R1))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_25(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    C1 = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + 0.4))) + ' W') + cv((C1 + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 - 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_26(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    C1 = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' W') + cv(C1)) + F)
    self.a(TMP)
    TMP = ('G1 U0.05 W0.2' + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_27(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    R1 = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X1)) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 U0.05 W0.2' + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_28(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    C1 = vbval(self.txt('TextBox5'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' W') + cv(C1)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((Z1 - C1))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_29(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    R1 = vbval(self.txt('TextBox4'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X1)) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)


def gen_Kako_Maebiki_3(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    Tanmen = vbval(self.txt('TextBox9'))
    AnaKei = vbval(self.txt('TextBox10'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((AnaKei - 0.4)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(Tanmen)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((C1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (C2 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' Z') + cv((((Z1 + C2) + 0.2) + Tanmen))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_30(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    C1 = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 Z' + cv(((Z1 - C1) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + (C1 * 2)))) + ' W') + cv(C1)) + F)
    self.a(TMP)


def gen_Kako_Maebiki_31(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    R1 = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 Z' + cv(((Z1 - R1) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G1 X' + cv((X1 + (R1 * 2)))) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)


def gen_Kako_Maebiki_32(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    X2 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 Z' + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X2)) + ' W') + cv(tank(X2, X1, D1))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_33(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    X2 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    R1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 Z' + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X2 - ((rt(D1, R1)).B * 2)))) + ' W') + cv((tank(X2, X1, D1) - (rt(D1, R1)).C))) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(X2)) + ' W') + cv(((rt(D1, R1)).A + (rt(D1, R1)).C))) + ' R') + cv(R1)) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_34(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    X2 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    R1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ((((('G1 Z' + cv(((Z1 + Tanmen) - (rt(D1, R1)).A))) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((((('G3 X' + cv((X1 + ((rt(D1, R1)).B * 2)))) + ' W') + cv(((rt(D1, R1)).A + (rt(D1, R1)).C))) + ' R') + cv(R1)) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' A=') + cv((rt(D1, R1)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((('G1 X' + cv(X2)) + ' W') + cv((tank(X2, X1, D1) - (rt(D1, R1)).C))) + F) + ' (C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_35(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    X2 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    R1 = vbval(self.txt('TextBox8'))
    R2 = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = ((((('G1 Z' + cv(((Z1 + Tanmen) - (rt(D1, R1)).A))) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((((('G3 X' + cv((X1 + ((rt(D1, R1)).B * 2)))) + ' W') + cv(((rt(D1, R1)).A + (rt(D1, R1)).C))) + ' R') + cv(R1)) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' A=') + cv((rt(D1, R1)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv((X2 - ((rt(D1, R2)).B * 2)))) + ' W') + cv(((tank(X2, X1, D1) - (rt(D1, R1)).C) - (rt(D1, R2)).C))) + F) + ' (B=') + cv((rt(D1, R2)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ' C=') + cv((rt(D1, R2)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(X2)) + ' W') + cv(((rt(D1, R2)).A + (rt(D1, R2)).C))) + ' R') + cv(R2)) + F) + ' (A=') + cv((rt(D1, R2)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_36(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    X2 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    R1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ((((('G1 Z' + cv(((Z1 + Tanmen) - (rt(D1, R1)).A))) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((((('G3 X' + cv((X1 + ((rt(D1, R1)).B * 2)))) + ' W') + cv(((rt(D1, R1)).A + (rt(D1, R1)).C))) + ' R') + cv(R1)) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' A=') + cv((rt(D1, R1)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((('G1 X' + cv((X2 + 0.4))) + ' W') + cv((tank((X2 + 0.4), X1, D1) - (rt(D1, R1)).C))) + F) + ' (C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_37(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    X2 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 Z' + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' W') + cv(tank((X2 + 0.4), X1, D1))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_38(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    C1 = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv(((X1 - (C1 * 2)) - 0.4))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 - 0.2) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + 0.4))) + ' W') + cv((C1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1.0)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_39(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    R1 = vbval(self.txt('TextBox5'))
    Tanmen = vbval(self.txt('TextBox6'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv(((X1 - (R1 * 2)) - 0.8))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 - 0.05) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X1)) + ' Z') + cv(((Z1 + R1) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 U0.05 W0.2' + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1.0)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_4(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    R1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv(((X1 - (R1 * 2)) - 0.8)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ('G1 Z-0.05' + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X1 - (R1 * 2)))) + ' Z0') + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X1)) + ' Z') + cv(C1)) + ' R') + cv(C1)) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(Z1)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' Z') + cv(((Z1 + C1) + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_40(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    Z2 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    Tanmen = vbval(self.txt('TextBox7'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (tann((Z2 + 0.2), D1) * 2)))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 - 0.2) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + 0.4))) + ' W') + cv(((Z2 + 0.2) + tank((X1 + 0.4), X1, D1)))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1.0)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_41(self):
    F = (' F' + cv(vbval(self.txt('TextBox2'))))
    X1 = vbval(self.txt('TextBox3'))
    Z1 = vbval(self.txt('TextBox4'))
    Z2 = vbval(self.txt('TextBox5'))
    D1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    Tanmen = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv((X1 - (tann((Z2 + 0.2), D1) * 2)))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 - 0.2) + Tanmen))) + F)
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R1)).B * 2)))) + ' W') + cv(((Z2 - (rt(D1, R1)).C) + 0.2))) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(X1)) + ' W') + cv(((rt(D1, R1)).A + (rt(D1, R1)).C))) + ' R') + cv(R1)) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)


def gen_Kako_Maebiki_42(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    Tanmen = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(((R1 + 0.2) + Tanmen))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((R1 * 2) + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((R1 * 2))) + ' Z') + cv((R1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + R1) + Tanmen))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_43(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    Tanmen = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((R1 + Tanmen))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((R1 * 2))) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + R1) + Tanmen))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_44(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    R2 = vbval(self.txt('TextBox7'))
    Tanmen = vbval(self.txt('TextBox8'))
    H1 = ((0.5 * vsqrt(2)) * R1)
    H2 = ((0.5 * vsqrt(2)) * R2)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((R1 + 0.2) + Tanmen) - H1) + H2))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((((H1 + R2) - H2) * 2) + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((((H1 + R2) - H2) * 2))) + ' Z') + cv((((R1 + Tanmen) - H1) + H2))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((H1 * 2))) + ' Z') + cv(((R1 + Tanmen) - H1))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((((H1 + R2) - H2) * 2)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(((((Z1 + R1) + Tanmen) - H1) + H2))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_45(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    R2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    Tanmen = vbval(self.txt('TextBox9'))
    H1 = ((0.5 * vsqrt(2)) * R1)
    H2 = ((0.5 * vsqrt(2)) * R2)
    H3 = (R2 - ((rt((90 - D1), R2)).A + (rt((90 - D1), R2)).C))
    H4 = (R2 - (rt((90 - D1), R2)).B)
    H5 = (Z1 - (rt((90 - D1), R2)).B)
    H6 = tann(H5, D1)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((((R1 + Tanmen) - H1) + H2) - H4) + H5))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((((((H1 + R2) - H2) - H3) + H6) * 2))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(((((H1 + R2) - H2) - H3) * 2))) + ' Z') + cv(((((R1 + Tanmen) - H1) + H2) - H4))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((H1 * 2))) + ' Z') + cv(((R1 + Tanmen) - H1))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_46(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    Z1 = vbval(self.txt('TextBox5'))
    R1 = vbval(self.txt('TextBox6'))
    R2 = vbval(self.txt('TextBox7'))
    R3 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    H1 = ((0.5 * vsqrt(2)) * R1)
    H2 = ((0.5 * vsqrt(2)) * R2)
    H3 = (R2 - ((rt((90 - D1), R2)).A + (rt((90 - D1), R2)).C))
    H4 = (R2 - (rt((90 - D1), R2)).B)
    H5 = (Z1 - (rt((90 - D1), R2)).B)
    H6 = tann(H5, D1)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((((((R1 + Tanmen) - H1) + H2) - H4) + H5) + (rt(D1, R3)).A) + 0.2))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((((((H1 + R2) - H2) - H3) + H6) * 2) + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((((((H1 + R2) - H2) - H3) + H6) * 2))) + ' Z') + cv(((((((R1 + Tanmen) - H1) + H2) - H4) + H5) + (rt(D1, R3)).A))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(((((((H1 + R2) - H2) - H3) + H6) - (rt(D1, R3)).B) * 2))) + ' Z') + cv(((((((R1 + Tanmen) - H1) + H2) - H4) + H5) - (rt(D1, R3)).C))) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(((((H1 + R2) - H2) - H3) * 2))) + ' Z') + cv(((((R1 + Tanmen) - H1) + H2) - H4))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((H1 * 2))) + ' Z') + cv(((R1 + Tanmen) - H1))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_47(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    Tanmen = vbval(self.txt('TextBox9'))
    D1 = vasin(vdiv(vdiv(X1, 2) - R2, R1 - R2))
    H1 = (R1 * math.cos(D1))
    H2 = ((R1 - R2) * math.cos(D1))
    H3 = (R1 * math.sin(D1))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((R1 + 0.2) + Tanmen) - H2))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv(((R1 + Tanmen) - H2))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((H3 * 2))) + ' Z') + cv(((R1 + Tanmen) - H1))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv(X1))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv((((Z1 + R1) + Tanmen) - H2))) + F)
    self.a(TMP)


def gen_Kako_Maebiki_48(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    D2 = vasin(vdiv(vdiv(X1, 2) - tann(Z1, D1) + R2 - rt(90 - D1, R2).A - R2, R1 - R2))
    H1 = (R1 * math.cos(D2))
    H2 = ((R1 - R2) * math.cos(D2))
    H3 = (R1 * math.sin(D2))
    H4 = (R2 - (rt((90 - D1), R2)).B)
    H5 = (Z1 - (rt((90 - D1), R2)).B)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(((((R1 + Tanmen) - H2) - H4) + H5))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(X1)) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R2)).C * 2)))) + ' Z') + cv((((R1 + Tanmen) - H2) - H4))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((H3 * 2))) + ' Z') + cv(((R1 + Tanmen) - H1))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_49(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    Tanmen = vbval(self.txt('TextBox10'))
    D2 = vasin(vdiv(vdiv(X1, 2) - R2, R1 - R2))
    H1 = (R1 * math.cos(D2))
    H2 = ((R1 - R2) * math.cos(D2))
    H3 = (R1 * math.sin(D2))
    H4 = (R2 - ((rt((90 - D1), R2)).A + (rt((90 - D1), R2)).C))
    H5 = (R2 - (rt((90 - D1), R2)).B)
    H6 = (Z1 - (rt((90 - D1), R2)).B)
    H7 = tann(H6, D1)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(((((R1 + Tanmen) - H2) - H5) + H6))) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv(((X1 - (H4 * 2)) + (H7 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (H4 * 2)))) + ' Z') + cv((((R1 + Tanmen) - H2) - H5))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((H3 * 2))) + ' Z') + cv(((R1 + Tanmen) - H1))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G3 X0 Z' + cv(Tanmen)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ('G1 X-0.2' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Maebiki_5(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 - (tann((Z1 + 0.2), D1) * 2))))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv(Z1)) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv((Z1 + Z2))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_6(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 - (tann((Z1 + 0.2), D1) * 2))))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R1)).B * 2)))) + ' Z') + cv((Z1 - (rt(D1, R1)).C))) + F) + ' (B=') + cv((rt(D1, R1)).B)) + ' C=') + cv((rt(D1, R1)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv(X1)) + ' Z') + cv((Z1 + (rt(D1, R1)).A))) + ' R') + cv(R1)) + F) + ' (A=') + cv((rt(D1, R1)).A)) + ')')
    self.a(TMP)
    TMP = (('G1 Z' + cv((Z1 + Z2))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_7(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)) - 0.8)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ('G1 Z-0.05' + F)
    self.a(TMP)
    TMP = (((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + ' Z0') + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' Z') + cv((rt((90 - D1), R1)).B)) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv(Z1)) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv((Z1 + Z2))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_8(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (('G0 X' + cv((X2 + 1))) + ' Z-1.0 T1')
    self.a(TMP)
    TMP = ('G0 X' + cv((((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)) - 0.8)))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = ('G1 Z-0.05' + F)
    self.a(TMP)
    TMP = (((((('G1 X' + cv(((X1 - (tann(Z1, D1) * 2)) - ((rt((90 - D1), R1)).A * 2)))) + ' Z0') + F) + ' (A=') + cv((rt((90 - D1), R1)).A)) + ')')
    self.a(TMP)
    TMP = ((((((((((('G2 X' + cv(((X1 - (tann(Z1, D1) * 2)) + ((rt((90 - D1), R1)).C * 2)))) + ' Z') + cv((rt((90 - D1), R1)).B)) + ' R') + cv(R1)) + F) + '(C=') + cv((rt((90 - D1), R1)).C)) + ' B=') + cv((rt((90 - D1), R1)).B)) + ')')
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X1 - ((rt(D1, R2)).B * 2)))) + ' Z') + cv((Z1 - (rt(D1, R2)).C))) + F) + ' (B=') + cv((rt(D1, R2)).B)) + ' C=') + cv((rt(D1, R2)).C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv(X1)) + ' Z') + cv((Z1 + (rt(D1, R2)).A))) + ' R') + cv(R2)) + F) + ' (A=') + cv((rt(D1, R2)).A)) + ')')
    self.a(TMP)
    TMP = (('G1 Z' + cv((Z1 + Z2))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Maebiki_9(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    Z2 = vbval(self.txt('TextBox7'))
    D1 = vbval(self.txt('TextBox8'))
    Tanmen = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = 'T100'
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv(Tanmen)) + 'T1')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G1 X-0.3' + F)
    self.a(TMP)
    TMP = 'G0 Z-1.0'
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 - (tann(((Z1 + 0.2) + Tanmen), D1) * 2))))
    self.a(TMP)
    TMP = 'G1 Z-0.2 F0.2'
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv(((Z1 + Z2) + Tanmen))) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)


def gen_Kako_Mizo_1(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - C1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W' + cv((MHaba - KHaba))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (C2 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' W') + cv((C2 + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_10(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + C2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W-' + cv(((MHaba - KHaba) - 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = (('G0 W-' + cv(((C1 + 0.2) + 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' W') + cv((C1 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G1 W0.1' + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((X1 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = (('G0 W-' + cv((C1 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' W') + cv((C1 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)


def gen_Kako_Mizo_11(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + R2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X2)) + ' Z') + cv(((Z1 + R2) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W-' + cv((MHaba - KHaba))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(X1)) + ' W-') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X1 + 0.05))) + ' W-0.2') + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_12(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + R2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X2)) + ' Z') + cv(((Z1 + R2) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W-' + cv(((MHaba - KHaba) - 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = (('G0 W-' + cv(((R1 + 0.2) + 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.05))) + F)
        self.a(TMP)
        TMP = ((('G1 X' + cv(X1)) + ' W0.2') + F)
        self.a(TMP)
        TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G1 W0.1' + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((X1 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = (('G0 W-' + cv((R1 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.05))) + F)
        self.a(TMP)
        TMP = ((('G1 X' + cv(X1)) + ' W0.2') + F)
        self.a(TMP)
        TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 X' + cv((X1 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X1 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)


def gen_Kako_Mizo_13(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + C2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R2 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' Z') + cv(((Z1 + Tanmen) - R2))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 W-' + cv((((MHaba - KHaba) - R1) - R2))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((MKei + (R1 * 2)))) + ' W-') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + 0.4))) + ' W-') + cv((C1 + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_14(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + C2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R2 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' Z') + cv(((Z1 + Tanmen) - R2))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 W-' + cv((((MHaba - KHaba) - R1) - R2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = (('G0 W-' + cv(((C1 + 0.2) + R1))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' W') + cv((C1 + 0.2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_15(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    R3 = vbval(self.txt('TextBox9'))
    R4 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + R2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X2)) + ' Z') + cv(((Z1 + R2) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R4 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' Z') + cv(((Z1 + Tanmen) - R4))) + ' R') + cv(R4)) + F)
    self.a(TMP)
    TMP = (('G1 W-' + cv((((MHaba - KHaba) - R3) - R4))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((MKei + (R3 * 2)))) + ' W-') + cv(R3)) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(X1)) + ' W-') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X1 + 0.05))) + ' W-0.2') + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_16(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    R3 = vbval(self.txt('TextBox9'))
    R4 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + R2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X2)) + ' Z') + cv(((Z1 + R2) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R4 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' Z') + cv(((Z1 + Tanmen) - R4))) + ' R') + cv(R4)) + F)
    self.a(TMP)
    TMP = (('G1 W-' + cv((((MHaba - KHaba) - R3) - R4))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = (('G0 W-' + cv(((R1 + 0.2) + R3))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv(X1)) + ' W0.2') + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' W') + cv(R1)) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R3 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' W') + cv(R3)) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_17(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    R3 = vbval(self.txt('TextBox9'))
    R4 = vbval(self.txt('TextBox10'))
    D1 = vbval(self.txt('TextBox11'))
    D2 = vbval(self.txt('TextBox12'))
    MKei = vbval(self.txt('TextBox13'))
    MHaba = vbval(self.txt('TextBox14'))
    KHaba = vbval(self.txt('TextBox15'))
    Tanmen = vbval(self.txt('TextBox16'))
    GetRT = None
    TmpVal = 0
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    GetRT = rt(D1, R1)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((((Z1 - tank(X1, MKei, D1)) + KHaba) - GetRT.A) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((((((((('G1 X' + cv(X1)) + ' W0.2') + F) + ' (A=') + cv(GetRT.A)) + ' B=') + cv(GetRT.B)) + ' C=') + cv(GetRT.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (GetRT.B * 2)))) + ' Z') + cv(((((Z1 - tank(X1, MKei, D1)) + GetRT.C) + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    GetRT = rt(D1, R2)
    if (D1 < 90):
        TMP = ((((((((((('G1 X' + cv((MKei + (GetRT.B * 2)))) + ' Z') + cv((((Z1 - GetRT.C) + KHaba) + Tanmen))) + F) + ' (A=') + cv(GetRT.A)) + ' B=') + cv(GetRT.B)) + ' C=') + cv(GetRT.C)) + ')')
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((MKei + (GetRT.B * 2)))) + F)
        self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' Z') + cv((((Z1 + GetRT.A) + KHaba) + Tanmen))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TmpVal = GetRT.A
    GetRT = rt(D2, R3)
    TMP = ((((((((('G1 W' + cv((((MHaba - KHaba) - GetRT.A) - TmpVal))) + F) + ' (A=') + cv(GetRT.A)) + ' B=') + cv(GetRT.B)) + ' C=') + cv(GetRT.C)) + ')')
    self.a(TMP)
    TMP = (((((('G3 X' + cv((MKei + (GetRT.B * 2)))) + ' W') + cv((GetRT.A + GetRT.C))) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TmpVal = GetRT.C
    GetRT = rt(D2, R4)
    if (D2 < 90):
        TMP = ((((((((((('G1 X' + cv((X2 - (GetRT.B * 2)))) + ' W') + cv(((tank(X2, MKei, D2) - TmpVal) - GetRT.C))) + F) + ' (A=') + cv(GetRT.A)) + ' B=') + cv(GetRT.B)) + ' C=') + cv(GetRT.C)) + ')')
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((X2 - (GetRT.B * 2)))) + F)
        self.a(TMP)
    TMP = (((((('G2 X' + cv(X2)) + ' W') + cv((GetRT.A + GetRT.C))) + ' R') + cv(R4)) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X2 + 0.05))) + ' W0.2') + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_18(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    R3 = vbval(self.txt('TextBox9'))
    R4 = vbval(self.txt('TextBox10'))
    D1 = vbval(self.txt('TextBox11'))
    D2 = vbval(self.txt('TextBox12'))
    MKei = vbval(self.txt('TextBox13'))
    MHaba = vbval(self.txt('TextBox14'))
    KHaba = vbval(self.txt('TextBox15'))
    Tanmen = vbval(self.txt('TextBox16'))
    GetRT1 = rt(D1, R1)
    GetRT2 = rt(D1, R2)
    GetRT3 = rt(D2, R3)
    GetRT4 = rt(D2, R4)
    TW1 = tank(X1, MKei, D1)
    TW2 = tank(X2, MKei, D2)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((((Z1 + MHaba) + TW2) + GetRT4.A) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.05))) + F)
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv(X2)) + ' Z') + cv(((((Z1 + MHaba) + TW2) + GetRT4.A) + Tanmen))) + F) + ' (A=') + cv(GetRT4.A)) + ' B=') + cv(GetRT4.B)) + ' C=') + cv(GetRT4.C)) + ')')
    self.a(TMP)
    TMP = (((((('G3 X' + cv((X2 - (GetRT4.B * 2)))) + ' Z') + cv(((((Z1 + MHaba) + TW2) - GetRT4.C) + Tanmen))) + ' R') + cv(R4)) + F)
    self.a(TMP)
    if (D2 < 90):
        TMP = ((((((((((('G1 X' + cv((MKei + (GetRT3.B * 2)))) + ' Z') + cv((((Z1 + MHaba) + GetRT3.C) + Tanmen))) + F) + ' (A=') + cv(GetRT3.A)) + ' B=') + cv(GetRT3.B)) + ' C=') + cv(GetRT3.C)) + ')')
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((MKei + (GetRT3.B * 2)))) + F)
        self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' Z') + cv((((Z1 - GetRT3.A) + MHaba) + Tanmen))) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TMP = ((((((((('G1 W-' + cv((((MHaba - KHaba) - GetRT2.A) - GetRT3.A))) + F) + ' (A=') + cv(GetRT2.A)) + ' B=') + cv(GetRT2.B)) + ' C=') + cv(GetRT2.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv((MKei + (GetRT2.B * 2)))) + ' W-') + cv((GetRT2.A + GetRT2.C))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    if (D1 < 90):
        TMP = ((((((((((('G1 X' + cv((X1 - (GetRT1.B * 2)))) + ' W-') + cv(((TW1 - GetRT2.C) - GetRT1.C))) + F) + ' (A=') + cv(GetRT1.A)) + ' B=') + cv(GetRT1.B)) + ' C=') + cv(GetRT1.C)) + ')')
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((X1 - (GetRT1.B * 2)))) + F)
        self.a(TMP)
    TMP = (((((('G3 X' + cv(X1)) + ' W-') + cv((GetRT1.A + GetRT1.C))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X1 + 0.05))) + ' W-0.2') + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_2(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - C1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W' + cv(((MHaba - KHaba) - 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = (('G0 W' + cv(((C2 + 0.2) + 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' W-') + cv((C2 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G1 W-0.1' + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((X2 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = (('G0 W' + cv((C2 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' W-') + cv((C2 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)


def gen_Kako_Mizo_3(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - R1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((((Z1 + KHaba) - R1) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W' + cv((MHaba - KHaba))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (R2 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X2)) + ' W') + cv(R2)) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X2 + 0.05))) + ' W0.2') + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_4(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - R1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((((Z1 + KHaba) - R1) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W' + cv(((MHaba - KHaba) - 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = (('G0 W' + cv(((R2 + 0.2) + 0.1))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.05))) + F)
        self.a(TMP)
        TMP = ((('G1 X' + cv(X2)) + ' W-0.2') + F)
        self.a(TMP)
        TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' W-') + cv(R2)) + ' R') + cv(R2)) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = ('G1 W-0.1' + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)
    else:
        TMP = (('G1 X' + cv((X2 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = (('G0 W' + cv((R2 + 0.2))) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.05))) + F)
        self.a(TMP)
        TMP = ((('G1 X' + cv(X2)) + ' W-0.2') + F)
        self.a(TMP)
        TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' W-') + cv(R2)) + ' R') + cv(R2)) + F)
        self.a(TMP)
        TMP = (('G1 X' + cv(MKei)) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
        TMP = (('G1 X' + cv((X2 + 0.4))) + F)
        self.a(TMP)
        TMP = ('G0 X' + cv((X2 + 1)))
        self.a(TMP)
        TMP = 'T0'
        self.a(TMP)


def gen_Kako_Mizo_5(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - C1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + R1))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((((MHaba - KHaba) - R1) - R2))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((MKei + (R2 * 2)))) + ' W') + cv(R2)) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (C2 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 + 0.4))) + ' W') + cv((C2 + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_6(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - C1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R1 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + R1))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((((MHaba - KHaba) - R1) - R2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = (('G0 W' + cv(((C2 + 0.2) + R2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' W-') + cv((C2 + 0.2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R2 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' W-') + cv(R2)) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_7(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    R3 = vbval(self.txt('TextBox9'))
    R4 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - R1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((((Z1 + KHaba) - R1) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R3 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + R3))) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((((MHaba - KHaba) - R3) - R4))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((MKei + (R4 * 2)))) + ' W') + cv(R4)) + ' R') + cv(R4)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 - (R2 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(X2)) + ' W') + cv(R2)) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv((X2 + 0.05))) + ' W0.2') + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_8(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    R1 = vbval(self.txt('TextBox7'))
    R2 = vbval(self.txt('TextBox8'))
    R3 = vbval(self.txt('TextBox9'))
    R4 = vbval(self.txt('TextBox10'))
    MKei = vbval(self.txt('TextBox11'))
    MHaba = vbval(self.txt('TextBox12'))
    KHaba = vbval(self.txt('TextBox13'))
    Tanmen = vbval(self.txt('TextBox14'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + KHaba) - R1) - 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((((Z1 + KHaba) - R1) + Tanmen))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R3 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv(MKei)) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + R3))) + ' R') + cv(R3)) + F)
    self.a(TMP)
    TMP = (('G1 W' + cv((((MHaba - KHaba) - R3) - R4))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = (('G0 W' + cv(((R2 + 0.2) + R4))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.05))) + F)
    self.a(TMP)
    TMP = ((('G1 X' + cv(X2)) + ' W-0.2') + F)
    self.a(TMP)
    TMP = (((((('G3 X' + cv((X2 - (R2 * 2)))) + ' W-') + cv(R2)) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((MKei + (R4 * 2)))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv(MKei)) + ' W-') + cv(R4)) + ' R') + cv(R4)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = ('G0 X' + cv((X2 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Mizo_9(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    X1 = vbval(self.txt('TextBox4'))
    X2 = vbval(self.txt('TextBox5'))
    Z1 = vbval(self.txt('TextBox6'))
    C1 = vbval(self.txt('TextBox7'))
    C2 = vbval(self.txt('TextBox8'))
    MKei = vbval(self.txt('TextBox9'))
    MHaba = vbval(self.txt('TextBox10'))
    KHaba = vbval(self.txt('TextBox11'))
    Tanmen = vbval(self.txt('TextBox12'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T200' + '(MIZO T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X2 + 1))) + ' Z') + cv((((Z1 + C2) + 0.2) + Tanmen))) + ' T2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X2 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X2 - (C2 * 2)))) + ' Z') + cv((Z1 + Tanmen))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(MKei)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    if (MHaba > KHaba):
        TMP = (('G1 W-' + cv((MHaba - KHaba))) + F)
        self.a(TMP)
        TMP = 'G4 U0.2'
        self.a(TMP)
    TMP = (('G1 X' + cv((X1 - (C1 * 2)))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 + 0.4))) + ' W-') + cv((C1 + 0.2))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_1(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    X2 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Z2 = vbval(self.txt('TextBox9'))
    C1 = vbval(self.txt('TextBox10'))
    C2 = vbval(self.txt('TextBox11'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + Tanmen) + KHaba) - C1) - 0.2))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (C1 * 2)))) + ' Z') + cv(((Z1 + Tanmen) + KHaba))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(X2)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(((((Z1 + Z2) + Tanmen) + KHaba) - C2))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(((X2 - (C2 * 2)) - 0.4))) + ' Z') + cv(((((Z1 + Z2) + Tanmen) + KHaba) + 0.2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_10(self):
    Zai = vbval(self.txt('TextBox2'))
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    Z1 = vbval(self.txt('TextBox7'))
    Z2 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    R1 = vbval(self.txt('TextBox10'))
    Kg = tann(Z2, D1)
    GetRT1 = rt((90 - D1), R1)
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv(X1)) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv((((Z1 + KHaba) + Tanmen) - Z2))) + F)
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv(((X1 - (Kg * 2)) + (GetRT1.C * 2)))) + ' Z') + cv((((Z1 + KHaba) + Tanmen) - GetRT1.B))) + F) + ' (A=') + cv(GetRT1.A)) + ' B=') + cv(GetRT1.B)) + ' C=') + cv(GetRT1.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv(((X1 - (Kg * 2)) - (GetRT1.A * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((((X1 - (Kg * 2)) - (GetRT1.A * 2)) - 0.8))) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + 0.05))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((Zai + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_11(self):
    Zai = vbval(self.txt('TextBox2'))
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    Z1 = vbval(self.txt('TextBox7'))
    Z2 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    R1 = vbval(self.txt('TextBox10'))
    R2 = vbval(self.txt('TextBox11'))
    Kg = tann(Z2, D1)
    GetRT1 = rt((90 - D1), R1)
    GetRT2 = rt(D1, R2)
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv(X1)) + F)
    self.a(TMP)
    TMP = ((((((((('G1 Z' + cv(((((Z1 + KHaba) + Tanmen) - Z2) - GetRT2.A))) + F) + ' (A=') + cv(GetRT2.A)) + ' B=') + cv(GetRT2.B)) + ' C=') + cv(GetRT2.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (GetRT2.B * 2)))) + ' G1 Z') + cv(((((Z1 + KHaba) + Tanmen) - Z2) + GetRT2.C))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv(((X1 - (Kg * 2)) + (GetRT1.C * 2)))) + ' Z') + cv((((Z1 + KHaba) + Tanmen) - GetRT1.B))) + F) + ' (A=') + cv(GetRT1.A)) + ' B=') + cv(GetRT1.B)) + ' C=') + cv(GetRT1.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv(((X1 - (Kg * 2)) - (GetRT1.A * 2)))) + ' Z') + cv(((Z1 + KHaba) + Tanmen))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((((X1 - (Kg * 2)) - (GetRT1.A * 2)) - 0.8))) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + 0.05))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((Zai + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_2(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    X2 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    Z2 = vbval(self.txt('TextBox9'))
    R1 = vbval(self.txt('TextBox10'))
    R2 = vbval(self.txt('TextBox11'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + Tanmen) + KHaba) - R1) - 0.2))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - R1))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv(((Z1 + Tanmen) + KHaba))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv(X2)) + F)
    self.a(TMP)
    TMP = 'G4 U0.2'
    self.a(TMP)
    TMP = (('G1 Z' + cv(((((Z1 + Z2) + Tanmen) + KHaba) - R2))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X2 - (R2 * 2)))) + ' Z') + cv((((Z1 + Z2) + Tanmen) + KHaba))) + ' R') + cv(R2)) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(((X2 - (R2 * 2)) - 0.8))) + ' Z') + cv(((((Z1 + Z2) + Tanmen) + KHaba) + 0.05))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_3(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    X2 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    Lg = tank((X1 + 0.4), X2, D1)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - Lg))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv(X2)) + ' Z') + cv(((Z1 + Tanmen) + KHaba))) + F)
    self.a(TMP)


def gen_Kako_Ura_4(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    X2 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    D1 = vbval(self.txt('TextBox10'))
    Lg = tank((X1 + 0.4), X2, D1)
    GetRT1 = rt(D1, R1)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - Lg))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X2 + (GetRT1.B * 2)))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - GetRT1.C))) + F) + ' B=') + cv(GetRT1.B)) + ' C=') + cv(GetRT1.C)) + ')')
    self.a(TMP)
    TMP = (((((((('G3 X' + cv(X2)) + ' Z') + cv((((Z1 + Tanmen) + KHaba) + GetRT1.A))) + ' R') + cv(R1)) + F) + ' A=') + cv(GetRT1.A))
    self.a(TMP)


def gen_Kako_Ura_5(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    X2 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    D1 = vbval(self.txt('TextBox10'))
    Lg = tank((X1 + 0.4), X2, D1)
    GetRT1 = rt((90 - D1), R1)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - Lg))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = ((((((((('G1 X' + cv((X2 + (GetRT1.C * 2)))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - GetRT1.B))) + F) + ' (B=') + cv(GetRT1.B)) + ' C=') + cv(GetRT1.C)) + ')')
    self.a(TMP)
    TMP = ((((((((('G2 X' + cv((X2 - (GetRT1.A * 2)))) + ' Z') + cv(((Z1 + Tanmen) + KHaba))) + ' R') + cv(R1)) + F) + ' (A=') + cv(GetRT1.A)) + ')')
    self.a(TMP)


def gen_Kako_Ura_6(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    X2 = vbval(self.txt('TextBox7'))
    Z1 = vbval(self.txt('TextBox8'))
    R1 = vbval(self.txt('TextBox9'))
    R2 = vbval(self.txt('TextBox10'))
    D1 = vbval(self.txt('TextBox11'))
    Lg = tank(X1, X2, D1)
    GetRT1 = rt(D1, R1)
    GetRT2 = rt((90 - D1), R2)
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv((((((Z1 + Tanmen) + KHaba) - Lg) - GetRT1.A) - 0.2))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv(X1)) + ' Z') + cv(((((Z1 + Tanmen) + KHaba) - Lg) - GetRT1.A))) + F) + ' (A=') + cv(GetRT1.A)) + ' B=') + cv(GetRT1.B)) + ' C=') + cv(GetRT1.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (GetRT1.B * 2)))) + ' Z') + cv(((((Z1 + Tanmen) + KHaba) - Lg) + GetRT1.C))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = ((((((((((('G1 X' + cv((X2 + (GetRT2.C * 2)))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - GetRT2.B))) + F) + ' (A=') + cv(GetRT2.A)) + ' B=') + cv(GetRT2.B)) + ' C=') + cv(GetRT2.C)) + ')')
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X2 - (GetRT2.A * 2)))) + ' Z') + cv(((Z1 + Tanmen) + KHaba))) + ' R') + cv(R2)) + F)
    self.a(TMP)


def gen_Kako_Ura_7(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    Z1 = vbval(self.txt('TextBox7'))
    C1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + Tanmen) + KHaba) - C1) - 0.2))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (((('G1 X' + cv(((X1 - (C1 * 2)) - 0.4))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) + 0.2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_8(self):
    S = self.txt('TextBox2')
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    Z1 = vbval(self.txt('TextBox7'))
    R1 = vbval(self.txt('TextBox8'))
    TMP = ''
    self.set_out('')
    TMP = ('M3 S' + S)
    self.a(TMP)
    TMP = ((('T300' + '(URA T=') + cv(KHaba)) + ')')
    self.a(TMP)
    TMP = (((('G0 X' + cv((X1 + 1))) + ' Z') + cv(((((Z1 + Tanmen) + KHaba) - R1) - 0.2))) + ' T3')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + ' F0.2')
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.05))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(X1)) + ' Z') + cv((((Z1 + Tanmen) + KHaba) - R1))) + F)
    self.a(TMP)
    TMP = (((((('G2 X' + cv((X1 - (R1 * 2)))) + ' Z') + cv(((Z1 + Tanmen) + KHaba))) + ' R') + cv(R1)) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv(((X1 - (R1 * 2)) - 0.8))) + ' Z') + cv((((Z1 + Tanmen) + KHaba) + 0.05))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((X1 + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((X1 + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)


def gen_Kako_Ura_9(self):
    Zai = vbval(self.txt('TextBox2'))
    F = (' F' + cv(vbval(self.txt('TextBox3'))))
    KHaba = vbval(self.txt('TextBox4'))
    Tanmen = vbval(self.txt('TextBox5'))
    X1 = vbval(self.txt('TextBox6'))
    Z1 = vbval(self.txt('TextBox7'))
    Z2 = vbval(self.txt('TextBox8'))
    D1 = vbval(self.txt('TextBox9'))
    TMP = ''
    self.set_out('')
    TMP = (('G1 X' + cv(X1)) + F)
    self.a(TMP)
    TMP = (('G1 Z' + cv((((Z1 + KHaba) + Tanmen) - Z2))) + F)
    self.a(TMP)
    TMP = (((('G1 X' + cv((X1 - (tann((Z2 + 0.2), D1) * 2)))) + ' Z') + cv((((Z1 + KHaba) + Tanmen) + 0.2))) + F)
    self.a(TMP)
    TMP = (('G1 X' + cv((Zai + 0.4))) + F)
    self.a(TMP)
    TMP = ('G0 X' + cv((Zai + 1)))
    self.a(TMP)
    TMP = 'T0'
    self.a(TMP)

