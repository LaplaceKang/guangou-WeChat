// pages/stadium/stadium.js
// var typeMap = require('../../utils/typeMap.js');
import {
  Map_CourtType
} from '../../utils/typeMap.js'

Page({

  /**
   * 页面的初始数据
   */
  data: {
    option1: [{
      text: '区域',
      value: 0
    }, ],
    option2: [{
        text: '篮球',
        value: 'a'
      },
      {
        text: '全部',
        value: 'b'
      },
      {
        text: '足球',
        value: 'c'
      },
      {
        text: '排球',
        value: 'd'
      },
      {
        text: '网球',
        value: 'e'
      },
      {
        text: '桌球',
        value: 'f'
      },
    ],
    option3: [{
      text: '智能排序',
      value: 3
    }, ],
    option4: [{
      text: '筛选',
      value: 6
    }, ],
    value1: 0,
    value2: 'a',
    value3: 3,
    value4: 6,
  },
  //筛选总场馆
  getVenue: function () {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/wx/venue/filterCourtType?cityid=' + that.data.cityid + '&courttypeid=' + that.data.courttypeid + '&longitude=' + that.data.longitude + '&latitude=' + that.data.latitude,
      method: "GET",
      success: function (res) {
        that.setData({
          venue: res.data.data
        })
        console.log(res.data.data)
      }
    })
  },
  //从util中获取总场馆运动类型
  getAllCourtType() {
    // option2: [
    //   { text: '篮球', value: 'a' },
    //   { text: '全部', value: 'b' },
    //   { text: '足球', value: 'c' },
    //   { text: '排球', value: 'd' },
    //   { text: '网球', value: 'e' },
    //   { text: '桌球', value: 'f' },
    // ],
    let that=this
    for (let i = 1; i <= Object.keys(Map_CourtType).length; i++) {
      // console.log(Map_CourtType[i+''])
      that.data.option2.push({ text: Map_CourtType[i+''], value: i+'' })
      that.setData({
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    console.log(options)
    console.log(options.courttypeid)
    that.setData({
      courttypeid: options.courttypeid,
      latitude: options.latitude,
      longitude: options.longitude,
      cityid: options.cityid
    })
    this.getAllCourtType()
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    this.getVenue()
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