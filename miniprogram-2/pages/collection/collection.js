// pages/collection/collection.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    openid: 'wx9a3377455576ee6b',
    longitude:116.346352,
    latitude:39.960501,
    page:1
  },

  getVenue:function(){
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/wx/user/getUserCollectedVenue?openid=' + that.data.openid+'&longitude=' + that.data.longitude+'&latitude='+ that.data.latitude+'&page='+ that.data.page,
      method: "GET",
      success: function (res) {
        that.setData({
          venue: res.data.data
        })
        console.log(res.data.data)
        console.log(res.data.data.courttype)
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getVenue()
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