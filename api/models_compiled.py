# Auto-generated pure-Python model predictions (zero dependencies)
import math

# --- Mumbai Model: XGBoost ---
# Input: [precipitation_sum, precipitation_hours, precip_3d_sum, precip_7d_sum]
import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score_mumbai(input):
    if input[0] < 7.7999988:
        var0 = -0.19951427
    else:
        if input[1] < 19.0:
            var0 = -0.18431373
        else:
            if input[0] < 18.099998:
                if input[0] < 10.800001:
                    var0 = 0.13450965
                else:
                    var0 = -0.19157895
            else:
                if input[0] < 54.7:
                    var0 = 0.14376271
                else:
                    var0 = 0.18314846
    if input[0] < 7.7999988:
        var1 = -0.18146667
    else:
        if input[1] < 19.0:
            var1 = -0.16868871
        else:
            if input[0] < 18.099998:
                if input[0] < 10.800001:
                    var1 = 0.1217761
                else:
                    var1 = -0.17481074
            else:
                if input[0] < 54.7:
                    var1 = 0.13012989
                else:
                    var1 = 0.16635554
    if input[0] < 7.7999988:
        var2 = -0.16789533
    else:
        if input[1] < 19.0:
            var2 = -0.15651761
        else:
            if input[0] < 18.099998:
                if input[0] < 10.800001:
                    var2 = 0.11109705
                else:
                    var2 = -0.16196243
            else:
                if input[0] < 54.7:
                    var2 = 0.118833505
                else:
                    var2 = 0.15328568
    if input[0] < 7.7999988:
        var3 = -0.15734719
    else:
        if input[1] < 19.0:
            var3 = -0.14675985
        else:
            if input[0] < 18.099998:
                if input[0] < 10.800001:
                    var3 = 0.101921014
                else:
                    var3 = -0.15180807
            else:
                if input[3] < 182.9:
                    var3 = 0.10045276
                else:
                    var3 = 0.13557753
    if input[0] < 7.7999988:
        var4 = -0.14894073
    else:
        if input[1] < 19.0:
            var4 = -0.13875133
        else:
            if input[0] < 18.099998:
                if input[0] < 10.800001:
                    var4 = 0.093879454
                else:
                    var4 = -0.1435837
            else:
                if input[0] < 54.7:
                    var4 = 0.09999589
                else:
                    var4 = 0.13499832
    if input[0] < 7.7999988:
        var5 = -0.14210817
    else:
        if input[1] < 19.0:
            var5 = -0.1320473
        else:
            if input[0] < 18.099998:
                if input[0] < 10.800001:
                    var5 = 0.086718015
                else:
                    var5 = -0.136787
            else:
                if input[0] < 54.7:
                    var5 = 0.092664205
                else:
                    var5 = 0.12746361
    if input[0] < 7.7999988:
        var6 = -0.1364665
    else:
        if input[1] < 19.0:
            var6 = -0.12633805
        else:
            if input[0] < 20.500002:
                if input[2] < 24.899998:
                    var6 = -0.22379866
                else:
                    var6 = 0.07058184
            else:
                if input[2] < 7.8999996:
                    var6 = 0.14234917
                else:
                    var6 = 0.09396704
    if input[0] < 7.7999988:
        var7 = -0.13174744
    else:
        if input[1] < 19.0:
            var7 = -0.12140103
        else:
            if input[0] < 20.500002:
                if input[2] < 24.899998:
                    var7 = -0.20107888
                else:
                    var7 = 0.06466836
            else:
                if input[2] < 7.8999996:
                    var7 = 0.13583578
                else:
                    var7 = 0.087971635
    if input[0] < 7.7999988:
        var8 = -0.12775712
    else:
        if input[0] < 18.099998:
            if input[0] < 10.800001:
                if input[2] < 24.899998:
                    var8 = -0.18338954
                else:
                    var8 = 0.097589955
            else:
                var8 = -0.13374843
        else:
            if input[3] < 182.9:
                if input[3] < 108.00001:
                    var8 = 0.08427522
                else:
                    var8 = -0.30104643
            else:
                if input[0] < 54.7:
                    var8 = 0.089740016
                else:
                    var8 = 0.118563674
    if input[0] < 7.7999988:
        var9 = -0.12435186
    else:
        if input[1] < 19.0:
            var9 = -0.114850216
        else:
            if input[0] < 54.7:
                if input[0] < 36.600002:
                    var9 = 0.06960924
                else:
                    var9 = -0.31319925
            else:
                if input[2] < 75.600006:
                    var9 = 0.1177785
                else:
                    var9 = 0.08927876
    if input[0] < 7.7999988:
        var10 = -0.12142276
    else:
        if input[0] < 20.500002:
            if input[2] < 24.899998:
                var10 = -0.16437635
            else:
                if input[3] < 252.4:
                    var10 = 0.05992028
                else:
                    var10 = -0.18550603
        else:
            if input[0] < 84.3:
                if input[0] < 68.6:
                    var10 = 0.072145045
                else:
                    var10 = -0.2496336
            else:
                var10 = 0.11284822
    if input[0] < 7.7999988:
        var11 = -0.11888564
    else:
        if input[2] < 163.59999:
            if input[3] < 313.40002:
                if input[0] < 9.100001:
                    var11 = -0.19716142
                else:
                    var11 = 0.056068417
            else:
                var11 = -0.25366324
        else:
            if input[1] < 24.0:
                var11 = 0.125867
            else:
                if input[3] < 348.3:
                    var11 = -0.2795503
                else:
                    var11 = 0.10719464
    if input[0] < 7.7999988:
        var12 = -0.11667442
    else:
        if input[0] < 54.7:
            if input[0] < 36.600002:
                if input[3] < 216.2:
                    var12 = 0.017547471
                else:
                    var12 = 0.09029736
            else:
                var12 = -0.26686937
        else:
            if input[2] < 75.600006:
                if input[3] < 105.4:
                    var12 = 0.06654724
                else:
                    var12 = 0.118214644
            else:
                if input[3] < 295.9:
                    var12 = -0.2943682
                else:
                    var12 = 0.105165206
    if input[0] < 7.7999988:
        var13 = -0.1147364
    else:
        if input[0] < 20.500002:
            if input[2] < 24.899998:
                var13 = -0.15289567
            else:
                if input[0] < 10.800001:
                    var13 = 0.0785033
                else:
                    var13 = -0.041099567
        else:
            if input[2] < 7.8999996:
                var13 = 0.11739235
            else:
                if input[2] < 40.699997:
                    var13 = -0.326483
                else:
                    var13 = 0.0730671
    if input[0] < 7.7999988:
        var14 = -0.113028996
    else:
        if input[0] < 54.7:
            if input[0] < 36.600002:
                if input[3] < 216.2:
                    var14 = 0.012758416
                else:
                    var14 = 0.082757734
            else:
                var14 = -0.23162222
        else:
            if input[2] < 75.600006:
                if input[3] < 105.4:
                    var14 = 0.057136294
                else:
                    var14 = 0.11350479
            else:
                if input[3] < 295.9:
                    var14 = -0.25780198
                else:
                    var14 = 0.09934588
    if input[0] < 7.7999988:
        var15 = -0.11151736
    else:
        if input[0] < 18.099998:
            if input[0] < 10.800001:
                if input[2] < 24.899998:
                    var15 = -0.14863035
                else:
                    var15 = 0.07152618
            else:
                var15 = -0.13338302
        else:
            if input[2] < 7.8999996:
                if input[2] < 5.5000005:
                    var15 = -0.1235575
                else:
                    var15 = 0.11988051
            else:
                if input[2] < 40.699997:
                    var15 = -0.2682983
                else:
                    var15 = 0.06582779
    if input[0] < 7.7999988:
        var16 = -0.110172726
    else:
        if input[2] < 163.59999:
            if input[3] < 313.40002:
                if input[0] < 9.100001:
                    var16 = -0.18335299
                else:
                    var16 = 0.039980087
            else:
                var16 = -0.24444361
        else:
            if input[1] < 24.0:
                var16 = 0.11166908
            else:
                if input[3] < 348.3:
                    var16 = -0.232263
                else:
                    var16 = 0.092021205
    if input[0] < 7.7999988:
        var17 = -0.10897104
    else:
        if input[0] < 54.7:
            if input[0] < 36.600002:
                if input[2] < 163.59999:
                    var17 = 0.0180731
                else:
                    var17 = 0.0966238
            else:
                var17 = -0.2083807
        else:
            if input[2] < 75.600006:
                if input[3] < 105.4:
                    var17 = 0.045304026
                else:
                    var17 = 0.10879078
            else:
                if input[3] < 295.9:
                    var17 = -0.23097645
                else:
                    var17 = 0.092119694
    if input[0] < 7.7999988:
        var18 = -0.107892014
    else:
        if input[0] < 54.7:
            if input[0] < 36.600002:
                if input[3] < 216.2:
                    var18 = 0.0049309223
                else:
                    var18 = 0.06955173
            else:
                var18 = -0.18764457
        else:
            if input[2] < 75.600006:
                if input[3] < 105.4:
                    var18 = 0.042473596
                else:
                    var18 = 0.106658295
            else:
                if input[3] < 295.9:
                    var18 = -0.20286453
                else:
                    var18 = 0.08920332
    if input[1] < 19.0:
        var19 = -0.108062856
    else:
        if input[0] < 18.099998:
            if input[0] < 10.800001:
                if input[2] < 24.899998:
                    var19 = -0.12875178
                else:
                    var19 = 0.054222357
            else:
                var19 = -0.13300776
        else:
            if input[2] < 7.8999996:
                var19 = 0.10901945
            else:
                if input[2] < 40.699997:
                    var19 = -0.24251464
                else:
                    var19 = 0.05451677
    if input[1] < 19.0:
        var20 = -0.107087314
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.5000005:
                var20 = -0.11717639
            else:
                var20 = 0.11316476
        else:
            if input[2] < 40.699997:
                if input[3] < 41.0:
                    var20 = 0.038324516
                else:
                    var20 = -0.18043943
            else:
                if input[2] < 46.3:
                    var20 = 0.0949887
                else:
                    var20 = 0.029966438
    if input[0] < 7.7999988:
        var21 = -0.10528989
    else:
        if input[2] < 163.59999:
            if input[3] < 313.40002:
                if input[0] < 9.100001:
                    var21 = -0.1712588
                else:
                    var21 = 0.028184285
            else:
                var21 = -0.2320766
        else:
            if input[1] < 24.0:
                var21 = 0.1022644
            else:
                if input[3] < 348.3:
                    var21 = -0.20785521
                else:
                    var21 = 0.080358796
    if input[1] < 19.0:
        var22 = -0.105629876
    else:
        if input[2] < 7.8999996:
            var22 = 0.100610964
        else:
            if input[2] < 24.899998:
                var22 = -0.1435972
            else:
                if input[2] < 163.59999:
                    var22 = 0.013071063
                else:
                    var22 = 0.07442516
    if input[1] < 19.0:
        var23 = -0.1048587
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.5000005:
                var23 = -0.116709135
            else:
                var23 = 0.10896476
        else:
            if input[2] < 40.699997:
                if input[3] < 41.0:
                    var23 = 0.037597027
                else:
                    var23 = -0.1712295
            else:
                if input[2] < 46.3:
                    var23 = 0.089862734
                else:
                    var23 = 0.021732775
    if input[1] < 19.0:
        var24 = -0.10414189
    else:
        if input[0] < 54.7:
            if input[0] < 36.600002:
                if input[3] < 216.2:
                    var24 = -0.005876011
                else:
                    var24 = 0.057246763
            else:
                var24 = -0.18215197
        else:
            if input[3] < 174.4:
                if input[0] < 84.3:
                    var24 = -0.2051891
                else:
                    var24 = 0.06125697
            else:
                if input[2] < 75.600006:
                    var24 = 0.10598526
                else:
                    var24 = 0.05375194
    if input[0] < 7.7999988:
        var25 = -0.102770746
    else:
        if input[0] < 84.3:
            if input[3] < 41.0:
                if input[1] < 24.0:
                    var25 = 0.08681711
                else:
                    var25 = -0.14370255
            else:
                if input[2] < 40.699997:
                    var25 = -0.16779503
                else:
                    var25 = 0.018824073
        else:
            if input[3] < 105.4:
                var25 = 0.037704412
            else:
                if input[3] < 295.9:
                    var25 = 0.07104577
                else:
                    var25 = 0.10321599
    if input[1] < 19.0:
        var26 = -0.10303599
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.5000005:
                var26 = -0.10941521
            else:
                var26 = 0.1060852
        else:
            if input[2] < 24.899998:
                var26 = -0.13270168
            else:
                if input[2] < 163.59999:
                    var26 = 0.006044041
                else:
                    var26 = 0.066764936
    if input[0] < 7.7999988:
        var27 = -0.10170593
    else:
        if input[0] < 84.3:
            if input[0] < 32.899998:
                if input[0] < 20.500002:
                    var27 = -0.0077413553
                else:
                    var27 = 0.050780743
            else:
                if input[3] < 174.4:
                    var27 = -0.23261316
                else:
                    var27 = 0.0062321746
        else:
            if input[3] < 105.4:
                var27 = 0.029727278
            else:
                if input[3] < 295.9:
                    var27 = 0.06773456
                else:
                    var27 = 0.101353906
    if input[1] < 19.0:
        var28 = -0.102058664
    else:
        if input[2] < 7.8999996:
            var28 = 0.09139067
        else:
            if input[2] < 24.899998:
                var28 = -0.1296783
            else:
                if input[2] < 163.59999:
                    var28 = 0.004315013
                else:
                    var28 = 0.061998278
    if input[1] < 19.0:
        var29 = -0.101482086
    else:
        if input[3] < 41.0:
            if input[0] < 10.0:
                var29 = -0.082430616
            else:
                if input[1] < 24.0:
                    var29 = 0.09248032
                else:
                    var29 = 0.02157755
        else:
            if input[2] < 40.699997:
                if input[0] < 8.200001:
                    var29 = -0.07906162
                else:
                    var29 = -0.16744946
            else:
                if input[2] < 46.3:
                    var29 = 0.08300905
                else:
                    var29 = 0.008998607
    if input[0] < 7.7999988:
        var30 = -0.10030087
    else:
        if input[0] < 54.7:
            if input[0] < 32.899998:
                if input[0] < 31.8:
                    var30 = 0.008073255
                else:
                    var30 = 0.089466564
            else:
                if input[1] < 24.0:
                    var30 = 0.04347021
                else:
                    var30 = -0.23659682
        else:
            if input[2] < 75.600006:
                if input[3] < 105.4:
                    var30 = -0.012836464
                else:
                    var30 = 0.09807476
            else:
                if input[3] < 295.9:
                    var30 = -0.19651721
                else:
                    var30 = 0.06918343
    if input[1] < 19.0:
        var31 = -0.10059251
    else:
        if input[3] < 41.0:
            if input[0] < 10.0:
                var31 = -0.079325296
            else:
                if input[1] < 24.0:
                    var31 = 0.088823125
                else:
                    var31 = 0.021686986
        else:
            if input[2] < 40.699997:
                var31 = -0.1514778
            else:
                if input[2] < 46.3:
                    var31 = 0.07900715
                else:
                    var31 = 0.006573435
    if input[1] < 19.0:
        var32 = -0.10003914
    else:
        if input[2] < 163.59999:
            if input[3] < 252.4:
                if input[0] < 9.100001:
                    var32 = -0.12808436
                else:
                    var32 = 0.021782028
            else:
                if input[0] < 84.3:
                    var32 = -0.27637506
                else:
                    var32 = 0.0715842
        else:
            if input[1] < 24.0:
                var32 = 0.09217689
            else:
                if input[3] < 348.3:
                    var32 = -0.20776992
                else:
                    var32 = 0.060545027
    if input[1] < 19.0:
        var33 = -0.099489324
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.999999:
                var33 = 0.057215672
            else:
                var33 = 0.097318895
        else:
            if input[2] < 24.899998:
                var33 = -0.12577134
            else:
                if input[2] < 163.59999:
                    var33 = -0.0012588834
                else:
                    var33 = 0.055165287
    if input[1] < 19.0:
        var34 = -0.098938756
    else:
        if input[3] < 41.0:
            if input[0] < 10.0:
                var34 = -0.07228062
            else:
                if input[3] < 37.6:
                    var34 = 0.046591617
                else:
                    var34 = 0.10660366
        else:
            if input[2] < 40.699997:
                var34 = -0.14643393
            else:
                if input[2] < 46.3:
                    var34 = 0.075078584
                else:
                    var34 = 0.0029650794
    if input[0] < 7.7999988:
        var35 = -0.09797344
    else:
        if input[0] < 54.7:
            if input[0] < 32.899998:
                if input[0] < 31.8:
                    var35 = 0.0027572967
                else:
                    var35 = 0.08657445
            else:
                if input[1] < 24.0:
                    var35 = 0.033989888
                else:
                    var35 = -0.21437447
        else:
            if input[3] < 105.4:
                if input[2] < 7.0999994:
                    var35 = 0.085633755
                else:
                    var35 = -0.2914008
            else:
                if input[2] < 75.600006:
                    var35 = 0.095525734
                else:
                    var35 = 0.015406786
    if input[1] < 19.0:
        var36 = -0.09800465
    else:
        if input[0] < 84.3:
            if input[2] < 163.59999:
                if input[3] < 252.4:
                    var36 = 0.0069384673
                else:
                    var36 = -0.24581455
            else:
                if input[1] < 24.0:
                    var36 = 0.08793537
                else:
                    var36 = -0.0050335187
        else:
            if input[3] < 295.9:
                if input[2] < 64.59999:
                    var36 = 0.07011555
                else:
                    var36 = -0.2043807
            else:
                var36 = 0.097115606
    if input[0] < 7.7999988:
        var37 = -0.09701382
    else:
        if input[3] < 41.0:
            if input[2] < 5.7999997:
                var37 = -0.08700914
            else:
                if input[2] < 7.8999996:
                    var37 = 0.09890484
                else:
                    var37 = 0.029458387
        else:
            if input[2] < 40.699997:
                var37 = -0.142206
            else:
                if input[2] < 46.3:
                    var37 = 0.072046235
                else:
                    var37 = 0.0006931577
    if input[1] < 19.0:
        var38 = -0.09695072
    else:
        if input[2] < 163.59999:
            if input[3] < 252.4:
                if input[3] < 234.5:
                    var38 = -0.0035370968
                else:
                    var38 = 0.08119614
            else:
                if input[0] < 84.3:
                    var38 = -0.22384559
                else:
                    var38 = 0.06595231
        else:
            if input[1] < 24.0:
                if input[0] < 21.400002:
                    var38 = 0.056750037
                else:
                    var38 = 0.09855764
            else:
                if input[3] < 348.3:
                    var38 = -0.192211
                else:
                    var38 = 0.054212015
    if input[0] < 7.7999988:
        var39 = -0.09597363
    else:
        if input[3] < 41.0:
            if input[2] < 5.7999997:
                var39 = -0.08336371
            else:
                if input[2] < 7.8999996:
                    var39 = 0.09780214
                else:
                    var39 = 0.027530735
        else:
            if input[2] < 40.699997:
                var39 = -0.13699713
            else:
                if input[2] < 46.3:
                    var39 = 0.069122456
                else:
                    var39 = -0.0007176364
    if input[1] < 19.0:
        var40 = -0.095823005
    else:
        if input[0] < 54.7:
            if input[0] < 32.899998:
                if input[0] < 31.8:
                    var40 = -0.00009143535
                else:
                    var40 = 0.083539344
            else:
                if input[2] < 163.59999:
                    var40 = -0.1994525
                else:
                    var40 = 0.022881571
        else:
            if input[3] < 105.4:
                if input[2] < 7.0999994:
                    var40 = 0.078912735
                else:
                    var40 = -0.25572821
            else:
                if input[2] < 75.600006:
                    var40 = 0.09308572
                else:
                    var40 = 0.010032306
    if input[0] < 7.7999988:
        var41 = -0.094860606
    else:
        if input[2] < 163.59999:
            if input[3] < 252.4:
                if input[2] < 126.3:
                    var41 = 0.0119308615
                else:
                    var41 = -0.1897779
            else:
                if input[0] < 84.3:
                    var41 = -0.20349205
                else:
                    var41 = 0.06300744
        else:
            if input[1] < 24.0:
                if input[0] < 21.400002:
                    var41 = 0.0531766
                else:
                    var41 = 0.097131446
            else:
                if input[0] < 25.900002:
                    var41 = -0.23546107
                else:
                    var41 = 0.042451717
    if input[1] < 19.0:
        var42 = -0.094642684
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.999999:
                var42 = 0.04723571
            else:
                var42 = 0.091444135
        else:
            if input[2] < 24.899998:
                var42 = -0.12228515
            else:
                if input[2] < 25.7:
                    var42 = 0.097136155
                else:
                    var42 = -0.0011465818
    if input[0] < 7.7999988:
        var43 = -0.09360558
    else:
        if input[0] < 9.6:
            if input[2] < 56.500004:
                var43 = -0.14364411
            else:
                if input[3] < 132.7:
                    var43 = 0.11338895
                else:
                    var43 = 0.026468083
        else:
            if input[0] < 18.099998:
                if input[3] < 41.0:
                    var43 = 0.06915786
                else:
                    var43 = -0.16091006
            else:
                if input[3] < 182.9:
                    var43 = -0.026784798
                else:
                    var43 = 0.036802422
    if input[0] < 7.7999988:
        var44 = -0.09286668
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.7999997:
                var44 = -0.09931045
            else:
                var44 = 0.0956875
        else:
            if input[3] < 37.6:
                var44 = -0.1418425
            else:
                if input[3] < 41.0:
                    var44 = 0.094431475
                else:
                    var44 = -0.0022154774
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[1] < 19.0:
        var46 = -0.092476085
    else:
        if input[0] < 84.3:
            if input[0] < 32.899998:
                if input[3] < 216.2:
                    var46 = -0.013956532
                else:
                    var46 = 0.043403815
            else:
                if input[3] < 182.9:
                    var46 = -0.1827601
                else:
                    var46 = -0.0044288244
        else:
            if input[3] < 105.4:
                var46 = -0.016697878
            else:
                if input[0] < 100.29999:
                    var46 = 0.08126285
                else:
                    var46 = 0.018617934
    if input[0] < 7.7999988:
        var47 = -0.09142088
    else:
        if input[2] < 7.8999996:
            if input[2] < 5.7999997:
                var47 = -0.09321933
            else:
                var47 = 0.0947179
        else:
            if input[2] < 24.899998:
                var47 = -0.11526511
            else:
                if input[2] < 25.7:
                    var47 = 0.09270537
                else:
                    var47 = -0.0020458526
    if input[0] < 7.7999988:
        var48 = -0.09056132
    else:
        if input[0] < 9.6:
            if input[2] < 56.500004:
                var48 = -0.13902938
            else:
                if input[3] < 132.7:
                    var48 = 0.11108998
                else:
                    var48 = 0.022157213
        else:
            if input[0] < 18.099998:
                if input[3] < 41.0:
                    var48 = 0.063357525
                else:
                    var48 = -0.15470496
            else:
                if input[3] < 182.9:
                    var48 = -0.023988679
                else:
                    var48 = 0.03238065
    if input[2] < 5.8999996:
        var49 = -0.097319774
    else:
        if input[2] < 7.8999996:
            var49 = 0.091037154
        else:
            if input[2] < 24.899998:
                var49 = -0.11019818
            else:
                if input[2] < 25.7:
                    var49 = 0.08824798
                else:
                    var49 = -0.0030823974
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[3] < 216.2:
                if input[2] < 60.200005:
                    var50 = 0.013157479
                else:
                    var50 = -0.28397292
            else:
                if input[2] < 89.3:
                    var50 = -0.17033336
                else:
                    var50 = 0.059779603
        else:
            if input[1] < 24.0:
                if input[2] < 115.5:
                    var50 = -0.1158767
                else:
                    var50 = 0.08628865
            else:
                var50 = -0.17782892
    else:
        if input[3] < 105.4:
            if input[2] < 7.0999994:
                var50 = 0.070430815
            else:
                var50 = -0.20784293
        else:
            if input[2] < 75.600006:
                var50 = 0.09030078
            else:
                if input[3] < 295.9:
                    var50 = -0.16693507
                else:
                    var50 = 0.0517109
    if input[2] < 5.8999996:
        var51 = -0.09602558
    else:
        if input[2] < 7.8999996:
            var51 = 0.088921845
        else:
            if input[2] < 40.699997:
                if input[0] < 10.800001:
                    var51 = 0.008942616
                else:
                    var51 = -0.13012722
            else:
                if input[2] < 46.3:
                    var51 = 0.06868329
                else:
                    var51 = -0.0067469785
    if input[2] < 163.59999:
        if input[3] < 252.4:
            if input[3] < 234.5:
                if input[2] < 98.100006:
                    var52 = 0.0033472271
                else:
                    var52 = -0.24190597
            else:
                if input[0] < 32.899998:
                    var52 = 0.09218061
                else:
                    var52 = -0.1171939
        else:
            if input[0] < 84.3:
                var52 = -0.18956591
            else:
                var52 = 0.053901937
    else:
        if input[1] < 24.0:
            if input[0] < 21.400002:
                var52 = 0.04657505
            else:
                var52 = 0.09393086
        else:
            if input[3] < 348.3:
                var52 = -0.1650381
            else:
                if input[3] < 367.3:
                    var52 = 0.06692785
                else:
                    var52 = 0.00024516237
    if input[0] < 7.7999988:
        var53 = -0.0881537
    else:
        if input[0] < 9.6:
            if input[2] < 56.500004:
                var53 = -0.1355245
            else:
                if input[3] < 132.7:
                    var53 = 0.10842737
                else:
                    var53 = 0.02061903
        else:
            if input[0] < 18.099998:
                if input[3] < 41.0:
                    var53 = 0.058575578
                else:
                    var53 = -0.1452261
            else:
                if input[3] < 182.9:
                    var53 = -0.022375368
                else:
                    var53 = 0.028740663
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[3] < 85.2:
                    var54 = 0.023861742
                else:
                    var54 = -0.03483283
            else:
                if input[3] < 150.5:
                    var54 = -0.098451324
                else:
                    var54 = 0.09509538
        else:
            if input[1] < 24.0:
                if input[2] < 115.5:
                    var54 = -0.10362726
                else:
                    var54 = 0.08250394
            else:
                var54 = -0.16395293
    else:
        if input[3] < 105.4:
            if input[2] < 7.0999994:
                var54 = 0.06720218
            else:
                var54 = -0.18708172
        else:
            if input[2] < 75.600006:
                if input[3] < 123.6:
                    var54 = 0.054075766
                else:
                    var54 = 0.09699072
            else:
                if input[3] < 295.9:
                    var54 = -0.14849341
                else:
                    var54 = 0.047163676
    if input[0] < 7.7999988:
        var55 = -0.087310635
    else:
        if input[0] < 9.6:
            if input[2] < 56.500004:
                var55 = -0.12966855
            else:
                if input[3] < 132.7:
                    var55 = 0.10685154
                else:
                    var55 = 0.021679621
        else:
            if input[0] < 18.099998:
                if input[3] < 41.0:
                    var55 = 0.05359158
                else:
                    var55 = -0.13921346
            else:
                if input[2] < 46.3:
                    var55 = 0.04116471
                else:
                    var55 = -0.007741452
    if input[3] < 216.2:
        if input[2] < 75.600006:
            if input[0] < 9.100001:
                var56 = -0.09870323
            else:
                if input[0] < 9.6:
                    var56 = 0.088903345
                else:
                    var56 = 0.0020918432
        else:
            var56 = -0.20450035
    else:
        if input[2] < 89.3:
            var56 = -0.156879
        else:
            if input[3] < 272.5:
                if input[0] < 36.600002:
                    var56 = 0.08008884
                else:
                    var56 = -0.10542587
            else:
                if input[2] < 132.5:
                    var56 = -0.165228
                else:
                    var56 = 0.023182048
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[3] < 216.2:
                if input[2] < 60.200005:
                    var57 = 0.010616604
                else:
                    var57 = -0.22685373
            else:
                if input[2] < 89.3:
                    var57 = -0.14815098
                else:
                    var57 = 0.05359329
        else:
            if input[1] < 24.0:
                if input[2] < 115.5:
                    var57 = -0.09521678
                else:
                    var57 = 0.07946702
            else:
                var57 = -0.15317796
    else:
        if input[3] < 105.4:
            if input[2] < 7.0999994:
                var57 = 0.06458652
            else:
                var57 = -0.17238171
        else:
            if input[2] < 75.600006:
                if input[2] < 44.4:
                    var57 = 0.03599907
                else:
                    var57 = 0.091223195
            else:
                if input[3] < 295.9:
                    var57 = -0.13356797
                else:
                    var57 = 0.044345275
    if input[2] < 5.8999996:
        var58 = -0.0938245
    else:
        if input[2] < 7.8999996:
            var58 = 0.086578414
        else:
            if input[2] < 40.699997:
                if input[0] < 10.800001:
                    var58 = 0.00970901
                else:
                    var58 = -0.12656687
            else:
                if input[2] < 46.3:
                    var58 = 0.06614362
                else:
                    var58 = -0.0076083243
    if input[3] < 405.5:
        if input[3] < 367.3:
            if input[2] < 5.8999996:
                var59 = -0.09229131
            else:
                if input[2] < 7.8999996:
                    var59 = 0.08471691
                else:
                    var59 = -0.003744126
        else:
            var59 = -0.17534214
    else:
        if input[0] < 54.7:
            var59 = 0.04071888
        else:
            var59 = 0.083401084
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[3] < 216.2:
                if input[2] < 60.200005:
                    var60 = 0.009676336
                else:
                    var60 = -0.20607863
            else:
                if input[2] < 89.3:
                    var60 = -0.14207177
                else:
                    var60 = 0.051499244
        else:
            if input[1] < 24.0:
                if input[2] < 115.5:
                    var60 = -0.090540044
                else:
                    var60 = 0.078088135
            else:
                var60 = -0.1454235
    else:
        if input[3] < 105.4:
            if input[2] < 7.0999994:
                var60 = 0.0588209
            else:
                var60 = -0.15927061
        else:
            if input[2] < 75.600006:
                if input[2] < 44.4:
                    var60 = 0.03159641
                else:
                    var60 = 0.08987885
            else:
                if input[3] < 295.9:
                    var60 = -0.12625384
                else:
                    var60 = 0.04112384
    if input[2] < 5.8999996:
        var61 = -0.09071898
    else:
        if input[2] < 7.8999996:
            var61 = 0.08235433
        else:
            if input[3] < 39.5:
                var61 = -0.115548484
            else:
                if input[3] < 41.0:
                    var61 = 0.08230018
                else:
                    var61 = -0.0036706475
    if input[3] < 405.5:
        if input[3] < 367.3:
            if input[3] < 216.2:
                if input[2] < 75.600006:
                    var62 = 0.003041907
                else:
                    var62 = -0.16324206
            else:
                if input[2] < 89.3:
                    var62 = -0.14004728
                else:
                    var62 = 0.037385073
        else:
            var62 = -0.1672068
    else:
        if input[0] < 54.7:
            var62 = 0.03676633
        else:
            var62 = 0.08107241
    if input[2] < 5.8999996:
        var63 = -0.08912353
    else:
        if input[2] < 7.8999996:
            var63 = 0.08018573
        else:
            if input[2] < 40.699997:
                if input[0] < 10.800001:
                    var63 = 0.00534008
                else:
                    var63 = -0.12057376
            else:
                if input[2] < 46.3:
                    var63 = 0.06324325
                else:
                    var63 = -0.0066099884
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 216.2:
                    var64 = -0.018294072
                else:
                    var64 = 0.044994947
            else:
                if input[2] < 213.20001:
                    var64 = -0.18800025
                else:
                    var64 = -0.002049045
        else:
            if input[2] < 180.09999:
                var64 = 0.07976335
            else:
                var64 = 0.03405673
    else:
        if input[3] < 105.4:
            var64 = -0.04053719
        else:
            if input[0] < 100.29999:
                if input[3] < 295.9:
                    var64 = 0.042123955
                else:
                    var64 = 0.08797743
            else:
                var64 = -0.002538794
    if input[0] < 7.7999988:
        var65 = -0.081454776
    else:
        if input[0] < 9.6:
            if input[2] < 56.500004:
                var65 = -0.12595986
            else:
                if input[3] < 132.7:
                    var65 = 0.103244536
                else:
                    var65 = 0.019987226
        else:
            if input[2] < 46.3:
                if input[2] < 40.699997:
                    var65 = -0.010391793
                else:
                    var65 = 0.07122545
            else:
                if input[3] < 182.9:
                    var65 = -0.13677858
                else:
                    var65 = 0.011372352
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[3] < 85.2:
                    var66 = 0.022576595
                else:
                    var66 = -0.031234352
            else:
                if input[3] < 150.5:
                    var66 = -0.074803494
                else:
                    var66 = 0.08992561
        else:
            if input[1] < 24.0:
                if input[2] < 115.5:
                    var66 = -0.079645075
                else:
                    var66 = 0.07470589
            else:
                var66 = -0.1373649
    else:
        if input[3] < 105.4:
            if input[2] < 7.0999994:
                var66 = 0.05447315
            else:
                var66 = -0.14026247
        else:
            if input[2] < 75.600006:
                if input[2] < 44.4:
                    var66 = 0.024011234
                else:
                    var66 = 0.08912816
            else:
                if input[3] < 295.9:
                    var66 = -0.11959185
                else:
                    var66 = 0.034238767
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 216.2:
                    var67 = -0.016799724
                else:
                    var67 = 0.04154714
            else:
                if input[2] < 213.20001:
                    var67 = -0.1781758
                else:
                    var67 = 0.0011504646
        else:
            if input[2] < 180.09999:
                var67 = 0.07855248
            else:
                var67 = 0.030737076
    else:
        if input[3] < 105.4:
            var67 = -0.031575732
        else:
            if input[0] < 100.29999:
                if input[3] < 295.9:
                    var67 = 0.04289607
                else:
                    var67 = 0.08592476
            else:
                var67 = -0.00504007
    if input[0] < 7.7999988:
        var68 = -0.080119364
    else:
        if input[0] < 9.6:
            if input[2] < 56.500004:
                var68 = -0.12022325
            else:
                if input[3] < 132.7:
                    var68 = 0.102186576
                else:
                    var68 = 0.020607797
        else:
            if input[2] < 46.3:
                if input[3] < 85.2:
                    var68 = 0.043042917
                else:
                    var68 = -0.07060944
            else:
                if input[3] < 105.4:
                    var68 = -0.19615464
                else:
                    var68 = -0.0033925367
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[3] < 85.2:
                    var69 = 0.021067897
                else:
                    var69 = -0.02853687
            else:
                var69 = 0.067477554
        else:
            if input[1] < 24.0:
                if input[2] < 115.5:
                    var69 = -0.07420864
                else:
                    var69 = 0.07224834
            else:
                var69 = -0.13125804
    else:
        if input[3] < 105.4:
            if input[2] < 7.0999994:
                var69 = 0.052808788
            else:
                var69 = -0.122379914
        else:
            if input[2] < 75.600006:
                if input[3] < 123.6:
                    var69 = 0.042929024
                else:
                    var69 = 0.09327359
            else:
                if input[3] < 295.9:
                    var69 = -0.11485886
                else:
                    var69 = 0.030301085
    if input[2] < 5.8999996:
        var70 = -0.08643221
    else:
        if input[2] < 7.8999996:
            var70 = 0.07786417
        else:
            if input[2] < 24.899998:
                var70 = -0.099080816
            else:
                if input[2] < 25.7:
                    var70 = 0.08463049
                else:
                    var70 = -0.002844468
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 234.5:
                    var71 = -0.0124694705
                else:
                    var71 = 0.055794477
            else:
                if input[2] < 213.20001:
                    var71 = -0.16899465
                else:
                    var71 = 0.0052135326
        else:
            if input[2] < 180.09999:
                var71 = 0.07766363
            else:
                var71 = 0.028744593
    else:
        if input[3] < 295.9:
            if input[2] < 64.59999:
                if input[3] < 105.4:
                    var71 = -0.013208759
                else:
                    var71 = 0.07081266
            else:
                var71 = -0.13519381
        else:
            var71 = 0.084153734
    if input[2] < 5.8999996:
        var72 = -0.08432744
    else:
        if input[2] < 7.8999996:
            var72 = 0.07599233
        else:
            if input[2] < 40.699997:
                if input[0] < 10.800001:
                    var72 = 0.0075201876
                else:
                    var72 = -0.115552925
            else:
                if input[2] < 46.3:
                    var72 = 0.05752767
                else:
                    var72 = -0.005049353
    if input[2] < 163.59999:
        if input[3] < 252.4:
            if input[3] < 234.5:
                if input[2] < 98.100006:
                    var73 = 0.0024475271
                else:
                    var73 = -0.16929843
            else:
                if input[3] < 244.70001:
                    var73 = 0.028928474
                else:
                    var73 = 0.08634701
        else:
            if input[0] < 84.3:
                var73 = -0.14174862
            else:
                var73 = 0.03811689
    else:
        if input[1] < 24.0:
            if input[0] < 21.400002:
                var73 = 0.039087728
            else:
                var73 = 0.08566176
        else:
            if input[0] < 25.900002:
                var73 = -0.17967127
            else:
                if input[0] < 28.999998:
                    var73 = 0.08785256
                else:
                    var73 = -0.016683113
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[3] < 216.2:
                if input[3] < 132.7:
                    var74 = 0.009940451
                else:
                    var74 = -0.1698253
            else:
                if input[2] < 89.3:
                    var74 = -0.12391639
                else:
                    var74 = 0.046080817
        else:
            if input[1] < 24.0:
                var74 = 0.017259382
            else:
                var74 = -0.12568875
    else:
        if input[3] < 105.4:
            if input[2] < 15.699999:
                var74 = 0.038870677
            else:
                var74 = -0.114540756
        else:
            if input[2] < 75.600006:
                if input[2] < 44.4:
                    var74 = 0.015877746
                else:
                    var74 = 0.0859892
            else:
                if input[3] < 295.9:
                    var74 = -0.106286764
                else:
                    var74 = 0.028063033
    if input[1] < 19.0:
        var75 = -0.077550165
    else:
        if input[0] < 9.6:
            if input[2] < 58.300003:
                var75 = -0.110826984
            else:
                if input[2] < 60.200005:
                    var75 = 0.10095432
                else:
                    var75 = 0.022870671
        else:
            if input[2] < 46.3:
                if input[3] < 85.2:
                    var75 = 0.04051802
                else:
                    var75 = -0.06942072
            else:
                if input[3] < 182.9:
                    var75 = -0.120437816
                else:
                    var75 = 0.008725617
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 234.5:
                    var76 = -0.01091377
                else:
                    var76 = 0.05004794
            else:
                if input[2] < 213.20001:
                    var76 = -0.15800358
                else:
                    var76 = -0.0012089328
        else:
            if input[0] < 54.7:
                var76 = 0.021112101
            else:
                var76 = 0.075937785
    else:
        if input[3] < 295.9:
            if input[2] < 64.59999:
                if input[2] < 56.500004:
                    var76 = 0.0028783635
                else:
                    var76 = 0.08134838
            else:
                var76 = -0.12440931
        else:
            var76 = 0.08192757
    if input[2] < 5.8999996:
        var77 = -0.08221816
    else:
        if input[2] < 7.8999996:
            var77 = 0.073300384
        else:
            if input[2] < 40.699997:
                if input[0] < 10.800001:
                    var77 = 0.007634369
                else:
                    var77 = -0.11267461
            else:
                if input[2] < 46.3:
                    var77 = 0.054647006
                else:
                    var77 = -0.0049022157
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[0] < 24.800001:
                    var78 = 0.0034464754
                else:
                    var78 = -0.058316972
            else:
                var78 = 0.06657337
        else:
            if input[1] < 24.0:
                var78 = 0.015960172
            else:
                var78 = -0.12143321
    else:
        if input[3] < 105.4:
            if input[3] < 42.7:
                var78 = 0.0007526767
            else:
                var78 = -0.08620731
        else:
            if input[2] < 75.600006:
                if input[2] < 44.4:
                    var78 = 0.015683925
                else:
                    var78 = 0.084797725
            else:
                if input[2] < 237.70001:
                    var78 = -0.049272474
                else:
                    var78 = 0.07442534
    if input[0] < 84.3:
        if input[0] < 9.6:
            if input[2] < 58.300003:
                var79 = -0.10491569
            else:
                if input[2] < 60.200005:
                    var79 = 0.09879764
                else:
                    var79 = 0.023023445
        else:
            if input[2] < 46.3:
                if input[0] < 28.199999:
                    var79 = 0.035639923
                else:
                    var79 = -0.108672775
            else:
                if input[3] < 182.9:
                    var79 = -0.16034594
                else:
                    var79 = 0.0024051561
    else:
        if input[3] < 295.9:
            if input[2] < 64.59999:
                if input[2] < 56.500004:
                    var79 = 0.00063146016
                else:
                    var79 = 0.078129195
            else:
                var79 = -0.11801902
        else:
            var79 = 0.08144324
    if input[2] < 5.8999996:
        var80 = -0.07927818
    else:
        if input[2] < 7.8999996:
            var80 = 0.07132551
        else:
            if input[2] < 24.899998:
                var80 = -0.09336505
            else:
                if input[2] < 25.7:
                    var80 = 0.0826116
                else:
                    var80 = -0.0029220665
    if input[2] < 40.699997:
        if input[3] < 41.0:
            if input[0] < 10.500003:
                var81 = -0.075668745
            else:
                if input[1] < 24.0:
                    var81 = 0.057162136
                else:
                    var81 = -0.037774436
        else:
            var81 = -0.10867553
    else:
        if input[0] < 9.6:
            if input[3] < 132.7:
                var81 = 0.08592356
            else:
                if input[0] < 7.7999997:
                    var81 = 0.07823594
                else:
                    var81 = -0.1423774
        else:
            if input[0] < 18.099998:
                var81 = -0.12066548
            else:
                if input[2] < 46.3:
                    var81 = 0.07614354
                else:
                    var81 = -0.0071022348
    if input[3] < 128.5:
        if input[2] < 46.3:
            if input[2] < 40.699997:
                if input[2] < 25.7:
                    var82 = 0.010697609
                else:
                    var82 = -0.11014923
            else:
                if input[2] < 44.4:
                    var82 = 0.029965514
                else:
                    var82 = 0.08831875
        else:
            if input[0] < 84.3:
                var82 = -0.15448761
            else:
                var82 = 0.019542757
    else:
        if input[3] < 132.7:
            var82 = 0.0846651
        else:
            if input[3] < 182.9:
                var82 = -0.12972523
            else:
                if input[0] < 28.199999:
                    var82 = -0.021955786
                else:
                    var82 = 0.032517266
    if input[3] < 405.5:
        if input[3] < 367.3:
            if input[0] < 9.6:
                if input[2] < 58.300003:
                    var83 = -0.09910669
                else:
                    var83 = 0.078548096
            else:
                if input[0] < 18.099998:
                    var83 = -0.05365335
                else:
                    var83 = 0.001828442
        else:
            var83 = -0.13303511
    else:
        if input[2] < 180.09999:
            var83 = 0.073424496
        else:
            var83 = 0.019942902
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 234.5:
                    var84 = -0.0111729195
                else:
                    var84 = 0.04871212
            else:
                if input[2] < 213.20001:
                    var84 = -0.1482091
                else:
                    var84 = 0.004112753
        else:
            if input[2] < 180.09999:
                var84 = 0.071774736
            else:
                var84 = 0.018671392
    else:
        if input[3] < 295.9:
            if input[2] < 64.59999:
                if input[2] < 56.500004:
                    var84 = -0.0037795564
                else:
                    var84 = 0.0762768
            else:
                var84 = -0.11419194
        else:
            var84 = 0.079545364
    if input[2] < 5.8999996:
        var85 = -0.0752339
    else:
        if input[2] < 7.8999996:
            var85 = 0.069509566
        else:
            if input[3] < 39.5:
                var85 = -0.096590936
            else:
                if input[3] < 41.0:
                    var85 = 0.07432931
                else:
                    var85 = -0.0030755068
    if input[3] < 405.5:
        if input[3] < 367.3:
            if input[0] < 9.6:
                if input[2] < 58.300003:
                    var86 = -0.09674754
                else:
                    var86 = 0.076525345
            else:
                if input[2] < 46.3:
                    var86 = 0.020432768
                else:
                    var86 = -0.020953624
        else:
            var86 = -0.12416973
    else:
        if input[0] < 54.7:
            var86 = 0.015544347
        else:
            var86 = 0.071468756
    if input[3] < 182.9:
        if input[2] < 64.59999:
            if input[2] < 58.300003:
                if input[3] < 85.2:
                    var87 = 0.015172272
                else:
                    var87 = -0.1551619
            else:
                if input[0] < 9.6:
                    var87 = 0.0915577
                else:
                    var87 = 0.016325912
        else:
            var87 = -0.12835525
    else:
        if input[0] < 28.199999:
            if input[2] < 118.90001:
                var87 = -0.14192097
            else:
                if input[2] < 195.00002:
                    var87 = 0.04362896
                else:
                    var87 = -0.16173223
        else:
            if input[2] < 98.100006:
                if input[3] < 244.70001:
                    var87 = 0.075976476
                else:
                    var87 = -0.067480035
            else:
                if input[3] < 264.8:
                    var87 = -0.14170644
                else:
                    var87 = 0.033959057
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 234.5:
                    var88 = -0.011357203
                else:
                    var88 = 0.047282424
            else:
                if input[0] < 28.999998:
                    var88 = -0.011422358
                else:
                    var88 = -0.17504615
        else:
            if input[2] < 180.09999:
                var88 = 0.06889018
            else:
                var88 = 0.013488191
    else:
        if input[3] < 295.9:
            if input[3] < 108.00001:
                if input[3] < 105.4:
                    var88 = -0.02286101
                else:
                    var88 = 0.07482415
            else:
                var88 = -0.060682606
        else:
            var88 = 0.07787395
    if input[0] < 84.3:
        if input[3] < 405.5:
            if input[3] < 272.5:
                if input[3] < 234.5:
                    var89 = -0.010202247
                else:
                    var89 = 0.04413667
            else:
                if input[0] < 28.999998:
                    var89 = -0.01036806
                else:
                    var89 = -0.17119558
        else:
            if input[0] < 54.7:
                var89 = 0.01002052
            else:
                var89 = 0.06877147
    else:
        if input[3] < 295.9:
            if input[3] < 108.00001:
                if input[3] < 105.4:
                    var89 = -0.02141656
                else:
                    var89 = 0.073206045
            else:
                var89 = -0.055546045
        else:
            var89 = 0.07636942
    if input[2] < 5.8999996:
        var90 = -0.07239125
    else:
        if input[2] < 7.8999996:
            var90 = 0.06757783
        else:
            if input[3] < 39.5:
                var90 = -0.09377579
            else:
                if input[3] < 41.0:
                    var90 = 0.071483724
                else:
                    var90 = -0.0030653428
    if input[2] < 40.699997:
        if input[3] < 41.0:
            if input[0] < 10.500003:
                var91 = -0.069313824
            else:
                if input[3] < 37.6:
                    var91 = -0.000021846485
                else:
                    var91 = 0.07955503
        else:
            var91 = -0.10084404
    else:
        if input[2] < 46.3:
            if input[0] < 16.099998:
                var91 = -0.09630041
            else:
                if input[0] < 24.800001:
                    var91 = 0.095689386
                else:
                    var91 = -0.043476455
        else:
            if input[3] < 105.4:
                var91 = -0.14414561
            else:
                if input[0] < 9.6:
                    var91 = 0.062464964
                else:
                    var91 = -0.00202886
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[2] < 118.90001:
                    var92 = -0.024278127
                else:
                    var92 = 0.025619585
            else:
                var92 = 0.06829379
        else:
            if input[1] < 24.0:
                var92 = 0.01637716
            else:
                var92 = -0.11362326
    else:
        if input[2] < 75.600006:
            if input[3] < 123.6:
                if input[2] < 56.500004:
                    var92 = -0.07643766
                else:
                    var92 = 0.036670443
            else:
                var92 = 0.08977053
        else:
            if input[0] < 84.3:
                if input[2] < 237.70001:
                    var92 = -0.17501698
                else:
                    var92 = 0.06729412
            else:
                var92 = 0.04312749
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[3] < 85.2:
                    var93 = 0.021728193
                else:
                    var93 = -0.025972456
            else:
                var93 = 0.065268196
        else:
            if input[1] < 24.0:
                var93 = 0.015310071
            else:
                var93 = -0.11014036
    else:
        if input[2] < 75.600006:
            if input[3] < 123.6:
                if input[2] < 56.500004:
                    var93 = -0.07087459
                else:
                    var93 = 0.03481732
            else:
                var93 = 0.08856584
        else:
            if input[2] < 237.70001:
                if input[0] < 84.3:
                    var93 = -0.16980325
                else:
                    var93 = 0.040786814
            else:
                var93 = 0.06570917
    if input[2] < 163.59999:
        if input[3] < 252.4:
            if input[3] < 244.70001:
                if input[2] < 98.100006:
                    var94 = 0.0065654027
                else:
                    var94 = -0.15048721
            else:
                var94 = 0.08100287
        else:
            if input[0] < 84.3:
                var94 = -0.12088957
            else:
                var94 = 0.0250134
    else:
        if input[0] < 58.200005:
            if input[0] < 25.900002:
                if input[1] < 22.0:
                    var94 = 0.06936261
                else:
                    var94 = -0.16772303
            else:
                if input[0] < 36.600002:
                    var94 = 0.08596006
                else:
                    var94 = 0.0073012
        else:
            var94 = -0.06652208
    if input[1] < 20.0:
        if input[0] < 27.499996:
            var95 = -0.09074532
        else:
            var95 = 0.039123934
    else:
        if input[0] < 9.6:
            if input[2] < 58.300003:
                var95 = -0.082921736
            else:
                if input[2] < 60.200005:
                    var95 = 0.090646885
                else:
                    var95 = 0.010902062
        else:
            if input[2] < 46.3:
                if input[0] < 24.800001:
                    var95 = 0.044592813
                else:
                    var95 = -0.058731753
            else:
                if input[3] < 182.9:
                    var95 = -0.098075435
                else:
                    var95 = 0.008333049
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[2] < 118.90001:
                    var96 = -0.023468668
                else:
                    var96 = 0.02396211
            else:
                var96 = 0.063432455
        else:
            if input[1] < 24.0:
                var96 = 0.01402299
            else:
                var96 = -0.10499834
    else:
        if input[2] < 75.600006:
            if input[3] < 123.6:
                if input[2] < 56.500004:
                    var96 = -0.06119432
                else:
                    var96 = 0.03767047
            else:
                var96 = 0.08727736
        else:
            if input[0] < 84.3:
                if input[2] < 237.70001:
                    var96 = -0.16384925
                else:
                    var96 = 0.06376328
            else:
                if input[3] < 313.40002:
                    var96 = 0.015447783
                else:
                    var96 = 0.054622915
    if input[0] < 54.7:
        if input[0] < 32.899998:
            if input[0] < 31.8:
                if input[3] < 85.2:
                    var97 = 0.020249834
                else:
                    var97 = -0.025704209
            else:
                var97 = 0.06040181
        else:
            if input[1] < 24.0:
                var97 = 0.013124895
            else:
                var97 = -0.1019239
    else:
        if input[2] < 75.600006:
            if input[3] < 123.6:
                if input[2] < 56.500004:
                    var97 = -0.056657474
                else:
                    var97 = 0.035782043
            else:
                var97 = 0.086013705
        else:
            if input[0] < 84.3:
                if input[2] < 237.70001:
                    var97 = -0.15904148
                else:
                    var97 = 0.062217113
            else:
                if input[3] < 313.40002:
                    var97 = 0.014490555
                else:
                    var97 = 0.05324465
    if input[2] < 5.8999996:
        var98 = -0.06806742
    else:
        if input[2] < 7.8999996:
            var98 = 0.06781773
        else:
            if input[3] < 39.5:
                var98 = -0.0911342
            else:
                if input[3] < 41.0:
                    var98 = 0.06633517
                else:
                    var98 = -0.0028884297
    if input[2] < 40.699997:
        if input[3] < 41.0:
            if input[0] < 10.500003:
                var99 = -0.065141864
            else:
                if input[3] < 37.6:
                    var99 = 0.0016091854
                else:
                    var99 = 0.07498391
        else:
            var99 = -0.09757595
    else:
        if input[2] < 46.3:
            if input[0] < 16.099998:
                var99 = -0.08936124
            else:
                if input[0] < 24.800001:
                    var99 = 0.09385622
                else:
                    var99 = -0.045683067
        else:
            if input[3] < 105.4:
                var99 = -0.12979381
            else:
                if input[0] < 9.6:
                    var99 = 0.060477614
                else:
                    var99 = -0.0031055855
    if input[0] < 84.3:
        if input[2] < 40.699997:
            if input[2] < 25.7:
                if input[2] < 24.899998:
                    var100 = -0.03203715
                else:
                    var100 = 0.07366806
            else:
                var100 = -0.098796204
        else:
            if input[2] < 46.3:
                if input[0] < 16.099998:
                    var100 = -0.08590971
                else:
                    var100 = 0.07494808
            else:
                if input[3] < 128.5:
                    var100 = -0.12361522
                else:
                    var100 = 0.0054589543
    else:
        if input[3] < 295.9:
            if input[3] < 108.00001:
                if input[3] < 105.4:
                    var100 = 0.0005801304
                else:
                    var100 = 0.07064024
            else:
                var100 = -0.06425802
        else:
            var100 = 0.072149865
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]


