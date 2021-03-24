// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    openid: 'wx9a3377455576ee6c'
  },
  // 事件处理函数
  toFirst: function(event) {
    wx.navigateTo({ //跳转页面
          url: '/pages/firstpage/firstpage'
        })
    },
    toCourse: function(event) {
      wx.navigateTo({ //跳转页面
            url: '/pages/course/course'
          })
      },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad() {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/wx/user/getUserInfo?openid=' + that.data.openid,
      method: "GET",
      success: function (res) {
        that.setData({
          checkintimes: res.data.data.checkintimes,
          nickname: res.data.data.nickname,
        })
        console.log(res.data)
      }
    })
  }
})