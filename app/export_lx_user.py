import pandas as pd
import json

# 假设JSON数据已读取到变量中（如果从文件读取，可使用with open语句）
# 这里的json_data替换为实际的JSON数据内容
json_data = {
    "msg": "操作成功",
    "total": 129,
    "code": 1,
    "codeVersion": "normal",
    "req_time_sequence": "/newadmin/api/user/manage/page$$2",
    "update_code": 0,
    "list": [
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110477918005063680"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110477918005063680"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10853600",
            "realname": "陈清华",
            "mobile": "",
            "email": "",
            "username": "qinghua8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110477918005063680"
            ],
            "login_num": 2,
            "create_time": "2025-07-16 11:54:43",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 16:01:07",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110487470967312896"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110487470967312896"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10853594",
            "realname": "郑嘉莹",
            "mobile": "",
            "email": "",
            "username": "jiaying8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110487470967312896"
            ],
            "login_num": 1,
            "create_time": "2025-07-16 11:52:40",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-16 15:32:25",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10851432",
            "realname": "位亚芳",
            "mobile": "18218578965",
            "email": "",
            "username": "weiyafang",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 3,
            "create_time": "2025-07-14 14:41:22",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:12:58",
            "role": "采购跟单",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "东莞仓",
            "userOrgDtos": [
                {
                    "orgName": "东莞仓",
                    "wholeOrgId": "1826135147145936897",
                    "orgId": "1826135147145936897"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10850179",
            "realname": "甘天浪",
            "mobile": "",
            "email": "",
            "username": "tianlang",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 4,
            "create_time": "2025-07-12 11:55:19",
            "last_login_ip": "14.216.25.17",
            "last_login_time": "2025-07-24 08:23:26",
            "role": "仓库管理,质检员",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10849010",
            "realname": "彭杏花",
            "mobile": "",
            "email": "",
            "username": "xinghua8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 11,
            "create_time": "2025-07-10 17:05:25",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 10:35:42",
            "role": "采购跟单",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 2,
                    "userEntityIds": [],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10835755",
            "realname": "张莹莹",
            "mobile": "",
            "email": "",
            "username": "yingying8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 8,
            "create_time": "2025-06-27 09:44:36",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 15:54:12",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 2,
                    "userEntityIds": [],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10829231",
            "realname": "周美娟",
            "mobile": "",
            "email": "",
            "username": "meijuan619",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "login_num": 3,
            "create_time": "2025-06-19 14:55:26",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-06-23 09:09:34",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10829227",
            "realname": "刘扬",
            "mobile": "",
            "email": "",
            "username": "liuyang619",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "login_num": 3,
            "create_time": "2025-06-19 14:54:05",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-06-27 15:08:24",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 2,
                    "userEntityIds": [],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10825393",
            "realname": "周灵琬",
            "mobile": "",
            "email": "",
            "username": "lingwan",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 6,
            "create_time": "2025-06-16 13:41:31",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 14:30:35",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10803504",
            "realname": "于水云",
            "mobile": "",
            "email": "",
            "username": "shuiyun",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "10829"
            ],
            "login_num": 12,
            "create_time": "2025-05-20 16:10:07",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:41:25",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部/采购开发",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10794047",
            "realname": "陈颜",
            "mobile": "",
            "email": "",
            "username": "chenyan8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 14,
            "create_time": "2025-05-09 11:39:28",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:05:03",
            "role": "采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 2,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110569569171750912",
                        "110583006917147648"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110569569171750912",
                        "110583006917147648"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10793925",
            "realname": "张艳桃",
            "mobile": "",
            "email": "",
            "username": "yantao8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110569569171750912",
                "110583006917147648"
            ],
            "login_num": 23,
            "create_time": "2025-05-09 10:28:17",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 08:54:44",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 2,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110478978569990144",
                        "110487470967312896"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110478978569990144",
                        "110487470967312896"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10786904",
            "realname": "余春莹",
            "mobile": "",
            "email": "",
            "username": "chunying8",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "seller_ids": [
                "110478978569990144",
                "110487470967312896"
            ],
            "login_num": 6,
            "create_time": "2025-04-28 11:39:01",
            "last_login_ip": "10.0.97.69",
            "last_login_time": "2025-06-05 09:47:44",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10786902",
            "realname": "孙文静",
            "mobile": "",
            "email": "",
            "username": "sunwenjing",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110481948018697728",
                "110481949849462272",
                "110481951351230976"
            ],
            "login_num": 4,
            "create_time": "2025-04-28 11:37:30",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 14:45:35",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10809",
                        "10810",
                        "10811"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10809",
                        "10810",
                        "10811",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10786264",
            "realname": "黄淑华",
            "mobile": "",
            "email": "",
            "username": "shuhua",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10809",
                "10810",
                "10811"
            ],
            "login_num": 14,
            "create_time": "2025-04-27 18:40:06",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 12:04:02",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 2,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110478979710751232",
                        "110506627817181184"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110478979710751232",
                        "110506627817181184"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10786262",
            "realname": "谭珍",
            "mobile": "",
            "email": "",
            "username": "tanzhen8",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110478979710751232",
                "110506627817181184"
            ],
            "login_num": 11,
            "create_time": "2025-04-27 18:39:07",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 10:37:17",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "东莞仓",
            "userOrgDtos": [
                {
                    "orgName": "东莞仓",
                    "wholeOrgId": "1826135147145936897",
                    "orgId": "1826135147145936897"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10779264",
            "realname": "邓晓晴",
            "mobile": "",
            "email": "",
            "username": "xiaoqing18",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 8,
            "create_time": "2025-04-18 18:15:13",
            "last_login_ip": "14.216.5.172",
            "last_login_time": "2025-05-30 11:17:12",
            "role": "仓库管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10837",
                        "10838",
                        "10839"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10837",
                        "10838",
                        "10839",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10767638",
            "realname": "江小芸",
            "mobile": "17828833013",
            "email": "",
            "username": "jiangxiaoyun",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10837",
                "10838",
                "10839"
            ],
            "login_num": 19,
            "create_time": "2025-04-07 10:30:41",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-20 19:39:54",
            "role": "运营管理,试用期员工",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110480134760059392",
                        "110507691712184832",
                        "110514010404378112"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110480134760059392",
                        "110507691712184832",
                        "110514010404378112"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10761263",
            "realname": "施德平",
            "mobile": "",
            "email": "",
            "username": "deping",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110480134760059392",
                "110507691712184832",
                "110514010404378112"
            ],
            "login_num": 23,
            "create_time": "2025-03-28 15:17:58",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:20:23",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10753403",
            "realname": "郑榕贵",
            "mobile": "",
            "email": "",
            "username": "ronggui",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "seller_ids": [
                "110481948018697728",
                "110481949849462272",
                "110481951351230976"
            ],
            "login_num": 5,
            "create_time": "2025-03-20 10:26:17",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-04-08 11:44:45",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营二部廖国荣组",
            "userOrgDtos": [
                {
                    "orgName": "运营二部廖国荣组",
                    "wholeOrgId": "1826134946325794818",
                    "orgId": "1826134946325794818"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10736259",
            "realname": "何国森",
            "mobile": "13528846827",
            "email": "",
            "username": "znder203",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10818",
                "10819",
                "10840",
                "10841",
                "10842"
            ],
            "login_num": 11,
            "create_time": "2025-03-03 14:19:56",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-17 17:33:39",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "",
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10702338",
            "realname": "杨静",
            "mobile": "18374744062",
            "email": "",
            "username": "znder201",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 26,
            "create_time": "2024-12-31 14:51:10",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 11:39:59",
            "role": "供应链管理,财务管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10692722",
            "realname": "李秋生",
            "mobile": "15013799510",
            "email": "",
            "username": "liqiusheng",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 54,
            "create_time": "2024-12-17 09:14:01",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:16:40",
            "role": "供应链管理,采购开发,采购跟单",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/郑春芳组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/郑春芳组",
                    "wholeOrgId": "1826134906265444353/1826136606690177025",
                    "orgId": "1826136606690177025"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10678512",
            "realname": "蔡雷",
            "mobile": "",
            "email": "",
            "username": "cailei1",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 29,
            "create_time": "2024-11-22 18:16:57",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 11:52:58",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/郑春芳组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/郑春芳组",
                    "wholeOrgId": "1826134906265444353/1826136606690177025",
                    "orgId": "1826136606690177025"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 2,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10678511",
            "realname": "习绫卿",
            "mobile": "",
            "email": "",
            "username": "lingqing",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 24,
            "create_time": "2024-11-22 18:15:55",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 09:09:46",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 4,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10829",
                        "10837",
                        "10838",
                        "10839"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10829",
                        "10837",
                        "10838",
                        "10839",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10676962",
            "realname": "莫淑媚",
            "mobile": "16782076992",
            "email": "",
            "username": "moshumei",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10829",
                "10837",
                "10838",
                "10839"
            ],
            "login_num": 39,
            "create_time": "2024-11-20 15:55:08",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 10:51:49",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110478978569990144",
                        "110487470967312896",
                        "110506627454519296",
                        "110521112427506176",
                        "110571362715833344"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110478978569990144",
                        "110487470967312896",
                        "110506627454519296",
                        "110521112427506176",
                        "110571362715833344"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10673131",
            "realname": "陈仲炯",
            "mobile": "13450504873",
            "email": "",
            "username": "zhongjiong",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110478978569990144",
                "110487470967312896",
                "110506627454519296",
                "110521112427506176",
                "110571362715833344"
            ],
            "login_num": 71,
            "create_time": "2024-11-13 19:35:19",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-20 17:05:24",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 4,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110478979710751232",
                        "110487470281773056",
                        "110506627817181184",
                        "110521111630981120"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110478979710751232",
                        "110487470281773056",
                        "110506627817181184",
                        "110521111630981120"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10673130",
            "realname": "宋丽贤",
            "mobile": "",
            "email": "",
            "username": "songlixian",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110478979710751232",
                "110487470281773056",
                "110506627817181184",
                "110521111630981120"
            ],
            "login_num": 51,
            "create_time": "2024-11-13 19:34:43",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:24:49",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "行政部",
            "userOrgDtos": [
                {
                    "orgName": "行政部",
                    "wholeOrgId": "1826569518013997057",
                    "orgId": "1826569518013997057"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10667215",
            "realname": "黄婧",
            "mobile": "18598060661",
            "email": "",
            "username": "znder125",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 11,
            "create_time": "2024-11-04 16:31:07",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-16 14:27:24",
            "role": "法务",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 8,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10664352",
            "realname": "麻桂琴",
            "mobile": "18374384058",
            "email": "",
            "username": "znder123",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 37,
            "create_time": "2024-10-30 13:51:07",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:07:36",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "东莞仓",
            "userOrgDtos": [
                {
                    "orgName": "东莞仓",
                    "wholeOrgId": "1826135147145936897",
                    "orgId": "1826135147145936897"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10662068",
            "realname": "田昌发",
            "mobile": "13533225030",
            "email": "",
            "username": "znder122",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 3,
            "create_time": "2024-10-26 15:33:39",
            "last_login_ip": "14.216.10.83",
            "last_login_time": "2024-11-05 16:40:41",
            "role": "仓库管理,质检员",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10809",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10809",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10656646",
            "realname": "周佳丽",
            "mobile": "15207490191",
            "email": "",
            "username": "znder121",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10809",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 48,
            "create_time": "2024-10-17 10:21:37",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:26:07",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "美国分公司",
            "userOrgDtos": [
                {
                    "orgName": "美国分公司",
                    "wholeOrgId": "1846063674951122946",
                    "orgId": "1846063674951122946"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 8,
                    "userEntityIds": [],
                    "orgEntityIds": [
                        "14337",
                        "9762",
                        "14338",
                        "14339",
                        "14872",
                        "14873",
                        "13853",
                        "13854"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "14337",
                        "9762",
                        "14338",
                        "14339",
                        "14872",
                        "14873",
                        "13853",
                        "13854"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10655259",
            "realname": "刘书睿",
            "mobile": "",
            "email": "shuruil906@gmail.com",
            "username": "znder120",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-10-15 13:45:28",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "仓库管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "物流部",
            "userOrgDtos": [
                {
                    "orgName": "物流部",
                    "wholeOrgId": "1826135115777048578",
                    "orgId": "1826135115777048578"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10647784",
            "realname": "林婵娟",
            "mobile": "19276696286",
            "email": "",
            "username": "znder118",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 33,
            "create_time": "2024-09-29 09:28:22",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:11:51",
            "role": "供应链管理,运营管理,仓库管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10646553",
            "realname": "周倩瑜",
            "mobile": "13421722989",
            "email": "",
            "username": "znder117",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 44,
            "create_time": "2024-09-26 14:51:13",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-18 11:14:24",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/林晓敏组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/林晓敏组",
                    "wholeOrgId": "1826134906265444353/1826136510865162242",
                    "orgId": "1826136510865162242"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 6,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10645958",
            "realname": "张晓婷",
            "mobile": "15059108468",
            "email": "",
            "username": "znder116",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 36,
            "create_time": "2024-09-25 16:28:37",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 14:01:04",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 6,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13853",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13853",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10638082",
            "realname": "王军",
            "mobile": "18926492546",
            "email": "",
            "username": "znder114",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 111,
            "create_time": "2024-09-11 19:42:20",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 18:56:44",
            "role": "供应链管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "东莞仓",
            "userOrgDtos": [
                {
                    "orgName": "东莞仓",
                    "wholeOrgId": "1826135147145936897",
                    "orgId": "1826135147145936897"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10635522",
            "realname": "仓库管理01",
            "mobile": "",
            "email": "",
            "username": "zd-cangku01",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 1,
            "create_time": "2024-09-07 17:50:37",
            "last_login_ip": "116.23.30.200",
            "last_login_time": "2024-09-07 17:53:15",
            "role": "仓库管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "质检部",
            "userOrgDtos": [
                {
                    "orgName": "质检部",
                    "wholeOrgId": "1826137730949640193",
                    "orgId": "1826137730949640193"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10635518",
            "realname": "质检测试01",
            "mobile": "",
            "email": "",
            "username": "zd-zhijian01",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 1,
            "create_time": "2024-09-07 17:42:18",
            "last_login_ip": "116.23.30.200",
            "last_login_time": "2024-09-07 17:44:18",
            "role": "质检员",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "美国分公司",
            "userOrgDtos": [
                {
                    "orgName": "美国分公司",
                    "wholeOrgId": "1846063674951122946",
                    "orgId": "1846063674951122946"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110544818145337856"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110544818145337856"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 8,
                    "userEntityIds": [],
                    "orgEntityIds": [
                        "14337",
                        "9762",
                        "14338",
                        "14339",
                        "14872",
                        "14873",
                        "13853",
                        "13854"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "14337",
                        "9762",
                        "14338",
                        "14339",
                        "14872",
                        "14873",
                        "13853",
                        "13854"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10635236",
            "realname": "王恢",
            "mobile": "13530349272",
            "email": "",
            "username": "znder113",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110544818145337856"
            ],
            "login_num": 17,
            "create_time": "2024-09-06 18:07:42",
            "last_login_ip": "98.97.21.120",
            "last_login_time": "2025-06-06 21:58:21",
            "role": "供应链管理,仓库管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "美国分公司",
            "userOrgDtos": [
                {
                    "orgName": "美国分公司",
                    "wholeOrgId": "1846063674951122946",
                    "orgId": "1846063674951122946"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 1,
                    "orgAuthNum": 8,
                    "userEntityIds": [
                        "9762"
                    ],
                    "orgEntityIds": [
                        "14337",
                        "9762",
                        "14338",
                        "14339",
                        "14872",
                        "14873",
                        "13853",
                        "13854"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "14337",
                        "14338",
                        "14339",
                        "14872",
                        "14873",
                        "13853",
                        "13854"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10635235",
            "realname": "卢胜",
            "mobile": "15220053213",
            "email": "",
            "username": "znder112",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-09-06 18:06:59",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "供应链管理,仓库管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "东莞仓",
            "userOrgDtos": [
                {
                    "orgName": "东莞仓",
                    "wholeOrgId": "1826135147145936897",
                    "orgId": "1826135147145936897"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10634659",
            "realname": "黄玉宏",
            "mobile": "17876457613",
            "email": "",
            "username": "Znder108",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 58,
            "create_time": "2024-09-05 19:08:05",
            "last_login_ip": "129.222.240.64",
            "last_login_time": "2025-07-24 00:53:26",
            "role": "仓库管理,质检员",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "质检部",
            "userOrgDtos": [
                {
                    "orgName": "质检部",
                    "wholeOrgId": "1826137730949640193",
                    "orgId": "1826137730949640193"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10634657",
            "realname": "马启龙",
            "mobile": "18292361305",
            "email": "",
            "username": "Znder107",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 189,
            "create_time": "2024-09-05 19:04:32",
            "last_login_ip": "14.216.25.17",
            "last_login_time": "2025-07-23 11:04:20",
            "role": "质检员",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 2,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10634571",
            "realname": "陈大明",
            "mobile": "13129574872",
            "email": "",
            "username": "Znder106",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 21,
            "create_time": "2024-09-05 17:13:13",
            "last_login_ip": "116.23.29.65",
            "last_login_time": "2025-06-26 15:15:54",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购开发",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10634011",
            "realname": "王增润",
            "mobile": "18126045285",
            "email": "",
            "username": "Znder105",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "login_num": 49,
            "create_time": "2024-09-04 19:21:04",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-06-30 09:55:18",
            "role": "供应链管理,采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购开发,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10634007",
            "realname": "王冠华",
            "mobile": "18320981835",
            "email": "",
            "username": "Znder102",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 47,
            "create_time": "2024-09-04 19:17:19",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:09:15",
            "role": "采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购开发,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10634006",
            "realname": "蒋真",
            "mobile": "15207474197",
            "email": "",
            "username": "Znder101",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 64,
            "create_time": "2024-09-04 19:15:37",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 08:59:06",
            "role": "采购跟单,供应商报价",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳财务部",
            "userOrgDtos": [
                {
                    "orgName": "深圳财务部",
                    "wholeOrgId": "1826135185145270274",
                    "orgId": "1826135185145270274"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "大明",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10629723",
            "realname": "方书礼",
            "mobile": "",
            "email": "",
            "username": "Znder100",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 61,
            "create_time": "2024-08-28 17:03:14",
            "last_login_ip": "14.19.39.148",
            "last_login_time": "2025-07-20 16:31:58",
            "role": "财务管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "IT部",
            "userOrgDtos": [
                {
                    "orgName": "IT部",
                    "wholeOrgId": "1826571617744797697",
                    "orgId": "1826571617744797697"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625411",
            "realname": "许康聪",
            "mobile": "",
            "email": "",
            "username": "Znder98",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 42,
            "create_time": "2024-08-21 18:23:12",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-03-24 16:52:37",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "IT部",
            "userOrgDtos": [
                {
                    "orgName": "IT部",
                    "wholeOrgId": "1826571617744797697",
                    "orgId": "1826571617744797697"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 58,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853",
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853",
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 2,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "16196",
                        "17922"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "16196",
                        "17922"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "范普选",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625408",
            "realname": "范普选",
            "mobile": "",
            "email": "",
            "username": "Znder97",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10808",
                "10809",
                "10810",
                "10811",
                "10813",
                "10814",
                "10816",
                "10817",
                "10818",
                "10819",
                "10829",
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "10850",
                "10851",
                "10852",
                "10853",
                "110477918005063680",
                "110478965997969920",
                "110478978569990144",
                "110478979257454592",
                "110478979710751232",
                "110480134760059392",
                "110481948018697728",
                "110481949849462272",
                "110481951351230976",
                "110481954998362112",
                "110481956446597120",
                "110481957947408384",
                "110487470281773056",
                "110487470967312896",
                "110506627454519296",
                "110506627817181184",
                "110507691712184832",
                "110514010404378112",
                "110521111630981120",
                "110521112427506176",
                "110544818145337856",
                "110569569171750912",
                "110571362715833344",
                "110583006917147648",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 158,
            "create_time": "2024-08-21 18:21:40",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 17:20:05",
            "role": "供应链管理,运营管理,子管理员,仓库管理,质检员,采购开发,采购跟单,运营组长,cangku 设置",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 1
        },
        {
            "wxNickName": "",
            "orgNames": "IT部",
            "userOrgDtos": [
                {
                    "orgName": "IT部",
                    "wholeOrgId": "1826571617744797697",
                    "orgId": "1826571617744797697"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "110478965997969920",
                        "110480134760059392",
                        "110481954998362112",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "110478965997969920",
                        "110480134760059392",
                        "110481954998362112",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625405",
            "realname": "IT开发96",
            "mobile": "",
            "email": "",
            "username": "Znder96",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10809",
                "10810",
                "10811",
                "10842",
                "110478965997969920",
                "110480134760059392",
                "110481954998362112",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 230,
            "create_time": "2024-08-21 18:19:11",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 15:51:10",
            "role": "IT开发测试",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/林晓敏组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/林晓敏组",
                    "wholeOrgId": "1826134906265444353/1826136510865162242",
                    "orgId": "1826136510865162242"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625113",
            "realname": "陈宝莹",
            "mobile": "19834887418",
            "email": "",
            "username": "Znder92",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 39,
            "create_time": "2024-08-21 13:56:23",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 10:26:39",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购开发",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625115",
            "realname": "刘相兰",
            "mobile": "18038183835",
            "email": "",
            "username": "Znder94",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 67,
            "create_time": "2024-08-21 13:56:23",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 11:25:08",
            "role": "采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625106",
            "realname": "刘璐",
            "mobile": "13510320219",
            "email": "",
            "username": "Znder84",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 89,
            "create_time": "2024-08-21 13:56:22",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 10:39:46",
            "role": "采购跟单,供应商报价",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110480134760059392",
                        "110507691712184832",
                        "110514010404378112"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110480134760059392",
                        "110507691712184832",
                        "110514010404378112"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625109",
            "realname": "易翠婷",
            "mobile": "15579567276",
            "email": "",
            "username": "Znder87",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110480134760059392",
                "110507691712184832",
                "110514010404378112"
            ],
            "login_num": 130,
            "create_time": "2024-08-21 13:56:22",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 10:18:58",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625110",
            "realname": "陈紫霞",
            "mobile": "18406664391",
            "email": "",
            "username": "Znder88",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 55,
            "create_time": "2024-08-21 13:56:22",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:48:16",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625103",
            "realname": "黄诗怡",
            "mobile": "18312167581",
            "email": "",
            "username": "Znder81",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110481948018697728",
                "110481949849462272",
                "110481951351230976"
            ],
            "login_num": 52,
            "create_time": "2024-08-21 13:56:21",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 14:46:49",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "否极泰来",
            "orgNames": "运营二部廖国荣组",
            "userOrgDtos": [
                {
                    "orgName": "运营二部廖国荣组",
                    "wholeOrgId": "1826134946325794818",
                    "orgId": "1826134946325794818"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 1,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625100",
            "realname": "蔡盈添",
            "mobile": "18948724501",
            "email": "",
            "username": "Znder78",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10818",
                "10819",
                "10840",
                "10841",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 127,
            "create_time": "2024-08-21 13:56:21",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:56:54",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "工业设计",
            "userOrgDtos": [
                {
                    "orgName": "工业设计",
                    "wholeOrgId": "1826569782167068673",
                    "orgId": "1826569782167068673"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625105",
            "realname": "张涛",
            "mobile": "18235187639",
            "email": "",
            "username": "Znder83",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:21",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2024-08-21 15:28:39",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 4,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110478965997969920",
                        "110478979257454592",
                        "110569569171750912",
                        "110583006917147648"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110478965997969920",
                        "110478979257454592",
                        "110569569171750912",
                        "110583006917147648"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625101",
            "realname": "钟秋萍",
            "mobile": "18579077562",
            "email": "",
            "username": "Znder79",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110478965997969920",
                "110478979257454592",
                "110569569171750912",
                "110583006917147648"
            ],
            "login_num": 63,
            "create_time": "2024-08-21 13:56:21",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:07:08",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625096",
            "realname": "陈慧",
            "mobile": "15273101824",
            "email": "",
            "username": "Znder73",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 44,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:10:10",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/郑春芳组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/郑春芳组",
                    "wholeOrgId": "1826134906265444353/1826136606690177025",
                    "orgId": "1826136606690177025"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625099",
            "realname": "刘琳琳",
            "mobile": "18379280619",
            "email": "",
            "username": "Znder77",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 45,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 10:32:06",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10842"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10842",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625094",
            "realname": "李百慧",
            "mobile": "15529509879",
            "email": "",
            "username": "Znder70",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "10842"
            ],
            "login_num": 54,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:41:26",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "工业设计",
            "userOrgDtos": [
                {
                    "orgName": "工业设计",
                    "wholeOrgId": "1826569782167068673",
                    "orgId": "1826569782167068673"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625097",
            "realname": "谢雄",
            "mobile": "18002228570",
            "email": "",
            "username": "Znder74",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 4,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2024-11-04 10:38:55",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "工业设计",
            "userOrgDtos": [
                {
                    "orgName": "工业设计",
                    "wholeOrgId": "1826569782167068673",
                    "orgId": "1826569782167068673"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625095",
            "realname": "姚毅松",
            "mobile": "18927568685",
            "email": "",
            "username": "Znder72",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "14.216.51.4",
            "last_login_time": "2024-08-21 15:29:55",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625098",
            "realname": "黄仁欢",
            "mobile": "13361618682",
            "email": "",
            "username": "Znder75",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 47,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 17:47:36",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "IT部",
            "userOrgDtos": [
                {
                    "orgName": "IT部",
                    "wholeOrgId": "1826571617744797697",
                    "orgId": "1826571617744797697"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625093",
            "realname": "徐星",
            "mobile": "18613117602",
            "email": "",
            "username": "Znder69",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:20",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625088",
            "realname": "陈盼",
            "mobile": "15226306482",
            "email": "",
            "username": "Znder64",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 3,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "103.165.80.99",
            "last_login_time": "2025-04-18 10:03:21",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625091",
            "realname": "李飞",
            "mobile": "18678784344",
            "email": "",
            "username": "Znder67",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:36:01",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110477918005063680"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110477918005063680"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625086",
            "realname": "丁敏敏",
            "mobile": "15707027951",
            "email": "",
            "username": "Znder62",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110477918005063680"
            ],
            "login_num": 48,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 16:49:51",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625089",
            "realname": "袁小清",
            "mobile": "17673133095",
            "email": "",
            "username": "Znder65",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 1,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:15:35",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625092",
            "realname": "李宗森",
            "mobile": "18827862365",
            "email": "",
            "username": "Znder68",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:35:39",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "行政部",
            "userOrgDtos": [
                {
                    "orgName": "行政部",
                    "wholeOrgId": "1826569518013997057",
                    "orgId": "1826569518013997057"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625087",
            "realname": "仇玉苗",
            "mobile": "18269321417",
            "email": "",
            "username": "Znder63",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 5,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2024-11-26 14:44:19",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10833",
                        "10834",
                        "10837",
                        "10838",
                        "10839",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10833",
                        "10834",
                        "10837",
                        "10838",
                        "10839",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625090",
            "realname": "马华仪",
            "mobile": "13822845998",
            "email": "",
            "username": "Znder66",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "seller_ids": [
                "10833",
                "10834",
                "10837",
                "10838",
                "10839",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 29,
            "create_time": "2024-08-21 13:56:19",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-03-20 09:33:59",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "行政部",
            "userOrgDtos": [
                {
                    "orgName": "行政部",
                    "wholeOrgId": "1826569518013997057",
                    "orgId": "1826569518013997057"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625080",
            "realname": "张玲",
            "mobile": "15817399871",
            "email": "",
            "username": "Znder55",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625083",
            "realname": "易欣",
            "mobile": "17704009732",
            "email": "",
            "username": "Znder58",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:36:57",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625081",
            "realname": "张显奇",
            "mobile": "18122487772",
            "email": "",
            "username": "Znder56",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 4,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "216.218.221.179",
            "last_login_time": "2025-03-18 11:13:56",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购开发",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625084",
            "realname": "孙双飞",
            "mobile": "18318677861",
            "email": "",
            "username": "Znder59",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 55,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 10:07:20",
            "role": "采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625079",
            "realname": "邓紫婷",
            "mobile": "15012838215",
            "email": "",
            "username": "Znder54",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 48,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 17:36:35",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625082",
            "realname": "唐林波",
            "mobile": "19873945357",
            "email": "",
            "username": "Znder57",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:19:41",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625085",
            "realname": "蔡鋆荧",
            "mobile": "13728709363",
            "email": "",
            "username": "Znder61",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 47,
            "create_time": "2024-08-21 13:56:18",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 11:46:11",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "日本站",
            "userOrgDtos": [
                {
                    "orgName": "日本站",
                    "wholeOrgId": "1826569129761742849",
                    "orgId": "1826569129761742849"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 4,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "10850",
                        "10851",
                        "10852",
                        "10853"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "10850",
                        "10851",
                        "10852",
                        "10853"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 1,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625075",
            "realname": "夏梅燕",
            "mobile": "17512069309",
            "email": "",
            "username": "Znder50",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10850",
                "10851",
                "10852",
                "10853"
            ],
            "login_num": 53,
            "create_time": "2024-08-21 13:56:17",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:08:17",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "设计部",
            "userOrgDtos": [
                {
                    "orgName": "设计部",
                    "wholeOrgId": "1826138302301118465",
                    "orgId": "1826138302301118465"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625078",
            "realname": "王伟彬",
            "mobile": "18138846731",
            "email": "",
            "username": "Znder53",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 3,
            "create_time": "2024-08-21 13:56:17",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2024-08-21 15:20:09",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625073",
            "realname": "冼妙桂",
            "mobile": "13189803651",
            "email": "",
            "username": "Znder48",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:17",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625076",
            "realname": "刘庆镕",
            "mobile": "17770848387",
            "email": "",
            "username": "Znder51",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:17",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:57:27",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625074",
            "realname": "侯梦倩",
            "mobile": "15294715835",
            "email": "",
            "username": "Znder49",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842"
            ],
            "login_num": 47,
            "create_time": "2024-08-21 13:56:17",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 11:56:32",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625077",
            "realname": "罗钰清",
            "mobile": "15528927367",
            "email": "",
            "username": "Znder52",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:17",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:17:36",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625072",
            "realname": "黎冠余",
            "mobile": "15112654345",
            "email": "",
            "username": "Znder47",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:16",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:18:54",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 6,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13853",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13853",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625069",
            "realname": "乔梁",
            "mobile": "15837671788",
            "email": "",
            "username": "Znder44",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 49,
            "create_time": "2024-08-21 13:56:16",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 11:49:48",
            "role": "采购开发,采购跟单",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 10,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625066",
            "realname": "黄紫怡",
            "mobile": "19177361119",
            "email": "",
            "username": "Znder41",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "10829",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 33,
            "create_time": "2024-08-21 13:56:16",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-03-24 09:14:47",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部,物流部,运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部",
                    "wholeOrgId": "1826134906265444353",
                    "orgId": "1826134906265444353"
                },
                {
                    "orgName": "物流部",
                    "wholeOrgId": "1826135115777048578",
                    "orgId": "1826135115777048578"
                },
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 1,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10833"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10833",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625071",
            "realname": "金伟",
            "mobile": "17386307682",
            "email": "",
            "username": "Znder46",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10833"
            ],
            "login_num": 21,
            "create_time": "2024-08-21 13:56:16",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 11:45:46",
            "role": "供应链管理,运营管理,仓库管理,昌盛邮箱",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625067",
            "realname": "兰雪宁",
            "mobile": "16624734980",
            "email": "",
            "username": "Znder42",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 48,
            "create_time": "2024-08-21 13:56:16",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 10:56:44",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625062",
            "realname": "梁晓欣",
            "mobile": "13927591704",
            "email": "",
            "username": "Znder37",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 59,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 09:07:37",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "行政部",
            "userOrgDtos": [
                {
                    "orgName": "行政部",
                    "wholeOrgId": "1826569518013997057",
                    "orgId": "1826569518013997057"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625065",
            "realname": "朱琳",
            "mobile": "13265609852",
            "email": "",
            "username": "Znder40",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 1,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2024-08-21 15:25:45",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625060",
            "realname": "郑丽省",
            "mobile": "13717025223",
            "email": "",
            "username": "Znder35",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 46,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-06-23 09:42:32",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购开发",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625063",
            "realname": "李康珍",
            "mobile": "13542070952",
            "email": "",
            "username": "Znder38",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 50,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:13:47",
            "role": "采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625061",
            "realname": "张彦平",
            "mobile": "18680350478",
            "email": "",
            "username": "Znder36",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.159",
            "last_login_time": "2024-08-21 15:16:35",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 8,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "10842"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "10842",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625064",
            "realname": "汤慧丹",
            "mobile": "18665307333",
            "email": "",
            "username": "Znder39",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "10829",
                "10842"
            ],
            "login_num": 56,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:11:48",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部",
                    "wholeOrgId": "1826135084440539138",
                    "orgId": "1826135084440539138"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625059",
            "realname": "孙媛",
            "mobile": "13886364198",
            "email": "",
            "username": "Znder34",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 51,
            "create_time": "2024-08-21 13:56:15",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:28:08",
            "role": "采购跟单,供应商报价",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625054",
            "realname": "唐珊",
            "mobile": "18370750050",
            "email": "",
            "username": "Znder29",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 49,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:05:40",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组,运营一部/郑春芳组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                },
                {
                    "orgName": "运营一部/郑春芳组",
                    "wholeOrgId": "1826134906265444353/1826136606690177025",
                    "orgId": "1826136606690177025"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625057",
            "realname": "郑春芳",
            "mobile": "14749736947",
            "email": "",
            "username": "Znder32",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 69,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "103.165.17.40",
            "last_login_time": "2025-07-22 11:04:11",
            "role": "运营管理,VC运营",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营二部廖国荣组",
            "userOrgDtos": [
                {
                    "orgName": "运营二部廖国荣组",
                    "wholeOrgId": "1826134946325794818",
                    "orgId": "1826134946325794818"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134479735668965376"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625052",
            "realname": "廖国荣",
            "mobile": "13610211282",
            "email": "",
            "username": "Znder27",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10818",
                "10819",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "134479735668965376"
            ],
            "login_num": 47,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 10:28:15",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "行政部",
            "userOrgDtos": [
                {
                    "orgName": "行政部",
                    "wholeOrgId": "1826569518013997057",
                    "orgId": "1826569518013997057"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625055",
            "realname": "郭培燊",
            "mobile": "13380349291",
            "email": "",
            "username": "Znder30",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 2,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "103.116.72.46",
            "last_login_time": "2024-08-22 09:39:58",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 3,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625058",
            "realname": "凌晓丹",
            "mobile": "15914533371",
            "email": "",
            "username": "Znder33",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110481954998362112",
                "110481956446597120",
                "110481957947408384"
            ],
            "login_num": 45,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 15:46:32",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 5,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625053",
            "realname": "林婧靓",
            "mobile": "18779193227",
            "email": "",
            "username": "Znder28",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 30,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 10:21:44",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625056",
            "realname": "黄鑫",
            "mobile": "17308466989",
            "email": "",
            "username": "Znder31",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 3,
            "create_time": "2024-08-21 13:56:14",
            "last_login_ip": "103.165.17.60",
            "last_login_time": "2024-08-21 16:02:53",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营二部廖国荣组",
            "userOrgDtos": [
                {
                    "orgName": "运营二部廖国荣组",
                    "wholeOrgId": "1826134946325794818",
                    "orgId": "1826134946325794818"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 8,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625046",
            "realname": "陈佳华",
            "mobile": "13112143087",
            "email": "",
            "username": "Znder21",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10818",
                "10819",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845"
            ],
            "login_num": 54,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-24 09:09:20",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "清脆",
            "orgNames": "采购部/采购开发,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 52,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853",
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853",
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "邹成帆",
            "feishuUsername": "",
            "isBindWX": 1,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625049",
            "realname": "邹成帆",
            "mobile": "15001714629",
            "email": "",
            "username": "Znder24",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10808",
                "10809",
                "10810",
                "10811",
                "10813",
                "10814",
                "10816",
                "10817",
                "10818",
                "10819",
                "10829",
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "10850",
                "10851",
                "10852",
                "10853",
                "110477918005063680",
                "110478965997969920",
                "110478978569990144",
                "110478979257454592",
                "110478979710751232",
                "110480134760059392",
                "110487470281773056",
                "110487470967312896",
                "110506627454519296",
                "110506627817181184",
                "110507691712184832",
                "110514010404378112",
                "110521111630981120",
                "110521112427506176",
                "110544818145337856",
                "110569569171750912",
                "110571362715833344",
                "110583006917147648",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 70,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "175.24.212.195",
            "last_login_time": "2025-07-24 11:27:21",
            "role": "供应链管理,运营管理,采购开发,采购跟单",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625047",
            "realname": "李愉欢",
            "mobile": "18938661503",
            "email": "",
            "username": "Znder22",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839"
            ],
            "login_num": 50,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:09:20",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "行政部",
            "userOrgDtos": [
                {
                    "orgName": "行政部",
                    "wholeOrgId": "1826569518013997057",
                    "orgId": "1826569518013997057"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625050",
            "realname": "刘果",
            "mobile": "13642368928",
            "email": "",
            "username": "Znder25",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳财务部",
            "userOrgDtos": [
                {
                    "orgName": "深圳财务部",
                    "wholeOrgId": "1826135185145270274",
                    "orgId": "1826135185145270274"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625045",
            "realname": "刘月华",
            "mobile": "15216234086",
            "email": "",
            "username": "Znder20",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 61,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 11:48:31",
            "role": "财务管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/林晓敏组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/林晓敏组",
                    "wholeOrgId": "1826134906265444353/1826136510865162242",
                    "orgId": "1826136510865162242"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 7,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134484380435902976",
                        "134479735668965376"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625048",
            "realname": "林晓敏",
            "mobile": "19867673695",
            "email": "",
            "username": "Znder23",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842"
            ],
            "login_num": 52,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:13:22",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625051",
            "realname": "涂盼",
            "mobile": "15012568047",
            "email": "",
            "username": "Znder26",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:13",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625038",
            "realname": "潘宗标",
            "mobile": "13530582023",
            "email": "",
            "username": "Znder13",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部/采购开发,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625041",
            "realname": "陈虹秀",
            "mobile": "13316561557",
            "email": "",
            "username": "Znder16",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "login_num": 29,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-06-30 09:23:28",
            "role": "采购跟单",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625044",
            "realname": "唐茂彰",
            "mobile": "18576482084",
            "email": "",
            "username": "Znder19",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营二部廖国荣组",
            "userOrgDtos": [
                {
                    "orgName": "运营二部廖国荣组",
                    "wholeOrgId": "1826134946325794818",
                    "orgId": "1826134946325794818"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 10,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625039",
            "realname": "贺",
            "mobile": "15521293129",
            "email": "",
            "username": "Znder14",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10818",
                "10819",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 49,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 15:10:14",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "独立站沃尔玛ebay",
            "userOrgDtos": [
                {
                    "orgName": "独立站沃尔玛ebay",
                    "wholeOrgId": "1826134997591457794",
                    "orgId": "1826134997591457794"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 23,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625042",
            "realname": "钟俊标",
            "mobile": "13640905007",
            "email": "",
            "username": "Znder17",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "110477918005063680",
                "110478965997969920",
                "110478978569990144",
                "110478979257454592",
                "110478979710751232",
                "110480134760059392",
                "110481948018697728",
                "110481949849462272",
                "110481951351230976",
                "110481954998362112",
                "110481956446597120",
                "110481957947408384",
                "110487470281773056",
                "110487470967312896",
                "110506627454519296",
                "110506627817181184",
                "110507691712184832",
                "110514010404378112",
                "110521111630981120",
                "110521112427506176",
                "110569569171750912",
                "110571362715833344",
                "110583006917147648"
            ],
            "login_num": 210,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "113.84.193.57",
            "last_login_time": "2025-07-24 12:46:45",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "采购部/采购开发,采购部/采购跟单",
            "userOrgDtos": [
                {
                    "orgName": "采购部/采购开发",
                    "wholeOrgId": "1826135084440539138/1826135364621295617",
                    "orgId": "1826135364621295617"
                },
                {
                    "orgName": "采购部/采购跟单",
                    "wholeOrgId": "1826135084440539138/1826135424757723138",
                    "orgId": "1826135424757723138"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 6,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339",
                        "17959"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339",
                        "17959"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625040",
            "realname": "陈凯",
            "mobile": "13925242304",
            "email": "",
            "username": "Znder15",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 55,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 09:29:58",
            "role": "供应链管理,采购开发",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营二部廖国荣组",
            "userOrgDtos": [
                {
                    "orgName": "运营二部廖国荣组",
                    "wholeOrgId": "1826134946325794818",
                    "orgId": "1826134946325794818"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 10,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10818",
                        "10819",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625043",
            "realname": "吴明倩",
            "mobile": "13433696036",
            "email": "",
            "username": "Znder18",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10818",
                "10819",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 48,
            "create_time": "2024-08-21 13:56:12",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-23 10:42:54",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳设计部",
            "userOrgDtos": [
                {
                    "orgName": "深圳设计部",
                    "wholeOrgId": "1826135253562757121",
                    "orgId": "1826135253562757121"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625033",
            "realname": "李春新",
            "mobile": "13423807357",
            "email": "",
            "username": "Znder08",
            "zid": "10566971",
            "is_master": 0,
            "status": 0,
            "seller": "",
            "login_num": 0,
            "create_time": "2024-08-21 13:56:11",
            "last_login_ip": "",
            "last_login_time": "-",
            "role": "",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳财务部",
            "userOrgDtos": [
                {
                    "orgName": "深圳财务部",
                    "wholeOrgId": "1826135185145270274",
                    "orgId": "1826135185145270274"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 58,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853",
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853",
                        "110477918005063680",
                        "110478965997969920",
                        "110478978569990144",
                        "110478979257454592",
                        "110478979710751232",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625036",
            "realname": "封秋乐",
            "mobile": "18276743197",
            "email": "fengql@znder.com",
            "username": "Znder11",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10808",
                "10809",
                "10810",
                "10811",
                "10813",
                "10814",
                "10816",
                "10817",
                "10818",
                "10819",
                "10829",
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "10850",
                "10851",
                "10852",
                "10853",
                "110477918005063680",
                "110478965997969920",
                "110478978569990144",
                "110478979257454592",
                "110478979710751232",
                "110480134760059392",
                "110481948018697728",
                "110481949849462272",
                "110481951351230976",
                "110481954998362112",
                "110481956446597120",
                "110481957947408384",
                "110487470281773056",
                "110487470967312896",
                "110506627454519296",
                "110506627817181184",
                "110507691712184832",
                "110514010404378112",
                "110521111630981120",
                "110521112427506176",
                "110544818145337856",
                "110569569171750912",
                "110571362715833344",
                "110583006917147648",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 47,
            "create_time": "2024-08-21 13:56:11",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 10:46:26",
            "role": "财务管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳财务部",
            "userOrgDtos": [
                {
                    "orgName": "深圳财务部",
                    "wholeOrgId": "1826135185145270274",
                    "orgId": "1826135185145270274"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625034",
            "realname": "马仕容",
            "mobile": "13560017924",
            "email": "",
            "username": "Znder09",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "login_num": 38,
            "create_time": "2024-08-21 13:56:11",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-14 14:39:49",
            "role": "财务管理,子管理员",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 1
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/周英杰组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 4,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10808",
                        "10816",
                        "10817",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625037",
            "realname": "周英杰",
            "mobile": "18682188759",
            "email": "",
            "username": "Znder12",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10808",
                "10816",
                "10817",
                "134479735668965376"
            ],
            "login_num": 48,
            "create_time": "2024-08-21 13:56:11",
            "last_login_ip": "103.165.17.40",
            "last_login_time": "2025-07-21 15:44:49",
            "role": "运营管理,VC运营",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部/吴婷婷组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 9,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10809",
                        "10810",
                        "10811",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625032",
            "realname": "吴婷婷",
            "mobile": "18818563936",
            "email": "",
            "username": "Znder07",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10809",
                "10810",
                "10811",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 54,
            "create_time": "2024-08-21 13:56:11",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-22 11:40:26",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "果",
            "orgNames": "运营一部/陈雨果组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 10,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10813",
                        "10814",
                        "10829",
                        "10842",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 1,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625035",
            "realname": "陈雨果",
            "mobile": "18617067126",
            "email": "",
            "username": "Znder10",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10813",
                "10814",
                "10829",
                "10842",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 52,
            "create_time": "2024-08-21 13:56:11",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 19:47:58",
            "role": "运营管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "运营一部,运营一部/周英杰组,运营一部/吴婷婷组,运营一部/林晓敏组,运营一部/郑春芳组,运营一部/陈雨果组,运营一部/李愉欢组",
            "userOrgDtos": [
                {
                    "orgName": "运营一部",
                    "wholeOrgId": "1826134906265444353",
                    "orgId": "1826134906265444353"
                },
                {
                    "orgName": "运营一部/周英杰组",
                    "wholeOrgId": "1826134906265444353/1826135525072891906",
                    "orgId": "1826135525072891906"
                },
                {
                    "orgName": "运营一部/吴婷婷组",
                    "wholeOrgId": "1826134906265444353/1826136451326464001",
                    "orgId": "1826136451326464001"
                },
                {
                    "orgName": "运营一部/林晓敏组",
                    "wholeOrgId": "1826134906265444353/1826136510865162242",
                    "orgId": "1826136510865162242"
                },
                {
                    "orgName": "运营一部/郑春芳组",
                    "wholeOrgId": "1826134906265444353/1826136606690177025",
                    "orgId": "1826136606690177025"
                },
                {
                    "orgName": "运营一部/陈雨果组",
                    "wholeOrgId": "1826134906265444353/1826136722656854018",
                    "orgId": "1826136722656854018"
                },
                {
                    "orgName": "运营一部/李愉欢组",
                    "wholeOrgId": "1826134906265444353/1826136834181472258",
                    "orgId": "1826136834181472258"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 49,
                    "orgAuthNum": 2,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ],
                    "orgEntityIds": [
                        "134484380435902976",
                        "134479735668965376"
                    ],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "110480134760059392",
                        "110481948018697728",
                        "110481949849462272",
                        "110481951351230976",
                        "110481954998362112",
                        "110481956446597120",
                        "110481957947408384",
                        "110487470281773056",
                        "110487470967312896",
                        "110506627454519296",
                        "110506627817181184",
                        "110507691712184832",
                        "110514010404378112",
                        "110521111630981120",
                        "110521112427506176",
                        "110544818145337856",
                        "110569569171750912",
                        "110571362715833344",
                        "110583006917147648",
                        "134479735668965376",
                        "134484380435902976"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10625030",
            "realname": "宋明丽",
            "mobile": "13172489553",
            "email": "",
            "username": "Znder05",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10808",
                "10809",
                "10810",
                "10811",
                "10813",
                "10814",
                "10816",
                "10817",
                "10818",
                "10819",
                "10829",
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "110480134760059392",
                "110481948018697728",
                "110481949849462272",
                "110481951351230976",
                "110481954998362112",
                "110481956446597120",
                "110481957947408384",
                "110487470281773056",
                "110487470967312896",
                "110506627454519296",
                "110506627817181184",
                "110507691712184832",
                "110514010404378112",
                "110521111630981120",
                "110521112427506176",
                "110544818145337856",
                "110569569171750912",
                "110571362715833344",
                "110583006917147648",
                "134479735668965376",
                "134484380435902976"
            ],
            "login_num": 58,
            "create_time": "2024-08-21 13:56:10",
            "last_login_ip": "103.165.17.40",
            "last_login_time": "2025-07-21 09:25:13",
            "role": "运营管理,cangku 设置",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "深圳财务部",
            "userOrgDtos": [
                {
                    "orgName": "深圳财务部",
                    "wholeOrgId": "1826135185145270274",
                    "orgId": "1826135185145270274"
                }
            ],
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 32,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "10803",
                        "10804",
                        "10805",
                        "10807",
                        "10808",
                        "10809",
                        "10810",
                        "10811",
                        "10813",
                        "10814",
                        "10816",
                        "10817",
                        "10818",
                        "10819",
                        "10829",
                        "10833",
                        "10834",
                        "10835",
                        "10836",
                        "10837",
                        "10838",
                        "10839",
                        "10840",
                        "10841",
                        "10842",
                        "10843",
                        "10844",
                        "10845",
                        "10850",
                        "10851",
                        "10852",
                        "10853"
                    ]
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "9762",
                        "13854",
                        "14337",
                        "14338",
                        "14339"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10624594",
            "realname": "文盛中",
            "mobile": "18123659779",
            "email": "wensz@znder.com",
            "username": "Znderinc888",
            "zid": "10566971",
            "is_master": 0,
            "status": 1,
            "seller": "",
            "seller_ids": [
                "10803",
                "10804",
                "10805",
                "10807",
                "10808",
                "10809",
                "10810",
                "10811",
                "10813",
                "10814",
                "10816",
                "10817",
                "10818",
                "10819",
                "10829",
                "10833",
                "10834",
                "10835",
                "10836",
                "10837",
                "10838",
                "10839",
                "10840",
                "10841",
                "10842",
                "10843",
                "10844",
                "10845",
                "10850",
                "10851",
                "10852",
                "10853"
            ],
            "login_num": 68,
            "create_time": "2024-08-20 18:29:53",
            "last_login_ip": "61.238.143.148",
            "last_login_time": "2025-07-21 17:12:27",
            "role": "财务管理",
            "editable": 1,
            "warehouse": "",
            "sysSubAdminFlag": 0
        },
        {
            "wxNickName": "",
            "orgNames": "",
            "assPerDtos": [
                {
                    "authType": "店铺",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                },
                {
                    "authType": "仓库",
                    "userAuthNum": 5,
                    "orgAuthNum": 0,
                    "userEntityIds": [
                        "13853",
                        "13854",
                        "14105",
                        "14872",
                        "14873"
                    ],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": [
                        "13853",
                        "13854",
                        "14105",
                        "14872",
                        "14873"
                    ]
                },
                {
                    "authType": "1688账号",
                    "userAuthNum": 0,
                    "orgAuthNum": 0,
                    "userEntityIds": [],
                    "orgEntityIds": [],
                    "authNames": "",
                    "entityIds": []
                }
            ],
            "dingUsername": "方书胜",
            "feishuUsername": "",
            "isBindWX": 0,
            "isBindJwt": 0,
            "isBindBI": 0,
            "unboundMobile": "",
            "isCanDelOrDisable": 1,
            "uid": "10566971",
            "realname": "方书胜",
            "mobile": "18925226557",
            "email": "",
            "username": "m.7682rMrdex5s",
            "zid": "10566971",
            "is_master": 1,
            "status": 1,
            "seller": "",
            "login_num": 201,
            "create_time": "2024-05-14 10:55:40",
            "last_login_ip": "223.73.113.89",
            "last_login_time": "2025-07-23 23:23:15",
            "role": "",
            "editable": 0,
            "warehouse": "",
            "sysSubAdminFlag": 0
        }
    ]
}

# 提取需要的字段
extracted_data = []
for user in json_data["list"]:
    extracted_data.append({
        "uid": user.get("uid"),
        "realname": user.get("realname"),
        "username": user.get("username")
    })

# 转换为DataFrame并保存为Excel
df = pd.DataFrame(extracted_data)
df.to_excel("user_info.xlsx", index=False)

print("Excel文件已生成：user_info.xlsx")