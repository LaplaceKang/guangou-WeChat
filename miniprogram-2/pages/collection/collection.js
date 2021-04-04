//导入要请求的DjangoURL
import {
  DjangoURL
} from '../../utils/util.js'

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
      url: DjangoURL+'wx/user/getUserCollectedVenue?openid=' + that.data.openid+'&longitude=' + that.data.longitude+'&latitude='+ that.data.latitude+'&page='+ that.data.page,
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

  //跳转到场馆详情页
  toCampus(event) {
    var that = this
    let index = parseInt(event.currentTarget.dataset.index) //获取点击的场馆的下标
    console.log(that.data.venue[index].venueid)
    let courttype = JSON.stringify(that.data.venue[index].courttype)
    // console.log(courttype)
    wx.navigateTo({ //跳转页面
      url: '/pages/campus/campus?venueid=' + that.data.venue[index].venueid + '&courttype=' + courttype + '&venuename=' + that.data.venue[index].venuename + '&longitude=' + that.data.venue[index].longitude + '&latitude=' + that.data.venue[index].latitude
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