# --- Konkan Base 1: Random Forest ---
# Input: [Rainfall_mm, Rainfall_3day, Rainfall_7day, Month]
def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score_konkan_rf(input):
    if input[1] <= 119.39999771118164:
        if input[0] <= 44.5:
            if input[2] <= 67.6500015258789:
                var0 = [0.8636363636363636, 0.13636363636363635]
            else:
                var0 = [1.0, 0.0]
        else:
            if input[0] <= 47.25:
                var0 = [0.0, 1.0]
            else:
                var0 = [1.0, 0.0]
    else:
        if input[1] <= 179.39999389648438:
            if input[2] <= 250.70000457763672:
                var0 = [0.2345679012345679, 0.7654320987654321]
            else:
                var0 = [1.0, 0.0]
        else:
            if input[0] <= 67.10000228881836:
                var0 = [1.0, 0.0]
            else:
                var0 = [0.08536585365853659, 0.9146341463414634]
    if input[2] <= 248.5:
        if input[2] <= 66.60000228881836:
            var1 = [1.0, 0.0]
        else:
            if input[0] <= 45.69999885559082:
                var1 = [0.825136612021858, 0.17486338797814208]
            else:
                var1 = [0.26865671641791045, 0.7313432835820896]
    else:
        if input[2] <= 519.4999847412109:
            if input[0] <= 48.70000076293945:
                var1 = [1.0, 0.0]
            else:
                var1 = [0.17475728155339806, 0.8252427184466019]
        else:
            if input[0] <= 72.45000076293945:
                var1 = [1.0, 0.0]
            else:
                var1 = [0.03125, 0.96875]
    if input[0] <= 35.5:
        if input[3] <= 6.5:
            if input[1] <= 25.550000190734863:
                var2 = [1.0, 0.0]
            else:
                var2 = [0.5111111111111111, 0.4888888888888889]
        else:
            var2 = [1.0, 0.0]
    else:
        if input[1] <= 180.79999542236328:
            if input[0] <= 50.35000038146973:
                var2 = [0.23478260869565218, 0.7652173913043478]
            else:
                var2 = [0.6666666666666666, 0.3333333333333333]
        else:
            if input[2] <= 396.40000915527344:
                var2 = [0.02631578947368421, 0.9736842105263158]
            else:
                var2 = [0.1510791366906475, 0.8489208633093526]
    if input[1] <= 119.25:
        if input[0] <= 45.69999885559082:
            if input[2] <= 67.6500015258789:
                var3 = [0.84375, 0.15625]
            else:
                var3 = [1.0, 0.0]
        else:
            if input[2] <= 186.95000457763672:
                var3 = [0.15384615384615385, 0.8461538461538461]
            else:
                var3 = [1.0, 0.0]
    else:
        if input[0] <= 67.30000305175781:
            if input[1] <= 148.4499969482422:
                var3 = [0.37735849056603776, 0.6226415094339622]
            else:
                var3 = [1.0, 0.0]
        else:
            if input[2] <= 166.5:
                var3 = [1.0, 0.0]
            else:
                var3 = [0.06934306569343066, 0.9306569343065694]
    if input[1] <= 119.39999771118164:
        if input[1] <= 58.79999923706055:
            if input[1] <= 25.199999809265137:
                var4 = [1.0, 0.0]
            else:
                var4 = [0.8348623853211009, 0.1651376146788991]
        else:
            if input[2] <= 138.5500030517578:
                var4 = [0.30666666666666664, 0.6933333333333334]
            else:
                var4 = [1.0, 0.0]
    else:
        if input[0] <= 86.94999694824219:
            if input[1] <= 136.25:
                var4 = [1.0, 0.0]
            else:
                var4 = [0.33064516129032256, 0.6693548387096774]
        else:
            if input[1] <= 198.8499984741211:
                var4 = [0.0, 1.0]
            else:
                var4 = [0.05084745762711865, 0.9491525423728814]
    if input[2] <= 278.75:
        if input[0] <= 35.35000038146973:
            if input[0] <= 11.150000095367432:
                var5 = [1.0, 0.0]
            else:
                var5 = [0.8130841121495327, 0.18691588785046728]
        else:
            if input[0] <= 36.650001525878906:
                var5 = [0.0, 1.0]
            else:
                var5 = [0.35514018691588783, 0.6448598130841121]
    else:
        if input[1] <= 179.14999389648438:
            var5 = [1.0, 0.0]
        else:
            if input[1] <= 246.04999542236328:
                var5 = [0.2206896551724138, 0.7793103448275862]
            else:
                var5 = [0.04878048780487805, 0.9512195121951219]
    if input[0] <= 45.39999961853027:
        if input[0] <= 35.650001525878906:
            if input[3] <= 6.5:
                var6 = [0.8295454545454546, 0.17045454545454544]
            else:
                var6 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var6 = [1.0, 0.0]
            else:
                var6 = [0.32, 0.68]
    else:
        if input[1] <= 180.6999969482422:
            if input[1] <= 137.6999969482422:
                var6 = [0.19540229885057472, 0.8045977011494253]
            else:
                var6 = [1.0, 0.0]
        else:
            if input[2] <= 245.34999084472656:
                var6 = [1.0, 0.0]
            else:
                var6 = [0.08239700374531835, 0.9176029962546817]
    if input[0] <= 35.650001525878906:
        if input[3] <= 6.5:
            if input[0] <= 11.150000095367432:
                var7 = [1.0, 0.0]
            else:
                var7 = [0.55, 0.45]
        else:
            var7 = [1.0, 0.0]
    else:
        if input[1] <= 180.6999969482422:
            if input[2] <= 249.9000015258789:
                var7 = [0.2773722627737226, 0.7226277372262774]
            else:
                var7 = [1.0, 0.0]
        else:
            if input[2] <= 274.34999084472656:
                var7 = [1.0, 0.0]
            else:
                var7 = [0.09689922480620156, 0.9031007751937985]
    if input[0] <= 35.60000038146973:
        if input[2] <= 67.9000015258789:
            if input[1] <= 25.5:
                var8 = [1.0, 0.0]
            else:
                var8 = [0.46808510638297873, 0.5319148936170213]
        else:
            var8 = [1.0, 0.0]
    else:
        if input[1] <= 336.5500030517578:
            if input[1] <= 263.5:
                var8 = [0.22569444444444445, 0.7743055555555556]
            else:
                var8 = [0.05555555555555555, 0.9444444444444444]
        else:
            var8 = [1.0, 0.0]
    if input[1] <= 136.6999969482422:
        if input[1] <= 58.94999885559082:
            if input[0] <= 11.150000095367432:
                var9 = [1.0, 0.0]
            else:
                var9 = [0.8227848101265823, 0.17721518987341772]
        else:
            if input[0] <= 45.44999885559082:
                var9 = [1.0, 0.0]
            else:
                var9 = [0.2571428571428571, 0.7428571428571429]
    else:
        if input[1] <= 336.5500030517578:
            if input[1] <= 246.04999542236328:
                var9 = [0.25136612021857924, 0.7486338797814208]
            else:
                var9 = [0.07407407407407407, 0.9259259259259259]
        else:
            var9 = [1.0, 0.0]
    if input[0] <= 45.69999885559082:
        if input[2] <= 65.4000015258789:
            var10 = [1.0, 0.0]
        else:
            if input[1] <= 147.04999542236328:
                var10 = [0.8647342995169082, 0.13526570048309178]
            else:
                var10 = [0.36666666666666664, 0.6333333333333333]
    else:
        if input[1] <= 176.25:
            if input[2] <= 271.5999984741211:
                var10 = [0.19318181818181818, 0.8068181818181818]
            else:
                var10 = [1.0, 0.0]
        else:
            if input[0] <= 67.10000228881836:
                var10 = [1.0, 0.0]
            else:
                var10 = [0.06072874493927125, 0.9392712550607287]
    if input[1] <= 136.25:
        if input[0] <= 44.89999961853027:
            if input[3] <= 6.5:
                var11 = [0.7954545454545454, 0.20454545454545456]
            else:
                var11 = [1.0, 0.0]
        else:
            if input[0] <= 46.95000076293945:
                var11 = [0.027777777777777776, 0.9722222222222222]
            else:
                var11 = [0.65, 0.35]
    else:
        if input[0] <= 91.4000015258789:
            if input[2] <= 258.3499984741211:
                var11 = [0.18, 0.82]
            else:
                var11 = [0.4875, 0.5125]
        else:
            if input[1] <= 336.5500030517578:
                var11 = [0.033816425120772944, 0.966183574879227]
            else:
                var11 = [1.0, 0.0]
    if input[0] <= 45.44999885559082:
        if input[1] <= 146.6999969482422:
            if input[2] <= 67.0:
                var12 = [0.7346938775510204, 0.2653061224489796]
            else:
                var12 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var12 = [1.0, 0.0]
            else:
                var12 = [0.0, 1.0]
    else:
        if input[1] <= 179.39999389648438:
            if input[0] <= 50.54999923706055:
                var12 = [0.05714285714285714, 0.9428571428571428]
            else:
                var12 = [0.6153846153846154, 0.38461538461538464]
        else:
            if input[2] <= 274.34999084472656:
                var12 = [1.0, 0.0]
            else:
                var12 = [0.08627450980392157, 0.9137254901960784]
    if input[0] <= 45.39999961853027:
        if input[1] <= 147.04999542236328:
            if input[2] <= 67.0:
                var13 = [0.7818181818181819, 0.21818181818181817]
            else:
                var13 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var13 = [1.0, 0.0]
            else:
                var13 = [0.06666666666666667, 0.9333333333333333]
    else:
        if input[0] <= 87.75:
            if input[0] <= 50.45000076293945:
                var13 = [0.14814814814814814, 0.8518518518518519]
            else:
                var13 = [0.6075949367088608, 0.3924050632911392]
        else:
            if input[2] <= 433.04998779296875:
                var13 = [0.051470588235294115, 0.9485294117647058]
            else:
                var13 = [0.0, 1.0]
    if input[2] <= 277.5:
        if input[0] <= 35.10000038146973:
            if input[3] <= 6.5:
                var14 = [0.7560975609756098, 0.24390243902439024]
            else:
                var14 = [1.0, 0.0]
        else:
            if input[0] <= 46.95000076293945:
                var14 = [0.11764705882352941, 0.8823529411764706]
            else:
                var14 = [0.42105263157894735, 0.5789473684210527]
    else:
        if input[2] <= 528.1499938964844:
            if input[1] <= 180.79999542236328:
                var14 = [1.0, 0.0]
            else:
                var14 = [0.15555555555555556, 0.8444444444444444]
        else:
            if input[0] <= 72.45000076293945:
                var14 = [1.0, 0.0]
            else:
                var14 = [0.06451612903225806, 0.9354838709677419]
    if input[1] <= 119.39999771118164:
        if input[0] <= 45.44999885559082:
            if input[1] <= 25.65000057220459:
                var15 = [0.8782608695652174, 0.12173913043478261]
            else:
                var15 = [1.0, 0.0]
        else:
            if input[2] <= 163.6500015258789:
                var15 = [0.18181818181818182, 0.8181818181818182]
            else:
                var15 = [1.0, 0.0]
    else:
        if input[2] <= 565.1000061035156:
            if input[0] <= 86.69999694824219:
                var15 = [0.48717948717948717, 0.5128205128205128]
            else:
                var15 = [0.046296296296296294, 0.9537037037037037]
        else:
            if input[2] <= 654.3500061035156:
                var15 = [1.0, 0.0]
            else:
                var15 = [0.2, 0.8]
    if input[0] <= 45.69999885559082:
        if input[0] <= 35.5:
            if input[1] <= 25.65000057220459:
                var16 = [0.8695652173913043, 0.13043478260869565]
            else:
                var16 = [1.0, 0.0]
        else:
            if input[0] <= 36.400001525878906:
                var16 = [0.0, 1.0]
            else:
                var16 = [1.0, 0.0]
    else:
        if input[1] <= 336.5500030517578:
            if input[2] <= 683.3999938964844:
                var16 = [0.1585014409221902, 0.8414985590778098]
            else:
                var16 = [1.0, 0.0]
        else:
            var16 = [1.0, 0.0]
    if input[1] <= 180.79999542236328:
        if input[2] <= 66.45000076293945:
            var17 = [1.0, 0.0]
        else:
            if input[2] <= 67.0:
                var17 = [0.0, 1.0]
            else:
                var17 = [0.722972972972973, 0.27702702702702703]
    else:
        if input[0] <= 65.75000190734863:
            var17 = [1.0, 0.0]
        else:
            if input[1] <= 339.8500061035156:
                var17 = [0.06792452830188679, 0.9320754716981132]
            else:
                var17 = [1.0, 0.0]
    if input[0] <= 45.69999885559082:
        if input[0] <= 35.35000038146973:
            if input[2] <= 67.5:
                var18 = [0.8198198198198198, 0.18018018018018017]
            else:
                var18 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var18 = [1.0, 0.0]
            else:
                var18 = [0.22727272727272727, 0.7727272727272727]
    else:
        if input[0] <= 87.0999984741211:
            if input[1] <= 81.79999923706055:
                var18 = [0.025, 0.975]
            else:
                var18 = [0.48214285714285715, 0.5178571428571429]
        else:
            if input[2] <= 683.3999938964844:
                var18 = [0.03167420814479638, 0.9683257918552036]
            else:
                var18 = [1.0, 0.0]
    if input[0] <= 45.39999961853027:
        if input[0] <= 35.60000038146973:
            if input[1] <= 25.65000057220459:
                var19 = [0.8666666666666667, 0.13333333333333333]
            else:
                var19 = [1.0, 0.0]
        else:
            if input[2] <= 211.8499984741211:
                var19 = [0.3076923076923077, 0.6923076923076923]
            else:
                var19 = [1.0, 0.0]
    else:
        if input[1] <= 338.0500030517578:
            if input[2] <= 99.54999923706055:
                var19 = [1.0, 0.0]
            else:
                var19 = [0.13066666666666665, 0.8693333333333333]
        else:
            var19 = [1.0, 0.0]
    if input[1] <= 119.39999771118164:
        if input[0] <= 44.89999961853027:
            if input[2] <= 67.0:
                var20 = [0.7596153846153846, 0.2403846153846154]
            else:
                var20 = [1.0, 0.0]
        else:
            if input[2] <= 164.8000030517578:
                var20 = [0.09375, 0.90625]
            else:
                var20 = [1.0, 0.0]
    else:
        if input[1] <= 180.5999984741211:
            if input[1] <= 149.64999389648438:
                var20 = [0.21875, 0.78125]
            else:
                var20 = [1.0, 0.0]
        else:
            if input[0] <= 90.75:
                var20 = [0.45454545454545453, 0.5454545454545454]
            else:
                var20 = [0.0380952380952381, 0.9619047619047619]
    if input[2] <= 248.5:
        if input[1] <= 58.94999885559082:
            if input[3] <= 6.5:
                var21 = [0.8852459016393442, 0.11475409836065574]
            else:
                var21 = [1.0, 0.0]
        else:
            if input[2] <= 201.54999542236328:
                var21 = [0.5037037037037037, 0.4962962962962963]
            else:
                var21 = [1.0, 0.0]
    else:
        if input[2] <= 527.0499877929688:
            if input[2] <= 448.0:
                var21 = [0.291866028708134, 0.7081339712918661]
            else:
                var21 = [1.0, 0.0]
        else:
            if input[0] <= 72.35000228881836:
                var21 = [1.0, 0.0]
            else:
                var21 = [0.0625, 0.9375]
    if input[1] <= 119.39999771118164:
        if input[2] <= 137.75:
            if input[0] <= 44.69999885559082:
                var22 = [0.8861386138613861, 0.11386138613861387]
            else:
                var22 = [0.10344827586206896, 0.896551724137931]
        else:
            var22 = [1.0, 0.0]
    else:
        if input[1] <= 207.5500030517578:
            if input[0] <= 89.14999771118164:
                var22 = [0.5555555555555556, 0.4444444444444444]
            else:
                var22 = [0.09859154929577464, 0.9014084507042254]
        else:
            if input[0] <= 67.10000228881836:
                var22 = [1.0, 0.0]
            else:
                var22 = [0.08928571428571429, 0.9107142857142857]
    if input[1] <= 119.04999923706055:
        if input[0] <= 45.69999885559082:
            if input[3] <= 6.5:
                var23 = [0.7325581395348837, 0.26744186046511625]
            else:
                var23 = [1.0, 0.0]
        else:
            if input[2] <= 101.5999984741211:
                var23 = [1.0, 0.0]
            else:
                var23 = [0.16216216216216217, 0.8378378378378378]
    else:
        if input[1] <= 265.90000915527344:
            if input[0] <= 89.14999771118164:
                var23 = [0.6160714285714286, 0.38392857142857145]
            else:
                var23 = [0.016666666666666666, 0.9833333333333333]
        else:
            if input[0] <= 58.10000038146973:
                var23 = [1.0, 0.0]
            else:
                var23 = [0.042735042735042736, 0.9572649572649573]
    if input[1] <= 147.0999984741211:
        if input[1] <= 58.94999885559082:
            if input[0] <= 11.150000095367432:
                var24 = [1.0, 0.0]
            else:
                var24 = [0.7831325301204819, 0.21686746987951808]
        else:
            if input[0] <= 45.69999885559082:
                var24 = [1.0, 0.0]
            else:
                var24 = [0.32558139534883723, 0.6744186046511628]
    else:
        if input[0] <= 67.45000076293945:
            if input[3] <= 8.5:
                var24 = [1.0, 0.0]
            else:
                var24 = [0.08333333333333333, 0.9166666666666666]
        else:
            if input[1] <= 180.6999969482422:
                var24 = [1.0, 0.0]
            else:
                var24 = [0.03614457831325301, 0.963855421686747]
    if input[0] <= 45.44999885559082:
        if input[0] <= 35.650001525878906:
            if input[2] <= 67.5:
                var25 = [0.8556701030927835, 0.14432989690721648]
            else:
                var25 = [1.0, 0.0]
        else:
            if input[1] <= 146.89999389648438:
                var25 = [1.0, 0.0]
            else:
                var25 = [0.25925925925925924, 0.7407407407407407]
    else:
        if input[0] <= 89.04999923706055:
            if input[0] <= 50.35000038146973:
                var25 = [0.08064516129032258, 0.9193548387096774]
            else:
                var25 = [0.5333333333333333, 0.4666666666666667]
        else:
            if input[0] <= 144.9000015258789:
                var25 = [0.013888888888888888, 0.9861111111111112]
            else:
                var25 = [1.0, 0.0]
    if input[1] <= 119.25:
        if input[0] <= 45.44999885559082:
            if input[2] <= 67.0:
                var26 = [0.831858407079646, 0.168141592920354]
            else:
                var26 = [1.0, 0.0]
        else:
            if input[2] <= 163.6500015258789:
                var26 = [0.15789473684210525, 0.8421052631578947]
            else:
                var26 = [1.0, 0.0]
    else:
        if input[0] <= 87.75:
            if input[1] <= 136.0999984741211:
                var26 = [1.0, 0.0]
            else:
                var26 = [0.38181818181818183, 0.6181818181818182]
        else:
            if input[1] <= 212.6500015258789:
                var26 = [0.0, 1.0]
            else:
                var26 = [0.033707865168539325, 0.9662921348314607]
    if input[2] <= 248.25:
        if input[0] <= 35.5:
            if input[3] <= 6.5:
                var27 = [0.7682926829268293, 0.23170731707317074]
            else:
                var27 = [1.0, 0.0]
        else:
            if input[2] <= 104.29999923706055:
                var27 = [1.0, 0.0]
            else:
                var27 = [0.26851851851851855, 0.7314814814814815]
    else:
        if input[0] <= 49.89999961853027:
            var27 = [1.0, 0.0]
        else:
            if input[1] <= 136.6999969482422:
                var27 = [1.0, 0.0]
            else:
                var27 = [0.11940298507462686, 0.8805970149253731]
    if input[0] <= 35.60000038146973:
        if input[3] <= 6.5:
            if input[0] <= 11.150000095367432:
                var28 = [1.0, 0.0]
            else:
                var28 = [0.5, 0.5]
        else:
            var28 = [1.0, 0.0]
    else:
        if input[0] <= 89.04999923706055:
            if input[0] <= 76.45000076293945:
                var28 = [0.3404255319148936, 0.6595744680851063]
            else:
                var28 = [1.0, 0.0]
        else:
            if input[0] <= 109.10000228881836:
                var28 = [0.0, 1.0]
            else:
                var28 = [0.05263157894736842, 0.9473684210526315]
    if input[0] <= 35.5:
        if input[2] <= 67.0:
            if input[0] <= 10.799999713897705:
                var29 = [1.0, 0.0]
            else:
                var29 = [0.4722222222222222, 0.5277777777777778]
        else:
            var29 = [1.0, 0.0]
    else:
        if input[1] <= 180.6999969482422:
            if input[2] <= 249.9000015258789:
                var29 = [0.26356589147286824, 0.7364341085271318]
            else:
                var29 = [1.0, 0.0]
        else:
            if input[1] <= 336.5500030517578:
                var29 = [0.12109375, 0.87890625]
            else:
                var29 = [1.0, 0.0]
    if input[0] <= 45.44999885559082:
        if input[0] <= 11.150000095367432:
            var30 = [1.0, 0.0]
        else:
            if input[0] <= 11.25:
                var30 = [0.08333333333333333, 0.9166666666666666]
            else:
                var30 = [0.9113924050632911, 0.08860759493670886]
    else:
        if input[0] <= 87.0999984741211:
            if input[2] <= 163.60000610351562:
                var30 = [0.09433962264150944, 0.9056603773584906]
            else:
                var30 = [0.504950495049505, 0.49504950495049505]
        else:
            if input[2] <= 683.3999938964844:
                var30 = [0.03686635944700461, 0.9631336405529954]
            else:
                var30 = [1.0, 0.0]
    if input[1] <= 119.39999771118164:
        if input[1] <= 58.44999885559082:
            if input[0] <= 11.150000095367432:
                var31 = [1.0, 0.0]
            else:
                var31 = [0.8169014084507042, 0.18309859154929578]
        else:
            if input[1] <= 77.75:
                var31 = [0.49295774647887325, 0.5070422535211268]
            else:
                var31 = [1.0, 0.0]
    else:
        if input[2] <= 519.3999938964844:
            if input[2] <= 454.54998779296875:
                var31 = [0.200836820083682, 0.799163179916318]
            else:
                var31 = [1.0, 0.0]
        else:
            if input[0] <= 64.95000076293945:
                var31 = [1.0, 0.0]
            else:
                var31 = [0.021505376344086023, 0.978494623655914]
    if input[0] <= 45.39999961853027:
        if input[0] <= 35.650001525878906:
            if input[2] <= 68.85000228881836:
                var32 = [0.8141592920353983, 0.18584070796460178]
            else:
                var32 = [1.0, 0.0]
        else:
            if input[1] <= 146.89999389648438:
                var32 = [1.0, 0.0]
            else:
                var32 = [0.15384615384615385, 0.8461538461538461]
    else:
        if input[2] <= 526.7999877929688:
            if input[0] <= 87.29999923706055:
                var32 = [0.45614035087719296, 0.543859649122807]
            else:
                var32 = [0.012578616352201259, 0.9874213836477987]
        else:
            if input[0] <= 69.70000076293945:
                var32 = [1.0, 0.0]
            else:
                var32 = [0.0, 1.0]
    if input[0] <= 45.44999885559082:
        if input[2] <= 200.4499969482422:
            if input[3] <= 6.5:
                var33 = [0.8108108108108109, 0.1891891891891892]
            else:
                var33 = [1.0, 0.0]
        else:
            if input[1] <= 142.5999984741211:
                var33 = [1.0, 0.0]
            else:
                var33 = [0.2857142857142857, 0.7142857142857143]
    else:
        if input[1] <= 179.39999389648438:
            if input[1] <= 137.6999969482422:
                var33 = [0.21686746987951808, 0.7831325301204819]
            else:
                var33 = [1.0, 0.0]
        else:
            if input[0] <= 67.10000228881836:
                var33 = [1.0, 0.0]
            else:
                var33 = [0.043824701195219126, 0.9561752988047809]
    if input[1] <= 119.04999923706055:
        if input[0] <= 45.44999885559082:
            if input[3] <= 6.5:
                var34 = [0.8271604938271605, 0.1728395061728395]
            else:
                var34 = [1.0, 0.0]
        else:
            if input[1] <= 79.79999923706055:
                var34 = [0.03125, 0.96875]
            else:
                var34 = [1.0, 0.0]
    else:
        if input[1] <= 245.5:
            if input[0] <= 89.14999771118164:
                var34 = [0.4462809917355372, 0.5537190082644629]
            else:
                var34 = [0.018867924528301886, 0.9811320754716981]
        else:
            if input[1] <= 337.8000030517578:
                var34 = [0.038461538461538464, 0.9615384615384616]
            else:
                var34 = [1.0, 0.0]
    if input[1] <= 119.39999771118164:
        if input[2] <= 137.8000030517578:
            if input[1] <= 58.79999923706055:
                var35 = [0.8888888888888888, 0.1111111111111111]
            else:
                var35 = [0.39285714285714285, 0.6071428571428571]
        else:
            var35 = [1.0, 0.0]
    else:
        if input[1] <= 180.6999969482422:
            if input[1] <= 148.4499969482422:
                var35 = [0.3157894736842105, 0.6842105263157895]
            else:
                var35 = [1.0, 0.0]
        else:
            if input[0] <= 67.10000228881836:
                var35 = [1.0, 0.0]
            else:
                var35 = [0.07380073800738007, 0.9261992619926199]
    if input[0] <= 35.60000038146973:
        if input[2] <= 67.0:
            if input[0] <= 10.650000095367432:
                var36 = [1.0, 0.0]
            else:
                var36 = [0.6206896551724138, 0.3793103448275862]
        else:
            var36 = [1.0, 0.0]
    else:
        if input[1] <= 180.79999542236328:
            if input[1] <= 151.64999389648438:
                var36 = [0.275, 0.725]
            else:
                var36 = [1.0, 0.0]
        else:
            if input[2] <= 265.8999938964844:
                var36 = [1.0, 0.0]
            else:
                var36 = [0.09701492537313433, 0.9029850746268657]
    if input[0] <= 45.69999885559082:
        if input[1] <= 146.6999969482422:
            if input[3] <= 6.5:
                var37 = [0.8, 0.2]
            else:
                var37 = [1.0, 0.0]
        else:
            if input[2] <= 259.4500045776367:
                var37 = [0.0, 1.0]
            else:
                var37 = [1.0, 0.0]
    else:
        if input[1] <= 176.14999389648438:
            if input[2] <= 181.20000457763672:
                var37 = [0.13114754098360656, 0.8688524590163934]
            else:
                var37 = [0.6511627906976745, 0.3488372093023256]
        else:
            if input[1] <= 259.3500061035156:
                var37 = [0.12751677852348994, 0.87248322147651]
            else:
                var37 = [0.031578947368421054, 0.968421052631579]
    if input[0] <= 45.69999885559082:
        if input[0] <= 35.5:
            if input[3] <= 6.5:
                var38 = [0.7849462365591398, 0.21505376344086022]
            else:
                var38 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var38 = [1.0, 0.0]
            else:
                var38 = [0.16666666666666666, 0.8333333333333334]
    else:
        if input[1] <= 338.0500030517578:
            if input[0] <= 91.4000015258789:
                var38 = [0.28378378378378377, 0.7162162162162162]
            else:
                var38 = [0.04878048780487805, 0.9512195121951219]
        else:
            var38 = [1.0, 0.0]
    if input[0] <= 35.10000038146973:
        if input[1] <= 25.850000381469727:
            if input[2] <= 63.150001525878906:
                var39 = [1.0, 0.0]
            else:
                var39 = [0.5714285714285714, 0.42857142857142855]
        else:
            var39 = [1.0, 0.0]
    else:
        if input[0] <= 87.75:
            if input[0] <= 50.75:
                var39 = [0.23958333333333334, 0.7604166666666666]
            else:
                var39 = [0.6506024096385542, 0.3493975903614458]
        else:
            if input[0] <= 145.25:
                var39 = [0.022935779816513763, 0.9770642201834863]
            else:
                var39 = [1.0, 0.0]
    if input[1] <= 136.6999969482422:
        if input[1] <= 58.94999885559082:
            if input[0] <= 10.799999713897705:
                var40 = [1.0, 0.0]
            else:
                var40 = [0.7051282051282052, 0.2948717948717949]
        else:
            if input[0] <= 45.69999885559082:
                var40 = [1.0, 0.0]
            else:
                var40 = [0.2236842105263158, 0.7763157894736842]
    else:
        if input[1] <= 180.79999542236328:
            if input[0] <= 51.95000076293945:
                var40 = [0.24, 0.76]
            else:
                var40 = [1.0, 0.0]
        else:
            if input[0] <= 67.10000228881836:
                var40 = [1.0, 0.0]
            else:
                var40 = [0.04819277108433735, 0.9518072289156626]
    if input[0] <= 45.69999885559082:
        if input[0] <= 35.60000038146973:
            if input[2] <= 67.70000076293945:
                var41 = [0.8380952380952381, 0.1619047619047619]
            else:
                var41 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var41 = [1.0, 0.0]
            else:
                var41 = [0.18181818181818182, 0.8181818181818182]
    else:
        if input[1] <= 336.5500030517578:
            if input[1] <= 179.39999389648438:
                var41 = [0.2967032967032967, 0.7032967032967034]
            else:
                var41 = [0.09608540925266904, 0.9039145907473309]
        else:
            var41 = [1.0, 0.0]
    if input[0] <= 35.60000038146973:
        if input[3] <= 6.5:
            if input[1] <= 25.949999809265137:
                var42 = [0.6842105263157895, 0.3157894736842105]
            else:
                var42 = [1.0, 0.0]
        else:
            var42 = [1.0, 0.0]
    else:
        if input[2] <= 102.64999771118164:
            var42 = [1.0, 0.0]
        else:
            if input[1] <= 180.5999984741211:
                var42 = [0.3333333333333333, 0.6666666666666666]
            else:
                var42 = [0.12075471698113208, 0.879245283018868]
    if input[0] <= 35.650001525878906:
        if input[2] <= 67.5:
            if input[2] <= 66.45000076293945:
                var43 = [1.0, 0.0]
            else:
                var43 = [0.0, 1.0]
        else:
            var43 = [1.0, 0.0]
    else:
        if input[0] <= 87.0999984741211:
            if input[1] <= 77.9000015258789:
                var43 = [0.13157894736842105, 0.868421052631579]
            else:
                var43 = [0.46153846153846156, 0.5384615384615384]
        else:
            if input[1] <= 193.1999969482422:
                var43 = [0.0, 1.0]
            else:
                var43 = [0.05357142857142857, 0.9464285714285714]
    if input[0] <= 45.69999885559082:
        if input[1] <= 147.04999542236328:
            if input[2] <= 67.0:
                var44 = [0.8648648648648649, 0.13513513513513514]
            else:
                var44 = [1.0, 0.0]
        else:
            if input[1] <= 153.54999542236328:
                var44 = [0.0, 1.0]
            else:
                var44 = [1.0, 0.0]
    else:
        if input[0] <= 89.14999771118164:
            if input[1] <= 79.5:
                var44 = [0.17647058823529413, 0.8235294117647058]
            else:
                var44 = [0.5053763440860215, 0.4946236559139785]
        else:
            if input[1] <= 339.8500061035156:
                var44 = [0.0211864406779661, 0.9788135593220338]
            else:
                var44 = [1.0, 0.0]
    if input[2] <= 137.45000457763672:
        if input[0] <= 44.60000038146973:
            if input[0] <= 10.949999809265137:
                var45 = [1.0, 0.0]
            else:
                var45 = [0.75, 0.25]
        else:
            if input[2] <= 106.89999771118164:
                var45 = [0.0, 1.0]
            else:
                var45 = [1.0, 0.0]
    else:
        if input[0] <= 35.05000114440918:
            var45 = [1.0, 0.0]
        else:
            if input[0] <= 89.04999923706055:
                var45 = [0.38953488372093026, 0.6104651162790697]
            else:
                var45 = [0.021739130434782608, 0.9782608695652174]
    var46 = add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), var4), var5), var6), var7), var8), var9), var10), var11), var12), var13), var14), var15), var16), var17), var18), var19), var20), var21), var22), var23), var24), var25), var26), var27), var28), var29), var30), var31), var32), var33), var34), var35), var36), var37), var38), var39), var40), var41), var42), var43), var44), var45)
    if input[2] <= 278.75:
        if input[1] <= 119.25:
            if input[1] <= 25.5:
                var47 = [1.0, 0.0]
            else:
                var47 = [0.7522935779816514, 0.24770642201834864]
        else:
            if input[1] <= 148.4499969482422:
                var47 = [0.2714285714285714, 0.7285714285714285]
            else:
                var47 = [1.0, 0.0]
    else:
        if input[1] <= 180.79999542236328:
            var47 = [1.0, 0.0]
        else:
            if input[2] <= 388.6999969482422:
                var47 = [0.043478260869565216, 0.9565217391304348]
            else:
                var47 = [0.1791044776119403, 0.8208955223880597]
    if input[0] <= 35.5:
        if input[3] <= 6.5:
            if input[0] <= 10.75:
                var48 = [1.0, 0.0]
            else:
                var48 = [0.46, 0.54]
        else:
            var48 = [1.0, 0.0]
    else:
        if input[0] <= 87.75:
            if input[1] <= 79.45000076293945:
                var48 = [0.09090909090909091, 0.9090909090909091]
            else:
                var48 = [0.48717948717948717, 0.5128205128205128]
        else:
            if input[1] <= 339.8500061035156:
                var48 = [0.03286384976525822, 0.9671361502347418]
            else:
                var48 = [1.0, 0.0]
    if input[0] <= 45.44999885559082:
        if input[1] <= 145.29999542236328:
            if input[2] <= 67.0:
                var49 = [0.8434782608695652, 0.1565217391304348]
            else:
                var49 = [1.0, 0.0]
        else:
            if input[2] <= 274.9500045776367:
                var49 = [0.1111111111111111, 0.8888888888888888]
            else:
                var49 = [1.0, 0.0]
    else:
        if input[0] <= 89.14999771118164:
            if input[1] <= 81.79999923706055:
                var49 = [0.02631578947368421, 0.9736842105263158]
            else:
                var49 = [0.550561797752809, 0.449438202247191]
        else:
            if input[2] <= 683.3999938964844:
                var49 = [0.043478260869565216, 0.9565217391304348]
            else:
                var49 = [1.0, 0.0]
    if input[0] <= 35.5:
        if input[3] <= 6.5:
            if input[0] <= 11.150000095367432:
                var50 = [1.0, 0.0]
            else:
                var50 = [0.6304347826086957, 0.3695652173913043]
        else:
            var50 = [1.0, 0.0]
    else:
        if input[1] <= 136.6999969482422:
            if input[0] <= 45.69999885559082:
                var50 = [1.0, 0.0]
            else:
                var50 = [0.2571428571428571, 0.7428571428571429]
        else:
            if input[0] <= 91.4000015258789:
                var50 = [0.3089430894308943, 0.6910569105691057]
            else:
                var50 = [0.04854368932038835, 0.9514563106796117]
    if input[0] <= 45.44999885559082:
        if input[1] <= 147.04999542236328:
            if input[3] <= 6.5:
                var51 = [0.8024691358024691, 0.19753086419753085]
            else:
                var51 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var51 = [1.0, 0.0]
            else:
                var51 = [0.0, 1.0]
    else:
        if input[0] <= 87.29999923706055:
            if input[0] <= 50.54999923706055:
                var51 = [0.078125, 0.921875]
            else:
                var51 = [0.4883720930232558, 0.5116279069767442]
        else:
            if input[0] <= 144.9000015258789:
                var51 = [0.02127659574468085, 0.9787234042553191]
            else:
                var51 = [1.0, 0.0]
    if input[0] <= 35.650001525878906:
        if input[2] <= 68.5:
            if input[2] <= 66.70000076293945:
                var52 = [1.0, 0.0]
            else:
                var52 = [0.0, 1.0]
        else:
            var52 = [1.0, 0.0]
    else:
        if input[0] <= 90.75:
            if input[2] <= 205.54999542236328:
                var52 = [0.12087912087912088, 0.8791208791208791]
            else:
                var52 = [0.4659090909090909, 0.5340909090909091]
        else:
            if input[1] <= 339.8500061035156:
                var52 = [0.0091324200913242, 0.9908675799086758]
            else:
                var52 = [1.0, 0.0]
    if input[1] <= 119.04999923706055:
        if input[3] <= 6.5:
            if input[2] <= 65.1500015258789:
                var53 = [1.0, 0.0]
            else:
                var53 = [0.4492753623188406, 0.5507246376811594]
        else:
            if input[0] <= 46.75:
                var53 = [1.0, 0.0]
            else:
                var53 = [0.28, 0.72]
    else:
        if input[2] <= 519.4999847412109:
            if input[0] <= 86.5999984741211:
                var53 = [0.5522388059701493, 0.44776119402985076]
            else:
                var53 = [0.007246376811594203, 0.9927536231884058]
        else:
            if input[1] <= 191.95000457763672:
                var53 = [1.0, 0.0]
            else:
                var53 = [0.07446808510638298, 0.925531914893617]
    if input[0] <= 45.44999885559082:
        if input[1] <= 146.6999969482422:
            if input[3] <= 6.5:
                var54 = [0.872093023255814, 0.12790697674418605]
            else:
                var54 = [1.0, 0.0]
        else:
            if input[1] <= 149.64999389648438:
                var54 = [0.0, 1.0]
            else:
                var54 = [1.0, 0.0]
    else:
        if input[1] <= 180.6999969482422:
            if input[1] <= 138.3499984741211:
                var54 = [0.23529411764705882, 0.7647058823529411]
            else:
                var54 = [1.0, 0.0]
        else:
            if input[0] <= 65.1500015258789:
                var54 = [1.0, 0.0]
            else:
                var54 = [0.072, 0.928]
    if input[0] <= 35.650001525878906:
        if input[3] <= 6.5:
            if input[2] <= 66.60000228881836:
                var55 = [1.0, 0.0]
            else:
                var55 = [0.5666666666666667, 0.43333333333333335]
        else:
            var55 = [1.0, 0.0]
    else:
        if input[2] <= 104.29999923706055:
            var55 = [1.0, 0.0]
        else:
            if input[0] <= 89.14999771118164:
                var55 = [0.3672316384180791, 0.632768361581921]
            else:
                var55 = [0.05106382978723404, 0.948936170212766]
    if input[1] <= 180.6999969482422:
        if input[0] <= 35.650001525878906:
            if input[3] <= 6.5:
                var56 = [0.7475728155339806, 0.2524271844660194]
            else:
                var56 = [1.0, 0.0]
        else:
            if input[1] <= 151.64999389648438:
                var56 = [0.31746031746031744, 0.6825396825396826]
            else:
                var56 = [1.0, 0.0]
    else:
        if input[2] <= 683.3999938964844:
            if input[0] <= 65.75000190734863:
                var56 = [1.0, 0.0]
            else:
                var56 = [0.0995850622406639, 0.9004149377593361]
        else:
            var56 = [1.0, 0.0]
    if input[0] <= 35.60000038146973:
        if input[1] <= 25.800000190734863:
            if input[1] <= 25.550000190734863:
                var57 = [1.0, 0.0]
            else:
                var57 = [0.0, 1.0]
        else:
            var57 = [1.0, 0.0]
    else:
        if input[0] <= 89.04999923706055:
            if input[0] <= 76.45000076293945:
                var57 = [0.3619631901840491, 0.6380368098159509]
            else:
                var57 = [1.0, 0.0]
        else:
            if input[2] <= 288.1999969482422:
                var57 = [0.06818181818181818, 0.9318181818181818]
            else:
                var57 = [0.0058823529411764705, 0.9941176470588236]
    if input[0] <= 35.60000038146973:
        if input[3] <= 6.5:
            if input[1] <= 26.100000381469727:
                var58 = [0.5813953488372093, 0.4186046511627907]
            else:
                var58 = [1.0, 0.0]
        else:
            var58 = [1.0, 0.0]
    else:
        if input[1] <= 190.29999542236328:
            if input[1] <= 78.5:
                var58 = [0.1, 0.9]
            else:
                var58 = [0.46017699115044247, 0.5398230088495575]
        else:
            if input[0] <= 65.6500015258789:
                var58 = [1.0, 0.0]
            else:
                var58 = [0.08050847457627118, 0.9194915254237288]
    if input[1] <= 136.0999984741211:
        if input[0] <= 45.44999885559082:
            if input[2] <= 67.9000015258789:
                var59 = [0.85, 0.15]
            else:
                var59 = [1.0, 0.0]
        else:
            if input[2] <= 181.25:
                var59 = [0.1206896551724138, 0.8793103448275862]
            else:
                var59 = [1.0, 0.0]
    else:
        if input[2] <= 519.4999847412109:
            if input[0] <= 91.4000015258789:
                var59 = [0.48484848484848486, 0.5151515151515151]
            else:
                var59 = [0.03496503496503497, 0.965034965034965]
        else:
            if input[0] <= 72.35000228881836:
                var59 = [1.0, 0.0]
            else:
                var59 = [0.024390243902439025, 0.975609756097561]
    if input[1] <= 136.6999969482422:
        if input[1] <= 58.44999885559082:
            if input[3] <= 6.5:
                var60 = [0.7285714285714285, 0.2714285714285714]
            else:
                var60 = [1.0, 0.0]
        else:
            if input[2] <= 175.95000457763672:
                var60 = [0.3924050632911392, 0.6075949367088608]
            else:
                var60 = [1.0, 0.0]
    else:
        if input[2] <= 198.25:
            var60 = [1.0, 0.0]
        else:
            if input[1] <= 336.5500030517578:
                var60 = [0.13134328358208955, 0.8686567164179104]
            else:
                var60 = [1.0, 0.0]
    if input[0] <= 34.85000038146973:
        if input[3] <= 6.5:
            if input[1] <= 25.949999809265137:
                var61 = [0.6744186046511628, 0.32558139534883723]
            else:
                var61 = [1.0, 0.0]
        else:
            var61 = [1.0, 0.0]
    else:
        if input[2] <= 104.29999923706055:
            var61 = [1.0, 0.0]
        else:
            if input[0] <= 87.29999923706055:
                var61 = [0.391304347826087, 0.6086956521739131]
            else:
                var61 = [0.053061224489795916, 0.9469387755102041]
    if input[0] <= 45.69999885559082:
        if input[1] <= 146.89999389648438:
            if input[2] <= 67.9000015258789:
                var62 = [0.8080808080808081, 0.1919191919191919]
            else:
                var62 = [1.0, 0.0]
        else:
            if input[1] <= 149.75:
                var62 = [0.0, 1.0]
            else:
                var62 = [1.0, 0.0]
    else:
        if input[1] <= 336.5500030517578:
            if input[0] <= 89.04999923706055:
                var62 = [0.352, 0.648]
            else:
                var62 = [0.02654867256637168, 0.9734513274336283]
        else:
            var62 = [1.0, 0.0]
    if input[1] <= 180.5999984741211:
        if input[1] <= 119.39999771118164:
            if input[0] <= 45.44999885559082:
                var63 = [0.9333333333333333, 0.06666666666666667]
            else:
                var63 = [0.13953488372093023, 0.8604651162790697]
        else:
            if input[1] <= 119.64999771118164:
                var63 = [0.0, 1.0]
            else:
                var63 = [0.640625, 0.359375]
    else:
        if input[1] <= 247.75:
            if input[0] <= 63.35000228881836:
                var63 = [1.0, 0.0]
            else:
                var63 = [0.09734513274336283, 0.9026548672566371]
        else:
            if input[2] <= 433.04998779296875:
                var63 = [0.027777777777777776, 0.9722222222222222]
            else:
                var63 = [0.0, 1.0]
    if input[1] <= 119.39999771118164:
        if input[1] <= 25.550000190734863:
            var64 = [1.0, 0.0]
        else:
            if input[3] <= 6.5:
                var64 = [0.5428571428571428, 0.45714285714285713]
            else:
                var64 = [0.9230769230769231, 0.07692307692307693]
    else:
        if input[0] <= 76.35000228881836:
            if input[2] <= 438.29998779296875:
                var64 = [0.43478260869565216, 0.5652173913043478]
            else:
                var64 = [1.0, 0.0]
        else:
            if input[0] <= 144.9000015258789:
                var64 = [0.0743801652892562, 0.9256198347107438]
            else:
                var64 = [1.0, 0.0]
    if input[0] <= 45.69999885559082:
        if input[2] <= 201.29999542236328:
            if input[1] <= 142.54999542236328:
                var65 = [0.9227272727272727, 0.07727272727272727]
            else:
                var65 = [0.10526315789473684, 0.8947368421052632]
        else:
            var65 = [1.0, 0.0]
    else:
        if input[0] <= 89.14999771118164:
            if input[0] <= 76.45000076293945:
                var65 = [0.23255813953488372, 0.7674418604651163]
            else:
                var65 = [1.0, 0.0]
        else:
            if input[1] <= 336.5500030517578:
                var65 = [0.03139013452914798, 0.968609865470852]
            else:
                var65 = [1.0, 0.0]
    if input[1] <= 180.79999542236328:
        if input[0] <= 35.60000038146973:
            if input[3] <= 6.5:
                var66 = [0.8061224489795918, 0.19387755102040816]
            else:
                var66 = [1.0, 0.0]
        else:
            if input[2] <= 249.9000015258789:
                var66 = [0.18446601941747573, 0.8155339805825242]
            else:
                var66 = [1.0, 0.0]
    else:
        if input[0] <= 91.4000015258789:
            if input[2] <= 431.29998779296875:
                var66 = [1.0, 0.0]
            else:
                var66 = [0.3333333333333333, 0.6666666666666666]
        else:
            if input[1] <= 352.0500030517578:
                var66 = [0.029411764705882353, 0.9705882352941176]
            else:
                var66 = [1.0, 0.0]
    if input[1] <= 119.39999771118164:
        if input[0] <= 44.89999961853027:
            if input[3] <= 6.5:
                var67 = [0.8414634146341463, 0.15853658536585366]
            else:
                var67 = [1.0, 0.0]
        else:
            if input[1] <= 79.5:
                var67 = [0.07692307692307693, 0.9230769230769231]
            else:
                var67 = [1.0, 0.0]
    else:
        if input[0] <= 89.14999771118164:
            if input[0] <= 76.5:
                var67 = [0.39166666666666666, 0.6083333333333333]
            else:
                var67 = [1.0, 0.0]
        else:
            if input[0] <= 145.25:
                var67 = [0.04477611940298507, 0.9552238805970149]
            else:
                var67 = [1.0, 0.0]
    if input[1] <= 119.25:
        if input[1] <= 25.5:
            var68 = [1.0, 0.0]
        else:
            if input[0] <= 45.44999885559082:
                var68 = [0.918918918918919, 0.08108108108108109]
            else:
                var68 = [0.3333333333333333, 0.6666666666666666]
    else:
        if input[1] <= 180.6999969482422:
            if input[1] <= 149.75:
                var68 = [0.35802469135802467, 0.6419753086419753]
            else:
                var68 = [1.0, 0.0]
        else:
            if input[0] <= 67.10000228881836:
                var68 = [1.0, 0.0]
            else:
                var68 = [0.0782608695652174, 0.9217391304347826]
    if input[0] <= 35.650001525878906:
        if input[3] <= 6.5:
            if input[1] <= 26.15000057220459:
                var69 = [0.5813953488372093, 0.4186046511627907]
            else:
                var69 = [1.0, 0.0]
        else:
            var69 = [1.0, 0.0]
    else:
        if input[2] <= 104.29999923706055:
            var69 = [1.0, 0.0]
        else:
            if input[1] <= 180.79999542236328:
                var69 = [0.3178294573643411, 0.6821705426356589]
            else:
                var69 = [0.09574468085106383, 0.9042553191489362]
    if input[0] <= 45.39999961853027:
        if input[0] <= 34.80000114440918:
            if input[3] <= 6.5:
                var70 = [0.7428571428571429, 0.2571428571428571]
            else:
                var70 = [1.0, 0.0]
        else:
            if input[1] <= 142.54999542236328:
                var70 = [1.0, 0.0]
            else:
                var70 = [0.2, 0.8]
    else:
        if input[0] <= 89.14999771118164:
            if input[2] <= 148.9000015258789:
                var70 = [0.02631578947368421, 0.9736842105263158]
            else:
                var70 = [0.4857142857142857, 0.5142857142857142]
        else:
            if input[2] <= 388.6999969482422:
                var70 = [0.023076923076923078, 0.9769230769230769]
            else:
                var70 = [0.08571428571428572, 0.9142857142857143]
    if input[2] <= 248.5:
        if input[0] <= 35.650001525878906:
            if input[3] <= 6.5:
                var71 = [0.7590361445783133, 0.24096385542168675]
            else:
                var71 = [1.0, 0.0]
        else:
            if input[2] <= 201.54999542236328:
                var71 = [0.24731182795698925, 0.7526881720430108]
            else:
                var71 = [1.0, 0.0]
    else:
        if input[0] <= 49.89999961853027:
            var71 = [1.0, 0.0]
        else:
            if input[0] <= 90.75:
                var71 = [0.38095238095238093, 0.6190476190476191]
            else:
                var71 = [0.05789473684210526, 0.9421052631578948]
    if input[0] <= 45.44999885559082:
        if input[0] <= 35.650001525878906:
            if input[2] <= 67.5:
                var72 = [0.847457627118644, 0.15254237288135594]
            else:
                var72 = [1.0, 0.0]
        else:
            if input[0] <= 36.400001525878906:
                var72 = [0.0, 1.0]
            else:
                var72 = [1.0, 0.0]
    else:
        if input[1] <= 179.39999389648438:
            if input[2] <= 184.0500030517578:
                var72 = [0.2, 0.8]
            else:
                var72 = [0.6451612903225806, 0.3548387096774194]
        else:
            if input[1] <= 337.8000030517578:
                var72 = [0.09642857142857143, 0.9035714285714286]
            else:
                var72 = [1.0, 0.0]
    if input[1] <= 119.04999923706055:
        if input[2] <= 138.85000610351562:
            if input[0] <= 45.44999885559082:
                var73 = [0.9050279329608939, 0.09497206703910614]
            else:
                var73 = [0.2, 0.8]
        else:
            var73 = [1.0, 0.0]
    else:
        if input[0] <= 89.14999771118164:
            if input[2] <= 250.70000457763672:
                var73 = [0.22727272727272727, 0.7727272727272727]
            else:
                var73 = [0.6595744680851063, 0.3404255319148936]
        else:
            if input[2] <= 581.4500122070312:
                var73 = [0.043689320388349516, 0.9563106796116505]
            else:
                var73 = [0.17647058823529413, 0.8235294117647058]
    if input[0] <= 45.39999961853027:
        if input[0] <= 35.650001525878906:
            if input[2] <= 67.5:
                var74 = [0.8220338983050848, 0.17796610169491525]
            else:
                var74 = [1.0, 0.0]
        else:
            if input[3] <= 8.5:
                var74 = [1.0, 0.0]
            else:
                var74 = [0.1, 0.9]
    else:
        if input[2] <= 246.1500015258789:
            if input[2] <= 181.25:
                var74 = [0.1746031746031746, 0.8253968253968254]
            else:
                var74 = [1.0, 0.0]
        else:
            if input[1] <= 136.0999984741211:
                var74 = [1.0, 0.0]
            else:
                var74 = [0.1003584229390681, 0.899641577060932]
    if input[1] <= 136.6999969482422:
        if input[0] <= 45.44999885559082:
            if input[3] <= 6.5:
                var75 = [0.7608695652173914, 0.2391304347826087]
            else:
                var75 = [1.0, 0.0]
        else:
            if input[1] <= 120.0:
                var75 = [0.16666666666666666, 0.8333333333333334]
            else:
                var75 = [1.0, 0.0]
    else:
        if input[0] <= 67.10000228881836:
            if input[1] <= 148.4499969482422:
                var75 = [0.12195121951219512, 0.8780487804878049]
            else:
                var75 = [1.0, 0.0]
        else:
            if input[1] <= 172.3499984741211:
                var75 = [1.0, 0.0]
            else:
                var75 = [0.05179282868525897, 0.9482071713147411]
    if input[0] <= 45.69999885559082:
        if input[0] <= 11.150000095367432:
            var76 = [1.0, 0.0]
        else:
            if input[0] <= 11.25:
                var76 = [0.045454545454545456, 0.9545454545454546]
            else:
                var76 = [0.8881987577639752, 0.11180124223602485]
    else:
        if input[1] <= 180.6999969482422:
            if input[0] <= 50.35000038146973:
                var76 = [0.09433962264150944, 0.9056603773584906]
            else:
                var76 = [0.7, 0.3]
        else:
            if input[1] <= 336.5500030517578:
                var76 = [0.08366533864541832, 0.9163346613545816]
            else:
                var76 = [1.0, 0.0]
    if input[0] <= 45.69999885559082:
        if input[0] <= 35.650001525878906:
            if input[3] <= 6.5:
                var77 = [0.7692307692307693, 0.23076923076923078]
            else:
                var77 = [1.0, 0.0]
        else:
            if input[1] <= 146.89999389648438:
                var77 = [1.0, 0.0]
            else:
                var77 = [0.20833333333333334, 0.7916666666666666]
    else:
        if input[1] <= 236.0:
            if input[2] <= 182.4000015258789:
                var77 = [0.1111111111111111, 0.8888888888888888]
            else:
                var77 = [0.30246913580246915, 0.6975308641975309]
        else:
            if input[0] <= 76.35000228881836:
                var77 = [1.0, 0.0]
            else:
                var77 = [0.02666666666666667, 0.9733333333333334]
    if input[1] <= 136.0999984741211:
        if input[0] <= 45.39999961853027:
            if input[3] <= 6.5:
                var78 = [0.7, 0.3]
            else:
                var78 = [1.0, 0.0]
        else:
            if input[0] <= 47.10000038146973:
                var78 = [0.0, 1.0]
            else:
                var78 = [0.6764705882352942, 0.3235294117647059]
    else:
        if input[1] <= 180.5999984741211:
            if input[1] <= 148.4499969482422:
                var78 = [0.21052631578947367, 0.7894736842105263]
            else:
                var78 = [1.0, 0.0]
        else:
            if input[0] <= 65.75000190734863:
                var78 = [1.0, 0.0]
            else:
                var78 = [0.07251908396946564, 0.9274809160305344]
    if input[0] <= 45.44999885559082:
        if input[1] <= 142.5999984741211:
            if input[3] <= 6.5:
                var79 = [0.7733333333333333, 0.22666666666666666]
            else:
                var79 = [1.0, 0.0]
        else:
            if input[2] <= 221.25:
                var79 = [0.0, 1.0]
            else:
                var79 = [1.0, 0.0]
    else:
        if input[1] <= 337.8000030517578:
            if input[2] <= 518.3999938964844:
                var79 = [0.18855218855218855, 0.8114478114478114]
            else:
                var79 = [0.029411764705882353, 0.9705882352941176]
        else:
            var79 = [1.0, 0.0]
    if input[0] <= 45.39999961853027:
        if input[0] <= 11.150000095367432:
            var80 = [1.0, 0.0]
        else:
            if input[0] <= 11.400000095367432:
                var80 = [0.07142857142857142, 0.9285714285714286]
            else:
                var80 = [0.8874172185430463, 0.11258278145695365]
    else:
        if input[1] <= 337.8000030517578:
            if input[2] <= 519.3999938964844:
                var80 = [0.1717557251908397, 0.8282442748091603]
            else:
                var80 = [0.034482758620689655, 0.9655172413793104]
        else:
            var80 = [1.0, 0.0]
    if input[0] <= 45.69999885559082:
        if input[3] <= 8.5:
            if input[2] <= 68.85000228881836:
                var81 = [0.8059701492537313, 0.19402985074626866]
            else:
                var81 = [1.0, 0.0]
        else:
            if input[1] <= 134.64999771118164:
                var81 = [1.0, 0.0]
            else:
                var81 = [0.1111111111111111, 0.8888888888888888]
    else:
        if input[2] <= 526.7999877929688:
            if input[0] <= 87.75:
                var81 = [0.4965986394557823, 0.5034013605442177]
            else:
                var81 = [0.018633540372670808, 0.9813664596273292]
        else:
            if input[0] <= 72.45000076293945:
                var81 = [1.0, 0.0]
            else:
                var81 = [0.024691358024691357, 0.9753086419753086]
    if input[1] <= 136.0999984741211:
        if input[1] <= 25.550000190734863:
            var82 = [1.0, 0.0]
        else:
            if input[1] <= 25.800000190734863:
                var82 = [0.041666666666666664, 0.9583333333333334]
            else:
                var82 = [0.8526785714285714, 0.14732142857142858]
    else:
        if input[0] <= 88.9000015258789:
            if input[1] <= 148.4499969482422:
                var82 = [0.0975609756097561, 0.9024390243902439]
            else:
                var82 = [0.5517241379310345, 0.4482758620689655]
        else:
            if input[1] <= 339.8500061035156:
                var82 = [0.031088082901554404, 0.9689119170984456]
            else:
                var82 = [1.0, 0.0]
    if input[0] <= 35.650001525878906:
        if input[2] <= 67.5:
            if input[2] <= 66.60000228881836:
                var83 = [1.0, 0.0]
            else:
                var83 = [0.0, 1.0]
        else:
            var83 = [1.0, 0.0]
    else:
        if input[1] <= 178.4499969482422:
            if input[0] <= 36.650001525878906:
                var83 = [0.0, 1.0]
            else:
                var83 = [0.44755244755244755, 0.5524475524475524]
        else:
            if input[0] <= 65.75000190734863:
                var83 = [1.0, 0.0]
            else:
                var83 = [0.09663865546218488, 0.9033613445378151]
    if input[0] <= 45.69999885559082:
        if input[1] <= 147.04999542236328:
            if input[3] <= 6.5:
                var84 = [0.7920792079207921, 0.2079207920792079]
            else:
                var84 = [1.0, 0.0]
        else:
            if input[0] <= 34.400001525878906:
                var84 = [1.0, 0.0]
            else:
                var84 = [0.1875, 0.8125]
    else:
        if input[2] <= 245.5999984741211:
            if input[2] <= 176.5999984741211:
                var84 = [0.13432835820895522, 0.8656716417910447]
            else:
                var84 = [1.0, 0.0]
        else:
            if input[2] <= 388.8500061035156:
                var84 = [0.06015037593984962, 0.9398496240601504]
            else:
                var84 = [0.21710526315789475, 0.7828947368421053]
    if input[0] <= 35.60000038146973:
        if input[3] <= 6.5:
            if input[2] <= 67.6500015258789:
                var85 = [0.6111111111111112, 0.3888888888888889]
            else:
                var85 = [1.0, 0.0]
        else:
            var85 = [1.0, 0.0]
    else:
        if input[0] <= 86.69999694824219:
            if input[0] <= 50.35000038146973:
                var85 = [0.24489795918367346, 0.7551020408163265]
            else:
                var85 = [0.5543478260869565, 0.44565217391304346]
        else:
            if input[0] <= 144.9000015258789:
                var85 = [0.02830188679245283, 0.9716981132075472]
            else:
                var85 = [1.0, 0.0]
    if input[0] <= 35.5:
        if input[2] <= 67.0:
            if input[2] <= 66.60000228881836:
                var86 = [1.0, 0.0]
            else:
                var86 = [0.0, 1.0]
        else:
            var86 = [1.0, 0.0]
    else:
        if input[0] <= 89.14999771118164:
            if input[0] <= 50.45000076293945:
                var86 = [0.24175824175824176, 0.7582417582417582]
            else:
                var86 = [0.5802469135802469, 0.41975308641975306]
        else:
            if input[1] <= 336.5500030517578:
                var86 = [0.037383177570093455, 0.9626168224299065]
            else:
                var86 = [1.0, 0.0]
    if input[0] <= 45.69999885559082:
        if input[2] <= 66.70000076293945:
            var87 = [1.0, 0.0]
        else:
            if input[2] <= 67.85000228881836:
                var87 = [0.0, 1.0]
            else:
                var87 = [0.9183673469387755, 0.08163265306122448]
    else:
        if input[0] <= 89.14999771118164:
            if input[0] <= 46.95000076293945:
                var87 = [0.023809523809523808, 0.9761904761904762]
            else:
                var87 = [0.5181818181818182, 0.4818181818181818]
        else:
            if input[0] <= 127.9000015258789:
                var87 = [0.04081632653061224, 0.9591836734693877]
            else:
                var87 = [0.0, 1.0]
    if input[1] <= 136.6999969482422:
        if input[2] <= 174.9000015258789:
            if input[2] <= 172.5500030517578:
                var88 = [0.77734375, 0.22265625]
            else:
                var88 = [0.0, 1.0]
        else:
            var88 = [1.0, 0.0]
    else:
        if input[1] <= 336.5500030517578:
            if input[0] <= 91.4000015258789:
                var88 = [0.38738738738738737, 0.6126126126126126]
            else:
                var88 = [0.035175879396984924, 0.964824120603015]
        else:
            var88 = [1.0, 0.0]
    if input[1] <= 119.20000076293945:
        if input[0] <= 45.69999885559082:
            if input[3] <= 6.5:
                var89 = [0.7888888888888889, 0.2111111111111111]
            else:
                var89 = [1.0, 0.0]
        else:
            if input[1] <= 79.5:
                var89 = [0.058823529411764705, 0.9411764705882353]
            else:
                var89 = [1.0, 0.0]
    else:
        if input[0] <= 87.75:
            if input[1] <= 267.1999969482422:
                var89 = [0.6166666666666667, 0.38333333333333336]
            else:
                var89 = [0.09523809523809523, 0.9047619047619048]
        else:
            if input[0] <= 145.25:
                var89 = [0.027906976744186046, 0.9720930232558139]
            else:
                var89 = [1.0, 0.0]
    if input[2] <= 278.75:
        if input[1] <= 119.25:
            if input[3] <= 6.5:
                var90 = [0.6458333333333334, 0.3541666666666667]
            else:
                var90 = [0.9398148148148148, 0.06018518518518518]
        else:
            if input[1] <= 149.64999389648438:
                var90 = [0.19696969696969696, 0.803030303030303]
            else:
                var90 = [1.0, 0.0]
    else:
        if input[1] <= 180.6999969482422:
            var90 = [1.0, 0.0]
        else:
            if input[2] <= 374.1499938964844:
                var90 = [0.039603960396039604, 0.9603960396039604]
            else:
                var90 = [0.15527950310559005, 0.84472049689441]
    if input[1] <= 180.79999542236328:
        if input[1] <= 57.89999961853027:
            if input[3] <= 6.5:
                var91 = [0.7625, 0.2375]
            else:
                var91 = [1.0, 0.0]
        else:
            if input[0] <= 45.39999961853027:
                var91 = [0.9042553191489362, 0.09574468085106383]
            else:
                var91 = [0.29411764705882354, 0.7058823529411765]
    else:
        if input[0] <= 65.75000190734863:
            var91 = [1.0, 0.0]
        else:
            if input[0] <= 91.4000015258789:
                var91 = [0.18, 0.82]
            else:
                var91 = [0.0182648401826484, 0.9817351598173516]
    if input[1] <= 147.0999984741211:
        if input[2] <= 66.70000076293945:
            var92 = [1.0, 0.0]
        else:
            if input[0] <= 45.44999885559082:
                var92 = [0.9207920792079208, 0.07920792079207921]
            else:
                var92 = [0.2967032967032967, 0.7032967032967034]
    else:
        if input[0] <= 90.75:
            if input[0] <= 76.95000076293945:
                var92 = [0.24324324324324326, 0.7567567567567568]
            else:
                var92 = [1.0, 0.0]
        else:
            if input[2] <= 265.8999938964844:
                var92 = [1.0, 0.0]
            else:
                var92 = [0.013574660633484163, 0.9864253393665159]
    if input[0] <= 45.69999885559082:
        if input[0] <= 35.35000038146973:
            if input[1] <= 25.65000057220459:
                var93 = [0.8333333333333334, 0.16666666666666666]
            else:
                var93 = [1.0, 0.0]
        else:
            if input[0] <= 36.650001525878906:
                var93 = [0.0, 1.0]
            else:
                var93 = [1.0, 0.0]
    else:
        if input[2] <= 181.20000457763672:
            if input[2] <= 139.45000457763672:
                var93 = [0.0, 1.0]
            else:
                var93 = [0.09523809523809523, 0.9047619047619048]
        else:
            if input[0] <= 90.20000076293945:
                var93 = [0.44144144144144143, 0.5585585585585585]
            else:
                var93 = [0.06403940886699508, 0.9359605911330049]
    if input[0] <= 35.60000038146973:
        if input[3] <= 6.5:
            if input[0] <= 11.150000095367432:
                var94 = [1.0, 0.0]
            else:
                var94 = [0.5365853658536586, 0.4634146341463415]
        else:
            var94 = [1.0, 0.0]
    else:
        if input[1] <= 118.75:
            if input[0] <= 45.44999885559082:
                var94 = [1.0, 0.0]
            else:
                var94 = [0.2564102564102564, 0.7435897435897436]
        else:
            if input[0] <= 89.14999771118164:
                var94 = [0.38333333333333336, 0.6166666666666667]
            else:
                var94 = [0.046511627906976744, 0.9534883720930233]
    if input[0] <= 35.650001525878906:
        if input[3] <= 6.5:
            if input[2] <= 61.20000076293945:
                var95 = [1.0, 0.0]
            else:
                var95 = [0.5384615384615384, 0.46153846153846156]
        else:
            var95 = [1.0, 0.0]
    else:
        if input[2] <= 102.64999771118164:
            var95 = [1.0, 0.0]
        else:
            if input[1] <= 246.04999542236328:
                var95 = [0.2509505703422053, 0.7490494296577946]
            else:
                var95 = [0.05511811023622047, 0.9448818897637795]
    if input[1] <= 136.6999969482422:
        if input[1] <= 58.94999885559082:
            if input[3] <= 6.5:
                var96 = [0.7543859649122807, 0.24561403508771928]
            else:
                var96 = [1.0, 0.0]
        else:
            if input[2] <= 175.95000457763672:
                var96 = [0.4725274725274725, 0.5274725274725275]
            else:
                var96 = [1.0, 0.0]
    else:
        if input[0] <= 90.20000076293945:
            if input[0] <= 35.05000114440918:
                var96 = [1.0, 0.0]
            else:
                var96 = [0.35294117647058826, 0.6470588235294118]
        else:
            if input[2] <= 265.8999938964844:
                var96 = [1.0, 0.0]
            else:
                var96 = [0.039603960396039604, 0.9603960396039604]
    if input[0] <= 35.35000038146973:
        if input[2] <= 67.0:
            if input[1] <= 25.199999809265137:
                var97 = [1.0, 0.0]
            else:
                var97 = [0.4, 0.6]
        else:
            var97 = [1.0, 0.0]
    else:
        if input[0] <= 89.04999923706055:
            if input[0] <= 76.9000015258789:
                var97 = [0.34838709677419355, 0.6516129032258065]
            else:
                var97 = [1.0, 0.0]
        else:
            if input[0] <= 145.25:
                var97 = [0.03333333333333333, 0.9666666666666667]
            else:
                var97 = [1.0, 0.0]
    if input[0] <= 35.650001525878906:
        if input[3] <= 6.5:
            if input[2] <= 67.6500015258789:
                var98 = [0.7142857142857143, 0.2857142857142857]
            else:
                var98 = [1.0, 0.0]
        else:
            var98 = [1.0, 0.0]
    else:
        if input[2] <= 246.3000030517578:
            if input[2] <= 201.54999542236328:
                var98 = [0.2222222222222222, 0.7777777777777778]
            else:
                var98 = [1.0, 0.0]
        else:
            if input[1] <= 136.6999969482422:
                var98 = [1.0, 0.0]
            else:
                var98 = [0.1384083044982699, 0.8615916955017301]
    if input[1] <= 136.25:
        if input[1] <= 25.15000057220459:
            var99 = [1.0, 0.0]
        else:
            if input[1] <= 25.65000057220459:
                var99 = [0.04, 0.96]
            else:
                var99 = [0.8136363636363636, 0.18636363636363637]
    else:
        if input[0] <= 88.9000015258789:
            if input[0] <= 34.400001525878906:
                var99 = [1.0, 0.0]
            else:
                var99 = [0.33858267716535434, 0.6614173228346457]
        else:
            if input[2] <= 265.8999938964844:
                var99 = [1.0, 0.0]
            else:
                var99 = [0.04568527918781726, 0.9543147208121827]
    if input[0] <= 45.69999885559082:
        if input[1] <= 146.6999969482422:
            if input[3] <= 6.5:
                var100 = [0.8470588235294118, 0.15294117647058825]
            else:
                var100 = [1.0, 0.0]
        else:
            if input[1] <= 149.64999389648438:
                var100 = [0.0, 1.0]
            else:
                var100 = [1.0, 0.0]
    else:
        if input[2] <= 246.1500015258789:
            if input[2] <= 181.20000457763672:
                var100 = [0.09090909090909091, 0.9090909090909091]
            else:
                var100 = [1.0, 0.0]
        else:
            if input[2] <= 518.3999938964844:
                var100 = [0.1485148514851485, 0.8514851485148515]
            else:
                var100 = [0.034482758620689655, 0.9655172413793104]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(var46, var47), var48), var49), var50), var51), var52), var53), var54), var55), var56), var57), var58), var59), var60), var61), var62), var63), var64), var65), var66), var67), var68), var69), var70), var71), var72), var73), var74), var75), var76), var77), var78), var79), var80), var81), var82), var83), var84), var85), var86), var87), var88), var89), var90), var91), var92), var93), var94), var95), var96), var97), var98), var99), var100), 0.01)


