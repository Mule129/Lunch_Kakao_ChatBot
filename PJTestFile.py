import json
a = {"mealServiceDietInfo":[{"head":[{"list_total_count":1},{"RESULT":{"CODE":"INFO-000","MESSAGE":"정상 처리되었습니다."}}]},{"row":[{"ATPT_OFCDC_SC_CODE":"N10","ATPT_OFCDC_SC_NM":"충청남도교육청","SD_SCHUL_CODE":"8140265","SCHUL_NM":"천안청수고등학교","MMEAL_SC_CODE":"2","MMEAL_SC_NM":"중식","MLSV_YMD":"20220510","MLSV_FGR":"440","DDISH_NM":"참치주먹밥  (1.5.9.10.13.)우동장국  (1.5.6.9.13.)신전떡볶이  (1.2.5.6.12.13.16.18.)탕수육  (1.5.6.10.13.)새우+김말이+어묵튀김  (1.5.6.9.12.16.)단무지  딸기  쿨피스파인맛  (2.13.)","ORPLC_INFO":"쌀 : 국내산김치류 : 국 돼지고기 : 국내산닭고기 : 국내산오리고기 : 국내산쇠고기 식육가공품 : 국내산돼지고기 식육가공품 : 국내산닭고기 식육가공품 : 국내산오리고기 가공품 : 국내산낙지 : 국내산고등어 : 국내산갈치 : 국내산오징어 : 국내산꽃게 : 국내산참조기 : 국내산콩 : 국내산","CAL_INFO":"962.9 Kcal","NTR_I":"비타민A(R.E) : 145.6티아민(mg) : 0.3리보플라빈(mg) : 0.6비타민C(mg) : 83.4칼슘(mg) : 427.7철분(mg) : 19.0","MLSV_FROM_YMD":"20220510","MLSV_TO_YMD":"20220510"}]}]} 

with open("./newfile.json","w") as file:
    json.dump(a, file, ensure_ascii = True, indent=4)
a = {"test":a}
a = dict(a)
print(a)