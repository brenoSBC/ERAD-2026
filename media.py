print("===========================")
print("========== FD  ============")
print("===========================\n")

omp_fd121_1 = 69842.81988230
omp_fd121_2 = 77914.70330006
omp_fd121_3 = 70678.16605777

rsp_fd121_1 = 62156.52471175
rsp_fd121_2 = 57750.91929601
rsp_fd121_3 = 59906.06076081

fd121_omp_media = (omp_fd121_1 + omp_fd121_2 + omp_fd121_3) / 3
fd121_rsp_media = (rsp_fd121_1 + rsp_fd121_2 + rsp_fd121_3) / 3

fd121_diferenca_relativa = ((fd121_rsp_media - fd121_omp_media) / fd121_omp_media) * 100

print("OMP -> Media FD_121: ", fd121_omp_media)
print("RSP -> Média FD_121: ", fd121_rsp_media)
print("Diferença relativa FD_121: ", fd121_diferenca_relativa, "%")



print("\n\n===========================")
print("========== SA  ============")
print("===========================\n")

omp_sa111_1 = 29658.07122563
omp_sa111_2 = 30466.06116660
omp_sa111_3 = 28807.51365637

rsp_sa111_1 = 26643.23727877
rsp_sa111_2 = 26096.52823757
rsp_sa111_3 = 27201.73482818

sa111_omp_media = (omp_sa111_1 + omp_sa111_2 + omp_sa111_3) / 3
sa111_rsp_media = (rsp_sa111_1 + rsp_sa111_2 + rsp_sa111_3) / 3

sa111_diferenca_relativa = ((sa111_rsp_media - sa111_omp_media) / sa111_omp_media) * 100

print("OMP -> Media SA_111: ", sa111_omp_media)
print("RSP -> Média SA_111: ", sa111_rsp_media)
print("Diferença relativa SA_111: ", sa111_diferenca_relativa, "%")

print("\n")

omp_sa131_1 = 11207.68938162
omp_sa131_2 = 11274.42535585
omp_sa131_3 = 10771.31373085

rsp_sa131_1 = 17550.08107974
rsp_sa131_2 = 18563.05503453
rsp_sa131_3 = 19013.48961194

sa131_omp_media = (omp_sa131_1 + omp_sa131_2 + omp_sa131_3) / 3
sa131_rsp_media = (rsp_sa131_1 + rsp_sa131_2 + rsp_sa131_3) / 3

sa131_diferenca_relativa = ((sa131_rsp_media - sa131_omp_media) / sa131_omp_media) * 100

print("OMP -> Media SA_131: ", sa131_omp_media)
print("RSP -> Média SA_131: ", sa131_rsp_media)
print("Diferença relativa SA_131: ", sa131_diferenca_relativa, "%")



print("\n\n===========================")
print("========== SD  ============")
print("===========================\n")

omp_sd1111_1 = 13129.62281082
omp_sd1111_2 = 13200.66682347
omp_sd1111_3 = 13401.47064265

rsp_sd1111_1 = 11731.10368606
rsp_sd1111_2 = 11982.84244108
rsp_sd1111_3 = 12492.19655783

sd1111_omp_media = (omp_sd1111_1 + omp_sd1111_2 + omp_sd1111_3) / 3
sd1111_rsp_media = (rsp_sd1111_1 + rsp_sd1111_2 + rsp_sd1111_3) / 3

sd1111_diferenca_relativa = ((sd1111_rsp_media - sd1111_omp_media) / sd1111_omp_media) * 100

print("OMP -> Media SD_1111: ", sd1111_omp_media)
print("RSP -> Média SD_1111: ", sd1111_rsp_media)
print("Diferença relativa SD_1111: ", sd1111_diferenca_relativa, "%")



print("\n\n===========================")
print("========== TM  ============")
print("===========================\n")

omp_tm1441_1 = 969.26710117
omp_tm1441_2 = 967.57270316
omp_tm1441_3 = 973.01019940

rsp_tm1441_1 = 978.51328328
rsp_tm1441_2 = 970.82330600
rsp_tm1441_3 = 973.33140668

tm1441_omp_media = (omp_tm1441_1 + omp_tm1441_2 + omp_tm1441_3) / 3
tm1441_rsp_media = (rsp_tm1441_1 + rsp_tm1441_2 + rsp_tm1441_3) / 3

tm1441_diferenca_relativa = ((tm1441_rsp_media - tm1441_omp_media) / tm1441_omp_media) * 100

print("OMP -> Media TM_1441: ", tm1441_omp_media)
print("RSP -> Média TM_1441: ", tm1441_rsp_media)
print("Diferença relativa TM_1441: ", tm1441_diferenca_relativa, "%")