# --- Konkan Base 2: XGBoost ---
# Input: [Rainfall_mm, Rainfall_3day, Rainfall_7day, Month]
import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score_konkan_xgb(input):
    if input[0] < 45.6:
        if input[1] < 147.9:
            if input[3] < 7.0:
                var0 = -0.34657043
            else:
                var0 = -0.59383035
        else:
            if input[1] < 151.4:
                var0 = 0.5383784
            else:
                var0 = -0.51111114
    else:
        if input[0] < 88.9:
            if input[0] < 50.9:
                var0 = 0.42698148
            else:
                var0 = -0.060434498
        else:
            var0 = 0.54562366
    if input[0] < 45.6:
        if input[1] < 147.9:
            if input[2] < 68.2:
                var1 = -0.2664821
            else:
                var1 = -0.4697267
        else:
            if input[1] < 151.4:
                var1 = 0.42308792
            else:
                var1 = -0.40484217
    else:
        if input[0] < 88.9:
            if input[0] < 76.8:
                var1 = 0.17083792
            else:
                var1 = -0.48915008
        else:
            var1 = 0.4165894
    if input[0] < 45.6:
        if input[1] < 147.9:
            if input[3] < 7.0:
                var2 = -0.16929176
            else:
                var2 = -0.4049877
        else:
            if input[1] < 151.4:
                var2 = 0.36281323
            else:
                var2 = -0.3462788
    else:
        if input[0] < 88.9:
            if input[0] < 47.2:
                var2 = 0.3720726
            else:
                var2 = -0.025665915
        else:
            if input[0] < 91.5:
                var2 = 0.23093066
            else:
                var2 = 0.35742572
    if input[0] < 67.3:
        if input[3] < 7.0:
            if input[0] < 11.2:
                var3 = -0.40544167
            else:
                var3 = 0.17777795
        else:
            if input[3] < 9.0:
                var3 = -0.42007443
            else:
                var3 = -0.1361345
    else:
        if input[1] < 180.7:
            if input[0] < 84.2:
                var3 = -0.45528865
            else:
                var3 = 0.3369759
        else:
            if input[0] < 68.4:
                var3 = 0.48780635
            else:
                var3 = 0.27403632
    if input[0] < 35.9:
        if input[1] < 26.1:
            if input[1] < 25.6:
                var4 = -0.36151272
            else:
                var4 = 0.7056955
        else:
            var4 = -0.36438513
    else:
        if input[0] < 91.5:
            if input[1] < 77.8:
                var4 = 0.255519
            else:
                var4 = -0.011577546
        else:
            if input[2] < 582.2:
                var4 = 0.2956319
            else:
                var4 = 0.11955548
    if input[0] < 67.3:
        if input[0] < 50.9:
            if input[0] < 35.9:
                var5 = -0.22653894
            else:
                var5 = 0.13520977
        else:
            var5 = -0.5157744
    else:
        if input[1] < 180.7:
            if input[0] < 84.2:
                var5 = -0.37329015
            else:
                var5 = 0.30625397
        else:
            if input[2] < 582.2:
                var5 = 0.24352689
            else:
                var5 = 0.013493539
    if input[0] < 11.2:
        var6 = -0.3267293
    else:
        if input[0] < 11.3:
            var6 = 0.53695005
        else:
            if input[0] < 35.9:
                var6 = -0.3308266
            else:
                var6 = 0.09059442
    if input[0] < 67.3:
        if input[2] < 250.6:
            if input[0] < 11.2:
                var7 = -0.31256735
            else:
                var7 = 0.028217528
        else:
            var7 = -0.39547753
    else:
        if input[2] < 524.5:
            if input[2] < 448.2:
                var7 = 0.1480894
            else:
                var7 = -0.6364136
        else:
            if input[2] < 582.2:
                var7 = 0.33590287
            else:
                var7 = -0.012964894
    if input[0] < 91.5:
        if input[0] < 11.2:
            var8 = -0.30116624
        else:
            if input[0] < 11.3:
                var8 = 0.39131773
            else:
                var8 = -0.072751
    else:
        if input[2] < 582.2:
            if input[2] < 309.7:
                var8 = 0.10229578
            else:
                var8 = 0.23061994
        else:
            var8 = 0.078801006
    if input[1] < 137.0:
        if input[2] < 174.2:
            if input[0] < 45.6:
                var9 = -0.14777613
            else:
                var9 = 0.18034497
        else:
            var9 = -0.39294726
    else:
        if input[1] < 138.1:
            var9 = 0.3356264
        else:
            if input[3] < 7.0:
                var9 = -0.3045
            else:
                var9 = 0.09689656
    if input[0] < 11.2:
        var10 = -0.28476563
    else:
        if input[0] < 11.3:
            var10 = 0.34279352
        else:
            if input[0] < 35.9:
                var10 = -0.30354235
            else:
                var10 = 0.03882686
    if input[0] < 91.5:
        if input[2] < 532.2:
            if input[1] < 215.8:
                var11 = -0.03494823
            else:
                var11 = -0.5772188
        else:
            if input[2] < 537.6:
                var11 = 0.34907198
            else:
                var11 = -0.36496192
    else:
        if input[2] < 390.1:
            if input[2] < 309.7:
                var11 = 0.05717128
            else:
                var11 = 0.25926653
        else:
            if input[2] < 469.5:
                var11 = -0.14027342
            else:
                var11 = 0.1464914
    if input[0] < 11.2:
        var12 = -0.27295998
    else:
        if input[0] < 11.3:
            var12 = 0.28793842
        else:
            if input[0] < 35.9:
                var12 = -0.28944162
            else:
                var12 = 0.028537298
    if input[0] < 11.2:
        var13 = -0.26183018
    else:
        if input[1] < 26.1:
            var13 = 0.25048408
        else:
            if input[0] < 35.9:
                var13 = -0.2891357
            else:
                var13 = 0.020343557
    if input[0] < 91.5:
        if input[1] < 268.7:
            if input[2] < 438.3:
                var14 = -0.016880697
            else:
                var14 = -0.44110844
        else:
            if input[1] < 285.8:
                var14 = 0.30979717
            else:
                var14 = -0.32519028
    else:
        if input[1] < 199.6:
            if input[0] < 108.9:
                var14 = 0.24767037
            else:
                var14 = 0.07598393
        else:
            if input[0] < 136.0:
                var14 = -0.026160127
            else:
                var14 = 0.18175207
    if input[1] < 137.0:
        if input[2] < 174.2:
            if input[0] < 45.6:
                var15 = -0.108689874
            else:
                var15 = 0.13663176
        else:
            var15 = -0.37717283
    else:
        if input[1] < 138.1:
            var15 = 0.2914585
        else:
            if input[0] < 36.9:
                var15 = 0.27950016
            else:
                var15 = -0.024309523
    if input[1] < 207.5:
        if input[1] < 199.6:
            if input[0] < 84.2:
                var16 = -0.06782825
            else:
                var16 = 0.24409956
        else:
            var16 = -0.58118534
    else:
        if input[1] < 215.8:
            if input[2] < 438.3:
                var16 = 0.3108694
            else:
                var16 = -0.0012604821
        else:
            if input[1] < 268.7:
                var16 = -0.30929974
            else:
                var16 = 0.11647085
    if input[2] < 66.6:
        var17 = -0.25042984
    else:
        if input[2] < 68.2:
            var17 = 0.31937307
        else:
            if input[0] < 35.9:
                var17 = -0.27026188
            else:
                var17 = 0.009674093
    if input[1] < 207.5:
        if input[0] < 50.9:
            if input[2] < 250.6:
                var18 = 0.07695937
            else:
                var18 = -0.2660253
        else:
            if input[0] < 85.0:
                var18 = -0.40578654
            else:
                var18 = 0.09992904
    else:
        if input[1] < 215.8:
            if input[2] < 438.3:
                var18 = 0.27837422
            else:
                var18 = -0.0029985092
        else:
            if input[1] < 268.7:
                var18 = -0.22351564
            else:
                var18 = 0.08989462
    if input[0] < 136.0:
        if input[2] < 582.2:
            if input[2] < 524.5:
                var19 = -0.040904693
            else:
                var19 = 0.26432225
        else:
            var19 = -0.5733407
    else:
        if input[1] < 306.6:
            var19 = 0.02013195
        else:
            var19 = 0.25314137
    if input[2] < 66.6:
        var20 = -0.23725931
    else:
        if input[2] < 68.2:
            var20 = 0.28618175
        else:
            if input[2] < 104.9:
                var20 = -0.29274306
            else:
                var20 = 0.0068008965
    if input[2] < 66.6:
        var21 = -0.22165354
    else:
        if input[2] < 68.2:
            var21 = 0.2611073
        else:
            if input[0] < 35.9:
                var21 = -0.25385383
            else:
                var21 = 0.009760779
    if input[0] < 136.0:
        if input[2] < 582.2:
            if input[2] < 524.5:
                var22 = -0.030887613
            else:
                var22 = 0.23967034
        else:
            var22 = -0.50774443
    else:
        if input[1] < 306.6:
            var22 = 0.012288396
        else:
            var22 = 0.236191
    if input[0] < 47.2:
        if input[2] < 202.5:
            if input[0] < 45.6:
                var23 = 0.016872082
            else:
                var23 = 0.26811674
        else:
            var23 = -0.27882135
    else:
        if input[0] < 49.8:
            var23 = -0.5404447
        else:
            if input[0] < 50.9:
                var23 = 0.25212553
            else:
                var23 = -0.05002495
    if input[2] < 582.2:
        if input[2] < 524.5:
            if input[2] < 448.2:
                var24 = 0.015237414
            else:
                var24 = -0.36733738
        else:
            if input[1] < 252.7:
                var24 = 0.05245875
            else:
                var24 = 0.1983547
    else:
        if input[0] < 109.7:
            var24 = -0.43605068
        else:
            var24 = 0.07665461
    if input[2] < 66.6:
        var25 = -0.20625724
    else:
        if input[2] < 68.2:
            var25 = 0.23792094
        else:
            if input[2] < 104.9:
                var25 = -0.2617132
            else:
                var25 = 0.005318993
    if input[1] < 137.0:
        if input[1] < 77.8:
            if input[0] < 44.8:
                var26 = -0.09200569
            else:
                var26 = 0.19431572
        else:
            if input[0] < 79.9:
                var26 = -0.38497734
            else:
                var26 = 0.22215319
    else:
        if input[0] < 68.4:
            if input[2] < 438.3:
                var26 = 0.17227477
            else:
                var26 = -0.2129442
        else:
            if input[0] < 91.5:
                var26 = -0.22642997
            else:
                var26 = 0.038881093
    if input[0] < 136.0:
        if input[1] < 215.8:
            if input[1] < 207.5:
                var27 = -0.030873977
            else:
                var27 = 0.20591205
        else:
            if input[2] < 532.2:
                var27 = -0.31429118
            else:
                var27 = 0.07194405
    else:
        if input[1] < 250.0:
            var27 = 0.23731972
        else:
            if input[1] < 316.2:
                var27 = -0.25224295
            else:
                var27 = 0.18011962
    if input[2] < 582.2:
        if input[2] < 524.5:
            if input[2] < 448.2:
                var28 = 0.011409355
            else:
                var28 = -0.31360778
        else:
            if input[0] < 76.8:
                var28 = 0.21377306
            else:
                var28 = 0.05323529
    else:
        var28 = -0.21566996
    if input[0] < 47.2:
        if input[2] < 202.5:
            if input[0] < 35.9:
                var29 = -0.03805174
            else:
                var29 = 0.1754994
        else:
            var29 = -0.24118488
    else:
        if input[2] < 246.3:
            if input[0] < 84.2:
                var29 = -0.41863164
            else:
                var29 = 0.20690957
        else:
            if input[2] < 250.6:
                var29 = 0.26980168
            else:
                var29 = -0.010251351
    if input[0] < 109.7:
        if input[1] < 292.5:
            if input[2] < 435.3:
                var30 = -0.04272294
            else:
                var30 = 0.12618901
        else:
            var30 = -0.3579793
    else:
        if input[2] < 390.1:
            if input[3] < 8.0:
                var30 = 0.040481783
            else:
                var30 = 0.2550859
        else:
            if input[2] < 601.3:
                var30 = -0.3332685
            else:
                var30 = 0.1836646
    if input[0] < 36.9:
        if input[0] < 35.9:
            if input[1] < 26.1:
                var31 = 0.1049415
            else:
                var31 = -0.22186756
        else:
            var31 = 0.25845727
    else:
        if input[0] < 45.6:
            var31 = -0.2827668
        else:
            if input[0] < 47.2:
                var31 = 0.1763588
            else:
                var31 = -0.031500716
    if input[0] < 136.0:
        if input[2] < 582.2:
            if input[2] < 524.5:
                var32 = -0.022836339
            else:
                var32 = 0.19215696
        else:
            var32 = -0.30681267
    else:
        if input[1] < 306.6:
            var32 = -0.07902648
        else:
            var32 = 0.23422204
    if input[2] < 390.1:
        if input[0] < 85.0:
            if input[0] < 50.9:
                var33 = 0.050017778
            else:
                var33 = -0.30558744
        else:
            if input[1] < 199.6:
                var33 = 0.26298454
            else:
                var33 = 0.01976509
    else:
        if input[2] < 435.3:
            var33 = -0.421128
        else:
            if input[0] < 76.8:
                var33 = 0.15838541
            else:
                var33 = -0.11550235
    if input[1] < 25.6:
        var34 = -0.18322995
    else:
        if input[1] < 26.1:
            var34 = 0.22528622
        else:
            if input[0] < 35.9:
                var34 = -0.20787476
            else:
                var34 = 0.0035923633
    if input[0] < 136.0:
        if input[1] < 215.8:
            if input[1] < 208.1:
                var35 = -0.024807101
            else:
                var35 = 0.18236095
        else:
            if input[1] < 268.7:
                var35 = -0.3112236
            else:
                var35 = 0.010388385
    else:
        if input[1] < 306.6:
            var35 = -0.06279845
        else:
            var35 = 0.2261924
    if input[2] < 390.1:
        if input[0] < 109.7:
            if input[1] < 199.6:
                var36 = 0.025778126
            else:
                var36 = -0.33443013
        else:
            if input[3] < 8.0:
                var36 = 0.012916337
            else:
                var36 = 0.24528992
    else:
        if input[2] < 435.3:
            var36 = -0.35889956
        else:
            if input[2] < 448.2:
                var36 = 0.13792579
            else:
                var36 = -0.09096754
    if input[3] < 9.0:
        if input[2] < 106.5:
            if input[2] < 104.9:
                var37 = 0.036358997
            else:
                var37 = 0.21463956
        else:
            if input[0] < 49.8:
                var37 = -0.36903724
            else:
                var37 = 0.020086907
    else:
        if input[2] < 137.3:
            var37 = -0.22637197
        else:
            if input[0] < 47.2:
                var37 = 0.19403866
            else:
                var37 = -0.0064837243
    if input[2] < 582.2:
        if input[1] < 207.5:
            if input[2] < 312.8:
                var38 = 0.015199649
            else:
                var38 = -0.25071722
        else:
            if input[1] < 215.8:
                var38 = 0.15817258
            else:
                var38 = 0.009503131
    else:
        var38 = -0.14548987
    if input[1] < 25.6:
        var39 = -0.16662449
    else:
        if input[0] < 36.9:
            if input[0] < 35.9:
                var39 = 0.04602346
            else:
                var39 = 0.2209981
        else:
            if input[0] < 45.6:
                var39 = -0.2432131
            else:
                var39 = 0.00072086725
    if input[2] < 390.1:
        if input[0] < 109.7:
            if input[1] < 199.6:
                var40 = 0.019615423
            else:
                var40 = -0.27181882
        else:
            if input[3] < 8.0:
                var40 = 0.040094323
            else:
                var40 = 0.22757295
    else:
        if input[2] < 435.3:
            var40 = -0.32208687
        else:
            if input[0] < 76.8:
                var40 = 0.117549
            else:
                var40 = -0.09251215
    if input[2] < 66.6:
        var41 = -0.15816267
    else:
        if input[2] < 68.2:
            var41 = 0.20017162
        else:
            if input[1] < 137.0:
                var41 = -0.07763149
            else:
                var41 = 0.018915506
    if input[2] < 390.1:
        if input[0] < 85.0:
            if input[0] < 50.9:
                var42 = 0.04086235
            else:
                var42 = -0.27148628
        else:
            if input[1] < 199.6:
                var42 = 0.2504052
            else:
                var42 = -0.027941737
    else:
        if input[2] < 435.3:
            var42 = -0.28795254
        else:
            if input[1] < 213.4:
                var42 = -0.19428821
            else:
                var42 = 0.05235211
    if input[1] < 77.8:
        if input[1] < 77.5:
            if input[3] < 7.0:
                var43 = 0.080600694
            else:
                var43 = -0.2288261
        else:
            var43 = 0.22371079
    else:
        if input[2] < 171.5:
            var43 = -0.30947664
        else:
            if input[1] < 119.2:
                var43 = -0.21879502
            else:
                var43 = 0.023751503
    if input[2] < 390.1:
        if input[0] < 109.7:
            if input[0] < 96.6:
                var44 = 0.016065773
            else:
                var44 = -0.20679793
        else:
            if input[1] < 250.0:
                var44 = 0.20788285
            else:
                var44 = 0.010910522
    else:
        if input[0] < 76.8:
            if input[0] < 66.6:
                var44 = -0.17469645
            else:
                var44 = 0.158815
        else:
            if input[2] < 447.3:
                var44 = -0.37851617
            else:
                var44 = -0.03785649
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[3] < 9.0:
        if input[0] < 49.8:
            if input[2] < 106.5:
                var46 = 0.10008853
            else:
                var46 = -0.32740366
        else:
            if input[0] < 50.9:
                var46 = 0.1931704
            else:
                var46 = -0.025295246
    else:
        if input[2] < 137.3:
            var46 = -0.17287701
        else:
            if input[2] < 138.0:
                var46 = 0.20625101
            else:
                var46 = 0.046378564
    if input[1] < 306.6:
        if input[0] < 108.9:
            if input[0] < 91.5:
                var47 = -0.015582856
            else:
                var47 = 0.10762446
        else:
            if input[2] < 305.1:
                var47 = 0.15777695
            else:
                var47 = -0.36383137
    else:
        if input[0] < 136.0:
            var47 = -0.099470496
        else:
            var47 = 0.21547985
    if input[2] < 582.2:
        if input[1] < 207.5:
            if input[1] < 194.0:
                var48 = 0.0033168509
            else:
                var48 = -0.24285965
        else:
            if input[2] < 309.7:
                var48 = -0.118215196
            else:
                var48 = 0.090506986
    else:
        var48 = -0.113688506
    if input[2] < 390.1:
        if input[0] < 85.0:
            if input[0] < 50.9:
                var49 = 0.026348313
            else:
                var49 = -0.24416341
        else:
            if input[1] < 199.6:
                var49 = 0.24294275
            else:
                var49 = -0.035449445
    else:
        if input[0] < 76.8:
            if input[2] < 438.3:
                var49 = 0.12946132
            else:
                var49 = -0.029870031
        else:
            if input[2] < 447.3:
                var49 = -0.32225108
            else:
                var49 = -0.030101486
    if input[1] < 306.6:
        if input[0] < 96.6:
            if input[0] < 91.5:
                var50 = -0.01616764
            else:
                var50 = 0.20433863
        else:
            if input[1] < 199.6:
                var50 = 0.12207535
            else:
                var50 = -0.25343668
    else:
        if input[0] < 136.0:
            var50 = -0.070183575
        else:
            var50 = 0.20382385
    if input[1] < 137.0:
        if input[1] < 77.8:
            if input[0] < 44.8:
                var51 = -0.07597943
            else:
                var51 = 0.13420723
        else:
            if input[0] < 71.2:
                var51 = -0.30733624
            else:
                var51 = 0.11113646
    else:
        if input[1] < 138.1:
            var51 = 0.18584211
        else:
            if input[0] < 36.9:
                var51 = 0.18633677
            else:
                var51 = -0.03300585
    if input[1] < 207.5:
        if input[1] < 151.4:
            if input[2] < 248.2:
                var52 = -0.025687467
            else:
                var52 = 0.15508008
        else:
            if input[0] < 101.3:
                var52 = -0.31470856
            else:
                var52 = 0.04872587
    else:
        if input[2] < 448.2:
            if input[3] < 8.0:
                var52 = 0.028044712
            else:
                var52 = 0.19868667
        else:
            if input[2] < 524.5:
                var52 = -0.22285445
            else:
                var52 = 0.04417492
    if input[2] < 582.2:
        if input[2] < 563.4:
            if input[1] < 306.6:
                var53 = -0.01737307
            else:
                var53 = 0.108855404
        else:
            var53 = 0.18038307
    else:
        var53 = -0.09807557
    if input[0] < 36.9:
        if input[0] < 35.9:
            if input[1] < 26.1:
                var54 = 0.060267333
            else:
                var54 = -0.1542667
        else:
            var54 = 0.18119077
    else:
        if input[0] < 45.6:
            var54 = -0.19352417
        else:
            if input[1] < 59.3:
                var54 = 0.177014
            else:
                var54 = -0.010332992
    if input[1] < 207.5:
        if input[2] < 312.8:
            if input[0] < 101.3:
                var55 = -0.016602255
            else:
                var55 = 0.1664448
        else:
            var55 = -0.17323813
    else:
        if input[2] < 448.2:
            if input[2] < 309.7:
                var55 = -0.055634283
            else:
                var55 = 0.13502699
        else:
            if input[2] < 524.5:
                var55 = -0.20024359
            else:
                var55 = 0.036742497
    if input[2] < 390.1:
        if input[0] < 109.7:
            if input[1] < 199.6:
                var56 = 0.021515379
            else:
                var56 = -0.18689546
        else:
            if input[3] < 8.0:
                var56 = 0.017952142
            else:
                var56 = 0.20312531
    else:
        if input[0] < 76.8:
            if input[0] < 76.4:
                var56 = 0.007486696
            else:
                var56 = 0.13169208
        else:
            if input[2] < 563.4:
                var56 = -0.22034572
            else:
                var56 = 0.040664688
    if input[2] < 582.2:
        if input[2] < 563.4:
            if input[0] < 96.6:
                var57 = 0.02097227
            else:
                var57 = -0.067667395
        else:
            var57 = 0.16166522
    else:
        var57 = -0.09094146
    if input[0] < 109.7:
        if input[0] < 96.6:
            if input[0] < 91.5:
                var58 = -0.014469907
            else:
                var58 = 0.15081519
        else:
            if input[1] < 215.8:
                var58 = -0.20904575
            else:
                var58 = 0.044131
    else:
        if input[1] < 250.0:
            var58 = 0.20293303
        else:
            if input[1] < 316.2:
                var58 = -0.20955575
            else:
                var58 = 0.1336468
    if input[2] < 248.2:
        if input[0] < 47.2:
            if input[2] < 138.0:
                var59 = 0.098862745
            else:
                var59 = -0.07536886
        else:
            if input[0] < 72.8:
                var59 = -0.28368244
            else:
                var59 = 0.09161504
    else:
        if input[2] < 250.6:
            var59 = 0.20247377
        else:
            if input[0] < 67.3:
                var59 = -0.15915965
            else:
                var59 = 0.01764931
    if input[2] < 582.2:
        if input[1] < 137.0:
            if input[2] < 138.0:
                var60 = 0.020066503
            else:
                var60 = -0.15130499
        else:
            if input[3] < 9.0:
                var60 = 0.012558951
            else:
                var60 = 0.15060276
    else:
        var60 = -0.08958258
    if input[0] < 109.7:
        if input[0] < 96.6:
            if input[0] < 91.5:
                var61 = -0.012549284
            else:
                var61 = 0.13156192
        else:
            if input[1] < 199.6:
                var61 = 0.061672
            else:
                var61 = -0.19183975
    else:
        if input[1] < 306.6:
            if input[2] < 309.7:
                var61 = 0.032616917
            else:
                var61 = -0.13824515
        else:
            var61 = 0.16611175
    if input[2] < 582.2:
        if input[2] < 563.4:
            if input[2] < 390.1:
                var62 = 0.015438652
            else:
                var62 = -0.052863415
        else:
            var62 = 0.15830487
    else:
        var62 = -0.08070861
    if input[2] < 248.2:
        if input[0] < 47.2:
            if input[1] < 138.1:
                var63 = -0.013873848
            else:
                var63 = 0.15326783
        else:
            if input[0] < 72.8:
                var63 = -0.256797
            else:
                var63 = 0.09276333
    else:
        if input[2] < 250.6:
            var63 = 0.1857166
        else:
            if input[2] < 309.7:
                var63 = -0.10097338
            else:
                var63 = 0.023282342
    if input[0] < 109.7:
        if input[0] < 96.6:
            if input[1] < 215.8:
                var64 = 0.025969978
            else:
                var64 = -0.08740155
        else:
            if input[1] < 199.6:
                var64 = 0.05752923
            else:
                var64 = -0.16339767
    else:
        if input[1] < 250.0:
            var64 = 0.19136642
        else:
            if input[1] < 316.2:
                var64 = -0.16815865
            else:
                var64 = 0.100750126
    if input[0] < 67.3:
        if input[0] < 50.9:
            if input[0] < 49.8:
                var65 = -0.035640936
            else:
                var65 = 0.12674905
        else:
            var65 = -0.16166008
    else:
        if input[0] < 68.4:
            var65 = 0.14312008
        else:
            if input[1] < 199.6:
                var65 = 0.075771324
            else:
                var65 = -0.019454159
    if input[1] < 268.7:
        if input[2] < 372.6:
            if input[0] < 85.0:
                var66 = -0.026505033
            else:
                var66 = 0.070704155
        else:
            if input[0] < 68.4:
                var66 = 0.04931726
            else:
                var66 = -0.18167241
    else:
        if input[2] < 582.2:
            if input[0] < 111.7:
                var66 = 0.15618184
            else:
                var66 = -0.040345274
        else:
            var66 = -0.05175597
    if input[1] < 306.6:
        if input[0] < 104.4:
            if input[1] < 207.5:
                var67 = -0.019202951
            else:
                var67 = 0.09738845
        else:
            if input[2] < 305.1:
                var67 = 0.057799853
            else:
                var67 = -0.18488652
    else:
        if input[0] < 136.0:
            var67 = -0.1332033
        else:
            var67 = 0.1976312
    if input[3] < 9.0:
        if input[3] < 8.0:
            if input[2] < 435.3:
                var68 = -0.03914734
            else:
                var68 = 0.0882835
        else:
            if input[0] < 109.7:
                var68 = -0.15930042
            else:
                var68 = 0.04196462
    else:
        if input[1] < 145.7:
            var68 = -0.027527597
        else:
            var68 = 0.14219396
    if input[2] < 138.0:
        if input[2] < 137.3:
            if input[3] < 7.0:
                var69 = 0.06594803
            else:
                var69 = -0.16927698
        else:
            var69 = 0.18072301
    else:
        if input[0] < 49.8:
            if input[0] < 36.9:
                var69 = 0.07499583
            else:
                var69 = -0.2645089
        else:
            if input[1] < 138.1:
                var69 = 0.13679145
            else:
                var69 = -0.019268753
    if input[2] < 138.0:
        if input[2] < 137.3:
            if input[0] < 11.3:
                var70 = 0.055610623
            else:
                var70 = -0.06655984
        else:
            var70 = 0.16645935
    else:
        if input[0] < 49.8:
            if input[0] < 36.9:
                var70 = 0.063575655
            else:
                var70 = -0.24131994
        else:
            if input[1] < 138.1:
                var70 = 0.11546076
            else:
                var70 = -0.013792998
    if input[2] < 582.2:
        if input[2] < 524.5:
            if input[0] < 109.7:
                var71 = -0.029967654
            else:
                var71 = 0.096142635
        else:
            if input[0] < 96.6:
                var71 = 0.107176654
            else:
                var71 = 0.028608648
    else:
        var71 = -0.06948544
    if input[2] < 138.0:
        if input[0] < 45.6:
            var72 = -0.03277438
        else:
            if input[0] < 46.6:
                var72 = 0.16371542
            else:
                var72 = 0.033450086
    else:
        if input[1] < 137.0:
            var72 = -0.1160286
        else:
            if input[0] < 50.9:
                var72 = 0.09119621
            else:
                var72 = -0.013420408
    if input[2] < 390.1:
        if input[0] < 85.0:
            if input[0] < 50.9:
                var73 = 0.022611614
            else:
                var73 = -0.17402497
        else:
            if input[1] < 199.6:
                var73 = 0.21322252
            else:
                var73 = -0.0505512
    else:
        if input[2] < 524.5:
            if input[0] < 68.4:
                var73 = 0.06449392
            else:
                var73 = -0.15349597
        else:
            if input[1] < 292.5:
                var73 = 0.09500162
            else:
                var73 = -0.088469535
    if input[1] < 306.6:
        if input[0] < 136.0:
            if input[2] < 524.5:
                var74 = -0.017547568
            else:
                var74 = 0.1206208
        else:
            var74 = -0.1370801
    else:
        if input[0] < 136.0:
            var74 = -0.09829163
        else:
            var74 = 0.18773803
    if input[2] < 390.1:
        if input[2] < 309.7:
            if input[1] < 194.0:
                var75 = 0.030605767
            else:
                var75 = -0.14855368
        else:
            if input[1] < 207.5:
                var75 = 0.02203381
            else:
                var75 = 0.15718706
    else:
        if input[0] < 76.8:
            if input[2] < 438.3:
                var75 = 0.08959641
            else:
                var75 = -0.030814169
        else:
            if input[2] < 563.4:
                var75 = -0.15076116
            else:
                var75 = 0.048606377
    if input[0] < 109.7:
        if input[3] < 7.0:
            if input[2] < 242.4:
                var76 = -0.021764245
            else:
                var76 = 0.13532089
        else:
            if input[2] < 524.5:
                var76 = -0.07478987
            else:
                var76 = 0.04761724
    else:
        if input[2] < 448.2:
            if input[1] < 250.0:
                var76 = 0.17733541
            else:
                var76 = 0.03232435
        else:
            var76 = -0.08621131
    if input[1] < 306.6:
        if input[1] < 250.0:
            if input[0] < 109.7:
                var77 = -0.009115764
            else:
                var77 = 0.16388832
        else:
            if input[0] < 101.3:
                var77 = 0.024627265
            else:
                var77 = -0.16156477
    else:
        if input[0] < 136.0:
            var77 = -0.0955681
        else:
            var77 = 0.17975631
    if input[0] < 47.2:
        if input[2] < 138.0:
            if input[0] < 45.6:
                var78 = -0.024330871
            else:
                var78 = 0.20601608
        else:
            var78 = -0.067267515
    else:
        if input[0] < 67.3:
            if input[2] < 246.3:
                var78 = -0.20493
            else:
                var78 = 0.024441445
        else:
            if input[2] < 582.2:
                var78 = 0.03223683
            else:
                var78 = -0.061675083
    if input[0] < 47.2:
        if input[2] < 138.0:
            if input[0] < 45.6:
                var79 = -0.018956004
            else:
                var79 = 0.19115598
        else:
            var79 = -0.05397985
    else:
        if input[0] < 67.3:
            if input[2] < 246.3:
                var79 = -0.18694912
            else:
                var79 = 0.020377323
        else:
            if input[3] < 7.0:
                var79 = -0.063277476
            else:
                var79 = 0.026874272
    if input[0] < 36.9:
        if input[1] < 76.8:
            var80 = 0.0011210628
        else:
            var80 = 0.11769311
    else:
        if input[1] < 306.6:
            if input[1] < 77.8:
                var80 = 0.057362743
            else:
                var80 = -0.04613234
        else:
            if input[0] < 136.0:
                var80 = -0.08248824
            else:
                var80 = 0.16504566
    if input[2] < 390.1:
        if input[0] < 85.0:
            if input[0] < 47.2:
                var81 = 0.029420124
            else:
                var81 = -0.09529917
        else:
            if input[1] < 199.6:
                var81 = 0.1960123
            else:
                var81 = -0.032153547
    else:
        if input[0] < 76.8:
            if input[2] < 438.3:
                var81 = 0.08598643
            else:
                var81 = -0.026333092
        else:
            if input[2] < 563.4:
                var81 = -0.13897036
            else:
                var81 = 0.047669344
    if input[2] < 582.2:
        if input[1] < 268.7:
            if input[0] < 96.6:
                var82 = 0.01754877
            else:
                var82 = -0.0735263
        else:
            if input[0] < 111.7:
                var82 = 0.13752504
            else:
                var82 = -0.041703045
    else:
        var82 = -0.07171769
    if input[1] < 306.6:
        if input[0] < 104.4:
            if input[0] < 91.5:
                var83 = -0.011121742
            else:
                var83 = 0.10798316
        else:
            if input[2] < 305.1:
                var83 = 0.049332205
            else:
                var83 = -0.14166372
    else:
        if input[0] < 136.0:
            var83 = -0.07148169
        else:
            var83 = 0.16071418
    if input[0] < 109.7:
        if input[3] < 7.0:
            if input[2] < 242.4:
                var84 = -0.014401949
            else:
                var84 = 0.12658314
        else:
            if input[2] < 524.5:
                var84 = -0.07108537
            else:
                var84 = 0.049542483
    else:
        if input[1] < 250.0:
            var84 = 0.1536623
        else:
            var84 = -0.025163302
    if input[2] < 582.2:
        if input[1] < 268.7:
            if input[1] < 215.8:
                var85 = 0.0170648
            else:
                var85 = -0.08960983
        else:
            if input[1] < 285.8:
                var85 = 0.12508143
            else:
                var85 = 0.0065228045
    else:
        var85 = -0.06537424
    if input[0] < 109.7:
        if input[0] < 96.6:
            if input[1] < 215.8:
                var86 = 0.03537675
            else:
                var86 = -0.11078732
        else:
            if input[2] < 305.1:
                var86 = -0.1278339
            else:
                var86 = -0.0037350077
    else:
        if input[2] < 448.2:
            var86 = 0.113281064
        else:
            var86 = -0.0713689
    if input[1] < 306.6:
        if input[0] < 96.6:
            if input[0] < 88.9:
                var87 = -0.014813329
            else:
                var87 = 0.11540693
        else:
            if input[1] < 199.6:
                var87 = 0.084695145
            else:
                var87 = -0.13477036
    else:
        var87 = 0.058209572
    if input[0] < 109.7:
        if input[0] < 36.9:
            if input[1] < 64.0:
                var88 = -0.003430681
            else:
                var88 = 0.088948295
        else:
            if input[2] < 524.5:
                var88 = -0.047245096
            else:
                var88 = 0.047364812
    else:
        if input[1] < 306.6:
            var88 = -0.036666606
        else:
            var88 = 0.120599516
    if input[2] < 582.2:
        if input[1] < 268.7:
            if input[2] < 330.0:
                var89 = 0.021589478
            else:
                var89 = -0.05775978
        else:
            if input[0] < 109.7:
                var89 = 0.11672193
            else:
                var89 = -0.02826815
    else:
        var89 = -0.060290948
    if input[0] < 109.7:
        if input[3] < 7.0:
            if input[2] < 242.4:
                var90 = -0.019981034
            else:
                var90 = 0.1087985
        else:
            if input[3] < 9.0:
                var90 = -0.056670506
            else:
                var90 = 0.035092533
    else:
        if input[1] < 306.6:
            var90 = -0.027515158
        else:
            var90 = 0.11038741
    if input[2] < 582.2:
        if input[0] < 67.3:
            if input[2] < 138.0:
                var91 = 0.02522438
            else:
                var91 = -0.06524873
        else:
            if input[3] < 7.0:
                var91 = -0.07217637
            else:
                var91 = 0.05956324
    else:
        var91 = -0.054421604
    if input[2] < 172.7:
        if input[1] < 59.3:
            if input[1] < 26.1:
                var92 = 0.04461528
            else:
                var92 = -0.011332438
        else:
            var92 = -0.09583708
    else:
        if input[2] < 250.6:
            if input[3] < 8.0:
                var92 = 0.0036336046
            else:
                var92 = 0.12254528
        else:
            if input[1] < 207.5:
                var92 = -0.062141884
            else:
                var92 = 0.01315137
    if input[2] < 390.1:
        if input[0] < 85.0:
            if input[0] < 47.2:
                var93 = 0.015865931
            else:
                var93 = -0.0828879
        else:
            if input[1] < 199.6:
                var93 = 0.1808403
            else:
                var93 = -0.031735864
    else:
        if input[0] < 76.8:
            var93 = 0.048845917
        else:
            if input[2] < 563.4:
                var93 = -0.13750646
            else:
                var93 = 0.046501346
    if input[0] < 109.7:
        if input[3] < 7.0:
            if input[2] < 242.4:
                var94 = -0.018719781
            else:
                var94 = 0.11178355
        else:
            if input[2] < 524.5:
                var94 = -0.0561451
            else:
                var94 = 0.0381309
    else:
        if input[2] < 390.1:
            var94 = 0.104361996
        else:
            var94 = -0.031534247
    if input[2] < 582.2:
        if input[0] < 45.6:
            if input[2] < 68.2:
                var95 = 0.036639698
            else:
                var95 = -0.074763425
        else:
            if input[1] < 77.8:
                var95 = 0.11356874
            else:
                var95 = 0.00048186717
    else:
        var95 = -0.054857936
    if input[1] < 137.0:
        if input[2] < 138.0:
            if input[0] < 45.6:
                var96 = -0.036644414
            else:
                var96 = 0.08703794
        else:
            var96 = -0.10448598
    else:
        if input[0] < 68.4:
            if input[1] < 151.4:
                var96 = 0.11690993
            else:
                var96 = 0.019508773
        else:
            if input[0] < 91.5:
                var96 = -0.11118639
            else:
                var96 = 0.018301439
    if input[2] < 172.7:
        if input[1] < 26.1:
            var97 = 0.040028952
        else:
            if input[2] < 136.5:
                var97 = -0.088613406
            else:
                var97 = -0.014524259
    else:
        if input[3] < 9.0:
            if input[0] < 67.3:
                var97 = -0.06474103
            else:
                var97 = 0.016217753
        else:
            var97 = 0.100978345
    if input[2] < 582.2:
        if input[2] < 435.3:
            if input[1] < 199.6:
                var98 = 0.028161671
            else:
                var98 = -0.09367913
        else:
            if input[0] < 76.8:
                var98 = 0.095429294
            else:
                var98 = -0.010132261
    else:
        var98 = -0.05129407
    if input[0] < 109.7:
        if input[0] < 96.6:
            if input[1] < 215.8:
                var99 = 0.026367666
            else:
                var99 = -0.095075175
        else:
            if input[1] < 200.6:
                var99 = -0.012054532
            else:
                var99 = -0.087086715
    else:
        if input[1] < 306.6:
            var99 = -0.033896953
        else:
            var99 = 0.10963448
    if input[0] < 67.3:
        if input[0] < 47.2:
            if input[2] < 138.0:
                var100 = 0.037853822
            else:
                var100 = -0.07053259
        else:
            var100 = -0.07934206
    else:
        if input[3] < 7.0:
            var100 = -0.059131663
        else:
            if input[0] < 109.7:
                var100 = 0.00033029867
            else:
                var100 = 0.09715022
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]


# --- Logistic Regression Meta-Classifier for Stacking ---
COEF_RF = 4.010366398368077
COEF_XGB = 0.41599063767920186
INTERCEPT = -1.4605369023434016

def score_konkan_final(input_array):
    p_rf = score_konkan_rf(input_array)[1]
    p_xgb = score_konkan_xgb(input_array)[1]
    
    # Stacking combining logic (meta-classifier Logistic Regression)
    z = (COEF_RF * p_rf) + (COEF_XGB * p_xgb) + INTERCEPT
    # Sigmoid function
    return 1.0 / (1.0 + math.exp(-z))
