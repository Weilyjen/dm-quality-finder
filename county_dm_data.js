const COUNTY_DM_DATA = {
  "updated": "115Q1",
  "source": "衛生福利部中央健康保險署公開品質資訊 (糖尿病給付改善方案)",
  "national": {
    "total_patients": 1916370,
    "total_enrolled": 960992,
    "total_institutions": 7765,
    "national_care_rate": 50.15,
    "hosp_count": 413,
    "hosp_patients": 1010574,
    "hosp_enrolled": 550002,
    "hosp_care_rate": 54.42,
    "clin_count": 7352,
    "clin_patients": 905796,
    "clin_enrolled": 410990,
    "clin_care_rate": 45.37,
    "active_clin_count": 1372,
    "active_clin_avg_rate": 66.76,
    "active_clin_med_rate": 70.69
  },
  "counties": [
    {
      "city": "新北市",
      "region": "北部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 1206,
      "total_patients": 262418,
      "total_enrolled": 132903,
      "total_care_rate": 50.65,
      "total_mean_rate": 13.83,
      "hosp_count": 42,
      "hosp_patients": 119663,
      "hosp_enrolled": 68871,
      "hosp_care_rate": 57.55,
      "hosp_mean_rate": 28.38,
      "hosp_patient_share": 45.6,
      "hosp_enrolled_share": 51.82,
      "hosp_avg_patients": 2849.1,
      "breakdown_med_center": {
        "count": 3,
        "patients": 45958,
        "enrolled": 27693
      },
      "breakdown_reg_hosp": {
        "count": 8,
        "patients": 55818,
        "enrolled": 31892
      },
      "breakdown_dist_hosp": {
        "count": 31,
        "patients": 17887,
        "enrolled": 9286
      },
      "clin_count": 1164,
      "clin_patients": 142755,
      "clin_enrolled": 64032,
      "clin_care_rate": 44.85,
      "clin_mean_rate": 13.3,
      "clin_patient_share": 54.4,
      "clin_enrolled_share": 48.18,
      "clin_avg_patients": 122.6,
      "clin_active_count": 224,
      "clin_active_care_rate": 71.04,
      "top_clinics": [
        {
          "name": "蘇景傑診所",
          "code": "3531054193",
          "dist": "新店區",
          "num": 2642,
          "den": 2987,
          "rate": 88.4
        },
        {
          "name": "中和班廷謝安慈診所",
          "code": "3531045943",
          "dist": "中和區",
          "num": 1641,
          "den": 2025,
          "rate": 81.0
        },
        {
          "name": "翰生診所",
          "code": "3531012695",
          "dist": "板橋區",
          "num": 1251,
          "den": 1603,
          "rate": 78.0
        }
      ],
      "top_hosps": [
        {
          "name": "醫療財團法人徐元智先生醫藥基金會亞東紀念醫院",
          "code": "1131010011",
          "type": "醫學中心",
          "num": 14463,
          "den": 21727,
          "rate": 66.6
        },
        {
          "name": "衛生福利部雙和醫院〈委託臺北醫學大學興建經營〉",
          "code": "1331040513",
          "type": "醫學中心",
          "num": 7114,
          "den": 13616,
          "rate": 52.2
        },
        {
          "name": "佛教慈濟醫療財團法人台北慈濟醫院",
          "code": "1131050515",
          "type": "醫學中心",
          "num": 6116,
          "den": 10615,
          "rate": 57.6
        }
      ],
      "rank_patients": 1,
      "rank_care_rate": 11
    },
    {
      "city": "高雄市",
      "region": "南部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 1143,
      "total_patients": 254132,
      "total_enrolled": 121836,
      "total_care_rate": 47.94,
      "total_mean_rate": 10.71,
      "hosp_count": 73,
      "hosp_patients": 122070,
      "hosp_enrolled": 66127,
      "hosp_care_rate": 54.17,
      "hosp_mean_rate": 30.15,
      "hosp_patient_share": 48.03,
      "hosp_enrolled_share": 54.28,
      "hosp_avg_patients": 1672.2,
      "breakdown_med_center": {
        "count": 4,
        "patients": 50228,
        "enrolled": 24443
      },
      "breakdown_reg_hosp": {
        "count": 10,
        "patients": 31721,
        "enrolled": 19021
      },
      "breakdown_dist_hosp": {
        "count": 59,
        "patients": 40121,
        "enrolled": 22663
      },
      "clin_count": 1070,
      "clin_patients": 132062,
      "clin_enrolled": 55709,
      "clin_care_rate": 42.18,
      "clin_mean_rate": 9.38,
      "clin_patient_share": 51.97,
      "clin_enrolled_share": 45.72,
      "clin_avg_patients": 123.4,
      "clin_active_count": 148,
      "clin_active_care_rate": 74.03,
      "top_clinics": [
        {
          "name": "文德診所",
          "code": "3507010150",
          "dist": "鳳山區",
          "num": 2758,
          "den": 2898,
          "rate": 95.2
        },
        {
          "name": "健維診所",
          "code": "3502081793",
          "dist": "苓雅區",
          "num": 2654,
          "den": 2922,
          "rate": 90.8
        },
        {
          "name": "川惠診所",
          "code": "3507321087",
          "dist": "三民區",
          "num": 2200,
          "den": 2527,
          "rate": 87.1
        }
      ],
      "top_hosps": [
        {
          "name": "長庚醫療財團法人高雄長庚紀念醫院",
          "code": "1142100017",
          "type": "醫學中心",
          "num": 9728,
          "den": 18038,
          "rate": 53.9
        },
        {
          "name": "阮綜合醫療社團法人阮綜合醫院",
          "code": "0902080013",
          "type": "區域醫院",
          "num": 5121,
          "den": 6793,
          "rate": 75.4
        },
        {
          "name": "義大醫療財團法人義大醫院",
          "code": "1142120001",
          "type": "醫學中心",
          "num": 5117,
          "den": 8529,
          "rate": 60.0
        }
      ],
      "rank_patients": 2,
      "rank_care_rate": 15
    },
    {
      "city": "臺中市",
      "region": "中部",
      "tier_type": "均衡照護",
      "tier_color": "#0284c7",
      "total_institutions": 1116,
      "total_patients": 237083,
      "total_enrolled": 111687,
      "total_care_rate": 47.11,
      "total_mean_rate": 12.96,
      "hosp_count": 55,
      "hosp_patients": 128043,
      "hosp_enrolled": 63967,
      "hosp_care_rate": 49.96,
      "hosp_mean_rate": 33.84,
      "hosp_patient_share": 54.01,
      "hosp_enrolled_share": 57.27,
      "hosp_avg_patients": 2328.1,
      "breakdown_med_center": {
        "count": 3,
        "patients": 40012,
        "enrolled": 15714
      },
      "breakdown_reg_hosp": {
        "count": 11,
        "patients": 58914,
        "enrolled": 33171
      },
      "breakdown_dist_hosp": {
        "count": 41,
        "patients": 29117,
        "enrolled": 15082
      },
      "clin_count": 1061,
      "clin_patients": 109040,
      "clin_enrolled": 47720,
      "clin_care_rate": 43.76,
      "clin_mean_rate": 11.88,
      "clin_patient_share": 45.99,
      "clin_enrolled_share": 42.73,
      "clin_avg_patients": 102.8,
      "clin_active_count": 189,
      "clin_active_care_rate": 74.47,
      "top_clinics": [
        {
          "name": "陳瑞明診所",
          "code": "3503020141",
          "dist": "東勢區",
          "num": 1764,
          "den": 1988,
          "rate": 88.7
        },
        {
          "name": "楊朝弘診所",
          "code": "3503270016",
          "dist": "西屯區",
          "num": 1694,
          "den": 1839,
          "rate": 92.1
        },
        {
          "name": "啟恩診所",
          "code": "3536060048",
          "dist": "(原縣)梧棲區",
          "num": 1465,
          "den": 2066,
          "rate": 70.9
        }
      ],
      "top_hosps": [
        {
          "name": "童綜合醫療社團法人童綜合醫院",
          "code": "0936060016",
          "type": "區域醫院",
          "num": 7080,
          "den": 11262,
          "rate": 62.9
        },
        {
          "name": "臺中榮民總醫院",
          "code": "0617060018",
          "type": "醫學中心",
          "num": 6320,
          "den": 15826,
          "rate": 39.9
        },
        {
          "name": "中山醫學大學附設醫院",
          "code": "1317040011",
          "type": "醫學中心",
          "num": 4856,
          "den": 10808,
          "rate": 44.9
        }
      ],
      "rank_patients": 3,
      "rank_care_rate": 16
    },
    {
      "city": "臺北市",
      "region": "北部",
      "tier_type": "醫院高度集中",
      "tier_color": "#f59e0b",
      "total_institutions": 643,
      "total_patients": 232285,
      "total_enrolled": 113634,
      "total_care_rate": 48.92,
      "total_mean_rate": 10.52,
      "hosp_count": 29,
      "hosp_patients": 177347,
      "hosp_enrolled": 92512,
      "hosp_care_rate": 52.16,
      "hosp_mean_rate": 45.28,
      "hosp_patient_share": 76.35,
      "hosp_enrolled_share": 81.41,
      "hosp_avg_patients": 6115.4,
      "breakdown_med_center": {
        "count": 7,
        "patients": 98063,
        "enrolled": 47965
      },
      "breakdown_reg_hosp": {
        "count": 8,
        "patients": 56999,
        "enrolled": 33727
      },
      "breakdown_dist_hosp": {
        "count": 14,
        "patients": 22285,
        "enrolled": 10820
      },
      "clin_count": 614,
      "clin_patients": 54938,
      "clin_enrolled": 21122,
      "clin_care_rate": 38.45,
      "clin_mean_rate": 8.88,
      "clin_patient_share": 23.65,
      "clin_enrolled_share": 18.59,
      "clin_avg_patients": 89.5,
      "clin_active_count": 85,
      "clin_active_care_rate": 66.2,
      "top_clinics": [
        {
          "name": "榮陽安心診所",
          "code": "3501163465",
          "dist": "北投區",
          "num": 1840,
          "den": 2184,
          "rate": 84.2
        },
        {
          "name": "好甘心診所",
          "code": "3501186208",
          "dist": "中正區",
          "num": 1075,
          "den": 1656,
          "rate": 64.9
        },
        {
          "name": "國泰醫療財團法人內湖國泰診所",
          "code": "4001110018",
          "dist": "內湖區",
          "num": 1037,
          "den": 1580,
          "rate": 65.6
        }
      ],
      "top_hosps": [
        {
          "name": "臺北市立聯合醫院",
          "code": "0101090517",
          "type": "區域醫院",
          "num": 20938,
          "den": 29034,
          "rate": 72.1
        },
        {
          "name": "三軍總醫院附設民眾診療服務處",
          "code": "0501110514",
          "type": "醫學中心",
          "num": 8368,
          "den": 13770,
          "rate": 60.8
        },
        {
          "name": "台灣基督長老教會馬偕醫療財團法人馬偕紀念醫院",
          "code": "1101100011",
          "type": "醫學中心",
          "num": 8351,
          "den": 22900,
          "rate": 36.5
        }
      ],
      "rank_patients": 4,
      "rank_care_rate": 13
    },
    {
      "city": "桃園市",
      "region": "北部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 601,
      "total_patients": 195235,
      "total_enrolled": 108537,
      "total_care_rate": 55.59,
      "total_mean_rate": 17.76,
      "hosp_count": 31,
      "hosp_patients": 96828,
      "hosp_enrolled": 54615,
      "hosp_care_rate": 56.4,
      "hosp_mean_rate": 39.21,
      "hosp_patient_share": 49.6,
      "hosp_enrolled_share": 50.32,
      "hosp_avg_patients": 3123.5,
      "breakdown_med_center": {
        "count": 1,
        "patients": 25973,
        "enrolled": 12919
      },
      "breakdown_reg_hosp": {
        "count": 9,
        "patients": 51225,
        "enrolled": 30856
      },
      "breakdown_dist_hosp": {
        "count": 21,
        "patients": 19630,
        "enrolled": 10840
      },
      "clin_count": 570,
      "clin_patients": 98407,
      "clin_enrolled": 53922,
      "clin_care_rate": 54.79,
      "clin_mean_rate": 16.59,
      "clin_patient_share": 50.4,
      "clin_enrolled_share": 49.68,
      "clin_avg_patients": 172.6,
      "clin_active_count": 135,
      "clin_active_care_rate": 76.47,
      "top_clinics": [
        {
          "name": "姜博文診所",
          "code": "3532040438",
          "dist": "楊梅區",
          "num": 1829,
          "den": 2244,
          "rate": 81.5
        },
        {
          "name": "光文診所",
          "code": "3532016928",
          "dist": "桃園區",
          "num": 1770,
          "den": 2118,
          "rate": 83.6
        },
        {
          "name": "活力診所",
          "code": "3532026540",
          "dist": "中壢區",
          "num": 1740,
          "den": 1923,
          "rate": 90.5
        }
      ],
      "top_hosps": [
        {
          "name": "長庚醫療財團法人林口長庚紀念醫院",
          "code": "1132070011",
          "type": "醫學中心",
          "num": 12919,
          "den": 25973,
          "rate": 49.7
        },
        {
          "name": "衛生福利部桃園醫院",
          "code": "0132010014",
          "type": "區域醫院",
          "num": 7198,
          "den": 10374,
          "rate": 69.4
        },
        {
          "name": "長庚醫療財團法人桃園長庚紀念醫院",
          "code": "1132071036",
          "type": "區域醫院",
          "num": 5548,
          "den": 11483,
          "rate": 48.3
        }
      ],
      "rank_patients": 5,
      "rank_care_rate": 3
    },
    {
      "city": "臺南市",
      "region": "南部",
      "tier_type": "基層高度主導",
      "tier_color": "#10b981",
      "total_institutions": 741,
      "total_patients": 160105,
      "total_enrolled": 81885,
      "total_care_rate": 51.14,
      "total_mean_rate": 13.39,
      "hosp_count": 30,
      "hosp_patients": 66517,
      "hosp_enrolled": 37572,
      "hosp_care_rate": 56.48,
      "hosp_mean_rate": 38.77,
      "hosp_patient_share": 41.55,
      "hosp_enrolled_share": 45.88,
      "hosp_avg_patients": 2217.2,
      "breakdown_med_center": {
        "count": 2,
        "patients": 22605,
        "enrolled": 13240
      },
      "breakdown_reg_hosp": {
        "count": 6,
        "patients": 27134,
        "enrolled": 15740
      },
      "breakdown_dist_hosp": {
        "count": 22,
        "patients": 16778,
        "enrolled": 8592
      },
      "clin_count": 711,
      "clin_patients": 93588,
      "clin_enrolled": 44313,
      "clin_care_rate": 47.35,
      "clin_mean_rate": 12.32,
      "clin_patient_share": 58.45,
      "clin_enrolled_share": 54.12,
      "clin_avg_patients": 131.6,
      "clin_active_count": 125,
      "clin_active_care_rate": 74.47,
      "top_clinics": [
        {
          "name": "永德康內科診所",
          "code": "3505310335",
          "dist": "永康區",
          "num": 2143,
          "den": 2719,
          "rate": 78.8
        },
        {
          "name": "仁欣診所",
          "code": "3505350651",
          "dist": "北區",
          "num": 2067,
          "den": 2436,
          "rate": 84.9
        },
        {
          "name": "周劍文診所",
          "code": "3505310273",
          "dist": "永康區",
          "num": 1821,
          "den": 2126,
          "rate": 85.7
        }
      ],
      "top_hosps": [
        {
          "name": "奇美醫療財團法人奇美醫院",
          "code": "1141310019",
          "type": "醫學中心",
          "num": 6818,
          "den": 8021,
          "rate": 85.0
        },
        {
          "name": "國立成功大學醫學院附設醫院",
          "code": "0421040011",
          "type": "醫學中心",
          "num": 6422,
          "den": 14584,
          "rate": 44.0
        },
        {
          "name": "台南市立醫院(委託秀傳醫療社團法人經營)",
          "code": "0905320023",
          "type": "區域醫院",
          "num": 5942,
          "den": 10159,
          "rate": 58.5
        }
      ],
      "rank_patients": 6,
      "rank_care_rate": 9
    },
    {
      "city": "彰化縣",
      "region": "中部",
      "tier_type": "醫院高度集中",
      "tier_color": "#f59e0b",
      "total_institutions": 369,
      "total_patients": 110958,
      "total_enrolled": 57111,
      "total_care_rate": 51.47,
      "total_mean_rate": 14.48,
      "hosp_count": 25,
      "hosp_patients": 67636,
      "hosp_enrolled": 38083,
      "hosp_care_rate": 56.31,
      "hosp_mean_rate": 32.87,
      "hosp_patient_share": 60.96,
      "hosp_enrolled_share": 66.68,
      "hosp_avg_patients": 2705.4,
      "breakdown_med_center": {
        "count": 1,
        "patients": 12583,
        "enrolled": 7034
      },
      "breakdown_reg_hosp": {
        "count": 3,
        "patients": 17277,
        "enrolled": 10969
      },
      "breakdown_dist_hosp": {
        "count": 21,
        "patients": 37776,
        "enrolled": 20080
      },
      "clin_count": 344,
      "clin_patients": 43322,
      "clin_enrolled": 19028,
      "clin_care_rate": 43.92,
      "clin_mean_rate": 13.14,
      "clin_patient_share": 39.04,
      "clin_enrolled_share": 33.32,
      "clin_avg_patients": 125.9,
      "clin_active_count": 72,
      "clin_active_care_rate": 64.73,
      "top_clinics": [
        {
          "name": "謝立偉診所",
          "code": "3537031550",
          "dist": "和美鎮",
          "num": 1794,
          "den": 2106,
          "rate": 85.2
        },
        {
          "name": "順心診所",
          "code": "3537013696",
          "dist": "彰化市",
          "num": 1039,
          "den": 1142,
          "rate": 91.0
        },
        {
          "name": "南恩內科診所",
          "code": "3537061530",
          "dist": "溪湖鎮",
          "num": 952,
          "den": 1246,
          "rate": 76.4
        }
      ],
      "top_hosps": [
        {
          "name": "彰化基督教醫療財團法人彰化基督教醫院",
          "code": "1137010024",
          "type": "醫學中心",
          "num": 7034,
          "den": 12583,
          "rate": 55.9
        },
        {
          "name": "彰化基督教醫療財團法人員林基督教醫院",
          "code": "1137050019",
          "type": "地區醫院",
          "num": 6959,
          "den": 13278,
          "rate": 52.4
        },
        {
          "name": "秀傳醫療社團法人秀傳紀念醫院",
          "code": "0937010019",
          "type": "區域醫院",
          "num": 4649,
          "den": 8238,
          "rate": 56.4
        }
      ],
      "rank_patients": 7,
      "rank_care_rate": 7
    },
    {
      "city": "屏東縣",
      "region": "南部",
      "tier_type": "基層高度主導",
      "tier_color": "#10b981",
      "total_institutions": 326,
      "total_patients": 72155,
      "total_enrolled": 35991,
      "total_care_rate": 49.88,
      "total_mean_rate": 15.96,
      "hosp_count": 22,
      "hosp_patients": 28345,
      "hosp_enrolled": 15819,
      "hosp_care_rate": 55.81,
      "hosp_mean_rate": 41.85,
      "hosp_patient_share": 39.28,
      "hosp_enrolled_share": 43.95,
      "hosp_avg_patients": 1288.4,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 5,
        "patients": 17423,
        "enrolled": 9771
      },
      "breakdown_dist_hosp": {
        "count": 17,
        "patients": 10922,
        "enrolled": 6048
      },
      "clin_count": 304,
      "clin_patients": 43810,
      "clin_enrolled": 20172,
      "clin_care_rate": 46.04,
      "clin_mean_rate": 14.08,
      "clin_patient_share": 60.72,
      "clin_enrolled_share": 56.05,
      "clin_avg_patients": 144.1,
      "clin_active_count": 64,
      "clin_active_care_rate": 69.51,
      "top_clinics": [
        {
          "name": "曾競鋒診所",
          "code": "3543014332",
          "dist": "屏東市",
          "num": 2577,
          "den": 3020,
          "rate": 85.3
        },
        {
          "name": "芯禾診所",
          "code": "3543014823",
          "dist": "屏東市",
          "num": 1131,
          "den": 1356,
          "rate": 83.4
        },
        {
          "name": "李洮俊診所",
          "code": "3543013862",
          "dist": "屏東市",
          "num": 1004,
          "den": 1221,
          "rate": 82.2
        }
      ],
      "top_hosps": [
        {
          "name": "輔英科技大學附設醫院",
          "code": "1343030018",
          "type": "區域醫院",
          "num": 3081,
          "den": 4475,
          "rate": 68.8
        },
        {
          "name": "屏基醫療財團法人屏東基督教醫院",
          "code": "1143010012",
          "type": "區域醫院",
          "num": 2467,
          "den": 4474,
          "rate": 55.1
        },
        {
          "name": "衛生福利部屏東醫院",
          "code": "0143010011",
          "type": "區域醫院",
          "num": 2128,
          "den": 3239,
          "rate": 65.7
        }
      ],
      "rank_patients": 8,
      "rank_care_rate": 12
    },
    {
      "city": "雲林縣",
      "region": "中部",
      "tier_type": "均衡照護",
      "tier_color": "#0284c7",
      "total_institutions": 202,
      "total_patients": 48756,
      "total_enrolled": 22571,
      "total_care_rate": 46.29,
      "total_mean_rate": 12.52,
      "hosp_count": 14,
      "hosp_patients": 28795,
      "hosp_enrolled": 15570,
      "hosp_care_rate": 54.07,
      "hosp_mean_rate": 34.47,
      "hosp_patient_share": 59.06,
      "hosp_enrolled_share": 68.98,
      "hosp_avg_patients": 2056.8,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 13062,
        "enrolled": 5611
      },
      "breakdown_dist_hosp": {
        "count": 12,
        "patients": 15733,
        "enrolled": 9959
      },
      "clin_count": 188,
      "clin_patients": 19961,
      "clin_enrolled": 7001,
      "clin_care_rate": 35.07,
      "clin_mean_rate": 10.88,
      "clin_patient_share": 40.94,
      "clin_enrolled_share": 31.02,
      "clin_avg_patients": 106.2,
      "clin_active_count": 31,
      "clin_active_care_rate": 70.99,
      "top_clinics": [
        {
          "name": "虎尾台全診所",
          "code": "3539032331",
          "dist": "虎尾鎮",
          "num": 801,
          "den": 948,
          "rate": 84.5
        },
        {
          "name": "洤華診所",
          "code": "3539020242",
          "dist": "斗南鎮",
          "num": 764,
          "den": 876,
          "rate": 87.2
        },
        {
          "name": "佑仁診所",
          "code": "3539111444",
          "dist": "二崙鄉",
          "num": 512,
          "den": 653,
          "rate": 78.4
        }
      ],
      "top_hosps": [
        {
          "name": "國立臺灣大學醫學院附設醫院雲林分院",
          "code": "0439010518",
          "type": "區域醫院",
          "num": 3469,
          "den": 8979,
          "rate": 38.6
        },
        {
          "name": "彰化基督教醫療財團法人雲林基督教醫院",
          "code": "1139040011",
          "type": "地區醫院",
          "num": 2867,
          "den": 4305,
          "rate": 66.6
        },
        {
          "name": "國立成功大學醫學院附設醫院斗六分院",
          "code": "0439010527",
          "type": "地區醫院",
          "num": 2382,
          "den": 3987,
          "rate": 59.7
        }
      ],
      "rank_patients": 9,
      "rank_care_rate": 18
    },
    {
      "city": "嘉義市",
      "region": "南部",
      "tier_type": "醫院高度集中",
      "tier_color": "#f59e0b",
      "total_institutions": 131,
      "total_patients": 42574,
      "total_enrolled": 23695,
      "total_care_rate": 55.66,
      "total_mean_rate": 17.66,
      "hosp_count": 11,
      "hosp_patients": 29384,
      "hosp_enrolled": 17218,
      "hosp_care_rate": 58.6,
      "hosp_mean_rate": 34.02,
      "hosp_patient_share": 69.02,
      "hosp_enrolled_share": 72.67,
      "hosp_avg_patients": 2671.3,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 3,
        "patients": 21387,
        "enrolled": 12219
      },
      "breakdown_dist_hosp": {
        "count": 8,
        "patients": 7997,
        "enrolled": 4999
      },
      "clin_count": 120,
      "clin_patients": 13190,
      "clin_enrolled": 6477,
      "clin_care_rate": 49.11,
      "clin_mean_rate": 16.16,
      "clin_patient_share": 30.98,
      "clin_enrolled_share": 27.33,
      "clin_avg_patients": 109.9,
      "clin_active_count": 29,
      "clin_active_care_rate": 66.48,
      "top_clinics": [
        {
          "name": "洪瑞禧診所",
          "code": "3522022914",
          "dist": "西區",
          "num": 547,
          "den": 682,
          "rate": 80.2
        },
        {
          "name": "開心診所",
          "code": "3522024098",
          "dist": "西區",
          "num": 511,
          "den": 638,
          "rate": 80.1
        },
        {
          "name": "安家診所",
          "code": "3522013684",
          "dist": "東區",
          "num": 471,
          "den": 611,
          "rate": 77.1
        }
      ],
      "top_hosps": [
        {
          "name": "戴德森醫療財團法人嘉義基督教醫院",
          "code": "1122010012",
          "type": "區域醫院",
          "num": 7240,
          "den": 12048,
          "rate": 60.1
        },
        {
          "name": "天主教中華聖母修女會醫療財團法人天主教聖馬爾定醫院",
          "code": "1122010021",
          "type": "區域醫院",
          "num": 3286,
          "den": 5636,
          "rate": 58.3
        },
        {
          "name": "陽明醫院",
          "code": "1522011115",
          "type": "地區醫院",
          "num": 3234,
          "den": 4780,
          "rate": 67.7
        }
      ],
      "rank_patients": 10,
      "rank_care_rate": 2
    },
    {
      "city": "宜蘭縣",
      "region": "東部",
      "tier_type": "基層高度主導",
      "tier_color": "#10b981",
      "total_institutions": 147,
      "total_patients": 42017,
      "total_enrolled": 25573,
      "total_care_rate": 60.86,
      "total_mean_rate": 20.13,
      "hosp_count": 8,
      "hosp_patients": 18883,
      "hosp_enrolled": 11913,
      "hosp_care_rate": 63.09,
      "hosp_mean_rate": 56.97,
      "hosp_patient_share": 44.94,
      "hosp_enrolled_share": 46.58,
      "hosp_avg_patients": 2360.4,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 3,
        "patients": 13152,
        "enrolled": 7798
      },
      "breakdown_dist_hosp": {
        "count": 5,
        "patients": 5731,
        "enrolled": 4115
      },
      "clin_count": 139,
      "clin_patients": 23134,
      "clin_enrolled": 13660,
      "clin_care_rate": 59.05,
      "clin_mean_rate": 18.01,
      "clin_patient_share": 55.06,
      "clin_enrolled_share": 53.42,
      "clin_avg_patients": 166.4,
      "clin_active_count": 36,
      "clin_active_care_rate": 77.33,
      "top_clinics": [
        {
          "name": "游能俊診所",
          "code": "3534021927",
          "dist": "羅東鎮",
          "num": 4621,
          "den": 5503,
          "rate": 84.0
        },
        {
          "name": "開蘭安心診所",
          "code": "3534012062",
          "dist": "宜蘭市",
          "num": 1424,
          "den": 1814,
          "rate": 78.5
        },
        {
          "name": "陳煥文內科診所",
          "code": "3534022157",
          "dist": "羅東鎮",
          "num": 840,
          "den": 1027,
          "rate": 81.8
        }
      ],
      "top_hosps": [
        {
          "name": "醫療財團法人羅許基金會羅東博愛醫院",
          "code": "1134020019",
          "type": "區域醫院",
          "num": 3219,
          "den": 5756,
          "rate": 55.9
        },
        {
          "name": "國立陽明交通大學附設醫院",
          "code": "0434010518",
          "type": "區域醫院",
          "num": 3172,
          "den": 4366,
          "rate": 72.7
        },
        {
          "name": "宜蘭仁愛醫療財團法人宜蘭仁愛醫院",
          "code": "1134010022",
          "type": "地區醫院",
          "num": 2171,
          "den": 2677,
          "rate": 81.1
        }
      ],
      "rank_patients": 11,
      "rank_care_rate": 1
    },
    {
      "city": "新竹市",
      "region": "北部",
      "tier_type": "醫院高度集中",
      "tier_color": "#f59e0b",
      "total_institutions": 125,
      "total_patients": 37452,
      "total_enrolled": 19845,
      "total_care_rate": 52.99,
      "total_mean_rate": 9.11,
      "hosp_count": 9,
      "hosp_patients": 23217,
      "hosp_enrolled": 12783,
      "hosp_care_rate": 55.06,
      "hosp_mean_rate": 39.27,
      "hosp_patient_share": 61.99,
      "hosp_enrolled_share": 64.41,
      "hosp_avg_patients": 2579.7,
      "breakdown_med_center": {
        "count": 1,
        "patients": 4086,
        "enrolled": 2620
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 11009,
        "enrolled": 5245
      },
      "breakdown_dist_hosp": {
        "count": 6,
        "patients": 8122,
        "enrolled": 4918
      },
      "clin_count": 116,
      "clin_patients": 14235,
      "clin_enrolled": 7062,
      "clin_care_rate": 49.61,
      "clin_mean_rate": 6.77,
      "clin_patient_share": 38.01,
      "clin_enrolled_share": 35.59,
      "clin_avg_patients": 122.7,
      "clin_active_count": 11,
      "clin_active_care_rate": 77.91,
      "top_clinics": [
        {
          "name": "安慎診所",
          "code": "3512011276",
          "dist": "東區",
          "num": 3677,
          "den": 4478,
          "rate": 82.1
        },
        {
          "name": "億安診所",
          "code": "3512013565",
          "dist": "東區",
          "num": 689,
          "den": 953,
          "rate": 72.3
        },
        {
          "name": "佳醫診所",
          "code": "3512013654",
          "dist": "東區",
          "num": 687,
          "den": 869,
          "rate": 79.1
        }
      ],
      "top_hosps": [
        {
          "name": "台灣基督長老教會馬偕醫療財團法人新竹馬偕紀念醫院",
          "code": "1112010519",
          "type": "區域醫院",
          "num": 5137,
          "den": 10822,
          "rate": 47.5
        },
        {
          "name": "國立臺灣大學醫學院附設醫院新竹臺大分院新竹醫院",
          "code": "0412040012",
          "type": "醫學中心",
          "num": 2620,
          "den": 4086,
          "rate": 64.1
        },
        {
          "name": "國泰醫療財團法人新竹國泰綜合醫院",
          "code": "1112010528",
          "type": "地區醫院",
          "num": 2426,
          "den": 3640,
          "rate": 66.6
        }
      ],
      "rank_patients": 12,
      "rank_care_rate": 4
    },
    {
      "city": "南投縣",
      "region": "中部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 178,
      "total_patients": 36783,
      "total_enrolled": 19381,
      "total_care_rate": 52.69,
      "total_mean_rate": 17.26,
      "hosp_count": 10,
      "hosp_patients": 17047,
      "hosp_enrolled": 9684,
      "hosp_care_rate": 56.81,
      "hosp_mean_rate": 56.33,
      "hosp_patient_share": 46.34,
      "hosp_enrolled_share": 49.97,
      "hosp_avg_patients": 1704.7,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 3,
        "patients": 6020,
        "enrolled": 3167
      },
      "breakdown_dist_hosp": {
        "count": 7,
        "patients": 11027,
        "enrolled": 6517
      },
      "clin_count": 168,
      "clin_patients": 19736,
      "clin_enrolled": 9697,
      "clin_care_rate": 49.13,
      "clin_mean_rate": 14.94,
      "clin_patient_share": 53.66,
      "clin_enrolled_share": 50.03,
      "clin_avg_patients": 117.5,
      "clin_active_count": 35,
      "clin_active_care_rate": 75.36,
      "top_clinics": [
        {
          "name": "陳宏麟診所",
          "code": "3538022537",
          "dist": "埔里鎮",
          "num": 1571,
          "den": 1850,
          "rate": 84.9
        },
        {
          "name": "黎俊奇診所",
          "code": "3538022242",
          "dist": "埔里鎮",
          "num": 743,
          "den": 743,
          "rate": 100.0
        },
        {
          "name": "安杏診所",
          "code": "3538022260",
          "dist": "埔里鎮",
          "num": 611,
          "den": 620,
          "rate": 98.6
        }
      ],
      "top_hosps": [
        {
          "name": "衛生福利部南投醫院",
          "code": "0138010027",
          "type": "區域醫院",
          "num": 2088,
          "den": 3899,
          "rate": 53.5
        },
        {
          "name": "佑民醫療社團法人佑民醫院",
          "code": "0938030016",
          "type": "地區醫院",
          "num": 1826,
          "den": 2793,
          "rate": 65.4
        },
        {
          "name": "臺中榮民總醫院埔里分院",
          "code": "0638020014",
          "type": "地區醫院",
          "num": 1394,
          "den": 2269,
          "rate": 61.4
        }
      ],
      "rank_patients": 13,
      "rank_care_rate": 5
    },
    {
      "city": "苗栗縣",
      "region": "北部",
      "tier_type": "基層高度主導",
      "tier_color": "#10b981",
      "total_institutions": 161,
      "total_patients": 36490,
      "total_enrolled": 18693,
      "total_care_rate": 51.23,
      "total_mean_rate": 19.01,
      "hosp_count": 12,
      "hosp_patients": 13371,
      "hosp_enrolled": 8082,
      "hosp_care_rate": 60.44,
      "hosp_mean_rate": 51.63,
      "hosp_patient_share": 36.64,
      "hosp_enrolled_share": 43.24,
      "hosp_avg_patients": 1114.2,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 3617,
        "enrolled": 2738
      },
      "breakdown_dist_hosp": {
        "count": 10,
        "patients": 9754,
        "enrolled": 5344
      },
      "clin_count": 149,
      "clin_patients": 23119,
      "clin_enrolled": 10611,
      "clin_care_rate": 45.9,
      "clin_mean_rate": 16.38,
      "clin_patient_share": 63.36,
      "clin_enrolled_share": 56.76,
      "clin_avg_patients": 155.2,
      "clin_active_count": 41,
      "clin_active_care_rate": 64.07,
      "top_clinics": [
        {
          "name": "心安診所",
          "code": "3535012511",
          "dist": "苗栗市",
          "num": 1416,
          "den": 1757,
          "rate": 80.6
        },
        {
          "name": "祥安診所",
          "code": "3535050146",
          "dist": "頭份市",
          "num": 779,
          "den": 866,
          "rate": 90.0
        },
        {
          "name": "後龍診所",
          "code": "3535061434",
          "dist": "後龍鎮",
          "num": 675,
          "den": 1309,
          "rate": 51.6
        }
      ],
      "top_hosps": [
        {
          "name": "大千綜合醫院",
          "code": "1535010051",
          "type": "地區醫院",
          "num": 1891,
          "den": 3401,
          "rate": 55.6
        },
        {
          "name": "重光醫院",
          "code": "1535051178",
          "type": "地區醫院",
          "num": 1514,
          "den": 2074,
          "rate": 73.0
        },
        {
          "name": "衛生福利部苗栗醫院",
          "code": "0135010016",
          "type": "區域醫院",
          "num": 1378,
          "den": 2017,
          "rate": 68.3
        }
      ],
      "rank_patients": 14,
      "rank_care_rate": 8
    },
    {
      "city": "嘉義縣",
      "region": "南部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 157,
      "total_patients": 32364,
      "total_enrolled": 15750,
      "total_care_rate": 48.67,
      "total_mean_rate": 15.25,
      "hosp_count": 4,
      "hosp_patients": 14777,
      "hosp_enrolled": 8205,
      "hosp_care_rate": 55.53,
      "hosp_mean_rate": 52.96,
      "hosp_patient_share": 45.66,
      "hosp_enrolled_share": 52.1,
      "hosp_avg_patients": 3694.2,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 13372,
        "enrolled": 7540
      },
      "breakdown_dist_hosp": {
        "count": 2,
        "patients": 1405,
        "enrolled": 665
      },
      "clin_count": 153,
      "clin_patients": 17587,
      "clin_enrolled": 7545,
      "clin_care_rate": 42.9,
      "clin_mean_rate": 14.26,
      "clin_patient_share": 54.34,
      "clin_enrolled_share": 47.9,
      "clin_avg_patients": 114.9,
      "clin_active_count": 34,
      "clin_active_care_rate": 71.14,
      "top_clinics": [
        {
          "name": "陳霆昌安糖診所",
          "code": "3540031377",
          "dist": "大林鎮",
          "num": 1629,
          "den": 1738,
          "rate": 93.7
        },
        {
          "name": "德家診所",
          "code": "3540011599",
          "dist": "朴子市",
          "num": 844,
          "den": 989,
          "rate": 85.3
        },
        {
          "name": "台大佳醫診所",
          "code": "3540131498",
          "dist": "中埔鄉",
          "num": 521,
          "den": 659,
          "rate": 79.1
        }
      ],
      "top_hosps": [
        {
          "name": "佛教慈濟醫療財團法人大林慈濟醫院",
          "code": "1140030012",
          "type": "區域醫院",
          "num": 3797,
          "den": 5528,
          "rate": 68.7
        },
        {
          "name": "長庚醫療財團法人嘉義長庚紀念醫院",
          "code": "1140010510",
          "type": "區域醫院",
          "num": 3743,
          "den": 7844,
          "rate": 47.7
        },
        {
          "name": "衛生福利部朴子醫院",
          "code": "0140010028",
          "type": "地區醫院",
          "num": 412,
          "den": 890,
          "rate": 46.3
        }
      ],
      "rank_patients": 15,
      "rank_care_rate": 14
    },
    {
      "city": "新竹縣",
      "region": "北部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 147,
      "total_patients": 29641,
      "total_enrolled": 12669,
      "total_care_rate": 42.74,
      "total_mean_rate": 9.45,
      "hosp_count": 9,
      "hosp_patients": 14790,
      "hosp_enrolled": 8606,
      "hosp_care_rate": 58.19,
      "hosp_mean_rate": 42.17,
      "hosp_patient_share": 49.9,
      "hosp_enrolled_share": 67.93,
      "hosp_avg_patients": 1643.3,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 5401,
        "enrolled": 3976
      },
      "breakdown_dist_hosp": {
        "count": 7,
        "patients": 9389,
        "enrolled": 4630
      },
      "clin_count": 138,
      "clin_patients": 14851,
      "clin_enrolled": 4063,
      "clin_care_rate": 27.36,
      "clin_mean_rate": 7.32,
      "clin_patient_share": 50.1,
      "clin_enrolled_share": 32.07,
      "clin_avg_patients": 107.6,
      "clin_active_count": 18,
      "clin_active_care_rate": 59.33,
      "top_clinics": [
        {
          "name": "惠慎診所",
          "code": "3533052044",
          "dist": "竹北市",
          "num": 810,
          "den": 994,
          "rate": 81.5
        },
        {
          "name": "天主教聖母診所",
          "code": "3533061669",
          "dist": "湖口鄉",
          "num": 560,
          "den": 866,
          "rate": 64.7
        },
        {
          "name": "德安聯合診所",
          "code": "3533031732",
          "dist": "竹東鎮",
          "num": 504,
          "den": 595,
          "rate": 84.7
        }
      ],
      "top_hosps": [
        {
          "name": "國立臺灣大學醫學院附設醫院新竹臺大分院生醫醫院",
          "code": "0433050018",
          "type": "區域醫院",
          "num": 2066,
          "den": 3376,
          "rate": 61.2
        },
        {
          "name": "中國醫藥大學新竹附設醫院",
          "code": "1333050017",
          "type": "地區醫院",
          "num": 1917,
          "den": 3882,
          "rate": 49.4
        },
        {
          "name": "東元醫療社團法人東元綜合醫院",
          "code": "0933050018",
          "type": "區域醫院",
          "num": 1910,
          "den": 2025,
          "rate": 94.3
        }
      ],
      "rank_patients": 16,
      "rank_care_rate": 20
    },
    {
      "city": "基隆市",
      "region": "北部",
      "tier_type": "均衡照護",
      "tier_color": "#0284c7",
      "total_institutions": 94,
      "total_patients": 29323,
      "total_enrolled": 13672,
      "total_care_rate": 46.63,
      "total_mean_rate": 14.55,
      "hosp_count": 7,
      "hosp_patients": 17184,
      "hosp_enrolled": 8017,
      "hosp_care_rate": 46.65,
      "hosp_mean_rate": 42.63,
      "hosp_patient_share": 58.6,
      "hosp_enrolled_share": 58.64,
      "hosp_avg_patients": 2454.9,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 13804,
        "enrolled": 6404
      },
      "breakdown_dist_hosp": {
        "count": 5,
        "patients": 3380,
        "enrolled": 1613
      },
      "clin_count": 87,
      "clin_patients": 12139,
      "clin_enrolled": 5655,
      "clin_care_rate": 46.59,
      "clin_mean_rate": 12.29,
      "clin_patient_share": 41.4,
      "clin_enrolled_share": 41.36,
      "clin_avg_patients": 139.5,
      "clin_active_count": 17,
      "clin_active_care_rate": 67.27,
      "top_clinics": [
        {
          "name": "彗恩診所",
          "code": "3511012279",
          "dist": "中正區",
          "num": 731,
          "den": 942,
          "rate": 77.6
        },
        {
          "name": "紀醫師診所",
          "code": "3511020226",
          "dist": "七堵區",
          "num": 670,
          "den": 762,
          "rate": 87.9
        },
        {
          "name": "康合診所",
          "code": "3511031256",
          "dist": "暖暖區",
          "num": 659,
          "den": 778,
          "rate": 84.7
        }
      ],
      "top_hosps": [
        {
          "name": "長庚醫療財團法人基隆長庚紀念醫院",
          "code": "1111060015",
          "type": "區域醫院",
          "num": 4008,
          "den": 8646,
          "rate": 46.4
        },
        {
          "name": "衛生福利部基隆醫院",
          "code": "0111070010",
          "type": "區域醫院",
          "num": 2396,
          "den": 5158,
          "rate": 46.5
        },
        {
          "name": "三軍總醫院基隆分院附設民眾診療服務處",
          "code": "0511040010",
          "type": "地區醫院",
          "num": 656,
          "den": 1680,
          "rate": 39.1
        }
      ],
      "rank_patients": 17,
      "rank_care_rate": 17
    },
    {
      "city": "花蓮縣",
      "region": "東部",
      "tier_type": "均衡照護",
      "tier_color": "#0284c7",
      "total_institutions": 116,
      "total_patients": 26946,
      "total_enrolled": 12186,
      "total_care_rate": 45.22,
      "total_mean_rate": 19.25,
      "hosp_count": 10,
      "hosp_patients": 14077,
      "hosp_enrolled": 6317,
      "hosp_care_rate": 44.87,
      "hosp_mean_rate": 37.29,
      "hosp_patient_share": 52.24,
      "hosp_enrolled_share": 51.84,
      "hosp_avg_patients": 1407.7,
      "breakdown_med_center": {
        "count": 1,
        "patients": 5129,
        "enrolled": 2948
      },
      "breakdown_reg_hosp": {
        "count": 2,
        "patients": 4402,
        "enrolled": 1497
      },
      "breakdown_dist_hosp": {
        "count": 7,
        "patients": 4546,
        "enrolled": 1872
      },
      "clin_count": 106,
      "clin_patients": 12869,
      "clin_enrolled": 5869,
      "clin_care_rate": 45.61,
      "clin_mean_rate": 17.55,
      "clin_patient_share": 47.76,
      "clin_enrolled_share": 48.16,
      "clin_avg_patients": 121.4,
      "clin_active_count": 28,
      "clin_active_care_rate": 67.04,
      "top_clinics": [
        {
          "name": "康寧診所",
          "code": "3545051404",
          "dist": "吉安鄉",
          "num": 637,
          "den": 734,
          "rate": 86.8
        },
        {
          "name": "光鹽診所",
          "code": "3545051468",
          "dist": "吉安鄉",
          "num": 574,
          "den": 658,
          "rate": 87.2
        },
        {
          "name": "國泰聯合診所",
          "code": "3545011142",
          "dist": "花蓮市",
          "num": 510,
          "den": 709,
          "rate": 71.9
        }
      ],
      "top_hosps": [
        {
          "name": "佛教慈濟醫療財團法人花蓮慈濟醫院",
          "code": "1145010010",
          "type": "醫學中心",
          "num": 2948,
          "den": 5129,
          "rate": 57.5
        },
        {
          "name": "臺灣基督教門諾會醫療財團法人門諾醫院",
          "code": "1145010038",
          "type": "區域醫院",
          "num": 949,
          "den": 3196,
          "rate": 29.7
        },
        {
          "name": "臺北榮民總醫院玉里分院",
          "code": "0645030011",
          "type": "地區醫院",
          "num": 651,
          "den": 1508,
          "rate": 43.2
        }
      ],
      "rank_patients": 18,
      "rank_care_rate": 19
    },
    {
      "city": "臺東縣",
      "region": "東部",
      "tier_type": "基層主導",
      "tier_color": "#0d9488",
      "total_institutions": 82,
      "total_patients": 17281,
      "total_enrolled": 9087,
      "total_care_rate": 52.58,
      "total_mean_rate": 23.07,
      "hosp_count": 7,
      "hosp_patients": 7999,
      "hosp_enrolled": 3769,
      "hosp_care_rate": 47.12,
      "hosp_mean_rate": 43.25,
      "hosp_patient_share": 46.29,
      "hosp_enrolled_share": 41.48,
      "hosp_avg_patients": 1142.7,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 1,
        "patients": 3714,
        "enrolled": 1744
      },
      "breakdown_dist_hosp": {
        "count": 6,
        "patients": 4285,
        "enrolled": 2025
      },
      "clin_count": 75,
      "clin_patients": 9282,
      "clin_enrolled": 5318,
      "clin_care_rate": 57.29,
      "clin_mean_rate": 21.18,
      "clin_patient_share": 53.71,
      "clin_enrolled_share": 58.52,
      "clin_avg_patients": 123.8,
      "clin_active_count": 28,
      "clin_active_care_rate": 73.78,
      "top_clinics": [
        {
          "name": "黃信揚診所",
          "code": "3546012483",
          "dist": "臺東市",
          "num": 958,
          "den": 1175,
          "rate": 81.5
        },
        {
          "name": "大溪診所",
          "code": "3546010818",
          "dist": "臺東市",
          "num": 834,
          "den": 834,
          "rate": 100.0
        },
        {
          "name": "關強內科診所",
          "code": "3546010765",
          "dist": "臺東市",
          "num": 500,
          "den": 500,
          "rate": 100.0
        }
      ],
      "top_hosps": [
        {
          "name": "台灣基督長老教會馬偕醫療財團法人台東馬偕紀念醫院",
          "code": "1146010014",
          "type": "區域醫院",
          "num": 1744,
          "den": 3714,
          "rate": 47.0
        },
        {
          "name": "東基醫療財團法人台東基督教醫院",
          "code": "1146010032",
          "type": "地區醫院",
          "num": 740,
          "den": 1738,
          "rate": 42.6
        },
        {
          "name": "天主教花蓮教區醫療財團法人台東聖母醫院",
          "code": "1146010041",
          "type": "地區醫院",
          "num": 454,
          "den": 583,
          "rate": 77.9
        }
      ],
      "rank_patients": 19,
      "rank_care_rate": 6
    },
    {
      "city": "澎湖縣",
      "region": "離島",
      "tier_type": "基層高度主導",
      "tier_color": "#10b981",
      "total_institutions": 50,
      "total_patients": 6755,
      "total_enrolled": 1920,
      "total_care_rate": 28.42,
      "total_mean_rate": 12.34,
      "hosp_count": 3,
      "hosp_patients": 2113,
      "hosp_enrolled": 1094,
      "hosp_care_rate": 51.77,
      "hosp_mean_rate": 35.22,
      "hosp_patient_share": 31.28,
      "hosp_enrolled_share": 56.98,
      "hosp_avg_patients": 704.3,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_dist_hosp": {
        "count": 3,
        "patients": 2113,
        "enrolled": 1094
      },
      "clin_count": 47,
      "clin_patients": 4642,
      "clin_enrolled": 826,
      "clin_care_rate": 17.79,
      "clin_mean_rate": 10.88,
      "clin_patient_share": 68.72,
      "clin_enrolled_share": 43.02,
      "clin_avg_patients": 98.8,
      "clin_active_count": 11,
      "clin_active_care_rate": 48.7,
      "top_clinics": [
        {
          "name": "澎湖縣馬公市第二衛生所",
          "code": "2344011027",
          "dist": "馬公市",
          "num": 180,
          "den": 272,
          "rate": 66.2
        },
        {
          "name": "澎湖縣西嶼鄉衛生所",
          "code": "2344040019",
          "dist": "西嶼鄉",
          "num": 155,
          "den": 301,
          "rate": 51.5
        },
        {
          "name": "澎湖縣七美鄉衛生所",
          "code": "2344060011",
          "dist": "七美鄉",
          "num": 86,
          "den": 191,
          "rate": 45.0
        }
      ],
      "top_hosps": [
        {
          "name": "衛生福利部澎湖醫院",
          "code": "0144010015",
          "type": "地區醫院",
          "num": 662,
          "den": 1025,
          "rate": 64.6
        },
        {
          "name": "三軍總醫院澎湖分院附設民眾診療服務處",
          "code": "0544010031",
          "type": "地區醫院",
          "num": 432,
          "den": 1052,
          "rate": 41.1
        },
        {
          "name": "天主教靈醫會醫療財團法人惠民醫院",
          "code": "1144010016",
          "type": "地區醫院",
          "num": 0,
          "den": 36,
          "rate": 0.0
        }
      ],
      "rank_patients": 20,
      "rank_care_rate": 22
    },
    {
      "city": "金門縣",
      "region": "離島",
      "tier_type": "基層高度主導",
      "tier_color": "#10b981",
      "total_institutions": 25,
      "total_patients": 5083,
      "total_enrolled": 2095,
      "total_care_rate": 41.22,
      "total_mean_rate": 16.52,
      "hosp_count": 1,
      "hosp_patients": 2150,
      "hosp_enrolled": 1005,
      "hosp_care_rate": 46.74,
      "hosp_mean_rate": 46.74,
      "hosp_patient_share": 42.3,
      "hosp_enrolled_share": 47.97,
      "hosp_avg_patients": 2150.0,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_dist_hosp": {
        "count": 1,
        "patients": 2150,
        "enrolled": 1005
      },
      "clin_count": 24,
      "clin_patients": 2933,
      "clin_enrolled": 1090,
      "clin_care_rate": 37.16,
      "clin_mean_rate": 15.26,
      "clin_patient_share": 57.7,
      "clin_enrolled_share": 52.03,
      "clin_avg_patients": 122.2,
      "clin_active_count": 7,
      "clin_active_care_rate": 52.53,
      "top_clinics": [
        {
          "name": "金門縣金城鎮衛生所",
          "code": "2390010010",
          "dist": "金城鎮",
          "num": 392,
          "den": 493,
          "rate": 79.5
        },
        {
          "name": "吾家診所",
          "code": "3590011218",
          "dist": "金城鎮",
          "num": 268,
          "den": 548,
          "rate": 48.9
        },
        {
          "name": "金門縣金湖鎮衛生所",
          "code": "2390030030",
          "dist": "金湖鎮",
          "num": 158,
          "den": 220,
          "rate": 71.8
        }
      ],
      "top_hosps": [
        {
          "name": "衛生福利部金門醫院",
          "code": "0190030516",
          "type": "地區醫院",
          "num": 1005,
          "den": 2150,
          "rate": 46.7
        }
      ],
      "rank_patients": 21,
      "rank_care_rate": 21
    },
    {
      "city": "連江縣",
      "region": "離島",
      "tier_type": "醫院高度集中",
      "tier_color": "#f59e0b",
      "total_institutions": 5,
      "total_patients": 534,
      "total_enrolled": 271,
      "total_care_rate": 50.75,
      "total_mean_rate": 46.38,
      "hosp_count": 1,
      "hosp_patients": 338,
      "hosp_enrolled": 173,
      "hosp_care_rate": 51.18,
      "hosp_mean_rate": 51.18,
      "hosp_patient_share": 63.3,
      "hosp_enrolled_share": 63.84,
      "hosp_avg_patients": 338.0,
      "breakdown_med_center": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_reg_hosp": {
        "count": 0,
        "patients": 0,
        "enrolled": 0
      },
      "breakdown_dist_hosp": {
        "count": 1,
        "patients": 338,
        "enrolled": 173
      },
      "clin_count": 4,
      "clin_patients": 196,
      "clin_enrolled": 98,
      "clin_care_rate": 50.0,
      "clin_mean_rate": 45.18,
      "clin_patient_share": 36.7,
      "clin_enrolled_share": 36.16,
      "clin_avg_patients": 49.0,
      "clin_active_count": 4,
      "clin_active_care_rate": 50.0,
      "top_clinics": [
        {
          "name": "連江縣北竿鄉衛生所",
          "code": "2391020010",
          "dist": "北竿鄉",
          "num": 42,
          "den": 80,
          "rate": 52.5
        },
        {
          "name": "連江縣東引鄉衛生所",
          "code": "2391040012",
          "dist": "東引鄉",
          "num": 40,
          "den": 63,
          "rate": 63.5
        },
        {
          "name": "連江縣莒光鄉西莒衛生所",
          "code": "2391030016",
          "dist": "莒光鄉",
          "num": 9,
          "den": 21,
          "rate": 42.9
        }
      ],
      "top_hosps": [
        {
          "name": "連江縣立醫院",
          "code": "0291010010",
          "type": "地區醫院",
          "num": 173,
          "den": 338,
          "rate": 51.2
        }
      ],
      "rank_patients": 22,
      "rank_care_rate": 10
    }
  ]
};