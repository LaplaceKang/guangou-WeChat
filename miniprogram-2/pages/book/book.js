// pages/book/book.js
import Dialog from '../../miniprogram/miniprogram_npm/weapp/dialog/dialog';
Page({
  /**
   * 页面的初始数据
   */
  data: {
    checked: true,
    option1: [
      { text: '篮球', value: 'a' },
      { text: '全部', value: 'b' },
      { text: '足球', value: 'c' },
      { text: '保龄球', value: 'd' },
    ],
    option2: [
      { text: '场内地图', value: 1 },
    ],
    value1: 'a',
    value2: 1,
    fruitTypeList: [{
      "fruitTypeId": 1,
      "typeName": "8：00"
    },
    {
      "fruitTypeId": 2,
      "typeName": "9：00"
    },
    {
      "fruitTypeId": 3,
      "typeName": "10：00"
    },
    {
      "fruitTypeId": 4,
      "typeName": "11：00"
    },
    {
      "fruitTypeId": 5,
      "typeName": "12：00"
    }, {
      "fruitTypeId": 6,
      "typeName": "13：00"
    },
    {
      "fruitTypeId": 7,
      "typeName": "14：00"
    },
    {
      "fruitTypeId": 8,
      "typeName": "15：00"
    },
    {
      "fruitTypeId": 9,
      "typeName": "16：00"
    },
    {
      "fruitTypeId": 10,
      "typeName": "17：00"
    },
    {
      "fruitTypeId": 11,
      "typeName": "18：00"
    },
  ],

    fruitList:[
    {
    "name":"A",
    "list":[
      {
        "pkId": 1,
        "price": "0",
      },
      {
        "pkId": 1,
        "price": "0",
      },        
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "0",
      },
      {
        "pkId": 1,
        "price": "0",
      },         
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "0",
      },  
    ]
    },
    {
      "name":"B",
      "list":[
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "0",
        },        
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "0",
        },  
        {
          "pkId": 1,
          "price": "0",
        },       
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "0",
        },  
      ]
    },
    {
    "name":"C",
    "list":[
      {
        "pkId": 1,
        "price": "0",
      },
      {
        "pkId": 1,
        "price": "0",
      },        
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "40",
      },        
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "0",
      },
      {
        "pkId": 1,
        "price": "0",
      },
      {
        "pkId": 1,
        "price": "40",
      },
      {
        "pkId": 1,
        "price": "0",
      },  
      {
        "pkId": 1,
        "price": "0",
      }, 
    ]
    },
    {
      "name":"D",
      "list":[
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "0",
        },        
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },        
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "0",
        },  
        {
          "pkId": 1,
          "price": "0",
        }, 
      ]
    },
    {
      "name":"E",
      "list":[
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "0",
        },        
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },        
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "0",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },
        {
          "pkId": 1,
          "price": "40",
        },  
        {
          "pkId": 1,
          "price": "0",
        }, 
      ]
    },
  ],
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    Dialog.alert({
      title: '通知',
      message: '1月13日场馆检修，暂停营业'
    }).then(() => {
      // on close
    });
  },
  toOrder: function(event) {
    wx.navigateTo({ //跳转页面
          url: '/pages/submit/submit'
        })
    },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})