import {
  DjangoURL
} from '../../utils/util.js'

Page({
  /**
   * 页面的初始数据
   */
  data: {
    page: 1,
    openid: 'wx9a3377455576ee6b'
  },
  toUse: function (event) {
    wx.navigateTo({ //跳转页面
      url: '/pages/used/used'
    })
  },
  toOrder: function (event) {
    wx.navigateTo({ //跳转页面
      url: '/pages/detailed/detailed'
    })
  },
  //获取用户的订单
  getOrder() {
    var that = this
    wx.request({
      url: DjangoURL + 'wx/order/getOrder?openid=' + that.data.openid + '&page=' + that.data.page,
      method: "GET",
      success: function (res) {
        that.setData({
          order:res.data.order
        })
        console.log(res.data)
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getOrder()
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