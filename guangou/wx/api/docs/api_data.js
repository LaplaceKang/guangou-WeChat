define({ "api": [
  {
    "type": "get",
    "url": "/wx/court/getCourtDetail",
    "title": "根据总场馆id与运动类型id获取其具体信息",
    "name": "_Court_getCourtDetail",
    "group": "Court",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "venueid",
            "description": "<p>总场馆ID(如：1)</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "courttypeid",
            "description": "<p>运动类型ID</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/court/getCourtDetail"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/court.py",
    "groupTitle": "Court"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "wx/api/docs/main.js",
    "group": "F_________________guangou_WeChat_guangou_wx_api_docs_main_js",
    "groupTitle": "F_________________guangou_WeChat_guangou_wx_api_docs_main_js",
    "name": ""
  },
  {
    "type": "get",
    "url": "/wx/user/getOrderSite",
    "title": "获取用户预订的场地",
    "name": "_user_getOrderSite",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "openid",
            "description": "<p>用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/user/getOrderSite"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/wx/user/getUserCollectedVenue",
    "title": "获取用户收藏的总场馆",
    "name": "_user_getUserCollectedVenue",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "openid",
            "description": "<p>用户openid (如：'wx9a3377455576ee6c','wx9a3377455576ee6b')</p>"
          },
          {
            "group": "Parameter",
            "type": "decimal",
            "optional": false,
            "field": "longitude",
            "description": "<p>用户所在位置的经度(如：116.346352)</p>"
          },
          {
            "group": "Parameter",
            "type": "decimal",
            "optional": false,
            "field": "latitude",
            "description": "<p>用户所在位置的纬度(如：39.960501)</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>页码</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/user/getUserCollectedVenue"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/wx/user/getUserDiscountCard",
    "title": "获取用户的卡包",
    "name": "_user_getUserDiscountCard",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "openid",
            "description": "<p>用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/user/getUserDiscountCard"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/wx/user/getUserInfo",
    "title": "获取用户信息（昵称、打卡次数）",
    "name": "_user_getUserInfo",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "openid",
            "description": "<p>用户openid (如：'wx9a3377455576ee6c')</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/user/getUserInfo"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/wx/venue/filterCourtType",
    "title": "根据总场馆的运动类型筛选总场馆",
    "name": "_venue_filterCourtType",
    "group": "Venue",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "courttypeid",
            "description": "<p>运动类型ID（如：1）</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "cityid",
            "description": "<p>用户所在城市ID（如：1）</p>"
          },
          {
            "group": "Parameter",
            "type": "decimal",
            "optional": false,
            "field": "longitude",
            "description": "<p>用户所在位置的经度(如：116.346352)</p>"
          },
          {
            "group": "Parameter",
            "type": "decimal",
            "optional": false,
            "field": "latitude",
            "description": "<p>用户所在位置的纬度(如：39.960501)</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>页码</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/venue/filterCourtType"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/venue.py",
    "groupTitle": "Venue"
  },
  {
    "type": "get",
    "url": "/wx/venue/getCourtType",
    "title": "获取主页展示的场馆类型",
    "name": "_venue_getCourtType",
    "group": "Venue",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "cityid",
            "description": "<p>用户所在城市ID</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/venue/getCourtType"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/venue.py",
    "groupTitle": "Venue"
  },
  {
    "type": "get",
    "url": "/wx/venue/getIndexVenue",
    "title": "获取主页展示的总场馆",
    "name": "_venue_getIndexVenue",
    "group": "Venue",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "cityid",
            "description": "<p>用户所在城市ID(如：1)</p>"
          },
          {
            "group": "Parameter",
            "type": "decimal",
            "optional": false,
            "field": "longitude",
            "description": "<p>用户所在位置的经度(如：116.346352)</p>"
          },
          {
            "group": "Parameter",
            "type": "decimal",
            "optional": false,
            "field": "latitude",
            "description": "<p>用户所在位置的纬度(如：39.960501)</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page",
            "description": "<p>页码</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/venue/getIndexVenue"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/venue.py",
    "groupTitle": "Venue"
  },
  {
    "type": "get",
    "url": "/wx/venue/getVenueDetail",
    "title": "根据总场馆id获取其具体信息",
    "name": "_venue_getVenueDetail",
    "group": "Venue",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "venueid",
            "description": "<p>总场馆ID(如：1)</p>"
          }
        ]
      }
    },
    "sampleRequest": [
      {
        "url": "/wx/venue/getVenueDetail"
      }
    ],
    "version": "0.0.0",
    "filename": "wx/venue.py",
    "groupTitle": "Venue"
  }
] });
