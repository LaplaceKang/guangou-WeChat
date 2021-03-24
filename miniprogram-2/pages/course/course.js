// pages/course/course.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    option1: [
      { text: '区域', value: 0 },
      { text: '全部区域', value: 1 },
      { text: '海淀区', value: 2 },
      { text: '密云区', value: 3 },
      { text: '延庆区', value: 4 },
      { text: '房山区', value: 5 },
    ],
    option2: [
      { text: '篮球', value: 'a' },
      { text: '全部', value: 'b' },
      { text: '足球', value: 'c' },
      { text: '排球', value: 'd' },
      { text: '网球', value: 'e' },
      { text: '桌球', value: 'f' },
    ],
    option3: [
      { text: '智能排序', value: 'x' },
    ],
    option4: [
      { text: '筛选', value: 'y' },
    ],
    value1: 0,
    value2: 'a',
    value3:'x',
    value4:'y'
  },
  toFirst: function(event) {
    wx.navigateTo({ //跳转页面
          url: '/pages/firstpage/firstpage'
        })
    },
    toMy: function(event) {
      wx.navigateTo({ //跳转页面
            url: '/pages/index/index'
          })
      },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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