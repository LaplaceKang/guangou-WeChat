// pages/campus/campus.js
import {
  Map_Facility
} from '../../utils/typeMap.js'

Page({
  /**
   * 页面的初始数据
   */
  data: {
       imgUrls:[
        "/images/4.jpg",
        "/images/4.jpg",
        "/images/4.jpg"
       ]
      },
      //事件处理函数
  toupper:function(){
  console.log("触发了toupper");
  },
  //获取总场馆信息
  getVenueDetail() {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/wx/venue/getVenueDetail?venueid=' + that.data.venueid + '&courttypeid=' + that.data.courttype[0].courttypeid,
      method: "GET",
      success: function (res) {
        that.setData({
          venue: res.data.data.venue,
          court:res.data.data.court
        })
        that.getCourtFaility()
        console.log(res.data)
      }
    })
  },
  //获取场馆的场地设施信息
  getCourtFaility(){
    let that=this
    let court=that.data.court
    court.facilityname=[]
    for (let i = 1; i <= court.facilityid.length; i++) {
      court.facilityname.push(Map_Facility[i+''])
      that.setData({
        court:court
      })
    }
    // console.log(court)
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this
    console.log(options)
    that.setData({
      courttype: JSON.parse(options.courttype),
      venuename: options.venuename,
      venueid: options.venueid,
      longitude: options.longitude,
      latitude: options.latitude
    })
    this.getVenueDetail()
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