//导入要请求的DjangoURL
import {
  DjangoURL
} from '../../utils/util.js'
import {
  Map_DiscountCardColor
} from '../../utils/typeMap.js'

Page({
  /**
   * 页面的初始数据
   */
  data: {
    openid: 'wx9a3377455576ee6a'
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: DjangoURL+'wx/user/getUserDiscountCard?openid=' + that.data.openid,
      method: "GET",
      success: function (res) {
        let card=res.data.data
        card.forEach(element => {
          element['color']=Map_DiscountCardColor[element['discountcardid__discountcardtypeid']]
          // console.log(element['color'])
        });
        that.setData({
          card:card
        })
      }
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