// 获取应用实例
const app = getApp()
//导入要请求的DjangoURL
import {
  DjangoURL
} from '../../utils/util.js'

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
      url: DjangoURL+'wx/user/getUserInfo?openid=' + that.data.openid,
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